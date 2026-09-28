"""E9: is each event better explained by something other than a new star?

For every classified event (artifacts/gallery/events.json, both arms) with a catalog detail
(viewer/catalog/<key>.json), gather independent evidence for alternative explanations:
  known star     SIMBAD stellar type within the aperture; SPICY YSO; Gaia DR3 source within 2"
                 (an optical counterpart at a deeply embedded position argues against a newborn)
  known variable Gaia DR3 vari_classifier_result within 2" (LPV, YSO, ECL, RR, DSCT, ...);
                 SIMBAD variable types (V*, Mi*, LP*, Or*, TT*, FU*, Em*)
  AGB / LPV      SIMBAD Mi*/LP*/AB*/C*/S*, Gaia class LPV, or Lomb-Scargle periodicity of the
                 forced light curve (P = 150-1500 d, FAP < 0.01; caveat: ~6-month cadence aliases)
  extinction     fade that reddens (d(W1-W2) >= +0.2) or brightening that turns bluer (<= -0.2)
  blend          >= 2 distinct NEOWISE catalog sources within 6" (positions clustered at > 2")
  artefact       rising offset twin (the field itself varies); an unusable (negative) pre-onset baseline is
                 its own lower rung: it voids the amplitude, not the event; low onset coverage is only reported
  prior source   AllWISE 2010 / GLIMPSE / MIPSGAL source within the aperture (a brightening of
                 something that was already there)
Best alternative (priority): artefact > known variable > known YSO / star > AGB-LPV > extinction >
blend > prior source > unexplained.  Writes artifacts/e9/alternatives.json.
"""
from __future__ import annotations

import io
import json
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import httpx
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "research"))
sys.path.insert(0, str(ROOT / "src"))
from build_catalog import R_MATCH, fit_hash, simbad_stellar  # noqa: E402
from e7b_symmetric import clean  # noqa: E402

OUT = ROOT / "artifacts" / "e9"
CAT = ROOT / "viewer" / "catalog"
GAIA = "https://gea.esac.esa.int/tap-server/tap/sync"
CACHE = ROOT / "cache" / "e9"
VARIABLE_OTYPES = ("V*", "Mi*", "LP*", "Or*", "TT*", "FU*", "Em*", "Pu*", "RR*", "Ce*", "Ir*", "Ro*", "Er*", "dS*")
AGB_OTYPES = ("Mi*", "LP*", "AB*", "C*", "S*", "OH*", "pA*")
NEO0 = 56640.0


def gaia(ra: float, dec: float, key: str) -> dict:
    """Gaia DR3 sources within 2" and their variability class, cached per key."""
    f = CACHE / f"gaia_{key}.json"
    if f.exists():
        return json.loads(f.read_text())
    q = (f"SELECT s.source_id, s.phot_g_mean_mag, s.phot_variable_flag, s.parallax, v.best_class_name, v.best_class_score "
         f"FROM gaiadr3.gaia_source AS s LEFT JOIN gaiadr3.vari_classifier_result AS v ON v.source_id = s.source_id "
         f"WHERE 1=CONTAINS(POINT('ICRS', s.ra, s.dec), CIRCLE('ICRS', {ra}, {dec}, {2 / 3600:.8f}))")
    out = {"ok": False, "sources": []}
    try:
        r = httpx.post(GAIA, data={"REQUEST": "doQuery", "LANG": "ADQL", "FORMAT": "csv", "QUERY": q}, timeout=120)
        if r.status_code == 200 and not r.text.lstrip().startswith("<"):
            d = pd.read_csv(io.StringIO(r.text))
            out = {"ok": True, "sources": clean(d.astype(object).where(d.notna(), None).to_dict("records"))}
    except httpx.HTTPError:
        pass
    CACHE.mkdir(parents=True, exist_ok=True)
    f.write_text(json.dumps(out))
    return out


