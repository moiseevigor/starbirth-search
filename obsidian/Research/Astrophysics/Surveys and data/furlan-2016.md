---
title: "The Herschel Orion Protostar Survey: Spectral Energy Distributions and Fits Using a Grid of Protostellar Models"
authors: E. Furlan, W. J. Fischer, B. Ali, A. M. Stutz, T. Stanke, J. J. Tobin, S. T. Megeath, M. Osorio, L. Hartmann, N. Calvet, C. A. Poteet, J. Booker, P. Manoj, D. M. Watson, L. Allen
year: 2016
venue: The Astrophysical Journal Supplement Series, 224, 5 (doi:10.3847/0067-0049/224/1/5)
url: https://arxiv.org/abs/1602.07314
language: en
domain: astrophysics
status: draft
methodology_type: empirical
citation_count: 184
citation_count_date: 2026-09-26
key_concepts: ["[[class-0-protostar]]", "[[luminosity-problem]]", "[[episodic-accretion]]", "[[accretion-outburst]]", "[[bolometric-temperature]]", "[[pacs-bright-red-source]]"]
extends: ["[[stutz-2013]]"]
contradicts: []
replicates: []
cites: ["[[stutz-2013]]", "[[safron-2015]]", "[[evans-2009]]", "[[dunham-2008]]", "[[dunham-2014]]"]
cited_by: ["[[fischer-2019]]", "[[zakri-2022]]", "[[lee-2021]]", "[[park-2021]]"]
quality_notes: "Standard HOPS SED/classification reference for Orion protostars; downstream Orion variability/outburst studies adopt its Class 0/I/flat labels. Class boundaries depend on inclination (edge-on Class I can appear Class 0). Citation count from Semantic Scholar."
author: moiseevigor
tags:
  - agent/research
  - user/moiseevigor
  - domain/astrophysics
  - topic/class-0-protostars
  - topic/sed-modeling
  - topic/spitzer-surveys
  - topic/protostar-observational-signatures
  - topic/protostellar-variability
  - topic/radiative-transfer
  - topic/herschel-protostar-surveys
  - topic/accretion-luminosity
  - paper
  - status/draft
---

# The Herschel Orion Protostar Survey: Spectral Energy Distributions and Fits Using a Grid of Protostellar Models

## Abstract

We present key results from the Herschel Orion Protostar Survey (HOPS): spectral energy distributions (SEDs) and model fits of 330 young stellar objects, predominantly protostars, in the Orion molecular clouds. This is the largest sample of protostars studied in a single, nearby star formation complex. With near-infrared photometry from 2MASS, mid- and far-infrared data from Spitzer and Herschel, and submillimeter photometry from APEX, our SEDs cover 1.2 – 870 μm and sample the peak of the protostellar envelope emission at ∼100 μm. Using mid-IR spectral indices and bolometric temperatures, we classify our sample into 92 Class 0 protostars, 125 Class I protostars, 102 flat-spectrum sources, and 11 Class II pre-main-sequence stars. We implement a simple protostellar model (including a disk in an infalling envelope with outflow cavities) to generate a grid of 30,400 model SEDs and use it to determine the best-fit model parameters for each protostar. We argue that far-IR data are essential for accurate constraints on protostellar envelope properties. We find that most protostars, and in particular the flat-spectrum sources, are well fit. The median envelope density and median inclination angle decrease from Class 0 to Class I to flat-spectrum protostars, despite the broad range in best-fit parameters in each of the three categories. We also discuss degeneracies in our model parameters. Our results confirm that the different protostellar classes generally correspond to an evolutionary sequence with a decreasing envelope infall rate, but the inclination angle also plays a role in the appearance, and thus interpretation, of the SEDs.

## TL;DR

Homogeneous 1.2–870 μm SEDs (2MASS, IRAC, IRS, MIPS 24, PACS 70/100/160, APEX 350/870) for 330 Orion YSOs at 420 pc, classified as 92 Class 0 / 125 Class I / 102 flat / 11 Class II, and fit with a 30,400-SED Whitney radiative-transfer grid. Class 0 median L_tot 5.5 L☉, ρ₁₀₀₀ 5.9×10⁻¹⁸ g cm⁻³, inclination 70°. From the machine-readable SED table (VizieR J/ApJS/224/5; vault-derived, not stated in the paper), Class 0 protostars are measured at 4.5 μm in 73/92 and at 3.6 μm in 60/92, but in K_s only 14/92; the 19 "PACS Bright Red sources" (PBRs, the reddest subset) are measured at 4.5 μm in only 9/19.

