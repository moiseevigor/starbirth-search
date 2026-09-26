import numpy as np
import pandas as pd

from starbirth.features.turn_on import N_VISITS, NEO_START_MJD, VISIT_DAYS, classify


def _rows(tid, visits, offset_arcsec=0.0, snr=20.0, jitter=0.0, seed=0):
    rng = np.random.default_rng(seed)
    visits = np.repeat(np.asarray(list(visits)), 12)  # ~12 exposures per visit
    n = len(visits)
    dra = (offset_arcsec + rng.normal(0, jitter, n)) / 3600
    return pd.DataFrame({
        "tid": tid, "t_ra": 100.0, "t_dec": 0.0, "ra": 100.0 + dra, "dec": 0.0,
        "mjd": NEO_START_MJD + np.asarray(visits) * VISIT_DAYS + 1, "w2snr": snr, "cc_flags": "0000",
    })


def test_classes():
    rows = pd.concat([
        _rows(0, range(10, N_VISITS)),          # bright turn-on
        _rows(1, range(N_VISITS)),              # steady
        _rows(2, [5, 12]),                      # sporadic
        _rows(3, range(10, N_VISITS), snr=6),   # late but faint: not significant
    ])
    c = classify(rows, 5)
    assert c.to_dict() == {0: "turn_on", 1: "steady", 2: "other", 3: "other", 4: "none"}


def test_edge_source_is_not_turn_on():
    # steady source at 2.9" with 0.3" scatter (E1-pilot tid 247): a fixed 3"
    # aperture drops ~40% of visits at random; tracking must keep every visit.
    rows = _rows(0, range(N_VISITS), offset_arcsec=2.9, jitter=0.3, seed=3)
    assert (np.abs(rows.ra - 100.0) * 3600 > 3).sum() >= 5  # the fixed aperture would lose these
    c = classify(rows, 1)
    assert c[0] == "steady"


def test_steady_neighbour_outliers_are_confused():
    # E1-pilot tid 1768: steady W2=10.6 star at 5" (every visit) whose rare
    # astrometric outliers fall within 3" in late visits only.
    star = _rows(0, np.repeat(np.arange(N_VISITS), 10), offset_arcsec=5.0, snr=50)
    outl = _rows(0, range(8, N_VISITS), offset_arcsec=1.5, snr=50)
    c = classify(pd.concat([star, outl]), 1)
    assert c[0] == "confused"


def test_flagged_steady_star_is_confused():
    # E1-pilot tid 362: steady W2~9.5 star, halo-flagged in almost every exposure,
    # a few clean ('0') exposures only in late visits.
    flagged = _rows(0, np.repeat(np.arange(N_VISITS), 10), snr=50).assign(cc_flags="0h00")
    rare = _rows(0, range(8, N_VISITS), snr=50)
    c = classify(pd.concat([flagged, rare]), 1)
    assert c[0] == "confused"


def test_single_exposure_detections_do_not_count():
    # offset-control tid 1463: one detection out of ~12 exposures per visit, late only
    one = _rows(0, range(8, N_VISITS), snr=15)
    one = one.groupby("mjd").head(1)
    assert classify(one, 1)[0] != "turn_on"
