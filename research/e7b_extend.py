"""Extend E7b tier-1 forced photometry to every on-arm position of a stratum (for the event gallery).

The E7b population estimate keeps its pre-registered sample (design.csv); these extra light curves
are used only to find more events for the feature-classified gallery and are cached under the same
naming (t1_on_<tid>.json), which the E7b analysis ignores because they are not in design.csv.
Usage: e7b_extend.py steady|variable|none [--workers N]
"""
from __future__ import annotations

import json
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "research"))
sys.path.insert(0, str(ROOT / "src"))
from e7b_symmetric import CACHE, STRATA, clean, light_curve  # noqa: E402
from starbirth.features.turn_on import classify  # noqa: E402


def main() -> None:
    stratum = sys.argv[1]
    workers = int(sys.argv[sys.argv.index("--workers") + 1]) if "--workers" in sys.argv else 12
    s = pd.read_csv(ROOT / "artifacts" / "e1_full" / "pilot_targets.csv")
    cls = classify(pd.read_csv(ROOT / "artifacts" / "e1_full" / "neowise_rows_on.csv"), len(s))
    tids = [int(t) for t in cls.index[cls.isin(STRATA[stratum])] if not (CACHE / f"t1_on_{t}.json").exists()]
    print(f"{stratum}: {len(tids)} positions to measure", flush=True)

    def one(t):
        r = light_curve(float(s.ra[t]), float(s.dec[t]))
        r.update(arm="on", tid=t, stratum=stratum, extended=True)
        (CACHE / f"t1_on_{t}.json").write_text(json.dumps(clean(r)))
    with ThreadPoolExecutor(workers) as ex:
        list(ex.map(one, tids))
    print("done", len(tids))


if __name__ == "__main__":
    main()
