import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parents[1] / "research"))
from build_catalog import checklist  # noqa: E402


def _detail(**over):
    d = {
        "arm": "on",
        "forced": {"tier1": {"onset_visit": 10, "post_sig": 12.0}, "tier2": {"onset_visit": 10, "post_sig": 12.0}, "confirmed": True},
        "archive": {"coverage": [200] * 22, "glimpse": [], "spicy": [], "allwise": []},
        "e1_rows": {"t": [], "snr": [], "sep": []},
        "diff_snr": 9.0, "offset_rise": False,
    }
    d.update(over)
    return d


def test_clean_case_is_birth_compatible():
    items, verdict = checklist(_detail())
    assert verdict == "birth-compatible" and all(i["pass"] for i in items) and len(items) == 8


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


def test_offset_arm_is_labelled_control():
    _, verdict = checklist(_detail(arm="off"))
    assert verdict.startswith("control:")