## Problem

What are the SEDs and physical envelope/disk parameters of a large, uniformly observed protostar sample in one nearby complex, and do SED classes (Class 0, I, flat) map onto an evolutionary sequence once far-IR (envelope-peak) data are included?

## Approach

- **Sample** (§II): 488 Spitzer protostars of Megeath et al. (2012) with 3.6–24 μm spectral index ≥ −0.3 → HOPS targets required a predicted PACS 70 μm flux ≥ 42 mJy and a 24 μm detection (so protostars in the Orion Nebula, where 24 μm is saturated, are excluded). Plus 16 Herschel-discovered protostars (15 from [[stutz-2013]], HOPS 394–408; one from Tobin et al., HOPS 409). From 410 HOPS IDs, removing duplicates, 31 likely extragalactic contaminants, unobserved/undetected-at-70 μm targets → 330 objects (§II).
- **Data** (§III.1): 2MASS JHK_s (4″ apertures), IRAC (2.4″ apertures), MIPS 24 μm (PSF), IRS 5–38 μm spectra (rebinned to 16 continuum/silicate points), PACS 70/100 (9.6″) and 160 μm (12.8″) with aperture corrections, APEX SABOCA 350 μm and LABOCA 870 μm beam fluxes. No heterogeneous literature data added. Photometry flags: 0 not observed, 1 measured, 2 upper limit, 3 not detected (Table 1 note).
- **Classification** (§III.3): n₄.₅₋₂₄ = 4.5–24 μm spectral index; T_bol = bolometric temperature (temperature of a blackbody with the same mean frequency as the SED; Myers & Ladd); L_bol by trapezoidal integration at 420 pc. Class 0: n₄.₅₋₂₄ > 0.3 and T_bol < 70 K; Class I: n₄.₅₋₂₄ > 0.3 and T_bol > 70 K; flat: −0.3 < n₄.₅₋₂₄ < 0.3; Class II: n₄.₅₋₂₄ < −0.3.
- **Model grid** (§IV): 2008 Whitney Monte Carlo radiative-transfer code; star + disk + TSC (Terebey–Shu–Cassen rotating infalling) envelope with outflow cavity; Ormel et al. "icsgra3" icy-grain opacities. "There are 3040 models in the grid; they cover 8 values for the total (i.e., intrinsic) luminosity, 4 disk radii, 19 envelope infall rates (which correspond to envelope densities), and 5 cavity opening angles", × 10 inclinations (18.2°–87.2°, equal steps in cos i) = 30,400 SEDs (§IV.1). Fixed: M★ = 0.5 M☉, M_disk = 0.05 M☉, envelope outer radius 10,000 AU. Model fluxes in 24 apertures 420–10,080 AU (§IV.2). External (ISRF) heating tested separately, not in grid (§IV.3).
- **Fitting** (§V): best fit by minimising R, "a measure of the average distance between model and data in units of the fractional uncertainty" (§VIII), with free foreground A_V and a luminosity scaling factor (0.5–2). ρ₁₀₀₀ = envelope density at 1000 AU (reference density).

## Key result

Classification (§III.3, Abstract):
- "92 Class 0 protostars, 125 Class I protostars, 102 flat-spectrum sources, and 11 Class II pre-main-sequence stars."
- Median L_bol, T_bol, n₄.₅₋₂₄: "1.1 L☉, 146 K, and 0.68"; L_bol distribution peaks near 1 L☉, range ~0.02 to several hundred L☉.
- Nine sources within ±5% of the 70 K Class 0/I boundary (§III.3).

Fit quality (§VI.1, §VIII):
- "About 70% of Class 0 protostars, 75% of Class I protostars, and close to 90% of flat-spectrum sources have reliable SED fits (R<4…)".
- Median R: 3.27 (Class 0), 3.18 (Class I), 2.58 (flat).

