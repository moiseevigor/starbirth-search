---
title: "Identifying the Low Luminosity Population of Embedded Protostars in the c2d Observations of Clouds and Cores"
authors: Michael M. Dunham, Antonio Crapsi, Neal J. Evans II, Tyler L. Bourke, Tracy L. Huard, Philip C. Myers, Jens Kauffmann
year: 2008
venue: The Astrophysical Journal Supplement Series 179, 249
url: https://arxiv.org/abs/0806.1754
language: en
domain: astrophysics
status: draft
methodology_type: empirical
citation_count: 241
citation_count_date: 2026-09-26
key_concepts: ["[[internal-luminosity]]", "[[luminosity-problem]]", "[[episodic-accretion]]", "[[prestellar-core]]", "[[class-0-protostar]]", "[[statistical-lifetime]]", "[[bolometric-temperature]]", "[[accretion-luminosity]]", "[[vello]]"]
extends: []
contradicts: []
replicates: []
cites: ["[[enoch-2008]]"]
cited_by: ["[[evans-2009]]", "[[enoch-2010]]", "[[pineda-2011]]", "[[stutz-2013]]", "[[dunham-2014]]", "[[konyves-2015]]", "[[safron-2015]]", "[[park-2021]]", "[[lee-2021]]", "[[zakri-2022]]", "[[elia-2022]]", "[[elia-2017]]", "[[enoch-2008]]", "[[furlan-2016]]"]
quality_notes: "Source of the widely used L_int = 3.3e8 F70^0.94 relation (F70 in erg cm^-2 s^-1 at 140 pc); the relation is reused verbatim by enoch-2010 and pineda-2011 to convert 70 µm fluxes/limits into internal luminosities. Citation count from Semantic Scholar (241). The observational calibration rests on only 11 modelled sources; the RADMC model grid (1460 SEDs) carries the fit."
author: moiseevigor
tags:
  - agent/research
  - user/moiseevigor
  - domain/astrophysics
  - topic/embedded-low-luminosity-protostars
  - topic/class-0-protostars
  - topic/prestellar-cores
  - topic/spitzer-surveys
  - topic/sed-modeling
  - topic/evolutionary-lifetimes
  - topic/accretion-outbursts
  - topic/accretion-luminosity
  - topic/radiative-transfer
  - topic/survey-completeness-reliability
  - paper
  - status/draft
---

# Identifying the Low Luminosity Population of Embedded Protostars in the c2d Observations of Clouds and Cores

## Abstract

(Verbatim from the arXiv v1 PDF.)

We present the results of a search for all embedded protostars with internal luminosities ≤ 1.0 L⊙ in the full sample of nearby, low-mass star-forming regions surveyed by the Spitzer Space Telescope Legacy Project "From Molecular Cores to Planet Forming Disks" (c2d). The internal luminosity of a source, L_int, is the luminosity of the central source and excludes luminosity arising from external heating. On average, the Spitzer c2d data are sensitive to embedded protostars with L_int ≥ 4 × 10^−3 (d/140 pc)^2 L⊙, a factor of 25 better than the sensitivity of the Infrared Astronomical Satellite (IRAS) to such objects. We present a set of selection criteria used to identify candidates from the Spitzer data and examine complementary data to decide whether each candidate is truly an embedded protostar. We find a tight correlation between the 70 µm flux and internal luminosity of a protostar, an empirical result based on both observations and detailed two-dimensional radiative transfer models of protostars. We identify 50 embedded protostars with L_int ≤ 1.0 L⊙; 15 have L_int ≤ 0.1 L⊙. The intrinsic distribution of source luminosities increases to lower luminosities. While we find sources down to the above sensitivity limit, indicating that the distribution may extend to luminosities lower than probed by these observations, we are able to rule out a continued rise in the distribution below L_int = 0.1 L⊙. Between 75 − 85% of cores classified as starless prior to being observed by Spitzer remain starless to our luminosity sensitivity; the remaining 15 − 25% harbor low-luminosity, embedded protostars. We compile complete Spectral Energy Distributions for all 50 objects and calculate standard evolutionary signatures (L_bol, T_bol, and L_bol/L_smm), and argue that these objects are inconsistent with the simplest picture of star formation wherein mass accretes from the core onto the protostar at a constant rate.

## TL;DR

The census paper for low-luminosity embedded protostars in c2d. It gives the **L_int–F70 relation**, L_int = 3.3 × 10^8 F70^0.94 L⊙ (F70 in erg cm^-2 s^-1, normalized to 140 pc). With it, c2d 70 µm maps reach **L_int ≥ 4 × 10^-3 (d/140 pc)^2 L⊙**. It finds 50 embedded protostars with L_int ≤ 1 L⊙, of which 15 are VeLLOs, and shows that **15–25% of pre-Spitzer "starless" cores actually host a protostar**. The excess of low-luminosity sources is used as statistical evidence against constant-rate accretion, pointing to episodic accretion.

