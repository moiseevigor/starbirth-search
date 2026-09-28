import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).parents[1] / "research"))
sys.path.insert(0, str(Path(__file__).parents[1] / "src"))
from e9_alternatives import periodicity  # noqa: E402


def test_cadence_window_peak_is_not_periodic():
    t = 2014 + np.arange(21) * 0.5
    f = 1000 + 200 * np.sin(2 * np.pi * t * 365.25 / 182.625)   # exactly at the sampling cadence
    r = periodicity(list(t), list(f), [20] * 21)
    assert r["window_peak"] and not r["periodic"]


def test_e9_verdict_is_withheld_when_incomplete():
    import json
    root = Path(__file__).parents[1]
    f = root / "artifacts" / "e9" / "alternatives.json"
    if not f.exists():
        return
    sm = json.load(open(f))["summary"]
    assert "complete" in sm and (sm["complete"] == (sm["n_with_details"] == sm["n_events"] and not sm["gaia_failed"]))