Parameters by class (Table 3, §VI.3):

| Median | Class 0 | Class I | Flat |
|---|---|---|---|
| L_tot (L☉) | 5.5 | 2.0 | 3.0 |
| ρ₁₀₀₀ (g cm⁻³) | 5.9×10⁻¹⁸ | 2.4×10⁻¹⁹ | 1.2×10⁻¹⁹ |
| cavity θ | 25° | 15° | 25° |
| R_disk (AU) | 100 | 50 | 5 |
| inclination i | 70° | 63° | 57° |
| foreground A_V | 9.2 | 8.9 | 10.1 |

- Corresponding envelope infall rates for a 0.5 M☉ star: "2.5×10⁻⁵, 1.0×10⁻⁶, and 5.0×10⁻⁷ M☉ yr⁻¹" (Class 0, I, flat; §VII.2).
- Class 0 L_tot distribution differs from Class I/flat (K–S significance < 0.015); Class 0 and I span ~0.06–600 L☉ (§VI.3).
- Model L_tot distribution peaks near 2.5 L☉ vs L_bol near 1 L☉ → L_bol systematically underestimates intrinsic luminosity (inclination/beaming + foreground extinction); "an increase in the luminosity by a factor of 2.5-3 would not solve" the luminosity problem — episodic accretion or mass-dependent accretion still needed (§VII.3).

PACS Bright Red sources (§VII.2.1): 19 PBRs (HOPS 169, 341, 354, 358, 359, 372, 373, 394, 397–405, 407, 409), defined by Stutz et al. via log(λF_λ(70)/λF_λ(24)) > 1.65; median ρ₁₀₀₀ = 1.2×10⁻¹⁷ g cm⁻³ (twice the Class 0 median); median envelope mass within 2500 AU 0.66 M☉ (0.07–1.83); median L_tot 5.6 L☉ (0.6–71.0); 14/19 fit with i ≥ 70°.

Sub-mm detection (§VII.2.3): "75% of Class 0+I protostars observed with SABOCA (350 μm) are detected, while only 47% of flat-spectrum sources have detections."

Variability (§III.2, Appendix B): "about 5% of the protostars with IRS, IRAC, and MIPS data could be variable" (≳ 50% mismatches between IRS, IRAC and MIPS fluxes). HOPS 223 (V2775 Ori) is the only SED affected by extreme variability (pre-outburst 2MASS/IRAC/MIPS, post-outburst IRS/PACS/APEX); HOPS 383 ([[safron-2015]]) uses post-outburst YSOVAR 3.6/4.5 μm fluxes.