## Problem

How complete is the census of embedded protostars at L_int ≤ 1 L⊙? How many cores called "starless" before Spitzer (on IRAS evidence) actually contain a protostar? The paper also asks what the low-luminosity population implies for accretion models. IRAS reached only L_int ≳ 0.1 (d/140 pc)^2 L⊙ (§1). Starless-core lifetimes come from counting starless versus protostellar cores, so hidden protostars bias those lifetimes (§6.3).

## Approach

- **Data**: full c2d Spitzer 3.6–160 µm imaging. That is five clouds (Serpens, Lupus I/III/IV, Cha II, Ophiuchus, Perseus; 125–500 pc) and 82 small-core regions containing 95 dense cores (§2).
- **Seven selection criteria** (§3):
  1. 24 µm detection with SNR ≥ 3.
  2. Coverage in at least two bands.
  3. 70 µm detection, unless the source is confused or not covered.
  4. A rising or flat SED from IRAC to 24 µm.
  5. A rising or flat SED from 24 to 70 µm.
  6. L_IR ≤ 0.5 L⊙.
  7. Not a galaxy under the Harvey et al. (2007b) classifier.
- **Relaxed criterion 1 (§3.3)**: an extra search for sources detected at 70 µm but not at 24 µm, aimed at very young or FHSC-like objects. It added 53 candidates, and only 4 weak ones survived visual inspection.
- **Calibrating the L_int proxy (§3.2)**: log–log fits of F_ν against L_int for 11 radiative-transfer-modelled c2d sources, plus a RADMC 2-D grid of 292 models × 5 inclinations = 1460 SEDs. The grid covers a 3000 K protostar at 0.03–10 L⊙, a 100 AU disk, and a 1–10 M⊙ envelope under an external ISRF.
- **Vetting (§5)**: complementary (sub)mm, dense-gas and outflow data sort the 218 surviving candidates into Groups 1–6 by likelihood.
- **Evolutionary indicators (§6.2)**: L_bol, T_bol and L_bol/L_smm are computed and placed on BLT diagrams against the Young & Evans (2005) and Myers et al. (1998) tracks. Here L_bol is the bolometric luminosity, T_bol the bolometric temperature and L_smm the submillimetre luminosity.

## Key result

- **L_int–F70 relation (§3.2, Eq. 2)**: L_int = 3.3 × 10^8 F70^0.94 L⊙, with F70 in cgs units (erg cm^−2 s^−1) and normalized to 140 pc. For the 11 observed sources the reduced χ² of the fit is χ²_r = 3 at 70 µm, χ²_r = 85 at 24 µm, and > 100 at every IRAC band. Models and observations agree to within 3% in slope and 1% in y-intercept.
- **Luminosity sensitivity (§3.2)**: the mean 70 µm 3σ point-source sensitivity of 38.6 mJy corresponds to ~4 × 10^-3 L⊙ at 140 pc. In general this is L_int ≥ 4 × 10^-3 (d/140 pc)^2 L⊙, a factor of 25 better than IRAS.
- **Census (§5–6.1)**: 726 raw candidates (673 plus 53 detected only at 70 µm) → 218 after inspection → 69 with some evidence of being embedded → 50 with complete SEDs. Of these, **15/50 (30%) have L_int ≤ 0.1 L⊙ (VeLLOs)**. A K-S test gives a 94.2% probability that the luminosities are not drawn from a uniform distribution. The distribution does not keep rising below 0.1 L⊙. Only ~2 sources between 2.5 × 10^-3 and 5 × 10^-2 L⊙ are estimated to be missed in the distant clouds.
- **"Starless" cores that host protostars (§6.3)**: 67 of 95 c2d cores (~70%) were starless before Spitzer. Of those, 9 (Groups 1–4) to 17 (all groups) host candidate embedded protostars, so approximately 75–85% of starless cores remain starless. Kirk et al. (2007) found ~95% in a sample of 22 cores.
- **Selection completeness (§4)**: the criteria recover 100% of Enoch et al.'s Class 0 objects with L_IR ≤ 0.5 L⊙. They recover ≥ 60% of Class I objects. 15/37 (40%) of Class I objects are missed because their flux falls from 24 to 70 µm.
- **Non-steady accretion (§6.4)**: the standard-model rate Ṁ ~ 2 × 10^-6 M⊙ yr^-1 onto a 0.08 M⊙, 3 R⊙ object would give L_acc ~ 1.6 L⊙, and VeLLOs are more than 10× fainter than that. For IRAM 04191 the outflow-averaged ⟨Ṁ⟩ ~ 5 × 10^-6 M⊙ yr^-1 would imply L_acc ~ 2 L⊙, against a measured L_int ~ 0.08 L⊙. Constant accretion predicts equal numbers per luminosity bin, but the observed counts rise toward low L. Together these support episodic accretion.
- **BLT diagram (§6.2.1)**: many Class I sources (T_bol ≥ 70 K) sit below every evolutionary track by up to an order of magnitude. The same effect in Class 0 sources may be hidden by ISRF heating adding to L_bol.

