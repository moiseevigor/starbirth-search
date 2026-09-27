"""Build the review catalog: viewer/catalog/index.js + one detail JSON per gallery candidate.

Catalog: every searched prestellar clump (0 < d <= 4 kpc) with its classification from
each phase (E1 class, SPICY host, E7b stratum/rise). Gallery: every flagged
'birth start' candidate (E1 turn_on/confused, E7b tier-1 rises) plus offset-control
rises, each with the full evidence bundle and an automatic checklist. Human decisions
are stored separately by scripts/serve_catalog.py in reviews/reviews.jsonl.
"""
from __future__ import annotations

import json
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "research"))
sys.path.insert(0, str(ROOT / "src"))
from e3_vet_candidate import archive, sep  # noqa: E402
from e7b_symmetric import CACHE as E7B_CACHE, clean, eligible, light_curve, stats  # noqa: E402
from starbirth.features.forced_phot import Floor  # noqa: E402
from starbirth.features.turn_on import classify  # noqa: E402
from viewer_imagery import diff_snr, hips_cutouts, neowise_stacks  # noqa: E402

A = ROOT / "artifacts"
OUT = ROOT / "viewer" / "catalog"
NEO0 = 56640.0
R_MATCH = 5.5     # arcsec: forced-photometry aperture radius (2 px), see starbirth.features.forced_phot


def yr(mjd):
    return np.round(2013.95 + (np.asarray(mjd, float) - NEO0) / 365.25, 3)


def classes() -> tuple[pd.Series, pd.Series]:
    f = A / "e1_full" / "classes.csv"
    s = pd.read_csv(A / "e1_full" / "pilot_targets.csv")
    if not f.exists():
        c = {arm: classify(pd.read_csv(A / "e1_full" / f"neowise_rows_{arm}.csv"), len(s)) for arm in ("on", "off")}
        pd.DataFrame(c).to_csv(f, index_label="tid")
    c = pd.read_csv(f, index_col="tid")
    return c["on"], c["off"]


# Spitzer Galactic-plane survey footprints used for the archival vetoes (Churchwell+2009; Carey+2009; Vela-Carina
# l = 255-295). Positions outside them get an 'unavailable' state, never a pass.
def spitzer_covered(l: float, b: float) -> bool:
    l = l % 360
    inner = (10 <= l <= 65 or 295 <= l <= 350) and abs(b) <= 1.0          # GLIMPSE I
    centre = (l <= 10 or l >= 350) and abs(b) <= 1.0                       # GLIMPSE II (|b| < 1 conservative)
    velcar = 255 <= l <= 295 and abs(b) <= 1.0                             # Vela-Carina
    return bool(inner or centre or velcar)


def mipsgal_covered(l: float, b: float) -> bool:
    l = l % 360
    return bool((10 <= l <= 65 or 295 <= l <= 350 or l <= 10 or l >= 350) and abs(b) <= 1.0)


STELLAR_OTYPES = ("*", "IR", "NIR", "MIR", "YSO", "Y*", "TT", "Or", "Em", "FU", "V*", "Ae")
NONSTELLAR_OTYPES = {"smm", "cor", "MoC", "DNe", "HII", "Cld", "Rad", "mm", "cm", "PoC", "GNe", "RNe", "ISM", "bub", "sh"}
# sub-mm / far-IR CLUMP catalogues that SIMBAD often types as 'Y*O': they are the clump itself, not a prior star
CLUMP_ID_PREFIXES = ("AGAL ", "HIGALBM", "[MML2017]", "ATLASGAL", "BGPS", "JCMTSF", "[EMM2017]", "[EMM2021]", "GRS ", "MSXDC")


def simbad_stellar(rows: list[dict]) -> list[dict]:
    """SIMBAD objects that indicate a pre-existing star/YSO (the Hi-GAL clump itself is 'smm' and is ignored)."""
    out = []
    for r in rows or []:
        ot = str(r.get("otype") or "")
        if not ot or ot in NONSTELLAR_OTYPES or ("error" in r and r.get("error")):
            continue
        if str(r.get("main_id") or "").startswith(CLUMP_ID_PREFIXES):
            continue
        if any(tok in ot for tok in STELLAR_OTYPES):
            out.append(r)
    return out