**Vault-derived near/mid-IR detection statistics** (computed by Researcher on 2026-09-26 from VizieR J/ApJS/224/5 tables 1–2; counts of flag = 1 "measured"; the remainder are upper limits or non-detections; Vega mags use the paper's zero points 666.7 Jy K_s, 280.9 Jy [3.6], 179.7 Jy [4.5]; not a number stated in the paper):

| Class (n) | J | H | K_s | [3.6] | [4.5] | [5.8] | [8.0] | [24] | [70] |
|---|---|---|---|---|---|---|---|---|---|
| 0 (92) | 2 | 5 | 14 | 60 | 73 | 67 | 58 | 79 | 92 |
| I (125) | 36 | 57 | 80 | 124 | 124 | 123 | 123 | 125 | 125 |
| flat (102) | 60 | 82 | 97 | 100 | 101 | 101 | 101 | 102 | 102 |
| II (11) | 8 | 8 | 9 | 9 | 11 | 10 | 10 | 11 | 11 |
| PBRs (19) | – | – | 1 | 8 | 9 | – | – | 10 | – |

- Class 0 detected-source magnitudes (Vega, at 420 pc): [4.5] median 12.16 (p10 10.09, p90 14.67, faintest 16.07); [3.6] median 13.84 (p10 12.09, p90 16.01); K_s median 14.28.
- Class I [4.5] median 10.60; flat [4.5] median 8.79.
- Reading: ~79% of Orion Class 0 protostars and ~47% of PBRs have a measured 4.5 μm flux (IRAC, 2.4″ aperture); ~15% have K_s. Caveat: the HOPS sample itself required Spitzer photometry (except the Herschel-discovered PBRs), so these fractions are conditional on that selection.

## Assumptions

- Single distance of 420 pc for all Orion sources; luminosity scaling factor absorbs some distance spread.
- Axisymmetric TSC envelope with constant infall rate; fixed M★, M_disk, envelope outer radius; one dust model (icy grains).
- No external heating in the grid (ISRF tested separately; §IV.3).
- Non-simultaneous photometry treated as a single static SED (Spitzer 2004–2009, Herschel 2009–2012, APEX); IRS scaled to IRAC/MIPS where needed.

## Limitations / scope

- Parameter degeneracies (§VI, §VII.2): higher envelope density ↔ higher inclination ↔ smaller cavity ↔ smaller disk radius all steepen the mid-IR slope and deepen silicate absorption; "the observed classes contain a mixture of evolutionary stages" (§VIII). T_bol is inclination-dependent, so edge-on Class I can be classified Class 0.
- Sample incompleteness: Orion Nebula excluded (24 μm saturation); "our sample could miss fainter flat-spectrum sources and Class 0 and Class I protostars" (§III.3); 41 likely protostars lack PACS data (Appendix D.2.1).
- 870 μm upper limits often due to confusion with bright, spatially varying emission (§VII.2.3).
- Variability can bias fits without inflating R (§VI.1).
- TSC model issues discussed in §VII.4 (not summarised here).
- Read in full via arXiv HTML (v2); detection statistics above computed from the published VizieR tables.

## Replication evidence

Partial. The Class 0/I/flat labels and SEDs are reused by later Orion variability studies in this vault ([[fischer-2019]], [[zakri-2022]], [[park-2021]], [[lee-2021]]). The PBR interpretation replicates/extends [[stutz-2013]] with full model fits. Physical parameters are model-dependent and not independently replicated here (resolved-imaging tests of inclination/disk radius are outside this vault).

## Why this paper matters

HOPS provides the most-used homogeneous SED catalogue and classification of protostars in a single nearby complex, and its median-per-class SEDs (Fig. 41) are a practical template for what Class 0 protostars look like from 1 to 870 μm: a deep 10 μm silicate absorption, a steeply rising mid-IR SED and a ~100 μm peak. Its explicit finding that inclination, not only evolution, drives class assignment is an important caveat for any lifetime or rate estimate based on Class 0/I counts.

The per-class detection statistics (derived here from the public tables) quantify how often Class 0 protostars at 420 pc are visible at 3.6–4.5 μm (roughly two-thirds to four-fifths) versus the near-IR (rarely), and show that the reddest PBRs are detected at 4.5 μm only about half the time.

## Quotes

1. > "far-IR data are essential for accurate constraints on protostellar envelope properties" — Abstract
2. > "the observed classes contain a mixture of evolutionary stages" — §VIII

## Open questions surfaced

- How do the Class 0 3.6/4.5 μm detection fractions scale with distance (e.g. 2–5 kpc Galactic-plane protostars) and with ~6″ vs 2″ resolution — i.e. what fraction of Class 0 protostars would a W1/W2 survey detect at all?
- Can resolved imaging (ALMA/VLA inclinations, disk radii) break the ρ₁₀₀₀–inclination degeneracy and re-sort Class 0 vs edge-on Class I?
- Does including ISRF heating or non-TSC envelopes change the ~30% of Class 0 SEDs with R ≥ 4?
- Promised Fischer et al. follow-up on L_tot evolution (§VII.3).

## Related material in vault

- Extends: [[stutz-2013]]
- Contradicts: —
- Replicates: —
- Concepts introduced/used: [[class-0-protostar]], [[luminosity-problem]], [[episodic-accretion]], [[accretion-outburst]], [[bolometric-temperature]], [[pacs-bright-red-source]]
- Cites: [[stutz-2013]], [[safron-2015]], [[evans-2009]], [[dunham-2008]], [[dunham-2014]]
- Cited by (in this vault): [[fischer-2019]], [[zakri-2022]], [[lee-2021]], [[park-2021]]
