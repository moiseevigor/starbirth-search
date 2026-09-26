---
title: "On the incidence of episodic accretion in Class I YSOs from VVV"
authors: Carlos Contreras Peña, Philip W. Lucas, Zhen Guo, Leigh Smith
year: 2024
venue: Monthly Notices of the Royal Astronomical Society, 528, 1823–1840
url: https://arxiv.org/abs/2401.14472
doi: 10.1093/mnras/stad3780
language: en
domain: astrophysics
status: draft
methodology_type: empirical
citation_count: 7
citation_count_date: 2026-09-26
key_concepts: ["[[accretion-outburst]]", "[[episodic-accretion]]", "[[luminosity-problem]]", "[[outburst-recurrence-time]]"]
extends: ["[[contreras-pena-2019]]"]
contradicts: []
replicates: []
cites: ["[[contreras-pena-2019]]", "[[fischer-2019]]", "[[park-2021]]", "[[zakri-2022]]", "[[evans-2009]]", "[[dunham-2014]]", "[[kuhn-2021]]", "[[lucas-2024]]"]
cited_by: ["[[lucas-2024]]"]
quality_notes: "Citation count from Semantic Scholar (DOI lookup), likely an undercount for a 2024 MNRAS paper. The FUor recurrence time rests on k = 43 long-term events, a far larger k than earlier Class I estimates (k = 2-3), but the Class I parent sample comes from colour selection and carries ~11% evolved-star contamination. Lucas et al. 2024 is cited as 'Lucas et al., submitted'."
author: moiseevigor
tags:
  - agent/research
  - user/moiseevigor
  - domain/astrophysics
  - topic/accretion-outbursts
  - topic/protostellar-variability
  - topic/time-domain-surveys
  - topic/vvv-survey
  - topic/yso-catalogs
  - topic/spitzer-surveys
  - topic/wise-neowise
  - topic/outburst-recurrence-rate
  - topic/survey-completeness-reliability
  - topic/survey-artefacts-and-contamination
  - paper
  - status/draft
---

# On the incidence of episodic accretion in Class I YSOs from VVV

## Abstract

Episodic accretion is one of the competing models to explain the observed luminosity spread in young stellar clusters. These short-lived high accretion events could also have a strong impact on planet formation. Observations of high-amplitude variability in young stellar objects (YSOs) due to large changes in the accretion rate provide direct observational evidence for episodic accretion. However there are still uncertainties in the frequency of these events and if episodic accretion is universal among YSOs. To determine the frequency of outbursts in Class I YSOs, we built a large and robust sample of objects at this evolutionary stage, and searched for high-amplitude near-infrared (ΔK_S > 2 mag) variability in the VIRAC2 database of the Vista Variables in the Via Lactea (VVV) survey. By complementing with near-IR (2MASS and DENIS) and mid-IR (WISE/Neo-WISE) data, we find that from ∼ 7000 Class I YSOs, 97 objects can be classified as eruptive variable YSOs. The duration of the outbursts vary from a few months to longer than 9 years, and cover a similar range of amplitudes. Values of ΔK_S > 5 mag, however, are only observed in outbursts with duration longer than 9 years. When considering different effects of completeness and contamination we estimate that the incidence of episodic accretion in Class I YSOs is between 2% and 3%. Finally, we determine a recurrence timescale of long-term outbursts (a.k.a FUors) of τ = 1.75 (+1.12/−0.87) kyr. The latter value agrees with previous estimates and is in line with the expectations of higher frequency of FUor outbursts during younger stages of evolution.

## TL;DR

The authors colour-select 7205 Class I YSOs (spectral index α₂₄ > −0.3) from SPICY, Robitaille et al. 2008 and Marton et al. 2016. They search the 5661 with VIRAC2 near-IR light curves (2010–2019) for ΔK_s > 2 mag and classify 97 as eruptive. That gives an incidence of 1.7% raw and 2.4–2.8% after completeness and contamination corrections. The FUor-type (> 9 yr) recurrence time is τ = 1.75 (+1.12/−0.87) kyr per Class I YSO. This is the largest-k Class I rate estimate to date, and it slots between the Class 0 (~0.4–1 kyr) and Class II (≳10 kyr) values.

## Problem

How often do Class I YSOs undergo accretion outbursts, and what is the recurrence interval of long (FUor-type) events? Earlier Class I intervals came from small samples or short baselines (k = 1–3 events), so their confidence intervals span more than a dex (§1, §6.2).

## Approach

