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
from e7b_symmetric import clean  # noqa: E402
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


def checklist(det: dict) -> tuple[list[dict], str]:
    """Machine evidence for 'birth start' = a new source where nothing was before."""
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
    within = lambda rows: [r for r in rows if (r.get("sep") or 99) <= R_MATCH]  # noqa: E731
    pre_sig = s.get("pre_sig")
    items = [
        ("covered_pre", "Position imaged before onset (field detections within 60\" in >= 80% of pre-onset visits)",
         bool(pre_cov) and np.mean([n > 0 for n in pre_cov]) >= 0.8),
        ("pre_quiet", "Forced pre-onset flux < 3 sigma (no source in the aperture before onset)",
         pre_sig is not None and pre_sig < 3),
        ("no_catalog_pre", f"No NEOWISE catalog W2 detection (SNR >= 5) within {R_MATCH}\" before onset", onset is not None and not pre_cat),
        ("no_spitzer", f"No Spitzer (GLIMPSE / Vela-Carina) or SPICY source within {R_MATCH}\"",
         not within(ar["glimpse"]) and not within(ar["spicy"])),
        ("no_allwise", f"No AllWISE (2010) source within {R_MATCH}\"", not within(ar["allwise"])),
        ("tier2_rise", "Rise confirmed with mask + uncertainty images (tier 2)", bool(fp.get("confirmed"))),
        ("post_signif", "Post-onset flux >= 5 sigma", (s.get("post_sig") or 0) >= 5),
        ("diff_source", "Point source at the target in the difference image (>= 5 sigma)", (det.get("diff_snr") or 0) >= 5),
        ("offset_quiet", "Offset twin (60\") shows no rise", det.get("offset_rise") is False),
    ]
    out = [{"id": i, "label": lab, "pass": bool(ok)} for i, lab, ok in items]
    fails = [o["id"] for o in out if not o["pass"]]
    verdict = "birth-compatible" if not fails else "refuted: " + ", ".join(fails)
    if det["arm"] == "off":
        verdict = "control: " + verdict
    return out, verdict


def detail(c: dict, rows: dict, rises: dict, props: pd.DataFrame) -> dict:
    key, tid, arm, ra, dec = c["key"], c["tid"], c["arm"], c["ra"], c["dec"]
    g = rows[arm][rows[arm].tid == tid].copy()
    g["sep"] = sep(g.ra, g.dec, ra, dec)
    g = g[g.sep <= 6].sort_values("mjd")
    ar = archive(key, ra, dec)
    lc = ar["lightcurve"]
    rec = lambda d, cols: [] if d is None or d.empty else d[[x for x in cols if x in d]].round(3).to_dict("records")  # noqa: E731
    r = rises.get((arm, tid), {})
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
                    "simbad": rec(ar["simbad"], ["main_id", "otype"])},
        "offset_rise": rises.get(("off" if arm == "on" else "on", tid), {}).get("confirmed", False) if arm == "on" else None,
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

    cands = {}
    for t in s.index:
        arm_hits = [("on", t)] if on_cls[t] in ("turn_on", "confused") or ("on", t) in rises else []
        arm_hits += [("off", t)] if ("off", t) in rises or off_cls[t] == "turn_on" else []
        for arm, tt in arm_hits:
            key = f"{'c' if arm == 'on' else 'x'}{tt}"
            cands[key] = {"key": key, "tid": int(tt), "arm": arm, "designation": s.designation[tt],
                          "ra": float(s.ra[tt]), "dec": float(s.dec[tt]) + (60 / 3600 if arm == "off" else 0),
                          "e1_class": (on_cls if arm == "on" else off_cls)[tt]}
    rows = {arm: pd.read_csv(A / "e1_full" / f"neowise_rows_{arm}.csv") for arm in ("on", "off")}
    rows = {arm: r[r.tid.isin([c["tid"] for c in cands.values()])] for arm, r in rows.items()}

    def build(c):
        f = OUT / f"{c['key']}.json"
        d = detail(c, rows, rises, props)
        f.write_text(json.dumps(clean(d)))
        return d

    with ThreadPoolExecutor(4) as ex:
        details = list(ex.map(build, cands.values()))
    write_index(details, s, on_cls, off_cls, res, measured, rises, spicy, cands)


def gallery_rows(details: list[dict]) -> list[dict]:
    return [{k: d[k] for k in ("key", "tid", "arm", "designation", "ra", "dec", "e1_class", "stratum",
                               "machine_verdict", "onset_year", "diff_snr")}
            | {"props": d["props"], "confirmed": d["forced"]["confirmed"],
               "dbic": (d["forced"]["tier2"] or d["forced"]["tier1"] or {}).get("dbic"),
               "thumb": f"img/{d['key']}/neowise_diff.png" if d["epochs"] else None,
               "n_epochs": len(d["epochs"]), "passes": sum(x["pass"] for x in d["checklist"]),
               "n_checks": len(d["checklist"])}
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
    for f in sorted(OUT.glob("*.json")):
        d = json.loads(f.read_text())
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
    rescore() if "--rescore" in sys.argv else main()
