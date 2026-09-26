"""E1-pilot: catalog-level turn-on rate in prestellar clumps.

Hypothesis: prestellar clumps with no AllWISE (2010-11) W2 source within R
acquire a *persistent* NEOWISE W2 detection at the clump position at a rate
    r_on = S + B  (births + bursts/artifacts)  per clump over 2014-2024.
Control: the same clumps' offset positions (+60" Dec) give the rate at which
catalog noise/confusion alone produces "persistent new sources".

Persistent = detected (w2snr>=5, cc_flags clean in W2) in >= 3 distinct
NEOWISE visits (~6-month bins), none of which is before 2014 by construction.
Output: artifacts/e1_pilot/neowise_rows.csv, summary printed.
"""
from __future__ import annotations

import argparse
import io
from pathlib import Path

import httpx
import numpy as np
import pandas as pd
from astropy.table import Table

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "artifacts" / "e1_pilot"
TAP = "https://irsa.ipac.caltech.edu/TAP/sync"


def neowise_rows(ra: np.ndarray, dec: np.ndarray, radius_arcsec: float, chunk: int = 200) -> pd.DataFrame:
    """Chunked: IRSA sync TAP times out (~5 min) on ~2000-target uploads."""
    parts = []
    for i in range(0, len(ra), chunk):
        r = _neowise_chunk(ra[i:i + chunk], dec[i:i + chunk], radius_arcsec)
        parts.append(r.assign(tid=r.tid + i))
    return pd.concat(parts, ignore_index=True)


def _neowise_chunk(ra: np.ndarray, dec: np.ndarray, radius_arcsec: float) -> pd.DataFrame:
    t = Table({"tid": np.arange(len(ra)), "ra": ra, "dec": dec})
    buf = io.BytesIO()
    t.write(buf, format="votable")
    q = f"""
SELECT t.tid, t.ra AS t_ra, t.dec AS t_dec, n.ra, n.dec, n.mjd, n.w2mpro, n.w2sigmpro,
       n.w2snr, n.cc_flags, n.qual_frame, n.nb
FROM TAP_UPLOAD.t AS t, neowiser_p1bs_psd AS n
WHERE 1=CONTAINS(POINT('ICRS', n.ra, n.dec), CIRCLE('ICRS', t.ra, t.dec, {radius_arcsec/3600:.8f}))
""".strip()
    r = httpx.post(TAP, data={"QUERY": q, "FORMAT": "csv", "UPLOAD": "t,param:tbl"},
                   files={"tbl": ("t.xml", buf.getvalue())}, timeout=3600)
    r.raise_for_status()
    if r.text.lstrip().startswith("<"):
        raise RuntimeError(r.text[:800])
    return pd.read_csv(io.StringIO(r.text))


NEO_START_MJD = 56640.0  # 2013-12-13, NEOWISE-R survey start
N_VISITS = 22  # ~6-month visits through 2024-08


def visit_table(rows: pd.DataFrame) -> pd.DataFrame:
    """tid x visit boolean: clean W2>=5sigma detection in that ~6-month visit."""
    ok = (rows.w2snr >= 5) & (rows.cc_flags.astype(str).str[1] == "0") & (rows.qual_frame > 0)
    g = rows[ok]
    v = ((g.mjd - NEO_START_MJD) // 182.625).astype(int).clip(0, N_VISITS - 1)
    return pd.crosstab(g.tid.values, v.values).gt(0).reindex(columns=range(N_VISITS), fill_value=False)


def classify(vt: pd.DataFrame, n_targets: int, min_pre: int = 3, min_post: int = 3,
             min_post_frac: float = 0.8) -> pd.Series:
    """none / steady / turn_on / other per target.

    ponytail: assumes every position is covered every visit (NEOWISE ~6-month
    cadence); upgrade = coverage from neowiser_p1bs_frm to turn gaps into limits.
    """
    out = pd.Series("none", index=range(n_targets))
    for tid, row in vt.iterrows():
        det = np.flatnonzero(row.values)
        if len(det) == 0:
            continue
        first = det[0]
        post = row.values[first:]
        if first >= min_pre and len(det) >= min_post and post.mean() >= min_post_frac:
            out[tid] = "turn_on"
        elif first < min_pre and row.values.mean() >= min_post_frac:
            out[tid] = "steady"
        else:
            out[tid] = "other"
    return out


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--n", type=int, default=2000)
    p.add_argument("--dmax", type=float, default=4.0)
    p.add_argument("--radius", type=float, default=3.0)
    p.add_argument("--seed", type=int, default=1)
    a = p.parse_args()
    OUT.mkdir(parents=True, exist_ok=True)

    # prestellar clumps with NO AllWISE W2 source at clump position (from E-1 match)
    m = pd.read_csv(ROOT / "artifacts" / "e_minus1" / "allwise_match.csv")
    cat = pd.read_csv(ROOT / "cache" / "higal360clump.csv")
    had = set(m.loc[m.sep.notna() & (m.w2snr >= 5), "designation"])
    pool = cat[(cat.evol_flag == 1) & (cat.dist > 0) & (cat.dist <= a.dmax) & ~cat.designation.isin(had)]
    # ponytail: AllWISE check only covers clumps sampled in E-1; unsampled ones are
    # re-checked below via the NEOWISE-era-only criterion (no pre-2014 data in NEOWISE-R anyway)
    s = pool.sample(min(a.n, len(pool)), random_state=a.seed).reset_index(drop=True)

    res = {}
    for label, dec_shift in (("on", 0.0), ("off", 60.0)):
        rows = neowise_rows(s.ra.values, s.dec.values + dec_shift / 3600, a.radius)
        rows.to_csv(OUT / f"neowise_rows_{label}.csv", index=False)
        c = classify(visit_table(rows), len(s))
        res[label] = c
        print(f"{label}: rows={len(rows)}", c.value_counts().to_dict())
    s["class_on"], s["class_off"] = res["on"].values, res["off"].values
    s.to_csv(OUT / "pilot_targets.csv", index=False)


if __name__ == "__main__":
    main()