def counterpart(ar: dict) -> str:
    """Most informative prior counterpart within the aperture: SPICY class > MIPSGAL 24um > AllWISE > SIMBAD star > none."""
    w = lambda rows: [r for r in rows or [] if (r.get("sep") if r.get("sep") is not None else 99) <= R_MATCH]  # noqa: E731
    sp = w(ar.get("spicy"))
    if sp:
        return f"SPICY {sp[0].get('class', '?')}"
    if w(ar.get("mipsgal")):
        return "MIPSGAL 24 um source"
    if w(ar.get("allwise")):
        return "AllWISE 2010 source"
    if w(simbad_stellar(ar.get("simbad", []))):
        return "SIMBAD star/YSO"
    if w(ar.get("glimpse")):
        return "GLIMPSE source"
    return "none"


def checklist(det: dict) -> tuple[list[dict], str]:
    """Machine evidence for 'birth start' = a new source where nothing was before.
    Each item is pass / fail / n/a (archive does not cover the position); n/a never counts as a pass."""
    fp = det.get("forced", {})
    s = fp.get("tier2") or fp.get("tier1") or {}
    onset = s.get("onset_visit")
    ar = det["archive"]
    cov = ar["coverage"]
    pre_cov = [n for v, n in zip(range(22), cov) if onset is not None and v < onset]
    e1 = det["e1_rows"]
    # anything inside the photometry aperture (R_MATCH = 5.5") contributes to the measured rise, so every
    # "was there a source before?" test uses that radius, not the 3" association radius
    pre_cat = [1 for t, snr, sp in zip(e1["t"], e1["snr"], e1["sep"])
               if onset is not None and t < 2013.95 + onset * 0.5 and (snr or 0) >= 5 and sp <= R_MATCH]
    # a separation of exactly 0.0 is a real match, so test for None rather than falsiness
    within = lambda rows: [r for r in rows if (r.get("sep") if r.get("sep") is not None else 99) <= R_MATCH]  # noqa: E731
    pre_sig = s.get("pre_sig")
    P = det.get("props", {})
    l, b = P.get("glon"), P.get("glat")
    sp_cov = spitzer_covered(l, b) if l is not None and b is not None else False
    mg_cov = mipsgal_covered(l, b) if l is not None and b is not None else False
    sb_rows = ar.get("simbad")
    # SIMBAD evidence is usable only if the query succeeded (no error row) and every row carries a separation
    sb_ok = sb_rows is not None and not any("error" in r and r.get("error") for r in sb_rows) and \
        all(r.get("sep") is not None for r in sb_rows)
    NA = object()
    items = [
        ("covered_pre", "Position imaged before onset (field detections within 60\" in >= 80% of pre-onset visits)",
         bool(pre_cov) and np.mean([n > 0 for n in pre_cov]) >= 0.8),
        # two-sided: a strongly negative baseline means the sky model failed, not that nothing was there
        ("pre_quiet", "Forced pre-onset flux consistent with zero (|pre| < 3 sigma; negative baselines are unusable)",
         pre_sig is not None and abs(pre_sig) < 3),
        ("no_catalog_pre", f"No NEOWISE catalog W2 detection (SNR >= 5) within {R_MATCH}\" before onset", onset is not None and not pre_cat),
        ("no_spitzer", f"No Spitzer (GLIMPSE / Vela-Carina) or SPICY source within {R_MATCH}\"",
         (not within(ar["glimpse"]) and not within(ar["spicy"])) if sp_cov else NA),
        ("no_mipsgal", f"No MIPSGAL 24 um source within {R_MATCH}\" (embedded sources absent at 3-5 um)",
         (not within(ar.get("mipsgal", []))) if mg_cov else NA),
        ("no_allwise", f"No AllWISE (2010) source within {R_MATCH}\"", not within(ar["allwise"])),
        ("no_simbad_star", f"No SIMBAD star / YSO / IR source within {R_MATCH}\" (clump entries ignored)",
         (not within(simbad_stellar(ar.get("simbad", [])))) if sb_ok else NA),
        ("tier2_rise", "Rise confirmed with mask + uncertainty images (tier 2)", bool(fp.get("confirmed"))),
        ("post_signif", "Post-onset flux >= 5 sigma", (s.get("post_sig") or 0) >= 5),
        ("diff_source", "Point source at the target in the difference image (>= 5 sigma)", (det.get("diff_snr") or 0) >= 5),
        ("offset_quiet", "Offset twin (60\") measured through tier 2 with the same photometry and shows no rise",
         (det.get("offset_status") == "quiet") if det["arm"] == "on" else NA),   # controls have no twin
    ]
    out = [{"id": i, "label": lab, "pass": (ok is not NA and bool(ok)), "na": ok is NA} for i, lab, ok in items]
    fails = [o["id"] for o in out if not o["pass"] and not o["na"]]
    nas = [o["id"] for o in out if o["na"]]
    if fails:
        verdict = "refuted: " + ", ".join(fails)
    elif nas:
        verdict = "birth-compatible (unverifiable: " + ", ".join(nas) + ")"
    else:
        verdict = "birth-compatible"
    if det["arm"] == "off":
        verdict = "control: " + verdict
    return out, verdict


