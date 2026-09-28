import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parents[1] / "research"))
from build_catalog import checklist  # noqa: E402


def _detail(**over):
    d = {
        "arm": "on",
        "forced": {"tier1": {"onset_visit": 10, "post_sig": 12.0, "pre_sig": 0.8},
                   "tier2": {"onset_visit": 10, "post_sig": 12.0, "pre_sig": 0.8}, "confirmed": True},
        "archive": {"coverage": [200] * 22, "glimpse": [], "spicy": [], "allwise": [], "mipsgal": [],
                    "simbad": [{"main_id": "HIGALBM G30.0+0.0", "otype": "smm", "sep": 0.1}]},
        "props": {"glon": 30.0, "glat": 0.2},
        "e1_rows": {"t": [], "snr": [], "sep": []},
        "diff_snr": 9.0, "offset_status": "quiet",
    }
    d.update(over)
    return d


def test_clean_case_is_birth_compatible():
    items, verdict = checklist(_detail())
    assert verdict == "birth-compatible" and all(i["pass"] for i in items) and len(items) == 11


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


def test_mipsgal_and_simbad_star_refute_but_clump_entry_does_not():
    base = _detail()
    d = _detail(archive={**base["archive"], "mipsgal": [{"mag_24": 6.4, "sep": 3.4}]})
    assert "no_mipsgal" in checklist(d)[1]
    d = _detail(archive={**base["archive"], "simbad": [{"main_id": "SPICY 1", "otype": "Y*?", "sep": 2.0}]})
    assert "no_simbad_star" in checklist(d)[1]
    assert checklist(_detail())[1] == "birth-compatible"          # the 'smm' clump entry is ignored


def test_uncovered_archive_is_unverifiable_not_pass():
    d = _detail(props={"glon": 120.0, "glat": 2.5})               # outside every Spitzer plane survey
    items, verdict = checklist(d)
    na = [i["id"] for i in items if i["na"]]
    assert "no_spitzer" in na and "no_mipsgal" in na and verdict.startswith("birth-compatible (unverifiable")


def test_tier1_only_twin_is_not_a_pass():
    _, verdict = checklist(_detail(offset_status="quiet (tier 1 only)"))
    assert "offset_quiet" in verdict


def test_offset_arm_is_labelled_control():
    items, verdict = checklist(_detail(arm="off", offset_status=None))
    assert verdict.startswith("control:") and not verdict.startswith("control: refuted")
    assert next(i for i in items if i["id"] == "offset_quiet")["na"]     # controls have no twin: n/a, not a failure


def test_simbad_veto_needs_separations_and_fires_inside_aperture():
    base = _detail()
    # a stellar SIMBAD object inside the aperture refutes
    d = _detail(archive={**base["archive"], "simbad": [{"main_id": "2MASS J1", "otype": "Y*O", "sep": 4.9}]})
    assert "no_simbad_star" in checklist(d)[1]
    # rows without a separation (the old serialiser) or an error row make the check unavailable, never a pass
    d = _detail(archive={**base["archive"], "simbad": [{"main_id": "2MASS J1", "otype": "Y*O"}]})
    items, _ = checklist(d)
    assert next(i for i in items if i["id"] == "no_simbad_star")["na"]
    d = _detail(archive={**base["archive"], "simbad": [{"error": "timeout"}]})
    items, _ = checklist(d)
    assert next(i for i in items if i["id"] == "no_simbad_star")["na"]


def test_archive_loader_adds_simbad_separation():
    import pandas as pd
    from e3_vet_candidate import with_sep
    d = with_sep(pd.DataFrame({"main_id": ["x"], "otype": ["Y*O"], "ra": [10.0 + 2.0 / 3600], "dec": [0.0]}), 10.0, 0.0)
    assert abs(d.sep.iloc[0] - 2.0) < 0.01
    assert with_sep(pd.DataFrame({"error": ["timeout"]}), 10.0, 0.0).shape == (1, 1)


