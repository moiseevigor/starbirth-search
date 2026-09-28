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


def test_every_displayed_alternative_has_inspectable_evidence():
    import json
    from pathlib import Path as P
    root = P(__file__).parents[1]
    idx = root / "viewer" / "catalog" / "index.js"
    if not idx.exists():
        return
    js = json.loads(idx.read_text().split("=", 1)[1].rstrip().rstrip(";"))
    checked = 0
    for g in js["gallery"]:
        if not g.get("alternative"):
            continue
        d = json.loads((root / "viewer" / "catalog" / f"{g['key']}.json").read_text())
        A = d.get("alternatives")
        if A is None:
            continue                     # details built before E9 ran: rescore refreshes them
        assert A["best"] == g["alternative"] and A["evidence"] and A["priority_path"]
        E = A["evidence"]
        if A["best"].startswith("known star with optical counterpart"):
            assert E["gaia_sources"] or E["simbad_rows"] or E["spicy_rows"]
        if A["best"].startswith("AGB"):
            assert any("LPV" == s.get("best_class_name") for s in E["gaia_sources"]) or E["simbad_rows"]
        checked += 1
    assert checked > 0 or not any(g.get("alternative") for g in js["gallery"])
