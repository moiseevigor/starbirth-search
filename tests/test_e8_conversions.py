import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).parents[1] / "research"))
from e8_extinction_budget import a45_from_sigma, w2_unextincted  # noqa: E402


def test_sigma_to_extinction_chain():
    # Sigma = 0.1 g cm^-2 -> N_H2 = 2.13e22 -> A_V = 22.8 -> A_K = 2.56 -> A_4.5 = 1.10 mag (whole column)
    a45 = a45_from_sigma(np.array([0.1]))[0]
    assert abs(a45 - 1.10) < 0.02


def test_w2_scaling_anchors_on_hops():
    assert abs(w2_unextincted(5.5, np.array([0.42]))[0] - 12.16) < 1e-9
    assert abs(w2_unextincted(55.0, np.array([4.2]))[0] - (12.16 - 2.5 + 5)) < 1e-9