def test_zero_separation_counts_as_a_match_and_clump_entries_are_ignored():
    base = _detail()
    d = _detail(archive={**base["archive"], "glimpse": [{"mag4_5": 12.0, "sep": 0.0}]})
    assert "no_spitzer" in checklist(d)[1]                       # 0.0" is inside the aperture
    d = _detail(archive={**base["archive"], "simbad": [{"main_id": "AGAL G345.084-00.614", "otype": "Y*O", "sep": 0.0}]})
    assert checklist(d)[1] == "birth-compatible"                 # the ATLASGAL clump entry is the clump itself


def test_canonical_fit_uses_tier2_only_when_confirmed():
    from build_catalog import canonical_fit
    # unconfirmed tier-2 fit with opposite sign and a different onset must NOT override the tier-1 event
    r = {"tier1": {"onset_visit": 8, "step": 1.0, "dbic": 100.0}, "tier2": {"onset_visit": 15, "step": -1.0, "dbic": 60.0}, "confirmed": False}
    f = canonical_fit(r)
    assert f["tier"] == 1 and f["onset_visit"] == 8 and f["direction"] == "up"
    r["confirmed"] = True; r["tier2"]["step"] = 2.0
    f = canonical_fit(r)
    assert f["tier"] == 2 and f["onset_visit"] == 15 and f["direction"] == "up"


def _strict_env(tmp_path, monkeypatch, events, rows, details):
    import json
    import build_catalog as bc
    (tmp_path / "e9").mkdir(exist_ok=True); (tmp_path / "gallery").mkdir(exist_ok=True)
    (tmp_path / "e9" / "alternatives.json").write_text(json.dumps({"summary": {}, "events": rows}))
    (tmp_path / "gallery" / "events.json").write_text(json.dumps(events))
    monkeypatch.setattr(bc, "A", tmp_path)
    return bc, details


def _det(key, fit=None, diff=7.0):
    return {"key": key, "fit": fit or {"tier": 1, "onset_visit": 8, "direction": "up"}, "diff_snr": diff, "onset_year": 2018.2, "offset_status": "quiet"}


def _row(bc, det, **over):
    return {"key": det["key"], "gaia_ok": True, "simbad_ok": True, "best": "x", "fit_hash": bc.fit_hash(det), **over}


def test_desk_build_validates_against_current_inputs(tmp_path, monkeypatch):
    import build_catalog as bc
    d1 = _det("c1")
    # 1) consistent: passes
    bc, dets = _strict_env(tmp_path, monkeypatch, [{"key": "c1"}], [_row(bc, d1)], [d1])
    assert "c1" in bc.alternatives_by_key(strict=True, details=dets)
    # 2) a failed query is refused even when the stored summary says complete
    bc, dets = _strict_env(tmp_path, monkeypatch, [{"key": "c1"}], [_row(bc, d1, gaia_ok=False)], [d1])
    _refused(bc, dets, "failed evidence")
    # 3) a newly added event without an E9 row
    bc, dets = _strict_env(tmp_path, monkeypatch, [{"key": "c1"}, {"key": "c2"}], [_row(bc, d1)], [d1, _det("c2")])
    _refused(bc, dets, "key sets differ")
    # 4) a missing detail for a current event
    bc, dets = _strict_env(tmp_path, monkeypatch, [{"key": "c1"}], [_row(bc, d1)], [])
    _refused(bc, dets, "key sets differ")
    # 5) duplicate E9 rows
    bc, dets = _strict_env(tmp_path, monkeypatch, [{"key": "c1"}], [_row(bc, d1), _row(bc, d1)], [d1])
    _refused(bc, dets, "duplicate")
    # 6) same key, changed fit / difference statistic since E9 ran
    bc, dets = _strict_env(tmp_path, monkeypatch, [{"key": "c1"}], [_row(bc, d1)], [_det("c1", diff=2.0)])
    _refused(bc, dets, "different fit")


def _refused(bc, dets, msg):
    try:
        bc.alternatives_by_key(strict=True, details=dets)
        assert False, f"expected refusal: {msg}"
    except RuntimeError as err:
        assert msg in str(err)
