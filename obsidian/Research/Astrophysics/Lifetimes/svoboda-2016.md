---
title: "The Bolocam Galactic Plane Survey. XIV. Physical Properties of Massive Starless and Star Forming Clumps"
authors: Brian E. Svoboda, Yancy L. Shirley, Cara Battersby, Erik W. Rosolowsky, Adam G. Ginsburg, Timothy P. Ellsworth-Bowers, Michele R. Pestalozzi, Miranda K. Dunham, Neal J. Evans II, John Bally, Jason Glenn
year: 2016
venue: The Astrophysical Journal 822, 59
url: https://arxiv.org/abs/1511.08810
language: en
domain: astrophysics
status: draft
methodology_type: empirical
citation_count: 52
citation_count_date: 2026-09-26
key_concepts: ["[[statistical-lifetime]]", "[[prestellar-core]]", "[[hi-gal-evolutionary-classification]]", "[[free-fall-time]]"]
extends: []
contradicts: []
replicates: []
cites: ["[[chomiuk-povich-2011]]", "[[dunham-2014]]"]
cited_by: ["[[battersby-2017]]", "[[elia-2017]]", "[[elia-2021]]"]
quality_notes: "Largest blind starless-clump-candidate sample at the time (2223 of 4683 BGPS clumps). The mass-dependent lifetime is anchored to a methanol-maser lifetime that itself scales inversely with the adopted Galactic SFR (chomiuk-povich-2011). Valid only for M > 10^3 M☉; lower masses are extrapolation."
author: moiseevigor
tags:
  - agent/research
  - user/moiseevigor
  - domain/astrophysics
  - topic/massive-clumps
  - topic/evolutionary-lifetimes
  - topic/prestellar-cores
  - topic/hi-gal
  - topic/spitzer-surveys
  - topic/source-distances
  - topic/clump-evolutionary-stages
  - topic/methanol-masers
  - paper
  - status/draft
---

# The Bolocam Galactic Plane Survey. XIV. Physical Properties of Massive Starless and Star Forming Clumps

## Abstract

We sort $4683$ molecular clouds between $10^\circ< \ell <65^\circ$ from the Bolocam Galactic Plane Survey based on observational diagnostics of star formation activity: compact $70$ $\mu{\rm m}$ sources, mid-IR color-selected YSOs, ${\rm H_2O}$ and ${\rm CH_3OH}$ masers, and UCHII regions. We also present a combined ${\rm NH_3}$-derived gas kinetic temperature and ${\rm H_2O}$ maser catalog for $1788$ clumps from our own GBT 100m observations and from the literature. We identify a subsample of $2223$ ($47.5\%$) starless clump candidates, the largest and most robust sample identified from a blind survey to date. Distributions of flux density, flux concentration, solid angle, kinetic temperature, column density, radius, and mass show strong ($>1$ dex) progressions when sorted by star formation indicator. The median starless clump candidate is marginally sub-virial ($\alpha \sim 0.7$) with $>75\%$ of clumps with known distance being gravitationally bound ($\alpha < 2$). These samples show a statistically significant increase in the median clump mass of $\Delta M \sim 170-370$ M$_\odot$ from the starless candidates to clumps associated with protostars. This trend could be due to (i) mass growth of the clumps at $\dot{M}\sim200-440$ Msun Myr$^{-1}$ for an average free-fall $0.8$ Myr time-scale, (ii) a systematic factor of two increase in dust opacity from starless to protostellar phases, (iii) and/or a variation in the ratio of starless to protostellar clump lifetime that scales as $\sim M^{-0.4}$. By comparing to the observed number of ${\rm CH_3OH}$ maser containing clumps we estimate the phase-lifetime of massive ($M>10^3$ M$_\odot$) starless clumps to be $0.37 \pm 0.08 \ {\rm Myr} \ (M/10^3 \ {\rm M}_\odot)^{-1}$; the majority ($M<450$ M$_\odot$) have phase-lifetimes longer than their average free-fall time.

## TL;DR

