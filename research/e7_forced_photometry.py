"""E7: faint turn-ons with forced photometry on NEOWISE-R W2 frames.

Hypothesis: positions the catalog did not flag as turn_on ("other", "confused",
and a random sample of "none") show persistent faint brightenings at a rate above
the 60" offset control.
Per position: forced aperture photometry on every W2 L1b frame (r = 2 px ~ 5.5",
sky = median of a 4-7 px annulus), flux normalised to zeropoint 22.5, median per
~6-month visit with robust error 1.2533*std/sqrt(n); then the E0 change-point
scan (best_persistent_step).  Detection threshold on delta-BIC is calibrated on the
offset control (false-positive rate <= 1%).
Resumable: one JSON per position in cache/e7/.  Writes artifacts/e7/forced.csv.
"""
from __future__ import annotations

import argparse
import io
import json
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import numpy as np
import pandas as pd
from astropy.io import fits
from astropy.wcs import WCS

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "research"))
sys.path.insert(0, str(ROOT / "src"))
from starbirth.features.change_point import best_persistent_step  # noqa: E402
from starbirth.features.turn_on import classify  # noqa: E402
from viewer_imagery import _cutout, _frames  # noqa: E402

NEO0, VISIT = 56640.0, 182.625
CACHE = ROOT / "cache" / "e7"
OUT = ROOT / "artifacts" / "e7"


def frame_flux(blob: bytes, ra: float, dec: float, r_ap: float = 2.0, r_in: float = 4.0, r_out: float = 7.0):
    with fits.open(io.BytesIO(blob)) as h:
        d, hdr = h[0].data.astype(float), h[0].header
    x, y = WCS(hdr).world_to_pixel_values(ra, dec)
    yy, xx = np.indices(d.shape)
    rr = np.hypot(xx - x, yy - y)
    ann = d[(rr >= r_in) & (rr < r_out) & np.isfinite(d)]
    ap = (rr < r_ap) & np.isfinite(d)
    if ann.size < 20 or ap.sum() < 8 or not (0 <= x < d.shape[1] and 0 <= y < d.shape[0]):
        return None
    flux = d[ap].sum() - ap.sum() * np.median(ann)
    return float(flux * 10 ** (-0.4 * (hdr.get("MAGZP", 22.5) - 22.5)))


def light_curve(ra: float, dec: float, per_visit: int = 6) -> dict:
    frames = _frames(ra, dec)
    by: dict[int, list[dict]] = {}
    for fr in frames:
        by.setdefault(int((fr["mjd"] - NEO0) // VISIT), []).append(fr)
    vis, f, e = [], [], []
    for v in sorted(by):
        fl = []
        for fr in sorted(by[v], key=lambda z: z["mjd"])[:per_visit]:
            b = _cutout(fr, ra, dec, 40)
            if b:
                try:
                    x = frame_flux(b, ra, dec)
                except Exception:  # noqa: BLE001  one corrupt frame must not kill the position
                    x = None
                if x is not None:
                    fl.append(x)
        if len(fl) >= 3:
            fl = np.array(fl)
            vis.append(v)
            f.append(float(np.median(fl)))
            e.append(float(max(1.2533 * fl.std(ddof=1) / np.sqrt(fl.size), 1e-3)))
    out = {"visit": vis, "flux": f, "err": e}
    if len(f) >= 8:
        cp = best_persistent_step(np.array(f), np.array(e), min_points_each_side=3)
        out.update(dbic=cp.delta_bic, step=cp.amplitude, pre=cp.pre_mean, post=cp.post_mean,
                   onset_visit=vis[cp.index] if cp.index is not None and cp.index < len(vis) else None)
    return out


def run_one(label: str, tid: int, ra: float, dec: float) -> dict:
    f = CACHE / f"{label}_{tid}.json"
    if f.exists():
        return json.loads(f.read_text())
    try:
        res = light_curve(ra, dec)
    except Exception as ex:  # noqa: BLE001
        res = {"error": str(ex)[:200]}
    res.update(label=label, tid=tid, ra=ra, dec=dec)
    CACHE.mkdir(parents=True, exist_ok=True)
    f.write_text(json.dumps(res))
    return res


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--n-none", type=int, default=500)
    p.add_argument("--workers", type=int, default=12)
    p.add_argument("--only", help="comma-separated tids (self-check)")
    a = p.parse_args()
    s = pd.read_csv(ROOT / "artifacts" / "e1_full" / "pilot_targets.csv")
    if a.only:
        tids = [int(x) for x in a.only.split(",")]
    else:
        cls = classify(pd.read_csv(ROOT / "artifacts" / "e1_full" / "neowise_rows_on.csv"), len(s))
        rng = np.random.default_rng(7)
        none = cls.index[cls == "none"].values
        tids = sorted(set(cls.index[cls.isin(["other", "confused", "turn_on"])]) |
                      set(rng.choice(none, min(a.n_none, none.size), replace=False)))
        OUT.mkdir(parents=True, exist_ok=True)
        pd.DataFrame({"tid": tids, "e1_class": cls.reindex(tids).values}).to_csv(OUT / "targets.csv", index=False)
    jobs = [(lab, int(t), float(s.ra[t]), float(s.dec[t]) + dd / 3600) for t in tids for lab, dd in (("on", 0.0), ("off", 60.0))]
    with ThreadPoolExecutor(a.workers) as ex:
        res = list(ex.map(lambda j: run_one(*j), jobs))
    OUT.mkdir(parents=True, exist_ok=True)
    df = pd.DataFrame([{k: v for k, v in r.items() if k not in ("visit", "flux", "err")} for r in res])
    if not a.only:
        df.to_csv(OUT / "forced.csv", index=False)
    print(df.drop(columns=[c for c in ("ra", "dec") if c in df]).to_string()[:3000] if a.only else df.describe())


if __name__ == "__main__":
    main()
