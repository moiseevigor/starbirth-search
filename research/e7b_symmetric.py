"""E7b: symmetric, stratified re-test of faint rises (answers the E7 adversarial review).

Design (pre-registered):
* Both arms are classified with the SAME E1 rule on their OWN detections: clump positions
  (on) and 60" offsets (off). Each arm is sampled per class stratum: all 'other/confused/
  turn_on', 500 random 'none', 300 random 'steady'. Arm rise rates are population-weighted
  (N_stratum / N_total) so they estimate the rate over all 19,219 positions of that arm.
* Tier 1 (all positions): forced photometry on quality-filtered frames (qual_frame > 0,
  moon_sep > 15 deg), per-visit errors with a systematic floor calibrated on the OFF arm
  (median reduced chi^2 = 1); change point; threshold T = population-weighted 99th
  percentile of eligible OFF delta-BIC (1% FPR).
* Tier 2 (every tier-1 rise, both arms): remeasure with L1b mask + uncertainty images;
  a rise is confirmed only if it still passes T.
* Decision rule: E7 'confirmed' iff the bootstrap 95% lower bound of (rate_on - rate_off)
  > 0 using tier-2-confirmed rises. Stratum-level one-sided Fisher tests are reported too.
* Injection-recovery: steps injected into real clump-position ('none' stratum) light
  curves, completeness vs injected aperture W2 magnitude.
Usage: e7b_symmetric.py tier1 | tier2 | analyze
"""
from __future__ import annotations

import io
import json
import math
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import httpx
import numpy as np
import pandas as pd
from astropy.io import ascii, fits
from astropy.wcs import WCS

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "research"))
sys.path.insert(0, str(ROOT / "src"))
from starbirth.features.change_point import best_persistent_step  # noqa: E402
from starbirth.features.forced_phot import Floor, calibrate_floor, frame_flux, visit_flux  # noqa: E402
from starbirth.features.turn_on import classify  # noqa: E402

NEO0, VISIT = 56640.0, 182.625
CACHE = ROOT / "cache" / "e7b"
FRAMES = ROOT / "cache" / "viewer" / "frames"
OUT = ROOT / "artifacts" / "e7b"
STRATA = {"variable": ["other", "confused", "turn_on"], "none": ["none"], "steady": ["steady"]}
SAMPLE = {"variable": None, "none": 500, "steady": 300}
PER_VISIT = 6
SIZE = 40


def _get(url, timeout=90):
    for _ in range(3):
        try:
            r = httpx.get(url, timeout=timeout)
            if r.status_code == 200:
                return r.content
        except httpx.HTTPError:
            pass
    return None


