"""Export every forced light curve from the (ignored) cache into tracked, hashed inputs.

data/lightcurves_t1.csv.gz / lightcurves_t2.csv.gz : one row per (arm, tid, visit) with flux, err
data/lightcurves_manifest.json                     : keys per tier, sha256 of each export, E7b floor and
                                                     threshold, git commit, n_frames/n_good per key
classify_events.py reads ONLY these files and fails on any manifest mismatch, so a clean checkout
reproduces the event population exactly.
"""
from __future__ import annotations

import gzip
import hashlib
import json
import subprocess
import sys
from datetime import date
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "research"))
from e7b_symmetric import CACHE, OUT as E7B  # noqa: E402

DATA = ROOT / "data"


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def required_t2_from_tracked_inputs() -> set[str]:
    """Required tier-2 keys, from tracked inputs only: every E7b tier-1 rise (artifacts/e7b/results.json) and the
    60\" twin of every clump candidate (data/twins.json, which must exist). Used by export AND load."""
    res = json.loads((E7B / "results.json").read_text())
    twins_file = DATA / "twins.json"
    if not twins_file.exists():
        raise RuntimeError("data/twins.json is missing: the required tier-2 set cannot be defined")
    twins = json.loads(twins_file.read_text())
    return {f"{r['arm']}_{int(r['tid'])}" for r in res["rises"]} | {f"off_{int(t)}" for t in twins}


def expected_universe() -> dict[str, dict]:
    """Expected light-curve keys from TRACKED inputs only (never from the cache):
    design.csv (both arms), the E1 class table for the extended 'steady' stratum (on arm), and the
    tracked list of offset twins data/twins.json (on-arm candidate tids whose 60" twin is measured)."""
    design = pd.read_csv(E7B / "design.csv")
    uni = {f"{a}_{int(t)}": {"group": "design", "stratum": st} for a, t, st in zip(design.arm, design.tid, design.stratum)}
    cls = pd.read_csv(ROOT / "artifacts" / "e1_full" / "classes.csv", index_col="tid")
    for t in cls.index[cls["on"] == "steady"]:
        uni.setdefault(f"on_{int(t)}", {"group": "extended", "stratum": "steady"})
    twins = json.loads((DATA / "twins.json").read_text()) if (DATA / "twins.json").exists() else []
    for t in twins:
        uni.setdefault(f"off_{int(t)}", {"group": "twin", "stratum": "twin"})
    return uni


def main() -> None:
    DATA.mkdir(exist_ok=True)
    res = json.loads((E7B / "results.json").read_text())
    uni = expected_universe()
    manifest = {"created": str(date.today()), "floor": res["floor"], "threshold_dbic": res["threshold_dbic"],
                "git_commit": subprocess.run(["git", "rev-parse", "HEAD"], capture_output=True, text=True, cwd=ROOT).stdout.strip(),
                "universe_size": len(uni), "tiers": {}}
    required_t2 = required_t2_from_tracked_inputs()
    manifest["required_t2"] = sorted(required_t2)
    for tier in (1, 2):
        rows, status = [], {}
        if tier == 1:
            expected = uni
        else:
            optional = {k: {"group": "optional", "stratum": uni.get(k, {}).get("stratum", "audit/injection")}
                        for k in (f.stem[3:] for f in CACHE.glob("t2_*.json")) if k not in required_t2}
            expected = {**{k: {**uni.get(k, {"group": "required"}), "required": True} for k in required_t2}, **optional}
        for key, meta in expected.items():
            f = CACHE / f"t{tier}_{key}.json"
            if not f.exists():
                status[key] = {**meta, "status": "missing"}
                continue
            lc = json.loads(f.read_text())
            if "error" in lc or "visit" not in lc:
                status[key] = {**meta, "status": "failed", "error": str(lc.get("error", "no data"))[:80]}
            elif not lc["visit"]:
                status[key] = {**meta, "status": "empty", "n_frames": lc.get("n_frames"), "n_good": lc.get("n_good")}
            else:
                status[key] = {**meta, "status": "ok", "n_frames": lc.get("n_frames"), "n_good": lc.get("n_good")}
                arm, tid = key.split("_")
                rows += [{"arm": arm, "tid": int(tid), "visit": v, "flux": round(x, 3), "err": round(e, 3)}
                         for v, x, e in zip(lc["visit"], lc["flux"], lc["err"])]
        req = {k for k, v in expected.items() if tier == 1 or v.get("required")}
        bad = sorted(k for k, v in status.items() if k in req and v["status"] in ("missing", "failed"))
        if bad:
            raise SystemExit(f"tier {tier}: {len(bad)} required light curves are missing or failed "
                             f"(e.g. {bad[:5]}); measure them before exporting")
        out = DATA / f"lightcurves_t{tier}.csv.gz"
        with gzip.open(out, "wt", newline="") as g:
            pd.DataFrame(rows).sort_values(["arm", "tid", "visit"]).to_csv(g, index=False)
        counts = pd.Series([v["status"] for v in status.values()]).value_counts().to_dict()
        manifest["tiers"][f"t{tier}"] = {"file": out.name, "sha256": sha(out), "n_rows": len(rows), "status_counts": counts,
                                         "keys": status}
        print(f"tier {tier}: {counts} -> {out.name} ({out.stat().st_size / 1e6:.2f} MB)")
    (DATA / "lightcurves_manifest.json").write_text(json.dumps(manifest, indent=0))
    print("manifest written")


if __name__ == "__main__":
    main()
