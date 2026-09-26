---
title: "The Lifetimes of Phases in High-Mass Star-Forming Regions"
authors: Cara Battersby, John Bally, Brian Svoboda
year: 2017
venue: The Astrophysical Journal 835, 263
url: https://arxiv.org/abs/1702.02199
language: en
domain: astrophysics
status: draft
methodology_type: empirical
citation_count: 25
citation_count_date: 2026-09-26
key_concepts: ["[[statistical-lifetime]]", "[[prestellar-core]]", "[[hi-gal-evolutionary-classification]]", "[[free-fall-time]]"]
extends: ["[[svoboda-2016]]"]
contradicts: []
replicates: []
cites: ["[[svoboda-2016]]", "[[chomiuk-povich-2011]]"]
cited_by: ["[[elia-2021]]"]
quality_notes: "Single 2°×2° field (ℓ = 30°, containing the W43 'mini-starburst'), so relative lifetimes may not be Galaxy-representative. The authors call their absolute lifetimes 'highly uncertain'. The relative 60–70% / 30–40% split is the robust product."
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
  - topic/galactic-star-formation-rate
  - topic/clump-evolutionary-stages
  - topic/methanol-masers
  - paper
  - status/draft
---

# The Lifetimes of Phases in High-Mass Star-Forming Regions

## Abstract

High-mass stars form within star clusters from dense, molecular regions, but is the process of cluster formation slow and hydrostatic or quick and dynamic? We link the physical properties of high-mass star-forming regions with their evolutionary stage in a systematic way, using Herschel and Spitzer data. In order to produce a robust estimate of the relative lifetimes of these regions, we compare the fraction of dense, molecular regions above a column density associated with high-mass star formation, N(H2) > 0.4-2.5 x 10^22 cm^-2, in the 'starless' (no signature of stars > 10 Msun forming) and star-forming phases in a 2x2 degree region of the Galactic Plane centered at l=30deg. Of regions capable of forming high-mass stars on ~1 pc scales, the starless (or embedded beyond detection) phase occupies about 60-70% of the dense molecular region lifetime and the star-forming phase occupies about 30-40%. These relative lifetimes are robust over a wide range of thresholds. We outline a method by which relative lifetimes can be anchored to absolute lifetimes from large-scale surveys of methanol masers and UCHII regions. A simplistic application of this method estimates the absolute lifetimes of the starless phase to be 0.2-1.7 Myr (about 0.6-4.1 fiducial cloud free-fall times) and the star-forming phase to be 0.1-0.7 Myr (about 0.4-2.4 free-fall times), but these are highly uncertain. This work uniquely investigates the star-forming nature of high-column density gas pixel-by-pixel and our results demonstrate that the majority of high-column density gas is in a starless or embedded phase.

## TL;DR

This is a pixel-by-pixel (not clump-based) lifetime analysis of the ℓ = 30° field using Hi-GAL T_dust / N(H2) maps and GLIMPSE 8 µm contrast. Dense molecular regions able to form high-mass stars spend **60–70% of their life "starless"** (no ≳10 M☉ star forming) and **30–40% star-forming**, robust to the column-density threshold. Absolute durations anchored to CH3OH masers or UCHII regions are **0.2–1.7 Myr starless and 0.1–0.7 Myr star-forming**, i.e., 0.6–4.1 and 0.4–2.4 free-fall times, and are highly uncertain.

## Problem

Is high-mass cluster formation slow and quasi-equilibrium (several t_ff) or fast and dynamic (~1 t_ff)? Clump-based lifetime estimates lump quiescent and active gas together: one mid-IR point source makes the whole clump "star-forming". The resulting estimates depend on the clump-finding algorithm (the same region is 1 BGPS clump, 3 or 5 ATLASGAL clumps).

## Approach