- **Parent sample (§2.2–2.3).** 132,578 YSO candidates in the VVV area are drawn from SPICY (Kuhn et al. 2021), Robitaille et al. (2008) and Marton et al. (2016). Class I selection has three steps: (i) detection at 22/24 µm, (ii) Gutermuth et al. 2009 or Koenig & Leisawitz 2014 colour criteria, which reject shock knots and PAH contamination, and (iii) α₂₄ > −0.3. This leaves 5541 + 663 + 1001 = **7205** Class I candidates.
- **Variability search (§3).** Sources are cross-matched to VIRAC2 (VVV PSF photometry from DoPHOT, 2010–2019, ~700 million sources) within 1″, giving 5661 matches. Amplitude is ΔK_s,p96 (96th minus 4th percentile), cut at **> 2 mag**, which yields 304 candidates. These are visually classified using 2MASS, DENIS, UKIDSS, Spitzer and WISE/NEOWISE light curves and 3′×3′ cutouts. The classes are Eruptive, Dipper, Fader, STV, Periodic and Unclassified (§3.1). Periodic sinusoids are mostly AGB contaminants.
- **Duration classes (§4.1).** Outbursts are sorted by t_out: short (≤ 1 yr), intermediate (1–9 yr) and long (> 9 yr).
- **Selection-effect modelling (§5.1, App. A).** Synthetic light curves span Δt_out = 30–4200 d and Δt_int = 90–12000 d, for ΔK = 1.5–3 and 3–5 mag, sampled at the VVV cadence.
- **Recurrence time (§6.1).** This follows the Bayesian Poisson method of [[contreras-pena-2019]], with prior p(τ) ∝ 1/τ and most probable τ = N t / (k + 1).

## Key result

- **Yield (§5.3).** Of the 5661 Class I YSOs with VIRAC2 counterparts, 304 (5.37%) show ΔK > 2 mag over the 9 yr of VVV/VVVX. Of those, 97 (∼1.71% of Class I YSOs) are classified as eruptive, and 70 of the 97 are new (§7).
- **By duration (§4.1, §5.3).** "we classify 43 YSOs as long-term, 37 as intermediate and 17 as short-term outbursts". As fractions of Class I YSOs, these are "0.3%, 0.65% and 0.76% ... short-term, intermediate and longterm".
- **Amplitudes (§4.1).** All duration classes span "2 < Δ < 4.8 mag". "The largest amplitudes (Δ > 4.8 mag), however, are associated exclusively with long-duration outbursts." Of the 16 objects with spectra, only 2 show FUor-like absorption spectra, both long-duration. Emission-line (EX Lupi-like) spectra dominate at all durations.
- **Completeness (§5.1).** The synthetic tests show "we might be missing as much as 75% of short-term outbursts and up to 30% of intermediate type outbursts". The correction factors are 4 (short) and 1.4 (intermediate). Long-term outbursts get no correction.
- **Contamination (§5.2).** 635 of 5661 sources could be classified as evolved stars under the Robitaille et al. 2008 criteria, a contamination of "∼ 11.2%". This gives N = 5026. If every source below the Wang & Chen (2019) extinction line in ΔW2/ΔK_s is extinction-driven, then 20 of 73 eruptive YSOs with valid WISE data would be contaminants. However, 9/11 spectroscopically confirmed eruptors also fall below the McClure (2009) line (§4.1).
- **Incidence (§5.3, §7).** "the incidence of episodic accretion among Class I YSOs raises from 1.71% to between 2.36 and 2.78%" once the α definition is varied. If only α > 0 counts as Class I, the VIRAC2 sample drops from 5661 to 3807; with α > 0.3 it drops to 2181 (§5.1).
- **FUor recurrence (§6.1).** k = 43 long-term events. t is "the mean between the 9 years covered by VVV and 19 years once we include 2MASS/DENIS" (so 14 yr). N = 5026 after contamination. The most probable τ "consistently moves between ≈ 1000 and 3000 yr" as t, N and α are varied. The final value is **τ = 1.75 (+1.12/−0.87) kyr**, with lower and upper limits of 884 and 2869 yr.
- **Luminosity (§4.2, §7).** In-outburst L_IR (integrated over 2–24 µm, not extinction-corrected) is "similar for all of the classes". Short outbursts can reach high luminosities.
- **Comparison (§6.2).** Earlier estimates include Fischer et al. 2019: 1000 yr (90% CI 690–40300 yr). Park et al. 2021: 683 yr (90% CI 356–1579 yr). Zakri et al. 2022 (Class 0): 438 yr (95% CI 161–1884 yr). Contreras Peña et al. 2019 (Class I contaminants): 13 (+15/−6) kyr. The ordering across Class 0 → I → II "seems to point to an increase in the frequency of these events for younger stages of evolution" (§6.3).

## Assumptions

