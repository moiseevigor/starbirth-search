"""E7b validation (answers the second adversarial review): image-level injection and a tier-1 negative audit.

injection-image: PSF point sources of aperture W2 magnitude m are added to the actual L1b frames of
  clump positions ('none' stratum, tier-1 negatives) from a random onset visit on, then run through
  the real chain: quality-filtered forced photometry -> visit combination -> systematic floor ->
  change point -> offset-calibrated threshold (tier 1); a subsample also through tier 2 (mask +
  uncertainty images) and the difference-image gate (>= 5 sigma at the target).
audit-negatives: a random sample of tier-1 NEGATIVE clump positions is remeasured with mask +
  uncertainty images; the fraction that cross the threshold at tier 2 is the tier-1 screening miss rate.
Writes artifacts/e7b/injection_image.json and negative_audit.json (merged by e7b_symmetric.py analyze).
"""
from __future__ import annotations

import json
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "research"))
sys.path.insert(0, str(ROOT / "src"))
from e7b_symmetric import CACHE, OUT, clean, eligible, light_curve, stats  # noqa: E402
from starbirth.features.forced_phot import Floor  # noqa: E402
from viewer_imagery import diff_snr  # noqa: E402

MAGS = [16.0, 15.0, 14.5, 14.0, 13.5, 13.0, 12.0]
MAGS_T2 = [15.0, 14.0, 13.0]
AUDIT_N = {"none": 60, "steady": 20, "variable": 30}      # per arm and stratum


def cp_interval(k: int, n: int, cl: float = 0.95) -> tuple[float, float]:
    """Exact Clopper-Pearson interval for a binomial proportion, by bisection (no scipy)."""
    import math
    a = (1 - cl) / 2
    cdf = lambda p, kk: sum(math.comb(n, i) * p**i * (1 - p) ** (n - i) for i in range(kk + 1))  # noqa: E731

    def solve(f):
        lo, hi = 0.0, 1.0
        for _ in range(60):
            m = (lo + hi) / 2
            lo, hi = (m, hi) if f(m) > 0 else (lo, m)
        return (lo + hi) / 2
    lower = 0.0 if k == 0 else solve(lambda p: a - (1 - cdf(p, k - 1)))
    upper = 1.0 if k == n else solve(lambda p: cdf(p, k) - a)
    return lower, upper


def calib() -> tuple[Floor, float, dict]:
    res = json.loads((OUT / "results.json").read_text())
    return Floor(**res["floor"]), float(res["threshold_dbic"]), res


def negatives(res: dict, stratum: str | None, n: int, seed: int, arm: str = "on") -> pd.DataFrame:
    d = pd.read_csv(OUT / "design.csv")
    rise_tids = {r["tid"] for r in res["rises"] if r["arm"] == arm}
    d = d[(d.arm == arm) & ~d.tid.isin(rise_tids)]
    if stratum:
        d = d[d.stratum == stratum]
    return d.sample(min(n, len(d)), random_state=seed)