- **Data** (§2): 25″-resolution Hi-GAL T_dust and N(H2) maps (160–500 µm modified-blackbody fits, diffuse Galactic component removed; Battersby et al. 2011). Also GLIMPSE 8 µm contrast, 6.7 GHz CH3OH masers (Pestalozzi et al. 2005) and UCHII regions (Wood & Churchwell 1989). Field: 2°×2° at [ℓ, b] = [30°, 0°], at distances of 5–9 kpc.
- **DMR** ("dense molecular region"): any pixel above a column-density threshold for high-mass star formation (§2.1). The Σ = 1 g cm^-2 criterion of Krumholz & McKee (2008) applied to a Mueller et al. (2002) core model (r_f ≈ 1000 AU, p = 1.8), beam-diluted, gives N(H2) = 0.8 ("conservative") and 0.4×10^22 cm^-2 ("generous"). The alternative Kauffmann & Pillai (2010, "KP10") criterion gives 1.6–2.5×10^22 cm^-2.
- **Starless vs. "starry"** (§2.2, Fig. 2): the 8 µm contrast (mid-IR dark / neutral / bright) is the primary discriminator. Dust temperature within 2σ/3σ of the dark or bright distributions is secondary (dark: 11–28 K conservative, 9–32 K generous; bright: 21–42 K / 12–47 K). For mid-IR-neutral pixels the split is at 25 K.
- **Detection floor**: the 8 µm limit of ~130 MJy/sr detects ~85% of Robitaille et al. (2006) model YSOs above 10 M☉. "Starless" therefore means only no high-mass star.
- **Relative lifetimes**: f_starless = N_starless/N_total, f_starry = N_starry/N_total (Eqs. 2–3).
- **Absolute anchoring** (§3.3–3.4):
  - Methanol masers: τ_total = τ_maser / f_maser (Eq. 4), with τ_maser = 35,000 yr (van der Walt 2005). Then τ_starless = f_starless τ_total and τ_starry = f_starry τ_total (Eqs. 5–6).
  - UCHII regions: τ_total = τ_UCHII / (f_starry f_UCHII) (Eq. 7), with τ_UCHII = 3.6×10^5 yr (15% of an O6 main-sequence lifetime) and f_UCHII = 50–100%.
- **Free-fall times** (§3.5): from the median pixel column density, assuming 1 pc size and a Gaussian profile (Svoboda et al. 2016, Eqs. 11–12).

## Key result

- Relative lifetimes (§3.2): "about 70% of the pixels are categorized as starless and 30% as starry" for any threshold in 0.3–1.3×10^22 cm^-2. At the KP10 thresholds (1.7–2.5×10^22 cm^-2), "about 63% are starless and 37% star-forming". Below ~0.3×10^22 cm^-2 the split is 50/50.
- Table 1 (verbatim, lifetimes in Myr):

| Criteria | N(H2) [cm^-2] | f_starless | f_starry | Anchor | τ_total | τ_starless | τ_starry |
|---|---|---|---|---|---|---|---|
| Generous | 0.4×10^22 | 0.71 | 0.29 | maser | 1.9 | 1.4 | 0.6 |
| Conservative | 0.8×10^22 | 0.72 | 0.28 | maser | 0.9 | 0.6 | 0.3 |
| Either | 0.4–0.8×10^22 | 0.7 | 0.3 | UCHII | 1.2–2.4 | 0.8–1.7 | 0.4–0.7 |
| KP10 near | 2.5×10^22 | 0.63 | 0.37 | maser | 0.3 | 0.2 | 0.1 |
| KP10 far | 1.6×10^22 | 0.63 | 0.37 | maser | 0.5 | 0.3 | 0.2 |
| Either KP | 1.6–2.5×10^22 | 0.63 | 0.37 | UCHII | 1.0–1.9 | 0.6–1.2 | 0.4–0.7 |
| Overall | 0.4–2.5×10^22 | 0.6–0.7 | 0.3–0.4 | both | 0.3–2.4 | 0.2–1.7 | 0.1–0.7 |

- Maser fraction (§3.3): f_maser = 2% (generous) and 4% (conservative), giving τ_total = 1.9 and 0.9 Myr. Under KP10, f_maser ≈ 7–12%. f_maser rises with the column-density threshold, while f_starless does not.
- In free-fall units (Table 2, §3.5): total 1.0–6.5 t_ff, starless 0.6–4.1 t_ff, starry 0.4–2.4 t_ff.
- Alternative anchor (§3.6): with the commonly assumed τ_starry = 2×10^5 yr (Zinnecker & Yorke 2007), the starless phase would be 0.3–0.5 Myr.
- Galactic SFR sanity check (§3.7): 0.5–3×10^5 M☉ of gas in the starry phase, 30% efficiency, 0.1–0.7 Myr. This gives 0.02–0.82 M☉ yr^-1 in the field and 0.3–20 M☉ yr^-1 extrapolated to the Galaxy, compared with the ~2 M☉ yr^-1 consensus ([[chomiuk-povich-2011]]). The result is inflated by W43.