## Assumptions

- The L_int proxy assumes an embedded protostar heated by a central source, with F70 dominated by the envelope's reprocessed internal luminosity. The 70 µm flux is taken to be insensitive to geometry, disk and ISRF (§3.2).
- The model grid uses a fixed 3000 K photosphere, a 100 AU disk, a 14,000 AU envelope of 1–10 M⊙, and a Black–Draine ISRF with random extinction and scale factor.
- Sensitivity is scaled from 140 pc by (d/140 pc)². Adopted cloud distances range from 125 to 260 pc; Perseus is taken at 250 ± 50 pc.
- The main selection requires a 24 µm detection (criterion 1), and the 70-µm-only extension recovered very little.

## Limitations / scope

- The observational calibration uses **n = 11** sources, most modelled with the same 1-D setup. The 2-D grid is the real anchor.
- The 3σ 70 µm sensitivity (~38.6 mJy mean) is too shallow for FHSCs. [[enoch-2010]] quotes c2d's 70 µm limit as ~75 mJy (5σ) and needed ~7.5 mJy to reach FHSC-level fluxes.
- Class I sources whose flux falls from 24 to 70 µm are missed (≥ 40% of the low-L_IR Class I sample).
- L_bol and T_bol errors from incomplete SED sampling are roughly 20–60% (App. B).
- Nothing can be said below ~10^-3 L⊙ (§6.1).
- VeLLO membership is defined by luminosity alone, so VeLLOs can mix very young protostars, protostars in quiescent phases and proto-brown dwarfs (discussed later in [[dunham-2014]]).

## Replication evidence

**Partial.** The relation was applied independently to Per-Bolo 58, where it gives L_int = 0.014 L⊙ against 0.012 L⊙ from full radiative-transfer modelling ([[enoch-2010]], §4.3). [[pineda-2011]] applied it to a 70 µm non-detection to get L < 1.6 × 10^-2 L⊙. [[dunham-2014]] (§4.2.2) combines the starless fraction with Schnee et al. (2012) into a revised **18%–38%** of "starless" cores hosting sources, somewhat higher than the 15–25% here. This paper's 15 VeLLOs are the c2d VeLLO sample cited in [[dunham-2014]].

## Why this paper matters

This is the standard reference for turning a 70 µm point-source flux (or upper limit) into an internal luminosity. At 70 µm, emission comes from dust warmed by an internal source and depends little on geometry. At 3–24 µm, emission depends strongly on inclination and cavities. The paper made "no 24 µm source" versus "70 µm source" a working diagnostic. Later FHSC searches ([[enoch-2010]], [[pineda-2011]]) and Herschel searches ([[stutz-2013]]) built on this split. Hi-GAL protostellar/starless clump classification relies on the same logic of a 70 µm detection.

It also quantified the "hidden protostar" correction to starless-core counts, which feeds into statistical lifetimes ([[enoch-2008]], [[evans-2009]]). It gave the statistical form of the luminosity problem (too many low-L_int sources for constant accretion), which later episodic-accretion models (Dunham & Vorobyov 2012, in [[dunham-2014]]) set out to reproduce.

## Quotes

1. > "a tight correlation between the 70 µm flux and internal luminosity of a protostar" — Abstract
2. > "Approximately 75−85% of starless cores remain starless" — §6.3

## Open questions surfaced

- What is the true lower end of the protostellar luminosity function below ~10^-3 L⊙? That needs deeper far-IR data than Spitzer (§6.1).
- What are the Class I sources whose flux falls from 24 to 70 µm: embedded protostars, or heavily extincted Stage II objects behind cores (§4)?
- Do some VeLLOs have higher past luminosities? Chemical tracers of past heating (e.g. Lee 2008) could tell (§6.4).
- How well does the L_int–F70 relation hold outside its calibration range, e.g. with Herschel PACS 70 µm photometry, at larger distances, or for FHSC-like sources that are not 3000 K photospheres?

## Related material in vault

- Extends: —
- Contradicts: —
- Replicates: —
- Concepts introduced/used: [[internal-luminosity]], [[luminosity-problem]], [[episodic-accretion]], [[prestellar-core]], [[class-0-protostar]], [[statistical-lifetime]], [[bolometric-temperature]], [[accretion-luminosity]], [[vello]]
- Cites: [[enoch-2008]]
- Cited by (in this vault): [[evans-2009]], [[enoch-2010]], [[pineda-2011]], [[stutz-2013]], [[dunham-2014]], [[konyves-2015]], [[safron-2015]], [[park-2021]], [[lee-2021]], [[zakri-2022]], [[elia-2022]], [[elia-2017]], [[enoch-2008]], [[furlan-2016]]
