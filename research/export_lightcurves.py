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


def main() -> None:
    DATA.mkdir(exist_ok=True)
    res = json.loads((E7B / "results.json").read_text())
    design = pd.read_csv(E7B / "design.csv")
    in_design = {(a, int(t)): st for a, t, st in zip(design.arm, design.tid, design.stratum)}
    manifest = {"created": str(date.today()), "floor": res["floor"], "threshold_dbic": res["threshold_dbic"],
                "git_commit": subprocess.run(["git", "rev-parse", "HEAD"], capture_output=True, text=True, cwd=ROOT).stdout.strip(),
                "tiers": {}}
    for tier in (1, 2):
        rows, keys, empty = [], {}, []
        for f in sorted(CACHE.glob(f"t{tier}_*.json")):
            _, arm, tid = f.stem.split("_")
            lc = json.loads(f.read_text())
            if "visit" not in lc:
                continue
            key = f"{arm}_{tid}"
            if not lc["visit"]:                       # measured, but no usable visit: recorded, not expected as rows
                empty.append(key)
                continue
            keys[key] = {"stratum": in_design.get((arm, int(tid)), lc.get("stratum", "extended")),
                         "in_design": (arm, int(tid)) in in_design, "n_frames": lc.get("n_frames"), "n_good": lc.get("n_good")}
            rows += [{"arm": arm, "tid": int(tid), "visit": v, "flux": round(x, 3), "err": round(e, 3)}
                     for v, x, e in zip(lc["visit"], lc["flux"], lc["err"])]
        out = DATA / f"lightcurves_t{tier}.csv.gz"
        with gzip.open(out, "wt", newline="") as g:
            pd.DataFrame(rows).sort_values(["arm", "tid", "visit"]).to_csv(g, index=False)
        manifest["tiers"][f"t{tier}"] = {"file": out.name, "sha256": sha(out), "n_keys": len(keys), "n_rows": len(rows),
                                         "keys": keys, "empty_keys": empty}
        print(f"tier {tier}: {len(keys)} light curves, {len(rows)} rows -> {out.name} ({out.stat().st_size / 1e6:.2f} MB)")
    (DATA / "lightcurves_manifest.json").write_text(json.dumps(manifest, indent=0))
    print("manifest written")


if __name__ == "__main__":
    main()