This paper sorts 4683 BGPS 1.1 mm clumps by star-formation indicators, with the Hi-GAL 70 µm compact source as the most sensitive one. 47.5% are starless clump candidates (SCCs). Near-equal counts imply comparable starless and protostellar clump lifetimes. Anchored to a methanol-maser lifetime, the SCC lifetime is **mass-dependent: τ_SCC ≈ 0.37 ± 0.08 Myr (10^3 M☉/M)** for M > 10^3 M☉. It is **< 0.03 Myr for M > 10^4 M☉**. Most SCCs (M < 450 M☉) outlive their ~0.8 Myr free-fall time.

## Problem

How long do massive (Galactic-plane, pc-scale) clumps remain starless before forming a detectable protostar, and does this depend on clump mass? What explains the systematic mass offset between starless and protostellar clumps?

## Approach

- **Sample** (§2–3): 4683 BGPS clumps in 10° < ℓ < 65°. New GBT NH3 (T_K) and 22 GHz H2O maser observations give a catalog of 1788 clumps.
- **Star-formation indicators** (§3): Hi-GAL 70 µm compact sources (visual inspection plus CuTeX), Robitaille et al. (2008) GLIMPSE red sources, RMS, EGOs, H2O and CH3OH (MMB, Pestalozzi 2005, Arecibo) masers, and CORNISH UCHII regions. Definitions:
  - **SCC** ("Starless Clump Candidate"): a clump with no indicator.
  - **Protostellar clump**: one or more indicators.
  - **70 µm Unique**: only a Hi-GAL compact source, i.e., candidates for deeply embedded (≈ Class 0/I) activity.
- **Distances** (§4): Bayesian distance probability density functions (DPDFs). Physical properties come from Monte Carlo sampling over 1640 well-constrained DPDFs.
- **Lifetimes** (§6.2.2): (a) global steady-state ratio N_SCC/N_proto. (b) Mass-resolved absolute lifetime τ_SCC = τ_CH3OH (N_SCC/N_CH3OH) (Eq. 13), computed in 0.0125-dex mass bins (following Battersby 2013 PhD thesis).
- **Reference clock**: the Class II 6.7 GHz CH3OH maser lifetime τ_CH3OH = 2.5–4.5×10^4 yr (van der Walt 2005, for SFR = 4 M☉ yr^-1). This is rescaled inversely to the Galactic SFR of 1.9 ± 0.4 M☉ yr^-1 ([[chomiuk-povich-2011]]), giving **τ_CH3OH = 6.1–9.3×10^4 yr**.
- **Free-fall time**: from the central density n_c of each clump. The average SCC ⟨t_ff⟩ = 0.8 Myr (§6.2.1).

## Key result

- Census (§3.5.1): "2223/4683 (47.5%) are starless candidates and 2460/4683 (52.5%) show some indicator". The Hi-GAL 70 µm source is present in "2168/2460 or 88% of Protostellar clumps".
- Steady-state reading (§6.2.2): the equal numbers imply "the typical lifetime of a starless clump candidate is nearly equal to the typical lifetime of a protostellar clump". The protostellar clump lifetime is taken as the cluster-formation timescale, "typically longer than 1 Myr and up to a few Myrs".
- **Mass-dependent lifetime** (§6.2.2, Fig. 20): "τ_SCC ∼ 0.37 ± 0.08 Myr (10^3 M⊙/M) for M > 10^3 M⊙". The ± is the systematic uncertainty in τ_CH3OH.
- Extrapolation (§6.2.2): the lifetime exceeds ⟨t_ff⟩ below ~450 M☉ (about twice the median SCC mass of 230 M☉). Clumps with M_H2 > 10^4 M☉ have "very short lifetimes τ ≲ 0.03 Myr", consistent with no SCCs above 1.4×10^4 M☉.
- Comparison: these lifetimes are "5 times longer and 3.5 times longer" than Tackenberg et al. (2012) for ATLASGAL clumps able to form 20 and 40 M☉ stars.
- Mass offset (§6.3): SCC-to-protostellar median mass difference is ΔM = 170–370 M☉. The candidate explanations are:
  - clump growth at Ṁ ~ 200–440 M☉ Myr^-1;
  - a factor 1.7–2.5 dust-opacity increase;
  - a lifetime ratio with N_SCC/N_proto ∝ M^−0.4 for 100 ≤ M ≤ 1000 M☉. The global N_SCC/N_proto is 613/1027 ≈ 0.597 in the Distance Sample.
