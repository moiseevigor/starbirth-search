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
    assert abs(w2_unextincted(5.5, np.array([0.42]), m_norm=12.16)[0] - 12.16) < 1e-9
    assert abs(w2_unextincted(55.0, np.array([4.2]), m_norm=12.16)[0] - (12.16 - 2.5 + 5)) < 1e-9


def test_e8_scalars_agree_with_bands_and_anchor_has_provenance():
    import json
    root = Path(__file__).parents[1]
    f = root / "artifacts" / "e8" / "extinction_budget.json"
    a = root / "data" / "hops_class0_mnorm.json"
    if not f.exists() or not a.exists():
        return                                        # artifacts not built in this checkout
    j, prov = json.load(open(f)), json.load(open(a))
    assert prov["source"].startswith("VizieR") and prov["n_used"] >= 50 and "sha256" in prov
    assert j["anchor"]["source"] == prov["source"]
    for p in j["per_lum"]:
        assert p["frac_detectable_no_ext"] == p["band_no_ext"][1]
        assert p["frac_detectable_clump_ext"] == p["band_clump_ext"][1]
