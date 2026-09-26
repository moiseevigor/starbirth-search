---
title: "The most variable VVV sources: eruptive protostars, dipping giants in the Nuclear Disc and others"
authors: P. W. Lucas, L. C. Smith, Z. Guo, C. Contreras Peña, D. Minniti, N. Miller, J. Alonso-García, M. Catelan, J. Borissova, R. K. Saito, R. Kurtev, M. G. Navarro, C. Morris, H. Muthu, D. Froebrich, V. D. Ivanov, A. Bayo, A. Caratti o Garatti, J. L. Sanders
year: 2024
venue: Monthly Notices of the Royal Astronomical Society, 528, 1789–1822
url: https://arxiv.org/abs/2401.14471
doi: 10.1093/mnras/stad3929
language: en
domain: astrophysics
status: draft
methodology_type: empirical
citation_count: 5
citation_count_date: 2026-09-26
key_concepts: ["[[accretion-outburst]]", "[[episodic-accretion]]", "[[confusion-limit]]"]
extends: []
contradicts: []
replicates: []
cites: ["[[lee-2021]]", "[[park-2021]]", "[[evans-2009]]", "[[kuhn-2021]]", "[[mainzer-2014]]", "[[meisner-2023]]", "[[contreras-pena-2024]]"]
cited_by: ["[[contreras-pena-2024]]"]
quality_notes: "Citation count from Semantic Scholar (DOI lookup), likely an undercount. This is a discovery and characterisation paper, not a rate paper: it gives no incidence or recurrence time. Spectroscopic confirmation is in the companion Guo et al. 2024 (MNRAS 528, 1769; 'GLK'), which is not in this vault. The companion rate paper is contreras-pena-2024."
author: moiseevigor
tags:
  - agent/research
  - user/moiseevigor
  - domain/astrophysics
  - topic/accretion-outbursts
  - topic/protostellar-variability
  - topic/time-domain-surveys
  - topic/vvv-survey
  - topic/survey-artefacts-and-contamination
  - paper
  - status/draft
---

# The most variable VVV sources: eruptive protostars, dipping giants in the Nuclear Disc and others

## Abstract

We have performed a comprehensive search of a VISTA Variables in the Via Lactea (VVV) database of 9.5 yr light curves for variable sources with ΔK_s ≥ 4 mag, aiming to provide a large sample of high amplitude eruptive young stellar objects (YSOs) and detect unusual or new types of infrared variable source. We find 222 variable or transient sources in the Galactic bulge and disc, most of which are new discoveries. The sample mainly comprises novae, YSOs, microlensing events, Long Period Variable stars (LPVs) and a few rare or unclassified sources. Additionally, we report the discovery of a significant population of aperiodic late-type giant stars suffering deep extinction events, strongly clustered in the Nuclear Disc of the Milky Way. We suggest that these are metal-rich stars in which radiatively driven mass loss has been enhanced by super-solar metallicity. Among the YSOs, 32/40 appear to be undergoing episodic accretion. Long-lasting YSO eruptions have a typical rise time of ∼2 yr, somewhat slower than the 6–12 month timescale seen in the few historical events observed on the rise. The outburst durations are usually at least 5 yr, somewhat longer than many lower amplitude VVV events detected previously. The light curves are diverse in nature, suggesting that multiple types of disc instability may occur. Eight long-duration extinction events are seen wherein the YSO dims for a year or more, attributable to inner disc structure. One binary YSO in NGC 6530 displays periodic extinction events (P=59 days) similar to KH 15D.

## TL;DR

This is a blind search of 562 deg² of VVV/VIRAC2 K_s light curves (2010–2019) for ΔK_s ≥ 4 mag. It returns 222 sources, of which only 40 are YSOs; the rest are novae, microlenses, LPVs and dipping giants. Of the 40 YSOs, 32 are eruptive. High-amplitude, long-duration YSO eruptions rise slowly: typically 600–1000 d in K_s, with a fitted T_fit peaking at 600–800 d. They usually last ≥ 5 yr, and their progenitors are mostly Class I or flat-spectrum. The paper is a false-positive census: at ΔK_s ≥ 4 mag, fewer than one in five sources is a YSO.

