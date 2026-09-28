import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).parents[1] / "research"))
sys.path.insert(0, str(Path(__file__).parents[1] / "src"))
from classify_events import ramp_vs_step  # noqa: E402


def _curve(kind, seed=0):
    rng = np.random.default_rng(seed)
    v = np.arange(21)
    f = np.full(21, 1000.0)
    if kind == "step":
        f[v >= 8] = 1600
    else:                                                    # ramp over 5 visits
        f = 1000 + 600 * np.clip((v - 8 + 1) / 5, 0, 1)
    f += rng.normal(0, 25, 21)
    return f, np.full(21, 25.0), v


def test_noisy_step_is_not_a_ramp():
    f, e, v = _curve("step")
    k, dbic = ramp_vs_step(f, e, v)
    assert dbic < 6


def test_gradual_rise_is_a_ramp_end_to_end():
    # the onset is found by the step scan (as in production), not supplied: the joint ramp fit must still win
    from classify_events import both_ways, features
    from starbirth.features.forced_phot import Floor
    f, e, v = _curve("ramp")
    st = both_ways({"visit": list(v), "flux": list(f), "err": list(e)}, Floor(0.0, 0.0))
    fe = features(st)
    assert fe["shape"] == "ramp" and 3 <= fe["rise_visits"] <= 7


def test_manifest_mismatch_fails_closed(tmp_path, monkeypatch):
    import gzip
    import hashlib
    import json
    import classify_events as ce
    from starbirth.features.forced_phot import Floor
    data = tmp_path / "data"; data.mkdir()
    f = data / "lightcurves_t1.csv.gz"
    with gzip.open(f, "wt") as g:
        g.write("arm,tid,visit,flux,err\non,1,0,1.0,1.0\n")
    man = {"threshold_dbic": 47.0, "floor": {"s_abs": 0.0, "s_rel": 0.0},
           "tiers": {"t1": {"file": f.name, "sha256": hashlib.sha256(f.read_bytes()).hexdigest(),
                            "keys": {"on_1": {"stratum": "x", "status": "ok"}, "on_2": {"stratum": "x", "status": "missing"}}}}}
    (data / "lightcurves_manifest.json").write_text(json.dumps(man))
    monkeypatch.setattr(ce, "ROOT", tmp_path)
    import export_lightcurves as ex
    monkeypatch.setattr(ex, "expected_universe", lambda: {"on_1": {}, "on_2": {}})
    try:
        ce.load_tracked(Floor(0.0, 0.0), 47.0)
        assert False, "a missing expected key must fail"
    except RuntimeError as err:
        assert "missing" in str(err)
    # a manifest that silently drops an expected key must also fail (the universe is independent of the cache)
    monkeypatch.setattr(ex, "expected_universe", lambda: {"on_1": {}, "on_2": {}, "on_3": {}})
    try:
        ce.load_tracked(Floor(0.0, 0.0), 47.0)
        assert False
    except RuntimeError as err:
        assert "expected universe" in str(err)


def test_ramp_duration_uses_visit_numbers_not_row_index():
    # a 4-visit ramp with visits 9 and 10 missing: row indices would compress it to ~2 rows
    v = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
    f = 1000 + 600 * np.clip((v - 8 + 1) / 4, 0, 1) + np.random.default_rng(2).normal(0, 20, v.size)
    k, dbic = ramp_vs_step(f, np.full(v.size, 20.0), v)
    assert dbic >= 6 and 3 <= k <= 5


def test_export_marks_failed_required_curves_fatal(tmp_path, monkeypatch):
    import json
    import export_lightcurves as ex
    monkeypatch.setattr(ex, "CACHE", tmp_path / "cache"); (tmp_path / "cache").mkdir()
    monkeypatch.setattr(ex, "DATA", tmp_path / "data"); monkeypatch.setattr(ex, "E7B", tmp_path / "e7b"); (tmp_path / "e7b").mkdir()
    (tmp_path / "data").mkdir(); (tmp_path / "data" / "twins.json").write_text("[]")
    (tmp_path / "e7b" / "results.json").write_text(json.dumps({"floor": {"s_abs": 0, "s_rel": 0}, "threshold_dbic": 47, "rises": []}))
    monkeypatch.setattr(ex, "expected_universe", lambda: {"on_1": {"group": "design", "stratum": "none"}})
    (tmp_path / "cache" / "t1_on_1.json").write_text(json.dumps({"error": "no frames"}))
    try:
        ex.main()
        assert False, "a failed required curve must abort the export"
    except SystemExit as err:
        assert "failed" in str(err)


def test_omitted_twin_in_manifest_fails_load(tmp_path, monkeypatch):
    import gzip
    import hashlib
    import json
    import classify_events as ce
    import export_lightcurves as ex
    from starbirth.features.forced_phot import Floor
    data = tmp_path / "data"; data.mkdir()
    def csv(name, rows):
        f = data / name
        with gzip.open(f, "wt") as g:
            g.write("arm,tid,visit,flux,err\n" + "".join(rows))
        return f
    f1 = csv("lightcurves_t1.csv.gz", ["on,1,0,1.0,1.0\n", "off,1,0,1.0,1.0\n"])
    f2 = csv("lightcurves_t2.csv.gz", ["on,1,0,1.0,1.0\n"])
    man = {"threshold_dbic": 47.0, "floor": {"s_abs": 0.0, "s_rel": 0.0}, "required_t2": ["on_1"],   # twin off_1 omitted
           "tiers": {"t1": {"file": f1.name, "sha256": hashlib.sha256(f1.read_bytes()).hexdigest(),
                            "keys": {"on_1": {"stratum": "x", "status": "ok"}, "off_1": {"stratum": "twin", "status": "ok"}}},
                     "t2": {"file": f2.name, "sha256": hashlib.sha256(f2.read_bytes()).hexdigest(),
                            "keys": {"on_1": {"stratum": "x", "status": "ok"}}}}}
    (data / "lightcurves_manifest.json").write_text(json.dumps(man))
    monkeypatch.setattr(ce, "ROOT", tmp_path)
    monkeypatch.setattr(ex, "expected_universe", lambda: {"on_1": {}, "off_1": {}})
    monkeypatch.setattr(ex, "required_t2_from_tracked_inputs", lambda: {"on_1", "off_1"})   # tracked truth includes the twin
    try:
        ce.load_tracked(Floor(0.0, 0.0), 47.0)
        assert False, "an omitted required twin must fail the load"
    except RuntimeError as err:
        assert "differs from the tracked inputs" in str(err)