- Virial state: median SCC virial parameter α = 0.7. More than 75% of clumps with known distance are bound (α < 2).

## Assumptions

- Steady state for the global ratio: "the clump formation rate is equal to the destruction rate" (§6.2.2).
- "all clumps capable of forming a 20 M⊙ star (M_clump > 1000 M⊙) will at some time form high-mass YSOs with detectable CH3OH masers" (§6.2.2).
- A single CH3OH maser lifetime applies per clump. Only 25/272 (9.2%) of MMB-associated clumps host more than one maser, so an age-spread bias is argued to be small.
- The maser lifetime scales inversely with the adopted Galactic SFR.
- The indicator ranking (70 µm → mid-IR → H2O → CH3OH → UCHII) is heuristic. The only secure transition is starless → protostellar (§3.5.1).

## Limitations / scope

- The analysis is "not advisable" below 10^3 M☉, where the all-clumps-form-masers assumption fails. The < 450 M☉ statement is an extrapolation.
- **Detection floor**: "starless" means no protostar above the 30–140 L☉ far-IR sensitivity of Galactic-plane surveys, corresponding to 1–2 M☉ protostars accreting at typical rates (§6.3.1). SCCs near the 70 M☉ BGPS 50% completeness limit could only form stars up to ~2.5 M☉, close to that floor.
- Pc-scale clumps at kpc distances are hierarchical and multi-core. A Hi-GAL "compact source" may be a protocluster.
- An infertile-SCC population would bias the lifetimes upward.
- Mass growth, opacity change and differential lifetimes cannot be disentangled with the current data (§6.3.3).

## Replication evidence

Partial. [[battersby-2017]] uses a pixel-based method in the ℓ = 30° field and finds a starless fraction of 60–70%. It argues the result is consistent with this paper's 47%, given that Svoboda et al. include lower column densities and lower-mass tracers. Heyer et al. (2016, ATLASGAL + MIPSGAL, not in vault) find ~70% starless.

## Why this paper matters

This paper brings the statistical-lifetime method to massive clumps on Galactic scales. It shows explicitly that a **single starless lifetime is ill-posed**: the lifetime scales roughly as M^-1, from > t_ff for typical clumps to < 0.03 Myr for > 10^4 M☉. It also establishes the Hi-GAL 70 µm compact source as the dominant (88%) and most sensitive protostellar indicator in the BGPS. That makes its "starless" category directly tied to the 70 µm detection floor, the same floor behind the [[hi-gal-evolutionary-classification]].

The absolute clock is a CH3OH maser lifetime that depends on the Galactic SFR ([[chomiuk-povich-2011]]). A different Milky Way SFR rescales every number here.

## Quotes

1. > "A single timescale cannot properly describe the starless clump evolution timescale" — §6.2.2
2. > "the only certain true evolutionary transition is from the starless clump phase" — §3.5.1

## Open questions surfaced

- How many SCCs host embedded protostars below the 30–140 L☉ 70 µm floor? Deeper far-IR/mm data would reclassify them and shorten the starless lifetime.
- Is the M^-1 scaling of τ_SCC physical (e.g., free-fall of denser massive clumps) or a maser-anchoring artefact?
- What is the relative weight of clump mass growth vs. differential lifetimes in producing the SCC/protostellar mass offset?
- How does the result change with the MMB-based maser counts and a modern Galactic SFR?

## Related material in vault

- Extends: —
- Contradicts: —
- Replicates: —
- Concepts introduced/used: [[statistical-lifetime]], [[prestellar-core]], [[hi-gal-evolutionary-classification]], [[free-fall-time]]
- Cites: [[chomiuk-povich-2011]] (Galactic SFR used to rescale the maser clock), [[dunham-2014]]
- Cited by (in this vault): [[battersby-2017]], [[elia-2017]], [[elia-2021]]
