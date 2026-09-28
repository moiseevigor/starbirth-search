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
    k, dbic = ramp_vs_step(f, e, v, 8, 1000, 1600)
    assert dbic < 6


def test_gradual_rise_is_a_ramp():
    f, e, v = _curve("ramp")
    k, dbic = ramp_vs_step(f, e, v, 8, 1000, 1600)
    assert dbic >= 6 and 3 <= k <= 7


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
           "tiers": {"t1": {"file": f.name, "sha256": hashlib.sha256(f.read_bytes()).hexdigest(), "keys": {"on_1": {"stratum": "x"}, "on_2": {"stratum": "x"}}}}}
    (data / "lightcurves_manifest.json").write_text(json.dumps(man))
    monkeypatch.setattr(ce, "ROOT", tmp_path)
    try:
        ce.load_tracked(Floor(0.0, 0.0), 47.0)
        assert False, "missing key must fail"
    except RuntimeError as err:
        assert "missing" in str(err)