- The Class I stage is defined by α₂₄ (3.4–22 µm or 4.5–24 µm colours) ≥ −0.3, which includes flat-spectrum sources.
- Long-term (> 9 yr) outbursts are treated as non-repeating on the survey timescale, so the Poisson rate method applies to FUors only (§6).
- The Poisson estimate assumes every Class I YSO takes part in FUor outbursts, a caveat the authors state explicitly in §6.3.
- Distances come from star-forming regions within 5′. Sources without one are assigned 3.5 kpc (Table 2 footnote).
- Long-term outbursts are assumed intrinsically high-amplitude, so no completeness correction is applied to them (§5.1).

## Limitations / scope

- **Saturation bias (§6.3).** VIRAC2 saturates at K_s ≈ 11 mag. Sources with quiescent K_s ≲ 13 mag are less likely to be recovered in outburst. A Monte Carlo test (§6.3, 1000 realisations) reproduces the observed deficit.
- **Extinction versus accretion.** The authors "cannot discard" some extinction-driven contaminants in the eruptive list, and the ΔW2/ΔK_s test is weakened because WISE and VVV are not fully contemporaneous (§4.1, §5.2).
- **Missed events.** Slow faders returning to quiescence with ΔK_s < 2 mag during the VVV window are missed (§6.3).
- **Malmquist bias.** This was checked with faintest-epoch K_s distributions and not detected at the faint end (§6.3, Fig. 10).
- **Nebulosity and confusion.** Class I selection relies on Gutermuth/Koenig colour cuts that reject PAH-contaminated apertures and shock knots (§2.3). Photometric blending in crowded bulge fields is handled by the VIRAC2 recalibration (§3). There is no dedicated blending analysis of the eruptive sample.
- **Spectra.** Only 16 of the 97 have spectroscopy, so FUor versus EXor classification is by duration only.
- **Scope.** Only the original VVV area is analysed; the VVVX extension areas are not.

## Replication evidence

Partial. The 2–3% incidence and ~kyr FUor interval are consistent with the mid-IR Class 0/I rates of [[fischer-2019]] and [[park-2021]] (~0.7–1 kyr), within their wide intervals. The high-amplitude end is examined independently in the companion paper [[lucas-2024]], which uses a ΔK_s ≥ 4 cut over the same VIRAC2 data. No independent-survey replication of τ_ClassI = 1.75 kyr exists yet.

## Why this paper matters

This is the first Class I FUor recurrence estimate built on dozens of events (k = 43) rather than 1–3. It makes Class I the best-constrained stage in the outburst-frequency sequence. The result supports the picture in which outburst frequency declines with evolutionary stage: Class 0 ≲ 1 kyr ([[zakri-2022]]), Class I ≈ 1–3 kyr (this work), Class II ≳ 10 kyr ([[contreras-pena-2019]]).

The paper also documents the systematics that any population rate must carry. These are colour-selection contamination (~11% evolved stars), extinction-driven look-alikes, a ~75% loss of isolated short outbursts at the VVV cadence, and a saturation-induced deficit of intrinsically bright outbursters. It argues that EX Lupi-type and intermediate events reach FUor-like luminosities. That bears on the [[luminosity-problem]]: the total 2.8% incidence is compared with the ~5% high-luminosity tail of Class I sources in Enoch et al. (2009).

## Quotes

1. > "incidence of episodic accretion in Class I YSOs is between 2% and 3%" — Abstract
2. > "we might be missing as much as 75% of short-term outbursts" — §5.1

## Open questions surfaced

- Do all Class I YSOs undergo FUor outbursts, or only a sub-population with massive compact discs (§6.3, citing Cieza et al. 2018 and Kóspál et al. 2021)? The Poisson τ is only meaningful under the "universal" assumption.
- How many Class I outbursts are hidden above the VIRAC2 saturation limit (quiescent K_s ≲ 13)? Saturation-corrected photometry could raise k.
- Would a lower cut (ΔK_s 1–2 mag) change the short/intermediate balance? Guo et al. 2021 have 25/55 spectroscopic eruptors at ΔK_s < 2 mag.
- Could simultaneous near- and mid-IR monitoring (VVVX with NEOWISE) resolve the extinction/accretion degeneracy in the ΔW2/ΔK_s diagnostic?

## Related material in vault

- Extends: [[contreras-pena-2019]]
- Contradicts: —
- Replicates: —
- Concepts introduced/used: [[accretion-outburst]], [[episodic-accretion]], [[luminosity-problem]], [[outburst-recurrence-time]]
- Cites: [[contreras-pena-2019]], [[fischer-2019]], [[park-2021]], [[zakri-2022]], [[evans-2009]], [[dunham-2014]], [[kuhn-2021]], [[lucas-2024]]
- Cited by (in this vault): [[lucas-2024]]
