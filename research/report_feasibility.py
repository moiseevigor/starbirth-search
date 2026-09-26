"""Write docs/FEASIBILITY.md (E-1 + E1-pilot) with figures in docs/figures/."""
from __future__ import annotations

import math
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402
import pandas as pd  # noqa: E402

from starbirth.glossary import markdown as glossary_md  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
DOCS, FIG = ROOT / "docs", ROOT / "docs" / "figures"
A = ROOT / "artifacts"


def se(p: float, n: int) -> float:
    return float(np.sqrt(p * (1 - p) / n))


def fig_w2(m: pd.DataFrame) -> pd.DataFrame:
    det = lambda p="": m[p + "sep"].notna() & (m[p + "w2snr"] >= 5)  # noqa: E731
    m = m.assign(on=det(), off=det("off_"), lm=m.l_bol / m.mass)
    pro = m[(m.evol_flag == 2) & (m.mass > 0) & np.isfinite(m.lm)].copy()
    pro["grp"] = pd.qcut(pro.lm, 4, labels=["proto Q1 (youngest L/M)", "proto Q2", "proto Q3", "proto Q4 (oldest)"]).astype(str)
    pre = m[m.evol_flag == 1].assign(grp="prestellar")
    t = pd.concat([pre, pro]).groupby("grp", sort=False).agg(n=("on", "size"), f_on=("on", "mean"), f_off=("off", "mean"))
    t = t.reindex(["prestellar", "proto Q1 (youngest L/M)", "proto Q2", "proto Q3", "proto Q4 (oldest)"])
    t["excess"] = t.f_on - t.f_off
    t["se_on"] = [se(p, n) for p, n in zip(t.f_on, t.n)]
    x = np.arange(len(t))
    fig, ax = plt.subplots(figsize=(7, 3.6))
    ax.bar(x - 0.2, 100 * t.f_on, 0.4, yerr=100 * t.se_on, label="at clump position (f_on)")
    ax.bar(x + 0.2, 100 * t.f_off, 0.4, label="60\" offset control (f_off)", color="0.6")
    ax.set_xticks(x, t.index, rotation=20, ha="right", fontsize=8)
    ax.set_ylabel("clumps with AllWISE W2 source\nwithin 3\" (%, linear)")
    ax.set_title("E-1: W2 visibility of Hi-GAL clumps (error bar = binomial SE)", fontsize=9)
    ax.legend(fontsize=8)
    fig.tight_layout()
    fig.savefig(FIG / "e_minus1_w2_visibility.png", dpi=130)
    plt.close(fig)
    return t


def fig_yield(g: pd.DataFrame) -> None:
    fig, ax = plt.subplots(figsize=(7, 3.6))
    for i, (d, sub) in enumerate(g.groupby("dmax_kpc", sort=False)):
        lab = f"d <= {d:g} kpc" if np.isfinite(d) else "all distances"
        x = np.arange(len(sub)) + 4 * i
        ax.scatter(x, sub.Y, marker="o", color="C0", label="signal Y" if i == 0 else None, zorder=3)
        ax.vlines(x + 0.3, sub.B_min, sub.B_max, color="C3", lw=4, label="burst background B (range)" if i == 0 else None)
        ax.text(x[1], 0.013, lab, ha="center", fontsize=8)
    ticks = np.concatenate([np.arange(3) + 4 * i for i in range(3)])
    ax.set_xticks(ticks, [f"{t:g}" for t in g.tau_proto_myr], fontsize=8)
    ax.set_xlabel("assumed protostellar-clump lifetime tau_proto (Myr)")
    ax.set_yscale("log")
    ax.set_ylim(0.01, 3000)
    ax.set_ylabel("expected events 2012-2024\n(count, log scale)")
    ax.axhline(1, color="0.5", lw=0.8, ls=":")
    ax.legend(fontsize=8, loc="upper left", ncol=2)
    ax.set_title("E-1: expected observable births vs accretion-burst impostors", fontsize=9)
    fig.tight_layout()
    fig.savefig(FIG / "e_minus1_yield.png", dpi=130)
    plt.close(fig)