## Problem

What are the highest-amplitude near-IR variables in the obscured inner Galaxy? In particular, what do the rise times, durations and light-curve shapes of high-amplitude (ΔK_s ≥ 4) YSO eruptions look like? Previous VVV searches found few YSOs above 4 mag (§1).

## Approach

- **Data (§2.1–2.2).** VIRAC2-α (2010–2018) and VIRAC2-β (2010–2019) hold DoPHOT profile-fitting photometry, with ~200 K_s epochs per source. Resolution is ~0.75″, sensitivity K_s ≈ 17.5, and saturation "in the range K_s = 11–12" (§2.1). Amplitudes use 1-day-binned fluxes with 3σ clipping.
- **Search (§2.4, App. A).** Candidate selection is followed by removal of false positives, which include saturation halos, stellar blends, asteroid+star blends and high-proper-motion blends (App. A). A parallel VVV DR4 aperture-photometry search goes down to ΔK_s > 3 mag and finds 105 sources (§2.3, App. C).
- **Classification (§3).** Classes are assigned from light-curve morphology, GLIMPSE/WISE colours, SIMBAD/VSX, Gaia DR3, location in star-forming regions and the companion spectroscopy (GLK).
- **Rise-time fitting (§4.1).** For 18 fully sampled rises, a piecewise tanh/logistic model is fitted with e-folding τ. The reported quantity is T_fit = 4τ, which covers 0.88 of the amplitude s.

## Key result

- **Census (§3).** The 222 sources are 70 CVs (novae), 40 YSOs, 38 microlensing events, 35 LPVs, 21 "dipping giants", 10 "unusual" and 8 "sparse" transients. Of the 222 sources, 162 (73 per cent) are VVV discoveries. "Most YSOs (35/40) lie at Galactic latitudes |b| < 1°".
- **YSO split (§4).** Of the 40 YSOs, 32 are eruptive and 8 are extinction dippers. Of the 32 eruptive YSOs, 20 (63%) are "classic" events with a smooth rise to a plateau lasting several years. Nine are irregular, and three more peaked in 2010 or earlier.
- **Rise times (§4.1).** "We see that the typical rise time is 600 to 1000 d". The fitted T_fit is "typically between 400 and 1000 days, with the peak at 600 to 800 days". For comparison, historical optical FUor rises were FU Ori ~6 months, V1057 Cyg 13 months, and V1515 Cyg ≥ 15 yr.
- **Durations (§7).** "The typical outburst duration is at least 5 yr, rather longer than many lower amplitude events". These durations are mostly lower limits because events continued past 2019.
- **Progenitor stage (§4.1).** The pre-outburst spectral index (WISE 3–22 µm or Spitzer 3–24 µm) has "mean spectral index is α = 0.16". "(14/16) systems fall in the Class I category (α > 0.3) or Flat Spectrum category".
- **Progenitor luminosity (§4.1).** The median quiescent K_s = 16.5 at 2–8 kpc gives 2 < M_Ks < 5. Comparison with Evans et al. (2009) suggests 0.2 < L_bol/L⊙ < 20, i.e. low-mass YSOs of roughly 0.2–3 M⊙.
- **Periodicity (§7).** "Periodic outbursts are not seen at these high amplitudes". One YSO (source 148) shows periodic 2 mag outbursts superimposed on a 3 mag classic outburst.
- **Dippers.** Eight YSO extinction events last ≥ 1 yr. Source 207 in NGC 6530 is KH 15D-like, with P = 59 d.
- **Non-YSO contaminants.** Of the 21 dipping giants, 18 are projected in the Nuclear Disc and 7 are spectroscopically confirmed late-type giants. Without spectra, these could be mistaken for AA Tau-like YSO dippers or eruptive YSOs (§3).

