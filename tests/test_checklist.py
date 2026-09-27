import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parents[1] / "research"))
from build_catalog import checklist  # noqa: E402


def _detail(**over):
    d = {
        "arm": "on",
        "forced": {"tier1": {"onset_visit": 10, "post_sig": 12.0, "pre_sig": 0.8},
                   "tier2": {"onset_visit": 10, "post_sig": 12.0, "pre_sig": 0.8}, "confirmed": True},
        "archive": {"coverage": [200] * 22, "glimpse": [], "spicy": [], "allwise": []},
        "e1_rows": {"t": [], "snr": [], "sep": []},
        "diff_snr": 9.0, "offset_status": "quiet",
    }
    d.update(over)
    return d


def test_clean_case_is_birth_compatible():
    items, verdict = checklist(_detail())
    assert verdict == "birth-compatible" and all(i["pass"] for i in items) and len(items) == 9


def test_bright_pre_onset_flux_refutes():
    # c868 / c1743: a 20-34 sigma source before onset is a brightening, not a birth
    d = _detail()
    d["forced"]["tier2"]["pre_sig"] = 20.1
    _, verdict = checklist(d)
    assert "pre_quiet" in verdict


def test_source_inside_aperture_but_beyond_3_arcsec_refutes():
    # c868: Spitzer Class I at 3.19" sat outside the old 3" test but inside the 5.5" aperture
    d = _detail(archive={"coverage": [200] * 22, "glimpse": [{"sep": 3.19}], "spicy": [], "allwise": []})
    _, verdict = checklist(d)
    assert "no_spitzer" in verdict


def test_prior_spitzer_source_refutes():
    d = _detail(archive={"coverage": [200] * 22, "glimpse": [{"sep": 2.7}], "spicy": [], "allwise": []})
    _, verdict = checklist(d)
    assert verdict.startswith("refuted") and "no_spitzer" in verdict


def test_catalog_detection_before_onset_refutes():
    d = _detail(e1_rows={"t": [2015.0], "snr": [8.0], "sep": [1.0]})
    _, verdict = checklist(d)
    assert "no_catalog_pre" in verdict


def test_uncovered_pre_onset_and_weak_diff_refute():
    d = _detail(archive={"coverage": [0] * 10 + [200] * 12, "glimpse": [], "spicy": [], "allwise": []}, diff_snr=2.0)
    _, verdict = checklist(d)
    assert "covered_pre" in verdict and "diff_source" in verdict


def test_unmeasured_or_rising_offset_twin_refutes():
    for status in ("unmeasured", "rise"):
        _, verdict = checklist(_detail(offset_status=status))
        assert "offset_quiet" in verdict, status


def test_negative_baseline_refutes():
    # a -7 sigma pre-onset flux is a failed sky model, not evidence of an empty position
    d = _detail()
    d["forced"]["tier2"]["pre_sig"] = -7.2
    _, verdict = checklist(d)
    assert "pre_quiet" in verdict


def test_gallery_cards_render_checks_out_of_n():
    html = (Path(__file__).parents[1] / "viewer" / "catalog.html").read_text()
    assert "${g.passes}/${g.n_checks}" in html and "${g.passes}/8" not in html


def test_offset_arm_is_labelled_control():
    _, verdict = checklist(_detail(arm="off"))
    assert verdict.startswith("control:")