def periodicity(year: list, flux: list, err: list) -> dict:
    from astropy.timeseries import LombScargle
    t, f, e = np.asarray(year, float) * 365.25, np.asarray(flux, float), np.asarray(err, float)
    if t.size < 10:
        return {"ok": False}
    ls = LombScargle(t, f, e)
    freq = np.linspace(1 / 1500, 1 / 150, 4000)
    power = ls.power(freq)
    i = int(np.argmax(power))
    fap = float(ls.false_alarm_probability(power[i], minimum_frequency=freq[0], maximum_frequency=freq[-1]))
    # a persistent step is itself well fit by a low-frequency sinusoid: only call it periodic when the sinusoid
    # (3 params) beats the two-level step model (3 params) in chi^2
    chi_sin = float(np.sum(((f - ls.model(t, freq[i])) / e) ** 2))
    from starbirth.features.change_point import best_persistent_step
    cp = best_persistent_step(f, e, min_points_each_side=3)
    step_model = np.where(np.arange(f.size) < (cp.index if cp.index is not None else f.size), cp.pre_mean, cp.post_mean)
    chi_step = float(np.sum(((f - step_model) / e) ** 2))
    P = 1 / freq[i]
    cadence = 182.625
    window = any(abs(P - h) / h < 0.15 for h in (cadence / 2, cadence, 2 * cadence, 365.25))   # sampling window peaks
    return {"ok": True, "period_d": round(P, 1), "power": round(float(power[i]), 3), "fap": fap,
            "chi2_sin": round(chi_sin, 1), "chi2_step": round(chi_step, 1), "window_peak": bool(window),
            "periodic": bool(fap < 0.01 and chi_sin < chi_step and not window),
            "note": "informational only: 6-month cadence aliases periods; never used alone to label an AGB/LPV"}


def colour_from_archive(key: str, onset_year: float) -> float | None:
    """d(W1-W2) = post - pre from catalog detections within 3" in artifacts/e3_vet/<key>/neowise_60arcsec.csv."""
    f = ROOT / "artifacts" / "e3_vet" / key / "neowise_60arcsec.csv"
    if not f.exists():
        return None
    try:
        d = pd.read_csv(f)
    except pd.errors.EmptyDataError:
        return None
    if d.empty or "w1mpro" not in d or "w2mpro" not in d:
        return None
    d = d[(d.sep <= 3) & (d.w2snr >= 5) & (d.w1snr >= 3)].dropna(subset=["w1mpro", "w2mpro"])
    yr = 2013.95 + (d.mjd - NEO0) / 365.25
    pre, post = d[yr < onset_year], d[yr >= onset_year]
    if len(pre) < 3 or len(post) < 3:
        return None
    return round(float((post.w1mpro - post.w2mpro).median() - (pre.w1mpro - pre.w2mpro).median()), 2)


def blend_count(e1: dict) -> int:
    """Distinct source positions among catalog detections within 6": cluster separations at > 2"."""
    seps = np.array(e1.get("sep", []), float)
    snr = np.array([s if s is not None else 0 for s in e1.get("snr", [])], float)
    seps = seps[snr >= 5]
    if seps.size == 0:
        return 0
    # separations alone cannot separate sources on a ring; use the spread as a proxy: two populations if range > 2"
    return 2 if (seps.max() - seps.min()) > 2.0 and seps.min() < 3 else 1