## Assumptions

Listed in §3.1:
1. The sample is complete and unbiased in time and space.
2. The DMRs represent all phases with equal probability, through a constant SFR or a large sample (the steady-state analogue).
3. DMRs are forming or will form high-mass stars.
4. Lifetimes do not depend on mass. This is justified by the small column-density range of the DMRs (threshold to 2× threshold).
5. Starless and star-forming regions have area proportional to mass.
6. 8 µm brightness plus T_dust reliably indicates the presence or absence of a high-mass star.
7. Above-threshold pixels contain beam-diluted dense cores, not beam-filling diffuse gas.

## Limitations / scope

- **Single field**: the field includes the W43 mini-starburst, likely in a higher-SFR phase, so results may not generalise to the whole Galaxy (§3.1).
- **Absolute lifetimes**: they rest on a van der Walt (2005) maser lifetime derived from a Galactic SFR and IMF, or on a 1989 UCHII lifetime with an assumed f_UCHII = 50–100%. A mid-B instead of an O6 star changes the UCHII anchor by ~5× (footnote 5).
- **Sensitivity**: only ≳10 M☉ forming stars are detected. "Starless" includes "embedded beyond detection" phases and regions with active low- or intermediate-mass star formation.
- **Geometry**: pole-on filaments would mimic high column density and inflate the starless fraction.
- **Ejected stars**: runaway high-mass stars could flag starless gas as "starry" by proxy.
- **Free-fall times**: these are "present day" estimates from simple geometric assumptions, not measured volume densities.

## Replication evidence

Partial agreement. The starless fraction of 60–70% matches Heyer et al. (2016, ATLASGAL + MIPSGAL, ~70% starless; not in vault). It is somewhat higher than [[svoboda-2016]] (47%), which the authors attribute to Svoboda et al. probing lower column density and lower-mass star-formation tracers. Table 3 compiles earlier starless fractions of 0.18–0.82 from IRDC and clump studies.

## Why this paper matters

The paper removes the clump-definition dependence from statistical lifetimes by counting pixels, and shows that the relative starless/star-forming split for high-mass-capable gas is stable at ~2:1 across thresholds. It makes explicit that the absolute timescale is set almost entirely by the anchor: maser vs. UCHII vs. an assumed 2×10^5 yr YSO phase gives a factor ~5–8 range. It also frames the result in free-fall units (starless 0.6–4.1 t_ff), which bears on the slow-vs.-dynamic debate for cluster formation.

Together with [[svoboda-2016]], it defines the high-mass branch of the [[statistical-lifetime]] literature. Here the reference clocks are maser/UCHII lifetimes tied to the Galactic SFR, rather than the low-mass Class II ~2 Myr clock.

## Quotes

1. > "the connection of our relative lifetimes to absolute lifetimes is extremely uncertain" — §3.2
2. > "assigning a single lifetime to regions of different masses and densities is a simplification" — §3.6

## Open questions surfaced

- Does the ~70/30 starless/star-forming split hold outside the W43-dominated ℓ = 30° field?
- Can MMB methanol-maser and CORNISH UCHII catalogs, both suggested by the authors, tighten the absolute anchors?
- How much of the "starless" gas hosts embedded high-mass protostars below the 8 µm limit? Far-IR (70 µm) tracers could test this, as in [[svoboda-2016]].
- How does the pixel-based fraction change at higher resolution, where clump confusion is less severe?

## Related material in vault

- Extends: [[svoboda-2016]] (applies the maser-anchoring method and its free-fall-time formulae to pixel-based DMRs)
- Contradicts: —
- Replicates: —
- Concepts introduced/used: [[statistical-lifetime]], [[prestellar-core]], [[hi-gal-evolutionary-classification]], [[free-fall-time]]
- Cites: [[svoboda-2016]], [[chomiuk-povich-2011]]
- Cited by (in this vault): [[elia-2021]]
