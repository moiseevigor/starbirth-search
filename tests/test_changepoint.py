import numpy as np
from starbirth.features.change_point import best_persistent_step


def test_detects_clear_step():
    rng = np.random.default_rng(1)
    y = np.r_[rng.normal(0, 1, 100), rng.normal(4, 1, 100)]
    s = np.ones_like(y)
    r = best_persistent_step(y, s, min_points_each_side=20)
    assert r.index is not None
    assert abs(r.index - 100) <= 5
    assert r.delta_bic > 20
    assert r.amplitude > 3


def test_no_strong_step_in_noise():
    rng = np.random.default_rng(2)
    y = rng.normal(0, 1, 200)
    s = np.ones_like(y)
    r = best_persistent_step(y, s, min_points_each_side=20)
    assert r.delta_bic < 20