def explain(ev: dict, det: dict) -> dict:
    ar, fp = det["archive"], det["forced"]
    within = lambda rows: [r for r in rows or [] if (r.get("sep") if r.get("sep") is not None else 99) <= R_MATCH]  # noqa: E731
    sb_all = ar.get("simbad")
    simbad_ok = sb_all is not None and not any(("error" in r and r.get("error")) for r in sb_all) and all(r.get("sep") is not None for r in sb_all)
    sb = within(sb_all or [])
    sb_types = [str(r.get("otype", "")) for r in sb if not str(r.get("main_id", "")).startswith(("AGAL", "HIGALBM", "[MML2017]", "[EMM"))]
    g = gaia(det["ra"], det["dec"], det["key"])
    gsrc = g["sources"]
    if not g.get("ok"):
        (CACHE / f"gaia_{det['key']}.json").unlink(missing_ok=True)     # do not cache a failed query
    gclass = [s["best_class_name"] for s in gsrc if s.get("best_class_name")]
    per = periodicity(ev["year"], ev["flux"], ev["err"])
    onset_year = det.get("onset_year") or ev["onset_year"]
    col = colour_from_archive(det["key"], onset_year)
    if col is None:
        col = (ev.get("colour") or {}).get("d_w1w2")
    fp1 = det.get("fit") or {}
    if not fp1:
        from build_catalog import canonical_fit
        fp1 = canonical_fit(fp) or {}
    up = fp1.get("direction", ev["direction"]) == "up"
    cov = det["archive"].get("coverage", [])
    onset_v = fp1.get("onset_visit") if fp1.get("onset_visit") is not None else int(round((ev["onset_year"] - 2013.95) / 0.5 - 0.5))
    low_cov = bool(cov and 0 <= onset_v < len(cov) and cov[onset_v] < 0.5 * np.median([c for c in cov if c > 0] or [1]))
    ev_ = {
        "known_star": bool(within(simbad_stellar(sb)) or within(ar.get("spicy", [])) or gsrc),
        "gaia_optical_g": min([s["phot_g_mean_mag"] for s in gsrc if s.get("phot_g_mean_mag") is not None], default=None),
        "known_variable": bool(any(t.startswith(VARIABLE_OTYPES) or any(v in t for v in VARIABLE_OTYPES) for t in sb_types) or gclass
                               or any(str(s.get("phot_variable_flag")) == "VARIABLE" for s in gsrc)),
        "gaia_classes": gclass,
        # AGB/LPV needs catalogue evidence (SIMBAD AGB types or a Gaia LPV class); periodicity is only reported
        "agb_lpv": bool(any(any(a in t for a in AGB_OTYPES) for t in sb_types) or any(c == "LPV" for c in gclass)),
        "periodic": per, "known_yso": bool(within(ar.get("spicy", [])) or any("Y*" in t or "TT*" in t or "Or*" in t or "FU*" in t for t in sb_types) or "YSO" in gclass),
        "extinction": bool(col is not None and ((not up and col >= 0.2) or (up and col <= -0.2))),
        "d_w1w2": col, "blend": blend_count(det["e1_rows"]) >= 2,
        # artefact = the measurement itself is untrustworthy: a failed sky model or a rising offset twin.
        # Low field coverage at the onset visit only blurs the onset time and is reported, not ranked.
        "artefact": bool((det.get("offset_status") or "").startswith("rise")),      # the field itself varies
        "bad_baseline": bool(ev["primary"] == "unusable baseline"),                 # pre-onset measurement unusable
        "onset_coverage_low": low_cov,
        "prior_source": bool(within(ar.get("allwise", [])) or within(ar.get("glimpse", [])) or within(ar.get("mipsgal", []))),
        # physical alternatives that need no catalogue: a source already in the aperture before onset, or a flux
        # change with no point source in the difference image (extended emission or sky-level change)
        "uncatalogued_prior": bool(fp1.get("pre_sig") is not None and fp1["pre_sig"] >= 3),
        # direction-aware: diff_snr is the positive peak for rises and the negative-peak magnitude for fades
        "no_point_source": bool(det.get("diff_snr") is not None and det["diff_snr"] < 5),
        "diff_direction": det.get("direction"),
        "_gaia_ok": bool(g.get("ok")),
    }
    ev_["evidence"] = {
        "simbad_ok": simbad_ok, "simbad_rows": sb, "spicy_rows": within(ar.get("spicy", [])),
        "gaia_ok": bool(g.get("ok")), "gaia_sources": gsrc, "periodicity": per, "d_w1w2": col,
        "blend_sources": blend_count(det["e1_rows"]), "pre_sig": fp1.get("pre_sig"), "diff_snr": det.get("diff_snr"),
        "offset_status": det.get("offset_status"), "onset_coverage_low": low_cov,
        "prior_rows": {"allwise": within(ar.get("allwise", [])), "glimpse": within(ar.get("glimpse", [])), "mipsgal": within(ar.get("mipsgal", []))},
    }
    ev_["_simbad_ok"] = simbad_ok
    order = [("artefact", "artefact / bad baseline"), ("known_variable", "known variable star (Gaia/SIMBAD)"),
             ("known_yso", "known YSO (SPICY/SIMBAD/Gaia): outburst or variability of an existing protostar"),
             ("known_star", "known star with optical counterpart"), ("agb_lpv", "AGB / long-period variable"),
             ("extinction", "variable extinction (colour follows the flux)"), ("blend", "blend of several sources"),
             ("prior_source", "brightening of a source already catalogued (AllWISE/GLIMPSE/MIPSGAL)"),
             ("uncatalogued_prior", "variability of an uncatalogued source already in the aperture (pre-onset flux >= 3 sigma)"),
             ("bad_baseline", "unusable pre-onset baseline (sky-model failure; amplitude not measurable)"),
             ("no_point_source", "no point source in the difference image (extended emission or sky-level change)")]
    best = next((lab for k, lab in order if ev_[k]), "unexplained by the archives")
    ev_["best"] = best
    ev_["priority_path"] = [{"flag": k, "label": lab, "fired": bool(ev_[k])} for k, lab in order]
    return ev_


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    events = json.loads((ROOT / "artifacts" / "gallery" / "events.json").read_text())
    have = [e for e in events if (CAT / f"{e['key']}.json").exists()]

    def one(e):
        det = json.loads((CAT / f"{e['key']}.json").read_text())
        x = explain(e, det)
        return {"key": e["key"], "arm": e["arm"], "primary": e["primary"], "designation": e["designation"],
                "gaia_ok": bool(x.pop("_gaia_ok", True)), "simbad_ok": bool(x.pop("_simbad_ok", True)),
                "fit_hash": fit_hash(det), **x}
    with ThreadPoolExecutor(6) as ex:
        rows = list(ex.map(one, have))
    df = pd.DataFrame(rows)
    missing = sorted(e["key"] for e in events if not (CAT / f"{e['key']}.json").exists())
    gaia_failed = sorted(r["key"] for r in rows if not r.get("gaia_ok", True))
    simbad_failed = sorted(r["key"] for r in rows if not r.get("simbad_ok", True))
    keys_events, keys_tested = [e["key"] for e in events], [r["key"] for r in rows]
    exact = len(set(keys_events)) == len(keys_events) and set(keys_events) == set(keys_tested) and len(keys_tested) == len(set(keys_tested))
    complete = exact and not missing and not gaia_failed and not simbad_failed
    summary = {"n_events": len(events), "n_with_details": len(rows), "complete": complete, "exact_key_match": exact,
               "missing_details": missing, "gaia_failed": gaia_failed, "simbad_failed": simbad_failed,
               "best_on": df[df.arm == "on"].best.value_counts().to_dict(),
               "best_off": df[df.arm == "off"].best.value_counts().to_dict(),
               "flags_on": {k: int(df[df.arm == "on"][k].sum()) for k in ("artefact", "bad_baseline", "known_variable", "known_yso", "known_star", "agb_lpv", "extinction", "blend", "prior_source", "uncatalogued_prior", "no_point_source")},
               "colour_available_on": int(df[df.arm == "on"].d_w1w2.notna().sum()),
               "unexplained_on": [r["key"] for r in rows if r["arm"] == "on" and r["best"].startswith("unexplained")],
               "gaia_ok": int(sum(1 for r in rows if r.get("periodic")))}
    (OUT / "alternatives.json").write_text(json.dumps(clean({"summary": summary, "events": rows})))
    print(json.dumps(summary, indent=1))


if __name__ == "__main__":
    main()
