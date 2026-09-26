"""E1-pilot: catalog-level turn-on rate in prestellar clumps.

Hypothesis: prestellar clumps with no AllWISE (2010-11) W2 source within R
acquire a *persistent* NEOWISE W2 detection at the clump position at a rate
    r_on = S + B  (births + bursts/artifacts)  per clump over 2014-2024.
Control: the same clumps' offset positions (+60" Dec) give the rate at which
catalog noise/confusion alone produces "persistent new sources".

Classification: starbirth.features.turn_on (source tracking, >= 10 SNR post-onset).
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

from starbirth.features.turn_on import classify

ROOT = Path(__file__).resolve().parents[1]
TAP = "https://irsa.ipac.caltech.edu/TAP/sync"


def neowise_rows(ra: np.ndarray, dec: np.ndarray, radius_arcsec: float, chunk: int = 200,
                 cache_dir: Path | None = None, retries: int = 3) -> pd.DataFrame:
    """Chunked (IRSA sync TAP times out ~5 min on ~2000-target uploads); each chunk
    is cached to cache_dir so a long run resumes after a crash or transient fault."""
    parts = []
    for i in range(0, len(ra), chunk):
        f = cache_dir / f"chunk_{i:06d}.csv" if cache_dir else None
        if f is not None and f.exists():
            parts.append(pd.read_csv(f))
            continue
        for attempt in range(retries):
            try:
                r = _neowise_chunk(ra[i:i + chunk], dec[i:i + chunk], radius_arcsec)
                break
            except (RuntimeError, httpx.HTTPError) as e:
                if attempt == retries - 1:
                    raise
                print(f"chunk {i}: retry {attempt + 1} after {type(e).__name__}", flush=True)
        r = r.assign(tid=r.tid + i)
        if f is not None:
            f.parent.mkdir(parents=True, exist_ok=True)
            r.to_csv(f, index=False)
        parts.append(r)
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


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--n", type=int, default=2000)
    p.add_argument("--dmax", type=float, default=4.0)
    p.add_argument("--radius", type=float, default=6.0, help="query radius; association uses 3\" + tracking")
    p.add_argument("--seed", type=int, default=1)
    p.add_argument("--out", default="e1_pilot", help="subdir of artifacts/")
    a = p.parse_args()
    out = ROOT / "artifacts" / a.out
    out.mkdir(parents=True, exist_ok=True)

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
        rows = neowise_rows(s.ra.values, s.dec.values + dec_shift / 3600, a.radius,
                            cache_dir=ROOT / "cache" / a.out / label)
        rows.to_csv(out / f"neowise_rows_{label}.csv", index=False)
        c = classify(rows, len(s))
        res[label] = c
        print(f"{label}: rows={len(rows)}", c.value_counts().to_dict())
    s["class_on"], s["class_off"] = res["on"].values, res["off"].values
    s.to_csv(out / "pilot_targets.csv", index=False)


if __name__ == "__main__":
    main()