def injection_image(n_pos: int = 40, n_t2: int = 12, workers: int = 8) -> dict:
    floor, thr, res = calib()
    pos = negatives(res, "none", n_pos, 81)
    rng = np.random.default_rng(82)
    onsets = {int(t): int(rng.integers(4, 16)) for t in pos.tid}
    jobs = [(r, m, full) for full in (False, True) for m in (MAGS if not full else MAGS_T2)
            for r in pos.itertuples() if (not full or r.Index in pos.index[:n_t2])]

    def one(job):
        r, m, full = job
        A = 10 ** (-0.4 * (m - 22.5))
        f = CACHE / "inj" / f"{r.tid}_{m}_{'t2' if full else 't1'}.json"
        if f.exists():
            return json.loads(f.read_text())
        lc = light_curve(r.ra, r.dec, full=full, inject=(A, onsets[int(r.tid)]))
        st = stats(lc, floor)
        out = {"tid": int(r.tid), "mag": m, "tier": 2 if full else 1, "onset": onsets[int(r.tid)],
               "recovered": bool(eligible(st) and st["dbic"] >= thr and abs(int(st["onset_visit"]) - onsets[int(r.tid)]) <= 1),
               "dbic": st.get("dbic")}
        f.parent.mkdir(parents=True, exist_ok=True)
        f.write_text(json.dumps(clean(out)))
        return out
    with ThreadPoolExecutor(workers) as ex:
        rows = list(ex.map(one, jobs))
    df = pd.DataFrame(rows)
    t1 = df[df.tier == 1].groupby("mag").recovered.agg(["mean", "size"]).reset_index()
    t2 = df[df.tier == 2].groupby("mag").recovered.agg(["mean", "size"]).reset_index()
    # difference-image gate on the injected sources (first n_t2 positions, tier-2 magnitudes)
    gate = []
    for m in MAGS_T2:
        A = 10 ** (-0.4 * (m - 22.5))
        passed = []
        for r in pos.head(n_t2).itertuples():
            f = CACHE / "inj" / f"{r.tid}_{m}_diff.json"
            if f.exists():
                snr = json.loads(f.read_text())["snr"]
            else:
                snr = diff_snr(r.ra, r.dec, onsets[int(r.tid)], inject=(A, onsets[int(r.tid)]))
                f.write_text(json.dumps({"snr": snr}))
            passed.append(bool(snr is not None and snr >= 5))
        gate.append({"mag": m, "passed": float(np.mean(passed)), "n": len(passed)})
    # joint recovery = tier 1 AND tier 2 AND difference-image gate (>= 5 sigma), per position, on the subsample
    per_pos = []
    for m in MAGS_T2:
        for r in pos.head(n_t2).itertuples():
            a1 = df[(df.tier == 1) & (df.tid == r.tid) & (df.mag == m)].recovered
            a2 = df[(df.tier == 2) & (df.tid == r.tid) & (df.mag == m)].recovered
            f = CACHE / "inj" / f"{r.tid}_{m}_diff.json"
            snr = json.loads(f.read_text())["snr"] if f.exists() else None
            per_pos.append({"tid": int(r.tid), "mag": m, "tier1": bool(a1.iloc[0]) if len(a1) else None,
                            "tier2": bool(a2.iloc[0]) if len(a2) else None, "diff_snr": snr,
                            "joint": bool(len(a1) and a1.iloc[0] and len(a2) and a2.iloc[0] and snr is not None and snr >= 5)})
    pp = pd.DataFrame(per_pos)
    joint = [{"mag": float(m), "recovered": float(g.joint.mean()), "k": int(g.joint.sum()), "n": int(len(g)),
              "ci95": list(cp_interval(int(g.joint.sum()), int(len(g))))} for m, g in pp.groupby("mag")]
    out = {"n_positions": int(len(pos)), "onset_tolerance_visits": 1,
           "tier1": [{"mag": float(m), "recovered": float(a), "n": int(n), "ci95": list(cp_interval(int(round(a * n)), int(n)))}
                     for m, a, n in t1.itertuples(index=False)],
           "tier2": [{"mag": float(m), "recovered": float(a), "n": int(n), "ci95": list(cp_interval(int(round(a * n)), int(n)))}
                     for m, a, n in t2.itertuples(index=False)],
           "diff_gate": gate, "joint": joint, "per_position": per_pos}
    (OUT / "injection_image.json").write_text(json.dumps(out))
    print(json.dumps(out, indent=1))
    return out


def audit_negatives(workers: int = 12) -> dict:
    """Tier-2 remeasurement of tier-1 negatives in BOTH arms and every stratum (AUDIT_N per cell)."""
    floor, thr, res = calib()
    design = pd.read_csv(OUT / "design.csv")
    n_arm = int(design.N_arm.iloc[0])
    jobs = pd.concat([negatives(res, st, n, 83 + i, arm) for i, (arm, (st, n)) in
                      enumerate((a, kv) for a in ("on", "off") for kv in AUDIT_N.items())])

    def one(r):
        f = CACHE / f"t2neg_{r.arm}_{r.tid}.json"
        if f.exists():
            lc = json.loads(f.read_text())
        else:
            lc = light_curve(r.ra, r.dec, full=True)
            f.write_text(json.dumps(clean(lc)))
        st = stats(lc, floor)
        return {"arm": r.arm, "tid": int(r.tid), "stratum": r.stratum, "N_stratum": int(r.N_stratum),
                "dbic2": st.get("dbic"), "rise2": bool(eligible(st) and st["dbic"] >= thr)}
    with ThreadPoolExecutor(workers) as ex:
        rows = list(ex.map(one, jobs.itertuples()))
    df = pd.DataFrame(rows)
    cells, miss_ub = [], {}
    for (arm, st), g in df.groupby(["arm", "stratum"]):
        k, n = int(g.rise2.sum()), int(len(g))
        lo, hi = cp_interval(k, n)
        cells.append({"arm": arm, "stratum": st, "k": k, "n": n, "miss_rate": k / n, "ci95": [lo, hi],
                      "weight": float(g.N_stratum.iloc[0] / n_arm)})
    for arm in ("on", "off"):
        miss_ub[arm] = float(sum(c["weight"] * c["ci95"][1] for c in cells if c["arm"] == arm))
    out = {"n": int(len(df)), "became_rise": int(df.rise2.sum()), "cells": cells,
           "weighted_miss_ub95": miss_ub, "tids_became_rise": [[r.arm, int(r.tid)] for r in df[df.rise2].itertuples()]}
    (OUT / "negative_audit.json").write_text(json.dumps(out))
    print(json.dumps({k: v for k, v in out.items() if k != "cells"}, indent=1))
    print(pd.DataFrame(cells).round(3).to_string())
    return out


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "injection-image"
    {"injection-image": injection_image, "audit-negatives": audit_negatives}[cmd]()
