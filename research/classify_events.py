"""Feature classification of every measured light curve (both arms) for the event gallery.

An 'event' is any light curve whose best two-level model beats a constant by the E7b threshold
(delta-BIC >= T, onset in visits 3-19), in EITHER direction. Features (all from the forced W2
light curve, the NEOWISE catalog rows and the archival bundle):
  amp_mag      -2.5 log10(post / pre) when pre > 3 sigma, else 'appearance' (pre consistent
               with zero) or 'unusable' (pre < -3 sigma: sky-model failure)
  shape        step (persistent, last 3 visits within 2 sigma of the post level) | flare (returns
               to within 2 sigma of the pre level) | ramp (rise spans >= 3 visits) | fade | dip
  rise_visits  visits between 10% and 90% of the step (ramp duration)
  colour       W1-W2 change (post minus pre) from catalog detections within 6", if both exist
  counterpart  SPICY class / AllWISE / MIPSGAL / SIMBAD star within the 5.5" aperture, or none
Primary label (priority): appearance > outburst (>= 2 mag) > brightening (>= 0.5) > fade/dip
(<= -0.5) > flare > ramp > weak.  Writes artifacts/gallery/events.json.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "research"))
sys.path.insert(0, str(ROOT / "src"))
from e7b_symmetric import CACHE, OUT as E7B, clean, stats  # noqa: E402
from starbirth.features.change_point import best_persistent_step  # noqa: E402
from starbirth.features.forced_phot import Floor  # noqa: E402

GAL = ROOT / "artifacts" / "gallery"
NEO0 = 56640.0


def load_tracked(floor: Floor, thr: float) -> dict:
    """Light curves from the tracked export; verifies the manifest (hashes, calibration) and fails on any mismatch."""
    import gzip
    import hashlib
    data = ROOT / "data"
    man = json.loads((data / "lightcurves_manifest.json").read_text())
    if abs(man["threshold_dbic"] - thr) > 1e-9 or man["floor"] != {"s_abs": floor.s_abs, "s_rel": floor.s_rel}:
        raise RuntimeError("manifest calibration differs from artifacts/e7b/results.json: re-run export_lightcurves.py")
    out = {}
    for tier, m in man["tiers"].items():
        f = data / m["file"]
        if hashlib.sha256(f.read_bytes()).hexdigest() != m["sha256"]:
            raise RuntimeError(f"{f.name} does not match its manifest hash")
        with gzip.open(f, "rt") as g:
            df = pd.read_csv(g)
        got = {f"{a}_{t}" for a, t in zip(df.arm, df.tid)}
        exp = set(m["keys"])
        if got != exp:
            raise RuntimeError(f"{tier}: {len(exp - got)} manifest keys missing, {len(got - exp)} extra: "
                               f"{sorted(exp ^ got)[:5]}")
        out[tier] = {(a, int(t)): {"visit": g.visit.tolist(), "flux": g.flux.tolist(), "err": g.err.tolist(),
                                   "stratum": m["keys"][f"{a}_{t}"]["stratum"]}
                     for (a, t), g in df.groupby(["arm", "tid"])}
    return out


def both_ways(lc: dict, floor: Floor) -> dict | None:
    """Best step in either direction with the same significance rule as E7b."""
    f, e, v = np.array(lc.get("flux", [])), np.array(lc.get("err", [])), np.array(lc.get("visit", []))
    if f.size < 8:
        return None
    e2 = floor.apply(f, e)
    cp = best_persistent_step(f, e2, min_points_each_side=3)
    if cp.index is None or cp.index >= v.size:
        return None
    onset = int(v[cp.index])
    pre, post = v < onset, v >= onset
    sem = lambda m: float(np.sqrt(np.sum(e2[m] ** 2)) / m.sum())  # noqa: E731
    return {"dbic": float(cp.delta_bic), "step": float(cp.amplitude), "onset_visit": onset,
            "pre": float(f[pre].mean()), "post": float(f[post].mean()), "pre_sig": float(f[pre].mean() / sem(pre)),
            "post_sig": float(f[post].mean() / sem(post)), "f": f, "e": e2, "v": v, "pre_m": pre, "post_m": post}


def ramp_vs_step(f, e, v, onset, pre, post) -> tuple[int, float]:
    """Compare a step at `onset` with linear ramps from `onset` lasting k visits (k = 2..8); returns the ramp
    duration (visits) and delta-BIC(step - ramp); positive = the ramp is preferred (one extra parameter)."""
    idx = np.arange(f.size)
    i0 = int(np.searchsorted(v, onset))
    step_m = np.where(idx < i0, pre, post)
    chi_step = float(np.sum(((f - step_m) / e) ** 2))
    best_k, best_chi = 1, np.inf
    for k in range(2, 9):
        frac = np.clip((v - onset) / (k * 1.0) + 1 / k, 0, 1)        # 0 before onset, 1 after k visits
        frac[idx < i0] = 0
        m = pre + frac * (post - pre)
        chi = float(np.sum(((f - m) / e) ** 2))
        if chi < best_chi:
            best_k, best_chi = k, chi
    n = f.size
    dbic = (chi_step + 3 * np.log(n)) - (best_chi + 4 * np.log(n))
    return best_k, float(dbic)


def features(s: dict) -> dict:
    f, e, v, pre, post = s["f"], s["e"], s["v"], s["pre_m"], s["post_m"]
    up = s["step"] > 0
    if s["pre_sig"] < -3:
        amp, amp_class = None, "unusable"
    elif s["pre_sig"] < 3 and up:
        amp, amp_class = None, "appearance"
    elif s["pre"] > 0 and s["post"] > 0:
        amp = float(-2.5 * np.log10(s["post"] / s["pre"]))          # negative = brighter
        amp_class = "measured"
    else:
        amp, amp_class = None, "unusable"
    # shape: does it come back? how long does the transition take?
    tail = f[post][-3:] if post.sum() >= 3 else f[post]
    tail_e = e[post][-3:] if post.sum() >= 3 else e[post]
    back_to_pre = bool(np.all(np.abs(tail - s["pre"]) <= 2 * tail_e)) if pre.any() else False
    at_post = bool(np.all(np.abs(tail - s["post"]) <= 2 * tail_e))
    rise_visits, ramp_dbic = ramp_vs_step(f, e, v, s["onset_visit"], s["pre"], s["post"])
    if up:
        shape = "flare" if back_to_pre and not at_post else ("ramp" if ramp_dbic >= 6 else "step")
    else:
        shape = "dip" if back_to_pre and not at_post else "fade"
    if amp_class == "appearance":
        primary = "appearance"
    elif amp is not None and amp <= -2.0:
        primary = "outburst"
    elif amp is not None and amp <= -0.5:
        primary = "brightening"
    elif amp is not None and amp >= 0.5:
        primary = "fade" if shape == "fade" else "dip"
    elif shape == "flare":
        primary = "flare"
    elif shape == "ramp":
        primary = "slow ramp"
    elif amp_class == "unusable":
        primary = "unusable baseline"
    else:
        primary = "weak"
    return {"amp_mag": None if amp is None else round(amp, 2), "amp_class": amp_class, "shape": shape,
            "rise_visits": rise_visits, "primary": primary, "direction": "up" if up else "down",
            "onset_year": round(2013.95 + (s["onset_visit"] + 0.5) * 0.5, 2), "dbic": round(s["dbic"]),
            "pre_sig": round(s["pre_sig"], 1), "post_sig": round(s["post_sig"], 1),
            "year": [round(2013.95 + (x + 0.5) * 0.5, 2) for x in v], "flux": [round(float(x), 1) for x in f],
            "err": [round(float(x), 1) for x in e]}


def colour_change(rows: pd.DataFrame, tid: int, onset_visit: int) -> dict | None:
    g = rows[(rows.tid == tid) & (rows.w2snr >= 5)]
    if g.empty or "w1mpro" not in g:
        return None
    g = g.dropna(subset=["w1mpro", "w2mpro"])
    v = ((g.mjd - NEO0) // 182.625).astype(int)
    pre, post = g[v < onset_visit], g[v >= onset_visit]
    if len(pre) < 3 or len(post) < 3:
        return None
    c_pre, c_post = float((pre.w1mpro - pre.w2mpro).median()), float((post.w1mpro - post.w2mpro).median())
    return {"w1w2_pre": round(c_pre, 2), "w1w2_post": round(c_post, 2), "d_w1w2": round(c_post - c_pre, 2)}


def main() -> None:
    res = json.loads((E7B / "results.json").read_text())
    floor, thr = Floor(**res["floor"]), float(res["threshold_dbic"])
    s = pd.read_csv(ROOT / "artifacts" / "e1_full" / "pilot_targets.csv")
    rows = {a: pd.read_csv(ROOT / "artifacts" / "e1_full" / f"neowise_rows_{a}.csv") for a in ("on", "off")}
    design = pd.read_csv(E7B / "design.csv")
    in_design = {(a, t): st for a, t, st in zip(design.arm, design.tid, design.stratum)}
    lcs = load_tracked(floor, thr)
    events = []
    for (arm, tid), lc in sorted(lcs["t1"].items()):
        st = both_ways(lc, floor)
        if st is None or st["dbic"] < thr or not (3 <= st["onset_visit"] <= 19):
            continue
        t2 = both_ways(lcs["t2"][(arm, tid)], floor) if (arm, tid) in lcs["t2"] else None
        fe = features(st)
        ev = {"key": f"{'c' if arm == 'on' else 'x'}{tid}", "arm": arm, "tid": tid, "designation": s.designation[tid],
              "ra": float(s.ra[tid]), "dec": float(s.dec[tid]) + (60 / 3600 if arm == "off" else 0),
              "stratum": in_design.get((arm, tid), lc.get("stratum", "extended")),
              "in_e7b_design": (arm, tid) in in_design,
              "tier2_confirmed": bool(t2 and t2["dbic"] >= thr and np.sign(t2["step"]) == np.sign(st["step"])),
              "colour": colour_change(rows[arm], tid, st["onset_visit"]), **fe}
        events.append(ev)
    GAL.mkdir(parents=True, exist_ok=True)
    (GAL / "events.json").write_text(json.dumps(clean(events)))
    df = pd.DataFrame(events)
    print(f"{len(df)} events; by arm/primary:")
    print(df.groupby(["arm", "primary"]).size().unstack(fill_value=0).to_string())


if __name__ == "__main__":
    main()
