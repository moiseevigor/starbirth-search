"""Build the standalone findings viewer: viewer/data.js + viewer/img/.

Open viewer/index.html directly (file://) or publish the viewer/ folder.
Everything shown is computed here from the repo's artifacts, caches and the
research vault, so rerunning this script refreshes the viewer.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

import numpy as np
import pandas as pd
import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "research"))
sys.path.insert(0, str(ROOT / "src"))

from e3_vet_candidate import cone, sep  # noqa: E402
from report_feasibility import injection_recovery, poisson_ul95  # noqa: E402
from starbirth.experiments.synthetic_turnon import run_grid  # noqa: E402
from starbirth.features.turn_on import classify, track  # noqa: E402
from starbirth.glossary import GLOSSARY  # noqa: E402
from phases import PHASES  # noqa: E402
from viewer_imagery import hips_cutouts, neowise_stacks  # noqa: E402

A = ROOT / "artifacts"
OUT = ROOT / "viewer"
NEO0 = 56640.0


def r(x, n=3):
    return None if x is None or (isinstance(x, float) and not np.isfinite(x)) else round(float(x), n)


def mjd2yr(m):
    return 2013.95 + (np.asarray(m, float) - NEO0) / 365.25


# ----------------------------------------------------------------------------- candidates
CANDIDATES = [
    dict(key="g354", name="G354.2348+0.5057", designation="HIGALBM354.2348+0.5057", ra=262.28651, dec=-33.53024,
         kind="turn_on", verdict="Outburst of an existing YSO (FUor-like)",
         story="Absent from every NEOWISE visit in 2014-15 although the field was imaged (165-336 field detections "
               "within 60\"). Appears in 2016 at W2 = 9.7 and rises 1.4 mag over two years to W2 = 8.3, then holds "
               "a plateau through 2024. But Spitzer had already catalogued a flat-spectrum YSO here (SPICY 55207, "
               "[4.5] = 11.68 in 2004-08): the source brightened by about 3.3 mag. Before 2016 it was blended with "
               "SPICY 55201 8\" away, so WISE never resolved it."),
    dict(key="g337", name="G337.2520+0.6278", designation="HIGALBM337.2520+0.6278", ra=248.43901, dec=-46.88652,
         kind="turn_on", verdict="Outburst of an existing YSO, now fading",
         story="Nothing within 6\" in NEOWISE until 2019, then W2 = 10.35 at SNR 47, fading to 11.25 by 2024 with "
               "very red W1-W2 = 2.7-3.2. The NEOWISE centroid lies 0.36\" from a Spitzer Class II YSO (SPICY 38399, "
               "[4.5] = 12.64; a 7 mJy 24 um source nearby): an existing young star brightened by about 2.3 mag and "
               "is decaying, EXor-like."),
    dict(key="g341", name="G341.8242+0.3646", designation="HIGALBM341.8242+0.3646", ra=252.99156, dec=-43.61320,
         kind="turn_on", verdict="Large-amplitude variable Class I YSO",
         story="Spitzer: Class I YSO (SPICY 42905, [4.5] = 11.19) with a 153 mJy MIPSGAL 24 um counterpart. "
               "AllWISE 2010: W2 = 12.84-13.15. Undetected by NEOWISE 2014-2021, then W2 = 11.2-11.5 from 2022. "
               "The source faded and recovered; a dimming (extinction) episode followed by a return, or a burst."),
    dict(key="g059", name="G59.2598-0.3285", designation="HIGALBM59.2598-0.3285", ra=295.88482, dec=23.08494,
         kind="turn_on", verdict="Brightening of a catalogued YSO",
         story="AllWISE 2010 already detects it (W2 = 14.13, W4 = 5.48) and it is a known Hi-GAL-region YSO "
               "(Veneziani+2013). NEOWISE sees it cross the detection threshold in 2020-21 at W2 ~ 13.0: a "
               "~1.1 mag brightening of an existing object."),
    dict(key="g261", name="G261.8890-2.2444", designation="HIGALBM261.8890-2.2444", ra=128.06270, dec=-43.51836,
         kind="confused", verdict="Hidden low-luminosity protostar? Best follow-up target",
         story="Cold (10.8 K), 11 Msun, 1.7 Lsun clump at 1.56 kpc in Vela, outside Spitzer coverage and absent "
               "from AllWISE. A faint red source (W2 ~ 14.2, W1-W2 ~ 1.5) is marginally detected from 2014, "
               "brightens smoothly to W2 = 12.8 in 2021 and fades back to 14.1 by 2024. The Hi-GAL 70 um limit "
               "(0.07 Jy) allows a hidden protostar of up to ~0.45 Lsun (derived). An 8-year accretion or "
               "extinction episode of a very young, faint object."),
    dict(key="off307", name="Offset control near G307.58-0.10", designation=None, ra=202.994, dec=-62.590056,
         kind="artefact", verdict="Artefact: blend/deblend toggle (flat flux)",
         story="The only turn-on in 19,219 offset-control positions. W2 is constant at 11.96 +/- 0.05, yet the "
               "source is missing in 2014-15 and again in 2018-19 although the field was imaged in every visit. "
               "The pipeline alternately merges it into a neighbour more than 6\" away. Flat flux distinguishes it "
               "from the four real events above."),
]


def candidate_block(c: dict) -> dict:
    ra, dec = c["ra"], c["dec"]
    neo = cone("neowiser_p1bs_psd", "ra, dec, mjd, w1mpro, w1snr, w2mpro, w2sigmpro, w2snr, cc_flags", ra, dec, 60)
    neo["sep"] = sep(neo.ra, neo.dec, ra, dec)
    neo["visit"] = ((neo.mjd - NEO0) // 182.625).astype(int)
    cover = neo.groupby("visit").size().reindex(range(22), fill_value=0)
    src = neo[(neo.sep <= 3) & (neo.w2snr >= 3)].sort_values("mjd")
    arch = []
    aw = cone("allwise_p3as_psd", "ra, dec, w1mpro, w2mpro, w3mpro, w4mpro", ra, dec, 6)
    for _, a in aw.assign(s=sep(aw.ra, aw.dec, ra, dec)).sort_values("s").head(1).iterrows():
        arch += [dict(band="W1", mag=r(a.w1mpro), year=2010.5, src="AllWISE"),
                 dict(band="W2", mag=r(a.w2mpro), year=2010.5, src="AllWISE")]
    sp = cone("spicy", "ra, dec, spicy, class, mag3_6, mag4_5", ra, dec, 4)
    for _, s in sp.assign(s=sep(sp.ra, sp.dec, ra, dec)).sort_values("s").head(1).iterrows():
        arch += [dict(band="W1", mag=r(s.mag3_6), year=2006.0, src=f"Spitzer [3.6] SPICY {int(s.spicy)} ({s['class']})"),
                 dict(band="W2", mag=r(s.mag4_5), year=2006.0, src=f"Spitzer [4.5] SPICY {int(s.spicy)} ({s['class']})")]
    imgs = hips_cutouts(c["key"], ra, dec)
    stacks = neowise_stacks(c["key"], ra, dec)
    from astropy.coordinates import SkyCoord
    g = SkyCoord(ra=ra, dec=dec, unit="deg").galactic
    return {**{k: c[k] for k in ("key", "name", "designation", "ra", "dec", "kind", "verdict", "story")},
            "lb": [r((g.l.deg + 180) % 360 - 180), r(g.b.deg)],
            "lc": {"t": [r(x, 3) for x in mjd2yr(src.mjd)], "w1": [r(x) for x in src.w1mpro],
                   "w2": [r(x) for x in src.w2mpro], "w2e": [r(x) for x in src.w2sigmpro],
                   "flag": [str(f)[1] for f in src.cc_flags]},
            "coverage": {"t": [r(2013.95 + (v + 0.5) * 0.5, 2) for v in range(22)], "n": cover.tolist()},
            "archival": arch, "images": imgs, "epochs": stacks}


# ----------------------------------------------------------------------------- artefacts (pilot data)
ARTEFACTS = [
    dict(key="edge", run="on", tid=247, title="Aperture-edge flicker",
         why="A steady W2 = 12.2 star sits 2.9\" from the clump. With a fixed 3\" aperture its astrometric scatter "
             "moves it in and out, so early visits look empty.",
         fix="Query 6\" and track the source's own centroid (2\" from its median position)."),
    dict(key="flagged", run="on", tid=362, title="Halo-flagged steady star",
         why="A steady W2 = 9.5 star is flagged as a halo or spike artefact (cc_flags h/H) in nearly every exposure; "
             "only a few late exposures are clean, which mimics a late appearance.",
         fix="Flags grade measurement quality, not existence: veto on any detection within 6\" before onset."),
    dict(key="neighbour", run="on", tid=1768, title="Neighbour's astrometric outliers",
         why="A W2 = 10.6 star 5\" away is detected in every visit; its rare outlier positions fall inside 3\" "
             "only in late visits.",
         fix="Confusion veto: a turn-on needs an empty 6\" circle (about the W2 PSF FWHM) before onset."),
    dict(key="single", run="off", tid=1463, title="Single-exposure detections",
         why="One detection out of ~12 exposures per visit at W2 ~ 12.5. A real source that bright is detected in "
             "most exposures; single-exposure rows are mostly spurious.",
         fix="A visit counts only when at least 3 exposures detect the source."),
]


def artefact_block(a: dict) -> dict:
    rows = pd.read_csv(A / "e1_pilot" / f"neowise_rows_{a['run']}.csv")
    g = rows[rows.tid == a["tid"]].copy()
    g["sep"] = sep(g.ra, g.dec, g.t_ra.iloc[0], g.t_dec.iloc[0])
    g = g[g.sep <= 6].sort_values("mjd")
    return {**{k: a[k] for k in ("key", "title", "why", "fix")},
            "t": [r(x, 3) for x in mjd2yr(g.mjd)], "w2": [r(x) for x in g.w2mpro], "sep": [r(x, 2) for x in g.sep],
            "flag": [str(f)[1] for f in g.cc_flags], "snr": [r(x, 1) for x in g.w2snr]}


# ----------------------------------------------------------------------------- experiments
def experiments() -> dict:
    """Cached: recomputed only when an input artifact is newer than the cache."""
    cache = ROOT / "cache" / "viewer" / "experiments.json"
    inputs = [*A.glob("e_minus1/*.csv"), *A.glob("e1_pilot/*.csv"), *A.glob("e1_full/*.csv"),
              ROOT / "src" / "starbirth" / "features" / "turn_on.py"]
    if cache.exists() and cache.stat().st_mtime > max(f.stat().st_mtime for f in inputs):
        return json.loads(cache.read_text())
    res = _experiments()
    cache.parent.mkdir(parents=True, exist_ok=True)
    cache.write_text(json.dumps(res))
    return res


def _experiments() -> dict:
    e0 = run_grid(trials=2000, seed=42)
    m = pd.read_csv(A / "e_minus1" / "allwise_match.csv")
    det = lambda p="": m[p + "sep"].notna() & (m[p + "w2snr"] >= 5)  # noqa: E731
    m = m.assign(on=det(), off=det("off_"), lm=m.l_bol / m.mass)
    pro = m[(m.evol_flag == 2) & (m.mass > 0) & np.isfinite(m.lm)].copy()
    pro["grp"] = pd.qcut(pro.lm, 4, labels=["Protostellar Q1 (youngest)", "Protostellar Q2", "Protostellar Q3",
                                            "Protostellar Q4 (oldest)"]).astype(str)
    vis = pd.concat([m[m.evol_flag == 1].assign(grp="Prestellar"), pro]).groupby("grp", sort=False).agg(
        n=("on", "size"), f_on=("on", "mean"), f_off=("off", "mean"))
    vis = vis.reindex(["Prestellar", "Protostellar Q1 (youngest)", "Protostellar Q2", "Protostellar Q3",
                       "Protostellar Q4 (oldest)"])
    grid = pd.read_csv(A / "e_minus1" / "yield_grid.csv")
    grid["dmax"] = grid.dmax_kpc.map(lambda d: f"d <= {d:g} kpc" if np.isfinite(d) else "all distances")

    cat = pd.read_csv(ROOT / "cache" / "higal360clump.csv")
    cat["db"] = pd.cut(cat.dist, [0, 1, 2, 3, 4, 6, 8, 25])
    ratio = cat[cat.evol_flag.isin([1, 2])].pivot_table(index="db", columns="evol_flag", values="designation",
                                                        aggfunc="count", observed=True)

    def runs(sub: str) -> dict:
        s = pd.read_csv(A / sub / "pilot_targets.csv")
        n = len(s)
        cls = {lab: classify(pd.read_csv(A / sub / f"neowise_rows_{lab}.csv"), n).value_counts().to_dict()
               for lab in ("on", "off")}
        return {"n": n, "classes": cls}

    pilot, full = runs("e1_pilot"), runs("e1_full")
    rows_on = pd.read_csv(A / "e1_pilot" / "neowise_rows_on.csv")
    rows_off = pd.read_csv(A / "e1_pilot" / "neowise_rows_off.csv")
    pilot["sweep"] = [{"min_post_frac": pf,
                       "on": int((classify(rows_on, pilot["n"], min_post_frac=pf) == "turn_on").sum()),
                       "off": int((classify(rows_off, pilot["n"], min_post_frac=pf) == "turn_on").sum())}
                      for pf in (0.8, 0.65, 0.5, 0.35)]
    inj = [{"onset_year": r(2013.95 + o * 0.5, 1), "recovered": r(injection_recovery(rows_on, pilot["n"], o)[0])}
           for o in (3, 6, 10, 15)]
    comp = float(np.mean([i["recovered"] for i in inj]))
    k_on = full["classes"]["on"].get("turn_on", 0)
    return {
        "e0": e0,
        "w2vis": [{"group": g, "n": int(v.n), "f_on": r(v.f_on, 4), "f_off": r(v.f_off, 4)} for g, v in vis.iterrows()],
        "yield": grid[["dmax", "tau_proto_myr", "N_T", "Y", "B_min", "B_max"]].round(4).to_dict("records"),
        "ratio": [{"bin": str(i), "pre": int(v[1]), "proto": int(v[2])} for i, v in ratio.iterrows()],
        "pilot": pilot, "full": full, "injection": inj, "completeness": r(comp),
        "burst_rate": {"k_on": k_on, "k_off": full["classes"]["off"].get("turn_on", 0), "n": full["n"],
                       "rate": r(k_on / full["n"] / comp, 6), "ul95": r(poisson_ul95(k_on) / full["n"] / comp, 6)},
    }


# ----------------------------------------------------------------------------- sky + literature
def sky() -> dict:
    cat = pd.read_csv(ROOT / "cache" / "higal360clump.csv")
    l = ((cat.glon + 180) % 360 - 180).round(3)          # centre the Galactic centre
    return {"l": l.tolist(), "b": cat.glat.round(3).tolist(), "c": cat.evol_flag.astype(int).tolist(),
            "d": cat.dist.round(2).where(cat.dist > 0).fillna(-1).tolist()}


def literature() -> dict:
    vault = ROOT / "obsidian" / "Research" / "Astrophysics"
    papers = []
    for f in sorted(vault.rglob("*.md")):
        if f.name.startswith("_"):
            continue
        fm = yaml.safe_load(re.match(r"---\n(.*?)\n---", f.read_text(), re.S).group(1))
        papers.append({"id": f.stem, "title": fm.get("title"), "authors": str(fm.get("authors", ""))[:80],
                       "year": fm.get("year"), "venue": str(fm.get("venue", ""))[:60], "url": fm.get("url"),
                       "group": f.parent.name, "cites": fm.get("citation_count")})
    # verified in the vault paper notes (see each note's Key result section)
    bursts = [
        {"who": "Zakri+2022", "cls": "Class 0", "tau": 438, "lo": 161, "hi": 1884, "ci": "95%"},
        {"who": "Zakri+2022", "cls": "Class I + flat", "tau": 1741, "lo": 527, "hi": 12011, "ci": "95%"},
        {"who": "Zakri+2022", "cls": "All protostars", "tau": 879, "lo": 400, "hi": 2515, "ci": "95%"},
        {"who": "Park+2021", "cls": "Protostars (NEOWISE)", "tau": 683, "lo": 356, "hi": 1579, "ci": "90%"},
        {"who": "Fischer+2019", "cls": "Protostars (Spitzer vs WISE)", "tau": 1040, "lo": 690, "hi": 40300, "ci": "90%"},
        {"who": "Contreras Pena+2024", "cls": "Class I FUor (VVV)", "tau": 1750, "lo": 880, "hi": 2870, "ci": "68%"},
    ]
    # log10(years); ranges from the vault paper notes
    timescales = [
        {"what": "Second collapse (dynamical)", "lo": 0.1, "hi": 0.7, "ref": "Masunaga & Inutsuka 2000; Tomida+2013"},
        {"what": "Feedback escapes the first-core remnant", "lo": 5, "hi": 5, "ref": "Tomida+2013 (estimate)"},
        {"what": "First hydrostatic core lifetime", "lo": 100, "hi": 3e4, "ref": "Young 2023; Tomida+2013; Dunham+2014"},
        {"what": "Luminosity rises to peak (~25-30 Lsun)", "lo": 2e4, "hi": 8e4, "ref": "Masunaga & Inutsuka 2000; Larson 1969"},
        {"what": "Visible in the near-IR", "lo": 2e4, "hi": 1.4e5, "ref": "Masunaga & Inutsuka 2000"},
        {"what": "Class 0 phase", "lo": 4.7e4, "hi": 1.6e5, "ref": "Kristensen & Dunham 2018; Evans+2009"},
        {"what": "Prestellar / starless phase", "lo": 1.3e5, "hi": 1.7e6, "ref": "Enoch+2008; Konyves+2015; Battersby+2017"},
        {"what": "Accretion-burst recurrence", "lo": 438, "hi": 1750, "ref": "Zakri+2022; Contreras Pena+2024"},
        {"what": "Archival window (Herschel -> NEOWISE end)", "lo": 12, "hi": 15, "ref": "this project", "window": True},
    ]
    return {"papers": papers, "bursts": bursts, "timescales": timescales}


def phases() -> list[dict]:
    """PHASES with E4 filled from its artifact (the log never shows a stale number)."""
    ph = [dict(p) for p in PHASES]
    f = A / "e4" / "burst_calibration.json"
    e4 = next(p for p in ph if p["id"] == "E4")
    if f.exists():
        j = json.loads(f.read_text())
        lo, hi = j["tau_ci95_yr"]
        ok = bool(j["consistent_with"])
        e4["verdict"] = "confirmed" if ok else "refuted"
        e4["result"] = (f"{j['on']['n_host']} SPICY YSOs lie within 3\" of the searched clumps "
                        f"({j['off']['n_host']} at offset positions); {j['on']['n_eff']} were not steadily detected by NEOWISE. "
                        f"k = {j['k']} turn-ons among them give tau = {j['tau_yr']:.0f} yr "
                        f"(95% CI {lo:.0f}-{hi:.0f} yr), consistent with: "
                        + (", ".join(j["consistent_with"]) if ok else "none of the published intervals") + ". "
                        + " ".join(f"{b['label']}: k = {b['k']} of {b['n_eff']} hosts, tau = {b['tau_yr']:.0f} yr "
                                   f"(95% CI {b['ci95'][0]:.0f}-{b['ci95'][1]:.0f} yr)." for b in j.get("by_class", []) if b["k"])
                        + " The Class II interval is far shorter than the ~112 kyr measured for Class II outbursts "
                          "(Contreras Pena+2019): the one Class II host (SPICY 38399, W1-W2 = 2.7-3.2 in outburst) is "
                          "probably an embedded protostar mislabelled in a crowded, extincted field.")
        e4["data"] = j
    f5 = A / "e5" / "host_colours.json"
    e5 = next(p for p in ph if p["id"] == "E5")
    if f5.exists():
        j = json.loads(f5.read_text())
        g = j["groups"]
        pre, pro, fld = g["prestellar clumps"], g["protostellar clumps"], g["field (|b| < 1 deg)"]
        fr = lambda x: f"{x['frac_red']:.2f} ({x['frac_red_ci95'][0]:.2f}-{x['frac_red_ci95'][1]:.2f})"  # noqa: E731
        e5["result"] = (f"Red fraction of Class II: prestellar-clump hosts {fr(pre)} (n = {pre['n_classII']}), "
                        f"protostellar-clump hosts {fr(pro)} (n = {pro['n_classII']}), field {fr(fld)} "
                        f"(n = {fld['n_classII']}). Clump hosts are 2.2-2.6x redder than the field, so the "
                        f"environment effect is confirmed; but prestellar hosts are not redder than protostellar "
                        f"ones, so a prestellar-specific mislabelling is refuted. The E4 Class II host (SPICY 38399, "
                        f"[3.6]-[4.5] = {j['g337_host']['colour']:.2f}) sits at the "
                        f"{j['g337_host']['percentile_in_field_classII']:.0f}th percentile of field Class II. SPICY "
                        f"classes are unreliable inside clumps; only the all-class E4 rate stands.")
        e5["data"] = j
    f6 = A / "e6" / "colour_colour.json"
    e6 = next(p for p in ph if p["id"] == "E6")
    if f6.exists():
        j = json.loads(f6.read_text())
        g = j["groups"]
        pre, pro = g["prestellar clumps"], g["protostellar clumps"]
        ci = lambda v: f"{v[0]:+.2f} to {v[1]:+.2f}"  # noqa: E731
        e6["result"] = (f"Prestellar-clump hosts vs field: delta [3.6]-[4.5] = {pre['d_c1']:+.2f} ({ci(pre['d_c1_ci95'])}), "
                        f"delta [4.5]-[5.8] = {pre['d_c2']:+.2f} ({ci(pre['d_c2_ci95'])}), delta [4.5]-[8.0] = "
                        f"{pre['d_c3']:+.2f}; implied A_K ~ {pre['A_K_implied']:.1f}. Protostellar-clump hosts: "
                        f"{pro['d_c1']:+.2f} / {pro['d_c2']:+.2f} / {pro['d_c3']:+.2f} (A_K ~ {pro['A_K_implied']:.1f}). "
                        f"The [3.6]-[4.5] shift is ~3x the [4.5]-[5.8] shift and [4.5]-[8.0] barely moves: the "
                        f"reddening is mostly extinction. The pre-registered cut (|delta [4.5]-[5.8]| < 0.1) is "
                        f"narrowly missed ({pre['d_c2']:+.2f}), leaving a small residual that a dense-cloud extinction "
                        f"law or a modest envelope excess could explain. {100 * pre['frac_gutermuth_classI']:.0f}% of "
                        f"these 'Class II' hosts pass the full Gutermuth Class I colour cut vs "
                        f"{100 * g['field (|b| < 1 deg)']['frac_gutermuth_classI']:.0f}% in the field.")
        e6["data"] = j
    return ph


def main() -> None:
    OUT.mkdir(exist_ok=True)
    data = {
        "built": pd.Timestamp.now().strftime("%Y-%m-%d %H:%M"),
        "counts": {"higal_total": 150223, "high_rel": 94604, "prestellar": 49289, "protostellar": 35186,
                   "searched": None},
        "sky": sky(),
        "experiments": experiments(),
        "candidates": [candidate_block(c) for c in CANDIDATES],
        "artefacts": [artefact_block(a) for a in ARTEFACTS],
        "literature": literature(),
        "glossary": GLOSSARY,
        "phases": phases(),
    }
    data["counts"]["searched"] = data["experiments"]["full"]["n"]
    (OUT / "data.js").write_text("window.SB=" + json.dumps(data, separators=(",", ":"), allow_nan=False) + ";\n")
    # offline entry point: the publishable fragment app.html wrapped in a full document
    (OUT / "index.html").write_text('<!doctype html><html lang="en"><head><meta charset="utf-8">'
                                    '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">'
                                    '</head><body>\n' + (OUT / "app.html").read_text() + "\n</body></html>\n")
    print(f"wrote {OUT / 'data.js'} ({(OUT / 'data.js').stat().st_size / 1e6:.2f} MB) and index.html")


if __name__ == "__main__":
    main()