def poisson_ul95(k: int) -> float:
    """lambda with P(X <= k | lambda) = 0.05 (one-sided 95% upper limit), by bisection."""
    cdf = lambda lam: sum(math.exp(-lam) * lam**i / math.factorial(i) for i in range(k + 1))  # noqa: E731
    lo, hi = 0.0, 50.0 + 5 * k
    for _ in range(60):
        mid = (lo + hi) / 2
        lo, hi = (mid, hi) if cdf(mid) > 0.05 else (lo, mid)
    return hi


def injection_recovery(rows: pd.DataFrame, n: int, onset: int) -> tuple[float, int]:
    """Delete pre-onset detections of the *source itself* (within 2" of its tracked
    centre) for steady SNR>=10 sources, keep neighbours, reclassify."""
    from starbirth.features.turn_on import _sep_arcsec, classify, track
    tr = track(rows)
    c = classify(rows, n)
    snr = tr.groupby("tid").w2snr.median()
    ids = [i for i in c.index[c == "steady"] if snr.get(i, 0) >= 10]
    cen = tr.groupby("tid")[["c_ra", "c_dec"]].first()
    r = rows.join(cen, on="tid")
    own = r.tid.isin(ids) & (_sep_arcsec(r.ra, r.dec, r.c_ra, r.c_dec) <= 2.0)
    pre = (r.mjd - 56640.0) // 182.625 < onset
    cc = classify(rows[~(own & pre).values], n).loc[ids]
    return float((cc == "turn_on").mean()), len(ids)


def result_txt(n: int, inj, sweep) -> str:
    comp = float(np.mean([r for _, r, _ in inj]))
    k = sweep[0]["turn_on on-source"]
    ul = poisson_ul95(k) / n / comp
    g = pd.read_csv(A / "e_minus1" / "yield_grid.csv")
    g4 = g[g.dmax_kpc == 4.0].iloc[0]
    b_lo, b_hi = g4.B_min / g4.n_pre, g4.B_max / g4.n_pre
    y_hi = g[g.dmax_kpc == 4.0].Y.max() / g4.n_pre
    n_full = int(g4.n_pre)
    return (
        f"**Result — prediction confirmed (null).** {k} turn-ons in {n} clumps. Completeness-corrected 95% upper "
        f"limit on the catalog-level turn-on rate: {ul:.1e} per clump over 2014-2024 (mean completeness {comp:.2f}). "
        f"E-1 predicts S+B per clump (d <= 4 kpc) of {b_lo:.1e}-{b_hi:.1e} (bursts) plus <= {y_hi:.1e} (births): "
        f"the pilot already touches the top of the burst range. The full d <= 4 kpc sample ({n_full:,} clumps) "
        f"would reach ~{poisson_ul95(0) / n_full / comp:.1e} per clump, i.e. it can bound f_hidden * p_lift / "
        "burst_interval — a population result even if no birth is found (E6).\n\n"
    )