def e7b_calibration() -> tuple[Floor, float]:
    res = json.loads((A / "e7b" / "results.json").read_text())
    return Floor(**res["floor"]), float(res["threshold_dbic"])


def offset_status(tid: int, rises: dict, floor: Floor, thr: float) -> str:
    """quiet / rise / quiet (tier 1 only) / unmeasured for the 60\" offset twin of clump position tid.
    'quiet' requires the tier-2 (mask + uncertainty) measurement, the same gate a candidate must pass."""
    f2, f1 = E7B_CACHE / f"t2_off_{tid}.json", E7B_CACHE / f"t1_off_{tid}.json"
    if f2.exists():
        st = stats(json.loads(f2.read_text()), floor)
        if st.get("ok"):
            return "rise" if (eligible(st) and st["dbic"] >= thr) else "quiet"
    if f1.exists():
        st = stats(json.loads(f1.read_text()), floor)
        if st.get("ok"):
            return "rise (tier 1 only)" if (eligible(st) and st["dbic"] >= thr) else "quiet (tier 1 only)"
    return "unmeasured"


def measure_offset_twins(tids: list[int], s: pd.DataFrame, workers: int = 12) -> int:
    """Forced photometry at the 60\" offset of every clump candidate that lacks it (same code path as E7b tier 1).
    Files use the E7b naming so offset_status() finds them; the E7b analysis ignores them (not in design.csv)."""
    todo = [t for t in tids if not ((E7B_CACHE / f"t1_off_{t}.json").exists() and (E7B_CACHE / f"t2_off_{t}.json").exists())]

    def one(t):
        for tier, full in ((1, False), (2, True)):
            f = E7B_CACHE / f"t{tier}_off_{t}.json"
            if f.exists():
                continue
            r = light_curve(float(s.ra[t]), float(s.dec[t]) + 60 / 3600, full=full)
            r.update(arm="off", tid=int(t), stratum="twin")
            f.write_text(json.dumps(clean(r)))
    with ThreadPoolExecutor(workers) as ex:
        list(ex.map(one, todo))
    return len(todo)


