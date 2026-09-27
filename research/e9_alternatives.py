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
  artefact       unusable baseline, rising offset twin, or onset in a visit with < 50% of the
                 median field coverage
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
from build_catalog import R_MATCH, simbad_stellar  # noqa: E402
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
    return {"ok": True, "period_d": round(1 / freq[i], 1), "power": round(float(power[i]), 3), "fap": fap,
            "chi2_sin": round(chi_sin, 1), "chi2_step": round(chi_step, 1),
            "periodic": bool(fap < 0.01 and chi_sin < chi_step),
            "note": "sinusoid-consistent only: 6-month cadence aliases the period"}


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
    sb = within(ar.get("simbad", []))
    sb_types = [str(r.get("otype", "")) for r in sb if not str(r.get("main_id", "")).startswith(("AGAL", "HIGALBM", "[MML2017]", "[EMM"))]
    g = gaia(det["ra"], det["dec"], det["key"])
    gsrc = g["sources"]
    gclass = [s["best_class_name"] for s in gsrc if s.get("best_class_name")]
    per = periodicity(ev["year"], ev["flux"], ev["err"])
    col = (ev.get("colour") or {}).get("d_w1w2")
    up = ev["direction"] == "up"
    cov = det["archive"].get("coverage", [])
    onset_v = int(round((ev["onset_year"] - 2013.95) / 0.5 - 0.5))
    low_cov = bool(cov and 0 <= onset_v < len(cov) and cov[onset_v] < 0.5 * np.median([c for c in cov if c > 0] or [1]))
    ev_ = {
        "known_star": bool(within(simbad_stellar(sb)) or within(ar.get("spicy", [])) or gsrc),
        "gaia_optical_g": min([s["phot_g_mean_mag"] for s in gsrc if s.get("phot_g_mean_mag") is not None], default=None),
        "known_variable": bool(any(t.startswith(VARIABLE_OTYPES) or any(v in t for v in VARIABLE_OTYPES) for t in sb_types) or gclass
                               or any(str(s.get("phot_variable_flag")) == "VARIABLE" for s in gsrc)),
        "gaia_classes": gclass,
        "agb_lpv": bool(any(any(a in t for a in AGB_OTYPES) for t in sb_types) or any(c == "LPV" for c in gclass) or per.get("periodic")),
        "periodic": per, "known_yso": bool(within(ar.get("spicy", [])) or any("Y*" in t or "TT*" in t or "Or*" in t or "FU*" in t for t in sb_types) or "YSO" in gclass),
        "extinction": bool(col is not None and ((not up and col >= 0.2) or (up and col <= -0.2))),
        "d_w1w2": col, "blend": blend_count(det["e1_rows"]) >= 2,
        "artefact": bool(ev["primary"] == "unusable baseline" or (det.get("offset_status") or "").startswith("rise") or low_cov),
        "prior_source": bool(within(ar.get("allwise", [])) or within(ar.get("glimpse", [])) or within(ar.get("mipsgal", []))),
    }
    order = [("artefact", "artefact / bad baseline"), ("known_variable", "known variable star (Gaia/SIMBAD)"),
             ("known_yso", "known YSO (SPICY/SIMBAD/Gaia): outburst or variability of an existing protostar"),
             ("known_star", "known star with optical counterpart"), ("agb_lpv", "AGB / long-period variable"),
             ("extinction", "variable extinction (colour follows the flux)"), ("blend", "blend of several sources"),
             ("prior_source", "brightening of a source already catalogued (AllWISE/GLIMPSE/MIPSGAL)")]
    best = next((lab for k, lab in order if ev_[k]), "unexplained by the archives")
    ev_["best"] = best
    return ev_


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    events = json.loads((ROOT / "artifacts" / "gallery" / "events.json").read_text())
    have = [e for e in events if (CAT / f"{e['key']}.json").exists()]

    def one(e):
        det = json.loads((CAT / f"{e['key']}.json").read_text())
        x = explain(e, det)
        return {"key": e["key"], "arm": e["arm"], "primary": e["primary"], "designation": e["designation"], **x}
    with ThreadPoolExecutor(6) as ex:
        rows = list(ex.map(one, have))
    df = pd.DataFrame(rows)
    summary = {"n_events": len(events), "n_with_details": len(rows),
               "best_on": df[df.arm == "on"].best.value_counts().to_dict(),
               "best_off": df[df.arm == "off"].best.value_counts().to_dict(),
               "flags_on": {k: int(df[df.arm == "on"][k].sum()) for k in ("artefact", "known_variable", "known_yso", "known_star", "agb_lpv", "extinction", "blend", "prior_source")},
               "unexplained_on": [r["key"] for r in rows if r["arm"] == "on" and r["best"].startswith("unexplained")],
               "gaia_ok": int(sum(1 for r in rows if r.get("periodic")))}
    (OUT / "alternatives.json").write_text(json.dumps(clean({"summary": summary, "events": rows})))
    print(json.dumps(summary, indent=1))


if __name__ == "__main__":
    main()