def pilot_section() -> str:
    from starbirth.features.turn_on import classify
    d = A / "e1_pilot"
    p = d / "pilot_targets.csv"
    if not p.exists() or not (d / "neowise_rows_on.csv").exists():
        return "_E1-pilot (6\" run) not finished yet._\n"
    n = len(pd.read_csv(p))
    rows = {lab: pd.read_csv(d / f"neowise_rows_{lab}.csv") for lab in ("on", "off")}
    sweep = []
    for pf in (0.8, 0.65, 0.5, 0.35):
        cl = {lab: classify(r, n, min_post_frac=pf) for lab, r in rows.items()}
        k = {lab: int((c == "turn_on").sum()) for lab, c in cl.items()}
        sweep.append({"min_post_frac": pf, "turn_on on-source": k["on"], "turn_on offset": k["off"],
                      "confused on / off": f"{(cl['on'] == 'confused').sum()} / {(cl['off'] == 'confused').sum()}",
                      "rate on (per clump)": f"{k['on']/n:.4f}",
                      "95% UL on (Poisson)": f"{poisson_ul95(k['on'])/n:.4f}"})
    base = classify(rows["on"], n).value_counts().to_dict()
    inj = [(o, *injection_recovery(rows["on"], n, o)) for o in (3, 6, 10, 15)]
    inj_txt = "; ".join(f"onset visit {o}: {r:.2f}" for o, r, _ in inj)
    return (
        f"Sample: {n} prestellar clumps, 0 < d <= 4 kpc, no AllWISE W2 source at the clump position "
        "(where E-1 sampled them). NEOWISE-R single exposures queried within 6\"; the source is *tracked* "
        "(centre = median of clean detections within 3\" of the clump; detections kept within 2\" of that "
        "centre) so aperture-edge sources cannot flicker. Clean = w2snr >= 5 and W2 cc_flag '0'.\n\n"
        "**turn_on** = first detection in NEOWISE visit >= 3 (i.e. after 2015), >= 3 detected visits, detected in "
        ">= min_post_frac of visits from onset, post-onset median SNR >= 10, and NOT **confused** (confused = "
        ">= 50% of pre-onset visits already have a clean detection within 6\", ~ the W2 PSF FWHM). Coverage assumed "
        f"complete every visit (no upper-limit bookkeeping yet). Class counts at min_post_frac 0.8: {base}.\n\n"
        + pd.DataFrame(sweep).to_markdown(index=False) + "\n\n"
        f"**Completeness (injection).** For the {inj[0][2]} steady SNR>=10 on-source sources, deleting the source's "
        f"own detections before the onset visit (neighbours kept) and reclassifying recovers: {inj_txt}. Losses are "
        "the confusion veto (a neighbour within 6\") — the price of rejecting blends.\n\n"
        + result_txt(n, inj, sweep) +
        "**Artefacts found and fixed by self-checks** (`tests/test_turn_on.py`): (1) a steady source on the 3\" "
        "aperture edge flickering in/out (-> tracking + 6\" query); (2) real detections dropped by a "
        "`qual_frame > 0` cut (-> removed); (3) a steady W2 = 10.6 star 5\" away whose rare astrometric outliers "
        "fell inside 3\" only in late visits (-> confusion veto). All candidate turn-ons so far had constant flux "
        "(+/-0.2 mag), i.e. none showed a physical brightening.\n"
    )


