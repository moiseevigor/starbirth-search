"""E-1(B): empirical W1/W2 detectability of the post-transition (protostellar) state.

Hypothesis: a Hi-GAL clump that has just become protostellar shows a W2 point
source at the clump position more often than a prestellar clump does (whose
matches are chance alignments / unrelated stars).  The excess
    Δf = f_match(protostellar) - f_match(prestellar)
is the probability that a turn-on is visible at 4.6 µm at all.

Crossmatch: AllWISE source table (epoch 2010-2011, ~ the Herschel epoch) via
IRSA TAP upload, radius R arcsec.  Output: artifacts/e_minus1/allwise_match.csv
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
HIGAL = ROOT / "cache" / "higal360clump.csv"
OUT = ROOT / "artifacts" / "e_minus1"
TAP = "https://irsa.ipac.caltech.edu/TAP/sync"


def fetch_higal() -> pd.DataFrame:
    if not HIGAL.exists():
        HIGAL.parent.mkdir(exist_ok=True)
        q = ("SELECT designation,glon,glat,ra,dec,f70,ulim_70,f22,f24,dist,d_flag,"
             "fit_type,evol_flag,mass,temp,l_bol,diam,surf_dens FROM higal360clump")
        r = httpx.post(TAP, data={"QUERY": q, "FORMAT": "csv"}, timeout=600)
        r.raise_for_status()
        HIGAL.write_bytes(r.content)
    return pd.read_csv(HIGAL)


def allwise_match(targets: pd.DataFrame, radius_arcsec: float) -> pd.DataFrame:
    """Nearest AllWISE source within radius for each target (server-side)."""
    # ponytail: int key — IRSA upload rejects unicodeChar columns
    t = Table({"tid": np.arange(len(targets)), "ra": targets.ra.values, "dec": targets.dec.values})
    buf = io.BytesIO()
    t.write(buf, format="votable")
    q = f"""
SELECT t.tid, a.ra AS a_ra, a.dec AS a_dec, a.w1mpro, a.w1sigmpro, a.w2mpro,
       a.w2sigmpro, a.w1snr, a.w2snr, a.cc_flags, a.ext_flg, t.ra AS t_ra, t.dec AS t_dec
FROM TAP_UPLOAD.t AS t, allwise_p3as_psd AS a
WHERE 1=CONTAINS(POINT('ICRS', a.ra, a.dec), CIRCLE('ICRS', t.ra, t.dec, {radius_arcsec/3600:.8f}))
""".strip()
    r = httpx.post(TAP, data={"QUERY": q, "FORMAT": "csv", "UPLOAD": "t,param:tbl"},
                   files={"tbl": ("t.xml", buf.getvalue())}, timeout=1800)
    r.raise_for_status()
    if r.text.lstrip().startswith("<"):  # TAP errors come back as VOTable
        raise RuntimeError(r.text[:800])
    m = pd.read_csv(io.StringIO(r.text))
    # ponytail: small-angle separation; fine at arcsec radii away from the poles
    m["sep"] = 3600 * np.hypot(((m.a_ra - m.t_ra + 180) % 360 - 180) * np.cos(np.radians(m.t_dec)), m.a_dec - m.t_dec)
    m = m.sort_values("sep").drop_duplicates("tid")  # nearest only
    m["designation"] = targets.designation.values[m.tid.values]
    return m.drop(columns="tid")


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--n-per-class", type=int, default=4000)
    p.add_argument("--radius", type=float, default=3.0)
    p.add_argument("--seed", type=int, default=0)
    p.add_argument("--offset-arcsec", type=float, default=60.0,
                   help="control: same targets shifted in dec -> chance-alignment baseline")
    a = p.parse_args()
    d = fetch_higal()
    rng = np.random.default_rng(a.seed)
    parts = []
    for flag in (1, 2):  # 1 = prestellar, 2 = protostellar
        g = d[d.evol_flag == flag]
        parts.append(g.iloc[rng.choice(len(g), min(a.n_per_class, len(g)), replace=False)])
    s = pd.concat(parts)
    m = allwise_match(s, a.radius)
    out = s.merge(m, on="designation", how="left")
    off = s.assign(dec=s.dec + a.offset_arcsec / 3600)
    mo = allwise_match(off, a.radius).add_prefix("off_").rename(columns={"off_designation": "designation"})
    out = out.merge(mo, on="designation", how="left")
    OUT.mkdir(parents=True, exist_ok=True)
    out.to_csv(OUT / "allwise_match.csv", index=False)
    print(f"wrote {len(out)} rows, matched {out.sep.notna().sum()}, offset-matched {out.off_sep.notna().sum()}")


if __name__ == "__main__":
    main()
