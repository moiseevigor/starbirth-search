"""Write docs/FEASIBILITY.md (E-1 + E1-pilot) with figures in docs/figures/."""
from __future__ import annotations

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


def pilot_section() -> str:
    p = A / "e1_pilot" / "pilot_targets.csv"
    if not p.exists() or "class_on" not in pd.read_csv(p, nrows=0).columns:
        return "_E1-pilot not run yet._\n"
    s = pd.read_csv(p)
    n = len(s)
    c = pd.DataFrame({"on-source": s.class_on.value_counts(), "offset control": s.class_off.value_counts()}).fillna(0).astype(int)
    c = c.reindex(["none", "steady", "other", "turn_on"]).fillna(0).astype(int)
    k_on, k_off = int(c.loc["turn_on", "on-source"]), int(c.loc["turn_on", "offset control"])
    return (
        f"Sample: {n} prestellar clumps with 0 < d <= 4 kpc and no AllWISE W2 source at the clump "
        "position (where E-1 sampled them), queried in NEOWISE-R single exposures within 3\".\n\n"
        "Per-visit detection = clean W2 (w2snr >= 5, cc_flags W2 = '0', qual_frame > 0) in a ~6-month visit. "
        "**turn_on** = first detection in visit >= 3 (not in 2014-2015), >= 3 detected visits, and detected in >= 80% "
        "of visits from the first detection onward. **steady** = detected from the start in >= 80% of visits. "
        "**other** = sporadic. Coverage is assumed complete every visit (no upper-limit bookkeeping yet).\n\n"
        + c.to_markdown() + "\n\n"
        f"Turn-on rate: on-source {k_on}/{n} = {k_on/n:.4f} (SE {se(k_on/n, n):.4f}); "
        f"offset control {k_off}/{n} = {k_off/n:.4f} (SE {se(k_off/n, n):.4f}).\n"
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

1. **Pilot verdict** (see above): if on-source ~ offset, catalog-level turn-ons are
   confusion-dominated -> move to forced photometry on unTimely/unWISE epoch coadds.
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