def detail(c: dict, rows: dict, rises: dict, props: pd.DataFrame) -> dict:
    key, tid, arm, ra, dec = c["key"], c["tid"], c["arm"], c["ra"], c["dec"]
    g = rows[arm][rows[arm].tid == tid].copy()
    g["sep"] = sep(g.ra, g.dec, ra, dec)
    g = g[g.sep <= 6].sort_values("mjd")
    ar = archive(key, ra, dec)
    lc = ar["lightcurve"]
    rec = lambda d, cols: [] if d is None or d.empty else d[[x for x in cols if x in d]].round(3).to_dict("records")  # noqa: E731
    r = rises.get((arm, tid), {})
    if not r:                                              # classified event without an E7b rise record (fade, ramp, extended)
        e = events_by_key().get(key)
        if e:
            r = {"tier1": {"dbic": e["dbic"], "onset_visit": int(round((e["onset_year"] - 2013.95) / 0.5 - 0.5)),
                           "pre_sig": e["pre_sig"], "post_sig": e["post_sig"], "step": 1.0 if e["direction"] == "up" else -1.0},
                 "tier2": None, "confirmed": bool(e.get("tier2_confirmed")), "stratum": e.get("stratum"),
                 "year": e["year"], "flux": e["flux"], "err": e["err"]}
    s = r.get("tier2") or r.get("tier1") or {}
    onset = s.get("onset_visit")
    h = props.loc[c["designation"]]
    det = {
        "key": key, "tid": tid, "arm": arm, "ra": ra, "dec": dec, "designation": c["designation"],
        "e1_class": c["e1_class"], "stratum": r.get("stratum"),
        "props": {k: (None if pd.isna(h[k]) else float(h[k])) for k in ("glon", "glat", "dist", "mass", "temp", "l_bol", "f70", "ulim_70", "f24")},
        "e1_rows": {"t": list(yr(g.mjd)), "w1": list(g.w1mpro.round(3)) if "w1mpro" in g else [],
                    "w2": list(g.w2mpro.round(3)), "snr": list(g.w2snr.round(1)), "sep": list(g.sep.round(2)),
                    "flag": [str(f)[1] for f in g.cc_flags]},
        "forced": {"tier1": r.get("tier1"), "tier2": r.get("tier2"), "confirmed": r.get("confirmed", False),
                   "year": r.get("year", []), "flux": r.get("flux", []), "err": r.get("err", [])},
        "archive": {"coverage": [int(x) for x in lc.field_dets_60.fillna(0)] if "field_dets_60" in lc else [0] * 22,
                    "allwise": rec(ar["allwise"], ["w1mpro", "w2mpro", "w3mpro", "w4mpro", "sep"]),
                    "glimpse": rec(ar["glimpse"], ["survey", "mag3_6", "mag4_5", "mag5_8", "mag8_0", "sep"]),
                    "mipsgal": rec(ar["mipsgal"], ["mag_24", "fnu_24", "sep"]),
                    "spicy": rec(ar["spicy"], ["spicy", "class", "alpha", "mag3_6", "mag4_5", "sep"]),
                    "simbad": rec(ar["simbad"], ["main_id", "otype", "sep", "error"])},
        "offset_status": offset_status(tid, rises, *e7b_calibration()) if arm == "on" else None,
        "baseline_flag": "negative" if (s.get("pre_sig") is not None and s["pre_sig"] <= -3) else "",
    }
    det["images"] = hips_cutouts(key, ra, dec)
    det["epochs"] = neowise_stacks(key, ra, dec)
    det["diff_snr"] = diff_snr(ra, dec, onset) if onset is not None else None
    det["onset_year"] = round(2013.95 + (onset + 0.5) * 0.5, 2) if onset is not None else None
    det["checklist"], det["machine_verdict"] = checklist(det)
    return det


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    s = pd.read_csv(A / "e1_full" / "pilot_targets.csv")
    props = pd.read_csv(ROOT / "cache" / "higal360clump.csv").set_index("designation")
    on_cls, off_cls = classes()
    res = json.loads((A / "e7b" / "results.json").read_text())
    rises = {(r["arm"], r["tid"]): r for r in res["rises"]}
    design = pd.read_csv(A / "e7b" / "design.csv")
    measured = {(a, t): st for a, t, st in zip(design.arm, design.tid, design.stratum)}
    spicy = set(pd.read_csv(A / "e4" / "spicy_on.csv").tid)

    ev = events_by_key()
    cands = {}
    for t in s.index:
        arm_hits = [("on", t)] if on_cls[t] in ("turn_on", "confused") or ("on", t) in rises or f"c{t}" in ev else []
        arm_hits += [("off", t)] if ("off", t) in rises or off_cls[t] == "turn_on" or f"x{t}" in ev else []
        for arm, tt in arm_hits:
            key = f"{'c' if arm == 'on' else 'x'}{tt}"
            cands[key] = {"key": key, "tid": int(tt), "arm": arm, "designation": s.designation[tt],
                          "ra": float(s.ra[tt]), "dec": float(s.dec[tt]) + (60 / 3600 if arm == "off" else 0),
                          "e1_class": (on_cls if arm == "on" else off_cls)[tt]}
    rows = {arm: pd.read_csv(A / "e1_full" / f"neowise_rows_{arm}.csv") for arm in ("on", "off")}
    rows = {arm: r[r.tid.isin([c["tid"] for c in cands.values()])] for arm, r in rows.items()}

    def build(c):
        f = OUT / f"{c['key']}.json"
        if f.exists():                                     # incremental: rescore refreshes existing details
            return json.loads(f.read_text())
        d = detail(c, rows, rises, props)
        f.write_text(json.dumps(clean(d)))
        return d

    with ThreadPoolExecutor(4) as ex:
        details = list(ex.map(build, cands.values()))
    write_index(details, s, on_cls, off_cls, res, measured, rises, spicy, cands)


EVENT_FIELDS = ("primary", "amp_mag", "amp_class", "shape", "rise_visits", "direction", "tier2_confirmed", "in_e7b_design")


def events_by_key() -> dict:
    f = A / "gallery" / "events.json"
    return {e["key"]: e for e in json.loads(f.read_text())} if f.exists() else {}