def main() -> None:
    FIG.mkdir(parents=True, exist_ok=True)
    m = pd.read_csv(A / "e_minus1" / "allwise_match.csv")
    g = pd.read_csv(A / "e_minus1" / "yield_grid.csv")
    r = pd.read_csv(A / "e_minus1" / "w2_rates.csv", index_col=0)["value"]
    t = fig_w2(m)
    fig_yield(g)
    gt = g.assign(dmax_kpc=g.dmax_kpc.map(lambda d: f"{d:g}" if np.isfinite(d) else "all"))
    md = f"""# Feasibility: can archival W1/W2 data catch a prestellar clump turning protostellar?

Question: before building the E1 pipeline, is the expected number of *observable*
prestellar->protostellar turn-ons in the Hi-GAL sample large enough, and larger
than the accretion-burst impostors that mimic them? Literature and parameter
sources: [LITERATURE.md](LITERATURE.md). Terms: glossary at the end.

## E-1(B) Detectability of the post-transition state at 4.6 um

**Hypothesis.** If a newborn protostar is visible in W2, Hi-GAL *protostellar*
clumps (the post-transition state) show a W2 point source at the clump position
more often than the chance-alignment rate; the youngest ones (lowest L/M) set
the detectability of a fresh turn-on. Prediction: excess df_W2 > 0.05.

**Test.** Random 4,000 prestellar + 4,000 protostellar clumps (all distances),
nearest AllWISE source within 3" with w2snr >= 5, server-side IRSA TAP upload;
control = same positions +60" in Dec.

![W2 match fraction (%, linear) at clump position vs 60 arcsec offset, by Hi-GAL class and L/M quartile](figures/e_minus1_w2_visibility.png)

{t.round(4).to_markdown()}

**Result — confirmed.** Youngest-quartile protostellar clumps: df_W2 =
{r['df_w2_young']:.3f}; all protostellar {r['df_w2_all']:.3f}; chance rate
f_off = {r['f_off']:.3f}. Prestellar clumps already show a small excess
f_prehost = {r['f_prehost']:.3f} (sources present at the Herschel epoch; vetoed).
Matched protostellar W2 sources are bright (median W2 ~ 10.2 mag vs NEOWISE
single-exposure 90% completeness ~14.3 mag), so a visible turn-on is a
high-SNR event: the limiting factor is *visibility and interpretation*, not
photometric noise. **Caveat:** a Hi-GAL protostellar clump is older and more
luminous (median L_bol ~ 10^2 L_sun) than a fresh second core; df_W2 is an
optimistic upper bound for a true birth (LITERATURE F3/F4).

## E-1(A) Expected signal Y vs burst background B

Steady state: N_pre/tau_pre = N_proto/tau_proto, so the transition count is
N_T = N_proto * dt / tau_proto (the observed ratio N_pre/N_proto = 1.3-1.7 at
every distance cancels). Y = N_T * df_W2 * (1 - f_prehost). Background
B = N_pre * f_hidden * dt / burst_interval * p_lift with f_hidden in
[0.05, 0.2], burst_interval in [438, 1000] yr, p_lift in [0.1, 0.5]
(p_lift is a guess — the least constrained factor). dt = 12 yr.

![Expected signal Y (dots) and burst background B range (bars), counts on log scale, vs assumed tau_proto, for three distance cuts](figures/e_minus1_yield.png)

{gt.round(3).to_markdown(index=False)}

**Result — partial.** The search is *not* dead on yield: Y ~ 0.06-0.4 within
4 kpc and ~0.15-1.1 for the whole catalogue. But even the most favourable
background B_min ~ 1-3 exceeds Y, and the realistic S/B is 0.003-0.35. A W2
turn-on alone therefore cannot claim a birth: **the experiment is a burst
search with a birth-discrimination problem**, and discrimination (pre-event
70/24 um depth, sub-mm, radio) decides the science, not W2 photometry.

## E1-pilot: empirical turn-on rate (S + B + artefacts)

**Hypothesis.** Catalog-level NEOWISE turn-ons at prestellar clump positions
exceed the offset-control rate. Prediction under E-1: on-source excess
~ (Y + B)/N_pre ~ 1e-4-3e-3 per clump — i.e. *undetectable* in a 2,000-clump
pilot unless artefacts/confusion dominate.

{pilot_section()}
## Open questions / next tests

1. **Full E1 run** over all prestellar clumps with 0 < d <= 4 kpc (same classifier,
   offset control): either candidates for vetting, or an upper limit ~10x tighter.
   Then forced photometry on unTimely/unWISE epoch coadds for faint (SNR < 10) turn-ons.
2. **Coverage bookkeeping**: use `neowiser_p1bs_frm` to turn missing visits into
   upper limits (current classifier assumes full coverage).
3. **p_lift**: measure it — burst amplitude distribution (Zakri+2022, Contreras
   Peña+2024) against the W2 depth at Hi-GAL distances.
4. **Birth vs burst discriminator**: pre-event Hi-GAL 70 um upper limit converted
   to L_int (LITERATURE F2) — a turn-on whose post-event W2 luminosity implies
   L_int far above the pre-event 70 um limit is more birth-like.
5. **Near sample** (d < 2 kpc, 22/24 um-quiet) to raise S/B.

{glossary_md()}"""
    (DOCS / "FEASIBILITY.md").write_text(md)
    print("wrote docs/FEASIBILITY.md")


if __name__ == "__main__":
    main()