def frames_q(ra, dec) -> pd.DataFrame:
    f = CACHE / "meta" / f"{ra:.5f}_{dec:.5f}.tbl"
    if not f.exists():
        b = _get(f"https://irsa.ipac.caltech.edu/ibe/search/wise/neowiser/p1bm_frm?POS={ra},{dec}"
                 "&columns=scan_id,frame_num,mjd_obs,band,scangrp,magzp,qual_frame,moon_sep,saa_sep&where=band%3D2")
        f.parent.mkdir(parents=True, exist_ok=True)
        f.write_bytes(b or b"")
    try:
        t = ascii.read(f, format="ipac").to_pandas()
    except Exception:  # noqa: BLE001
        return pd.DataFrame()
    t["visit"] = ((t.mjd_obs - NEO0) // VISIT).astype(int)
    return t


def cutout(fr, ra, dec, kind="int") -> bytes | None:
    f = FRAMES / (f"{fr.scan_id}{int(fr.frame_num):03d}_{ra:.5f}_{dec:.5f}.fits" if kind == "int"
                  else f"{fr.scan_id}{int(fr.frame_num):03d}_{ra:.5f}_{dec:.5f}_{kind}.fits")
    if f.exists():
        return f.read_bytes()
    suffix = "fits" if kind == "int" else "fits.gz"
    b = _get(f"https://irsa.ipac.caltech.edu/ibe/data/wise/neowiser/p1bm_frm/{fr.scangrp}/{fr.scan_id}/"
             f"{int(fr.frame_num):03d}/{fr.scan_id}{int(fr.frame_num):03d}-w2-{kind}-1b.{suffix}"
             f"?center={ra},{dec}&size={SIZE}arcsec&gzip=false")
    if b:
        f.parent.mkdir(parents=True, exist_ok=True)
        f.write_bytes(b)
    return b


PSF_SIGMA_PX = 6.4 / 2.355 / 2.75   # W2 PSF FWHM 6.4" (Wright+2010) on 2.75"/px L1b frames


def inject_psf(img: np.ndarray, x: float, y: float, flux_dn: float, sigma_px: float = PSF_SIGMA_PX) -> np.ndarray:
    """Return img plus a Gaussian point source of total flux flux_dn centred at pixel (x, y)."""
    yy, xx = np.indices(img.shape)
    g = np.exp(-((xx - x) ** 2 + (yy - y) ** 2) / (2 * sigma_px**2))
    return img + flux_dn * g / (2 * np.pi * sigma_px**2)


def light_curve(ra, dec, full=False, inject=None) -> dict:
    """inject=(flux_zp, onset_visit): add a PSF of that ZP-22.5 flux to every frame from onset_visit on."""
    t = frames_q(ra, dec)
    if t.empty:
        return {"error": "no frames"}
    n_all = len(t)
    t = t[(t.qual_frame > 0) & (t.moon_sep > 15)]
    vis, fl, er = [], [], []
    for v, g in t.sort_values("mjd_obs").groupby("visit"):
        ff, ee = [], []
        for fr in g.head(PER_VISIT).itertuples():
            b = cutout(fr, ra, dec)
            if not b:
                continue
            try:
                with fits.open(io.BytesIO(b)) as h:
                    img, hdr = h[0].data, h[0].header
                unc = msk = None
                if full:
                    bu, bm = cutout(fr, ra, dec, "unc"), cutout(fr, ra, dec, "msk")
                    if not (bu and bm):
                        continue
                    with fits.open(io.BytesIO(bu)) as hu, fits.open(io.BytesIO(bm)) as hm:
                        unc, msk, hdr_m = hu[0].data, hm[0].data, hm[0].header
                    if unc.shape != msk.shape:
                        continue
                    # the int cutout may be larger (cache shared with the viewer, keyed without size):
                    # all three come from the same frame grid, so align by the CRPIX offset
                    dx = int(round(hdr["CRPIX1"] - hdr_m["CRPIX1"]))
                    dy = int(round(hdr["CRPIX2"] - hdr_m["CRPIX2"]))
                    h_, w_ = msk.shape
                    if dx < 0 or dy < 0 or dy + h_ > img.shape[0] or dx + w_ > img.shape[1]:
                        continue
                    img, hdr = img[dy:dy + h_, dx:dx + w_], hdr_m
                x, y = WCS(hdr).world_to_pixel_values(ra, dec)
                if inject is not None and int(v) >= inject[1]:
                    img = inject_psf(img.astype(float), float(x), float(y),
                                     inject[0] / 10 ** (-0.4 * (float(fr.magzp) - 22.5)))
                r = frame_flux(img, float(x), float(y), float(fr.magzp), unc=unc, msk=msk)
            except Exception:  # noqa: BLE001  a corrupt frame must not kill the position
                r = None
            if r:
                ff.append(r[0])
                ee.append(r[1])
        vf = visit_flux(ff, ee) if ff else None
        if vf:
            vis.append(int(v))
            fl.append(vf[0])
            er.append(vf[1])
    return {"visit": vis, "flux": fl, "err": er, "n_frames": n_all, "n_good": int(len(t))}


def design() -> pd.DataFrame:
    s = pd.read_csv(ROOT / "artifacts" / "e1_full" / "pilot_targets.csv")
    n = len(s)
    rows = []
    rng = np.random.default_rng(71)
    for arm, dd in (("on", 0.0), ("off", 60.0)):
        cls = classify(pd.read_csv(ROOT / "artifacts" / "e1_full" / f"neowise_rows_{arm}.csv"), n)
        for st, cl in STRATA.items():
            pool = cls.index[cls.isin(cl)].values
            k = SAMPLE[st]
            pick = pool if k is None or k >= pool.size else rng.choice(pool, k, replace=False)
            for t in sorted(int(x) for x in pick):
                rows.append(dict(arm=arm, stratum=st, tid=t, e1_class=cls[t], N_stratum=int(pool.size), N_arm=n,
                                 ra=float(s.ra[t]), dec=float(s.dec[t]) + dd / 3600))
    # interleave arms and strata so a partial run is already symmetric
    d = pd.DataFrame(rows).sample(frac=1, random_state=73).reset_index(drop=True)
    OUT.mkdir(parents=True, exist_ok=True)
    d.to_csv(OUT / "design.csv", index=False)
    return d


def run_tier(tier: int, jobs: pd.DataFrame, workers: int = 12) -> list[dict]:
    def one(r):
        f = CACHE / f"t{tier}_{r.arm}_{r.tid}.json"
        if f.exists():
            return json.loads(f.read_text())
        res = light_curve(r.ra, r.dec, full=(tier == 2))
        res.update(arm=r.arm, tid=int(r.tid), stratum=r.stratum)
        f.parent.mkdir(parents=True, exist_ok=True)
        f.write_text(json.dumps(res))
        return res
    with ThreadPoolExecutor(workers) as ex:
        return list(ex.map(one, jobs.itertuples()))


def stats(lc: dict, floor: Floor) -> dict:
    f, e, v = np.array(lc.get("flux", [])), np.array(lc.get("err", [])), np.array(lc.get("visit", []))
    if f.size < 8:
        return {"ok": False}
    e2 = floor.apply(f, e)
    cp = best_persistent_step(f, e2, min_points_each_side=3)
    onset = int(v[cp.index]) if cp.index is not None and cp.index < v.size else None
    pre, post = v < (onset if onset is not None else -1), v >= (onset if onset is not None else 1e9)
    sem = lambda m: float(np.sqrt(np.sum(e2[m] ** 2)) / m.sum()) if m.sum() else np.nan  # noqa: E731
    return {"ok": True, "dbic": float(cp.delta_bic), "step": float(cp.amplitude), "onset_visit": onset,
            "pre": float(f[pre].mean()) if pre.any() else np.nan, "post": float(f[post].mean()) if post.any() else np.nan,
            "pre_sig": float(f[pre].mean() / sem(pre)) if pre.sum() >= 3 else np.nan,
            "post_sig": float(f[post].mean() / sem(post)) if post.sum() >= 3 else np.nan}


def clean(o):
    """NaN/inf -> None recursively (json.dumps would emit invalid bare NaN)."""
    if isinstance(o, dict):
        return {k: clean(v) for k, v in o.items()}
    if isinstance(o, (list, tuple)):
        return [clean(v) for v in o]
    if isinstance(o, (float, np.floating)):
        return float(o) if np.isfinite(o) else None
    if isinstance(o, np.integer):
        return int(o)
    return o


def eligible(s: dict) -> bool:
    return s.get("ok") and s["step"] > 0 and s["onset_visit"] is not None and 3 <= s["onset_visit"] <= 19


def wquantile(x, w, q):
    o = np.argsort(x)
    x, w = np.asarray(x)[o], np.asarray(w)[o]
    c = np.cumsum(w) / w.sum()
    return float(x[np.searchsorted(c, q)])


def fisher_one_sided(k1, n1, k2, n2) -> float:
    """P(K1 >= k1) under the hypergeometric null (arm 1 not more rise-prone than arm 2)."""
    K, N = k1 + k2, n1 + n2
    tot = math.comb(N, K)
    return sum(math.comb(n1, i) * math.comb(n2, K - i) for i in range(k1, min(K, n1) + 1)) / tot


def main() -> None:
    cmd = sys.argv[1] if len(sys.argv) > 1 else "analyze"
    d = pd.read_csv(OUT / "design.csv") if (OUT / "design.csv").exists() else design()
    if cmd == "tier1":
        run_tier(1, d, workers=24)
        print("tier1 done", len(d))
        return
    lcs = {(r["arm"], r["tid"]): r for r in (json.loads(f.read_text()) for f in CACHE.glob("t1_*.json"))}
    d = d[[(a, t) in lcs for a, t in zip(d.arm, d.tid)]].copy()
    off_curves = [(np.array(lcs[("off", t)]["flux"]), np.array(lcs[("off", t)]["err"]))
                  for t in d[d.arm == "off"].tid if len(lcs[("off", t)].get("flux", [])) >= 8]
    floor = calibrate_floor(off_curves)
    st = {k: stats(v, floor) for k, v in lcs.items()}
    d["w"] = d.N_stratum / d.groupby(["arm", "stratum"]).tid.transform("size")
    d["elig"] = [eligible(st[(a, t)]) for a, t in zip(d.arm, d.tid)]
    d["dbic"] = [st[(a, t)].get("dbic", np.nan) for a, t in zip(d.arm, d.tid)]
    off = d[(d.arm == "off") & d.elig]
    offall = d[d.arm == "off"]
    # population FPR 1%: weighted 99th percentile over ALL off positions (non-eligible count as below)
    x = np.where(offall.elig, offall.dbic, -np.inf)
    T = wquantile(x, offall.w.values, 0.99) if len(off) else np.inf
    T = max(T, 20.0)
    d["rise1"] = d.elig & (d.dbic >= T)
    if cmd == "tier2":
        run_tier(2, d[d.rise1])
        print("tier2 done", int(d.rise1.sum()))
        return
    lc2 = {(r["arm"], r["tid"]): r for r in (json.loads(f.read_text()) for f in CACHE.glob("t2_*.json"))}
    st2 = {k: stats(v, floor) for k, v in lc2.items()}
    d["rise2"] = [bool(r1 and (a, t) in st2 and eligible(st2[(a, t)]) and st2[(a, t)]["dbic"] >= T)
                  for r1, a, t in zip(d.rise1, d.arm, d.tid)]
    have2 = all((a, t) in st2 for a, t in zip(d[d.rise1].arm, d[d.rise1].tid))

    def arm_rate(g, col):
        return float(sum(gg[col].mean() * gg.N_stratum.iloc[0] for _, gg in g.groupby("stratum")) / g.N_arm.iloc[0])

    rng = np.random.default_rng(72)
    res = {"floor": {"s_abs": floor.s_abs, "s_rel": floor.s_rel}, "threshold_dbic": T, "tier2_complete": have2,
           "strata": [], "rates": {}}
    for col in ("rise1", "rise2"):
        r_on, r_off = arm_rate(d[d.arm == "on"], col), arm_rate(d[d.arm == "off"], col)
        boots = []
        for _ in range(2000):
            b = pd.concat([g.sample(len(g), replace=True, random_state=int(rng.integers(1e9)))
                           for _, g in d.groupby(["arm", "stratum"])])
            boots.append(arm_rate(b[b.arm == "on"], col) - arm_rate(b[b.arm == "off"], col))
        res["rates"][col] = {"on": r_on, "off": r_off, "diff": r_on - r_off,
                             "diff_ci95": [float(np.percentile(boots, 2.5)), float(np.percentile(boots, 97.5))]}
    for (stratum), g in d.groupby("stratum"):
        on, off_ = g[g.arm == "on"], g[g.arm == "off"]
        k1, k2 = int(on.rise2.sum()), int(off_.rise2.sum())
        res["strata"].append({"stratum": stratum, "on": [k1, len(on), int(on.N_stratum.iloc[0])],
                              "off": [k2, len(off_), int(off_.N_stratum.iloc[0])],
                              "tier1": [int(on.rise1.sum()), int(off_.rise1.sum())],
                              "fisher_p_one_sided": fisher_one_sided(k1, len(on), k2, len(off_))})
    lo = res["rates"]["rise2"]["diff_ci95"][0]
    res["verdict"] = "confirmed" if (have2 and lo > 0) else ("pending" if not have2 else "null")
    # injection-recovery on real clump backgrounds ('none' stratum, non-rises)
    base = [lcs[("on", t)] for t in d[(d.arm == "on") & (d.stratum == "none") & ~d.rise1].tid
            if len(lcs[("on", t)].get("flux", [])) >= 12]
    inj = []
    for mag in (16.0, 15.0, 14.5, 14.0, 13.5, 13.0, 12.0):
        A, rec = 10 ** (-0.4 * (mag - 22.5)), []
        for lc in base:
            v = np.array(lc["visit"])
            on_v = int(rng.integers(4, 16))
            f = np.array(lc["flux"]) + A * (v >= on_v)
            e = np.sqrt(np.array(lc["err"]) ** 2)
            s = stats({"visit": list(v), "flux": list(f), "err": list(e)}, floor)
            rec.append(eligible(s) and s["dbic"] >= T)
        inj.append({"mag": mag, "recovered": float(np.mean(rec)), "n": len(rec)})
    res["injection"] = inj
    # every rise, both arms, fully serialised (the viewer and the catalog use this list)
    rises = []
    for r in d[d.rise1].itertuples():
        s1, s2 = st[(r.arm, r.tid)], st2.get((r.arm, r.tid), {})
        lc = lcs[(r.arm, r.tid)]
        rises.append({"arm": r.arm, "tid": int(r.tid), "stratum": r.stratum, "e1_class": r.e1_class,
                      "ra": r.ra, "dec": r.dec, "tier1": s1, "tier2": s2, "confirmed": bool(r.rise2),
                      "year": [round(2013.95 + (x + 0.5) * 0.5, 2) for x in lc["visit"]],
                      "flux": [round(x, 1) for x in lc["flux"]],
                      "err": [round(float(x), 1) for x in floor.apply(lc["flux"], lc["err"])]})
    res["rises"] = rises
    for extra in ("injection_image", "negative_audit"):          # written by e7b_validation.py
        f = OUT / f"{extra}.json"
        if f.exists():
            res[extra] = json.loads(f.read_text())
    na = res.get("negative_audit", {})
    if "weighted_miss_ub95" in na:
        # tier-1 screening can only hide rises; bound the population rate of each arm from above by
        # r + m_ub * (1 - r), and report the range of the difference under the worst asymmetry
        r2 = res["rates"]["rise2"]
        m_on, m_off = na["weighted_miss_ub95"]["on"], na["weighted_miss_ub95"]["off"]
        r_on, r_off = r2["on"], r2["off"]
        r2["screening"] = {"miss_ub95_on": m_on, "miss_ub95_off": m_off,
                           "diff_range_adj": [r_on - (r_off + m_off * (1 - r_off)), (r_on + m_on * (1 - r_on)) - r_off]}
        # verdict rule unchanged (bootstrap LB > 0); screening can only widen the range, so a null stays null
        res["verdict_note"] = ("screening asymmetry cannot produce a confirmed verdict from a null one here; it widens the "
                               "range of the true difference to [%.1e, %.1e]" % tuple(r2["screening"]["diff_range_adj"]))
    (OUT / "results.json").write_text(json.dumps(clean(res)))
    print(json.dumps({k: v for k, v in res.items() if k not in ("rises",)}, indent=1, default=str)[:4000])


if __name__ == "__main__":
    main()