def gallery_rows(details: list[dict]) -> list[dict]:
    ev = events_by_key()
    return [{k: d[k] for k in ("key", "tid", "arm", "designation", "ra", "dec", "e1_class", "stratum",
                               "machine_verdict", "onset_year", "diff_snr")}
            | {k: ev.get(d["key"], {}).get(k) for k in EVENT_FIELDS}
            | {"d_w1w2": (ev.get(d["key"], {}).get("colour") or {}).get("d_w1w2"), "counterpart": counterpart(d["archive"])}
            | {"props": d["props"], "confirmed": d["forced"]["confirmed"], "offset_status": d.get("offset_status"),
               "dbic": (d["forced"]["tier2"] or d["forced"]["tier1"] or {}).get("dbic"),
               "thumb": f"img/{d['key']}/neowise_diff.png" if d["epochs"] else None,
               "n_epochs": len(d["epochs"]), "passes": sum(x["pass"] for x in d["checklist"]),
               "n_na": sum(x.get("na", False) for x in d["checklist"]), "n_checks": len(d["checklist"])}
            for d in details]


def rescore() -> None:
    """Recompute checklists/verdicts from the saved detail files (no network) and rewrite index.js."""
    s = pd.read_csv(A / "e1_full" / "pilot_targets.csv")
    on_cls, off_cls = classes()
    res = json.loads((A / "e7b" / "results.json").read_text())
    rises = {(r["arm"], r["tid"]): r for r in res["rises"]}
    design = pd.read_csv(A / "e7b" / "design.csv")
    measured = {(a, t): st for a, t, st in zip(design.arm, design.tid, design.stratum)}
    spicy = set(pd.read_csv(A / "e4" / "spicy_on.csv").tid)
    details, cands = [], {}
    floor, thr = e7b_calibration()
    rec = lambda df, cols: [] if df is None or df.empty else df[[x for x in cols if x in df]].round(3).to_dict("records")  # noqa: E731
    for f in sorted(OUT.glob("*.json")):
        d = json.loads(f.read_text())
        # refresh the archival tables from the cached CSVs (adds SIMBAD separations / error provenance; no network)
        ar = archive(d["key"], d["ra"], d["dec"])
        d["archive"].update({"simbad": rec(ar["simbad"], ["main_id", "otype", "sep", "error"]),
                             "mipsgal": rec(ar["mipsgal"], ["mag_24", "fnu_24", "sep"])})
        if d["arm"] == "on":
            d["offset_status"] = offset_status(d["tid"], rises, floor, thr)
            sig = ((d["forced"].get("tier2") or d["forced"].get("tier1") or {}).get("pre_sig"))
            d["baseline_flag"] = "negative" if (sig is not None and sig <= -3) else ""
        d["checklist"], d["machine_verdict"] = checklist(d)
        f.write_text(json.dumps(clean(d)))
        details.append(d)
        cands[d["key"]] = d
    write_index(details, s, on_cls, off_cls, res, measured, rises, spicy, cands)


def write_index(details, s, on_cls, off_cls, res, measured, rises, spicy, cands) -> None:
    gallery = gallery_rows(details)
    cat = pd.DataFrame({"tid": s.index, "designation": s.designation, "l": s.glon.round(3), "b": s.glat.round(3),
                        "dist": s.dist.round(2), "mass": s.mass.round(1), "temp": s.temp.round(1),
                        "lbol": s.l_bol.round(1), "e1_on": on_cls.reindex(s.index).values,
                        "e1_off": off_cls.reindex(s.index).values,
                        "spicy_host": s.index.isin(list(spicy)),
                        "e7b": [measured.get(("on", t), "") for t in s.index],
                        "rise": [("tier2" if rises[("on", t)]["confirmed"] else "tier1") if ("on", t) in rises else ""
                                 for t in s.index],
                        "key": [f"c{t}" if f"c{t}" in cands else "" for t in s.index]})
    meta = {"built": pd.Timestamp.now().strftime("%Y-%m-%d %H:%M"), "e7b": {k: v for k, v in res.items() if k != "rises"},
            "n_catalog": len(cat), "n_gallery": len(gallery)}
    js = {"meta": meta, "columns": list(cat.columns), "rows": clean(cat.values.tolist()), "gallery": clean(gallery)}
    (OUT / "index.js").write_text("window.CAT=" + json.dumps(js, separators=(",", ":")) + ";\n")
    print(f"catalog {len(cat)} rows, gallery {len(gallery)} candidates -> {OUT}")


if __name__ == "__main__":
    if "--measure-offsets" in sys.argv:
        _s = pd.read_csv(A / "e1_full" / "pilot_targets.csv")
        _tids = [json.loads(f.read_text())["tid"] for f in OUT.glob("c*.json")]
        print("measured offset twins:", measure_offset_twins(_tids, _s))
    elif "--rescore" in sys.argv:
        rescore()
    else:
        main()