## Assumptions

- ΔK_s from binned, clipped light curves slightly under-estimates true amplitudes because of sparse sampling. Some sources just under 4 mag are retained (§2.2).
- YSO status is assigned from several indicators. Projection in a star-forming region is down-weighted within 10° of the Galactic centre, where star-formation tracers are ubiquitous (§3).
- Rise times are read from sparse VVV sampling, with error bars from visual inspection (§4.1).

## Limitations / scope

- **No rate.** The paper gives no incidence or recurrence estimate because the ΔK_s ≥ 4 selection is not tied to a defined YSO parent sample. Rates are in [[contreras-pena-2024]].
- **Nebulosity and blending (§4.1, footnote 5).** "Bright and highly structured nebulosity is typically not well handled by photometric pipelines". WISE, GLIMPSE, MIPSGAL and VVV detections therefore had to be verified by eye, and blended sources were removed. Several eruptive YSOs lack a spectral index because they are veiled by strong nebulosity gradients or blending, so their SEDs cannot be assumed to be bluer. One YSO (VVV 1640-4846) sits in a compact nebula and needed custom aperture photometry (§3).
- **Confusion.** Near the Galactic centre, blends and a very high surface density of cloud cores make YSO/giant discrimination ambiguous without spectra (§3, §5).
- **Saturation.** Saturation at K_s ≈ 11–12 needs corrected photometry. A search with saturation-corrected photometry "would probably yield some additional discoveries" (App. A).
- **Coverage.** Only the original VVV area is searched; the VVVX extensions are excluded.

## Replication evidence

Partial. The FUor/EXor nature of most classic events is confirmed spectroscopically in the companion Guo et al. 2024 (GLK). [[contreras-pena-2024]] independently finds, over the same VIRAC2 data, that ΔK_s > 4.8 mag occurs only in outbursts lasting more than 9 yr. This agrees with the long durations here. The slow ~2 yr near-IR rise has not yet been tested by an independent survey.

## Why this paper matters

The paper sets the empirical shape of high-amplitude embedded outbursts in the near-IR. Rises of about 2 yr are slower than the canonical 6–12 month optical FUor rises, and durations of at least 5 yr are typical. This matters for designing detection criteria in sparse-cadence surveys such as NEOWISE (6-month cadence): a 2 yr rise is resolved by ~4 NEOWISE visits.

It is equally useful as a contamination census. At ΔK_s ≥ 4 mag across the inner Galaxy, most sources are novae, microlenses, LPVs or metal-rich dipping giants rather than YSOs. The paper also catalogues false positives from nebulosity, blending, saturation halos and asteroids that any blind infrared outburst search must remove.

## Quotes

1. > "Periodic outbursts are not seen at these high amplitudes" — §7
2. > "Bright and highly structured nebulosity is typically not well handled by photometric pipelines" — §4.1, footnote 5

## Open questions surfaced

- Why do near-IR rise times (~600–1000 d) exceed optical FUor rises? Is this a wavelength effect, instability location or disc viscosity (§7, citing Liu et al. 2022)?
- Do the 9 irregular eruptive YSOs, which have multiple maxima within 9.5 yr, form a distinct instability class (compare the Multiple Timescale Variables of Guo et al. 2020, 2021)? Most lack spectra.
- How many ΔK_s ≥ 4 eruptions are missed because progenitors are veiled by nebulosity or saturate?
- Could lower-amplitude analogues of the Nuclear Disc dipping giants contaminate YSO variability samples at |l| < 2°?

## Related material in vault

- Extends: —
- Contradicts: —
- Replicates: —
- Concepts introduced/used: [[accretion-outburst]], [[episodic-accretion]], [[confusion-limit]]
- Cites: [[lee-2021]], [[park-2021]], [[evans-2009]], [[kuhn-2021]], [[mainzer-2014]], [[meisner-2023]], [[contreras-pena-2024]]
- Cited by (in this vault): [[contreras-pena-2024]]
