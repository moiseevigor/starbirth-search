---
title: "Determining the recurrence timescale of long-lasting YSO outbursts"
authors: Carlos Contreras Peña, Tim Naylor, Sam Morrell
year: 2019
venue: Monthly Notices of the Royal Astronomical Society, 486, 4590 (doi:10.1093/mnras/stz1019)
url: https://arxiv.org/abs/1904.04068
language: en
domain: astrophysics
status: draft
methodology_type: empirical
citation_count: 35
citation_count_date: 2026-09-26
key_concepts: ["[[accretion-outburst]]", "[[episodic-accretion]]", "[[outburst-recurrence-time]]"]
extends: []
contradicts: []
replicates: []
cites: ["[[fischer-2019]]", "[[evans-2009]]", "[[dunham-2014]]"]
cited_by: ["[[park-2021]]", "[[zakri-2022]]", "[[contreras-pena-2024]]", "[[lee-2021]]"]
quality_notes: "Class II rate rests on k = 6 events (3 spectroscopically confirmed, 2 literature-supported, 1 unconfirmed); SSS-vs-Gaia uses only ~5 epochs over ~55 yr, so short outbursts and dips can masquerade as long outbursts — authors rely on literature light curves to veto. Its Bayesian tau formalism (Eqs. 8-9) is reused by Park et al. 2021 and cited by Zakri et al. 2022."
author: moiseevigor
tags:
  - agent/research
  - user/moiseevigor
  - domain/astrophysics
  - topic/accretion-outbursts
  - topic/time-domain-surveys
  - topic/protostellar-variability
  - topic/yso-catalogs
  - topic/outburst-recurrence-rate
  - paper
  - status/draft
---

# Determining the recurrence timescale of long-lasting YSO outbursts

## Abstract

We have determined the rate of large accretion events in class I and II young stellar objects (YSOs) by comparing the all-sky digitised photographic plate surveys provided by SuperCOSMOS with the latest data release from Gaia (DR2). The long mean baseline of 55 years along with a large sample of class II YSOs (≃15,000) allows us to study approximately 1 million YSO-years. We find 139 objects with ∆R ≥ 1 mag, most of which are found at amplitudes between 1 and 3 mag. The majority of YSOs in this group show irregular variability or long-lasting fading events, which is best explained as hot spots due to accretion or by variable extinction. There is a tail of YSOs at ∆R ≥ 3 mag and they seem to represent a different population. Surprisingly many objects in this group show high-amplitude irregular variability over timescales shorter than 10 years, in contrast with the view that high-amplitude objects always have long outbursts. However, we find 6 objects that are consistent with undergoing large, long lasting accretion events, 3 of them previously unknown. This yields an outburst recurrence timescale of 112 kyr, with a 68% confidence interval [74 to 180] kyr. This represents the first robust determination of the outburst rate in class II YSOs and shows that YSOs in their planet-forming stage do in fact undergo large accretion events, and with timescales of ≃100,000 years. In addition, we find that outbursts in the class II stage are ≃10 times less frequent than during the class I stage.

## TL;DR

Compares SuperCOSMOS photographic-plate magnitudes (B, R1, R2, I; 1950s–1990s) with Gaia DR2 G (epoch 2015.5) for ~14,000 Class II YSOs over a mean 55.6 yr baseline (782,959 YSO-yr). 139 variables with ΔR ≥ 1 mag; only 6 Class II long-lasting (FUor-like) outbursts survive vetting → τ = 112 (+68/−38) kyr (1/τ prior, 68% CI 74–180 kyr). Class I rates derived as a by-product are ~3–13 kyr, i.e. ~10× more frequent — the counterpoint to the ~1 kyr protostellar rates of [[fischer-2019]] / [[park-2021]].

## Problem

Do long-lasting, high-amplitude accretion outbursts occur during the planet-forming Class II phase at all, and how often per star? Previous estimates (Scholz et al. 2013) did not separate classes and had only two-epoch, ~5 yr baselines (§1, §6.1.1).

## Approach

- **Sample (§2.2):** 77,873 SIMBAD YSO-type objects → Class II selected via Marton et al. (2016) + Koenig & Leisawitz (2014) WISE colours (3253), Megeath et al. (2012) α_IRAC (−1.6 < α < 0.3; 1671 + 605 + 86), Gutermuth et al. (2009) (1060), c2d α ([[evans-2009]]; 994), AllWISE colours (4883), 2MASS CTTS locus (1536), MYStIX (1400) → 15,404 Class II. 1318 with estimated G > 22.5 mag removed → N = 14,077.
- **Epochs (§2.1, §6):** SSS plates (POSS-I/II, SERC, AAO, ESO; depth R ≃ 20) vs Gaia DR2; per-star baseline from oldest plate to 2015.5; total 782,959 yr, mean 55.6 yr.
- **Detection statistic (§3.1):** for each YSO, local calibration of G − M_sss from stars within |G − G_YSO| ≤ 0.2 in a 2° × 2° box; Δ_YSO = (x − u)ᵀ Σ⁻¹ (x − u) − χ²(5σ)_(k=4), a Mahalanobis distance of the 4 colours (G − B, G − R1, G − R2, G − I) relative to non-variables minus the 5σ (99.99996%) χ² value for 4 d.o.f. Candidate if Δ_YSO > 0 (Eq. 2); final cuts Δ_YSO ≥ 70 with a univariate > 5σ band, or Δ_YSO ≥ 100 (§3.2).
- **Plate-artefact veto (§3.3):** N_sss/N_Gaia < 0.45 within 3′ × 3′ → unlikely variable (501 of 1576 removed).
- **Visual/literature vetting (§3.4):** 1075 candidates inspected with SSA cutouts, Pan-STARRS, SkyMapper, VizieR photometry → 139 true high-amplitude variables.
- **Rate statistics (§6):** Poisson P(k|R) = (Rt)^k e^(−Rt)/k!, τ = 1/(RN); with a flat prior p(τ|k) = (Nt)^(k−1) e^(−Nt/τ) / [(k−2)! τ^k], mode τ = Nt/k; with a 1/τ prior p(τ|k) = (Nt)^k e^(−Nt/τ) / [(k−1)! τ^(k+1)], mode τ = Nt/(k+1) (Eqs. 6–9). 68% CI = highest-density interval.

## Key result

- **Amplitude distribution (§3.4, §4):** 139 variables with ΔR ≥ 1 mag (66 new); sample incomplete below 2 mag, none detected below 1 mag; df/dA agrees with Cep OB3b i-band reference at 2 mag and plateaus at ΔR > 3.5 mag with a bump near ~4–4.5 mag — a possibly distinct population.
- **Mechanism by amplitude (§5.1–5.2):** 101 of 108 objects with 1–3 mag show fading events or irregular variability (hot spots or extinction); of 28 with ΔR ≥ 3 mag, 7 are long-lasting outbursts, others fading or irregular (likely short accretion events).
- **Outburst sample (§5.3–5.4, Table 3):** 9 long-lasting outbursts (6 known: V1057 Cyg, HBC 722, V350 Cep, V733 Cep, V960 Mon, V582 Aur; 3 new: 2MASS J02335340+6156501, 2MASS J08410676−4052174, WRAY 15-488). 3 (V1057 Cyg, V350 Cep, V960 Mon) likely Class I/envelope-bearing → k = 6 Class II.
- **Class II recurrence (§6):** flat prior τ = 131 (+91/−48) kyr; preferred 1/τ prior "τ=112+68 −38 kyr (68 percent confidence)", i.e. [74, 180] kyr.
- **Systematics (§7.4):** dropping unconfirmed V9 → 130 kyr; removing ~3.5% non-YSO and 7% Class I contamination → 100 kyr (117 kyr without V9); all within the 68% CI.
- **Class I rates (§6.1.1, §7.4; 1/τ prior, 68%):** Scholz et al. (2013) sample A: 3.0 (+12.7/−1.9) kyr; sample B: 6.0 (+25.3/−3.9) kyr; from the 3 Class I contaminants among 1043 Class I: 13 (+15/−6) kyr → outbursts ~10× more frequent in Class I.
- **Theory comparison (§6.1.2):** Bae et al. (2014) GI+MRI rates via Hillenbrand & Findeisen (2015): 12.5 kyr (Class I), 333 kyr (Class II); the Class II theoretical value "is formally rejected at a 95.3% confidence level".
- **Duration criterion:** outbursts shorter than ~10 yr (EXor/MNor-like, e.g. ASASSN-13db) are excluded by design (§5.2, §9).

## How outbursts were separated from other variability

- Physical model for counting: quiescence of centuries+, rise > 4 mag within ≲ a decade, then bright for decades (§6).
- Amplitude: cool spots (~0.1 mag) excluded by construction; 1–3 mag mostly hot-spot/extinction.
- Light-curve shape from all available literature photometry: repetitive bright/faint (irregular) or long fades → not outbursts. Case studies: V20 (apparent 3.2 mag outburst revealed by PTF as irregular short-term variability) and V3/V1219 Cyg (apparent 4.7 mag outburst actually repetitive fading events) (§5.2).
- Spectroscopic confirmation where available (V2, V10, V36; V4 in prep.; V51 literature); SED spectral index α and envelope evidence to separate Class II from Class I (§5.4, §7.1).

## Assumptions

- All Class II YSOs share one outburst rate; single mechanism (caveat §8 notes multiple mechanisms would invalidate per-star extrapolation).
- Objects not in Gaia and faint/undetected in SSS are non-variable; stars with estimated G ≤ 22.5 and ΔR ≥ 2 would be detected (§4).
- 1/τ prior (equal probability per decade of τ) preferred (§6).

## Limitations / scope

- Optical/Class II only — not directly a protostellar rate; embedded Class 0/I sources are invisible to plates and Gaia.
- Five sparse epochs; classification of many variables marked uncertain ("?") (§3.4).
- Selection partly by variability for FU* / Or* SIMBAD classes (§7.5).
- Abstract says "approximately 1 million YSO-years" while §6/§9 give 782,959 yr (≃ 800,000).

## Replication evidence

Partial: [[park-2021]] finds no FUor outbursts among 4477 Class II disks in 6.5 yr of NEOWISE, "consistent with" 112 kyr. Class I ~10× ratio agrees in sense with [[fischer-2019]] and [[zakri-2022]] protostellar rates of ~0.4–1 kyr (different samples/classes).

## Why this paper matters

First observational Class II outburst recurrence timescale, and the statistical formalism (Poisson + Bayes with flat vs 1/τ priors) that later protostellar rate papers adopt. Together with the Spitzer/WISE protostellar rates it establishes an evolutionary gradient: ~0.4–1 kyr for mid-IR-selected Orion/Gould Belt protostars ([[fischer-2019]], [[zakri-2022]], [[park-2021]]), ~3–13 kyr for Class I here (different samples, near-IR/optical selection, 1–3 events — not a like-for-like comparison with the protostellar values), and ~10⁵ yr for Class II.

## Quotes

1. > "outbursts in the class II stage are ≃10 times less frequent" — Abstract
2. > "in contrast with the view that high-amplitude objects always have long outbursts" — Abstract

## Open questions surfaced

- Nature of the ΔR > 3.5 mag plateau population with irregular, < 10 yr high-amplitude variability.
- Spectroscopic confirmation of 2MASS J08410676−4052174 (V9).
- Whether planet-induced thermal instability or binary perturbation drives Class II outbursts (GI+MRI disfavoured by the rate) (§8).
- Large hidden faint-YSO population needed to reconcile Gaia-alert discovery rates (Gaia17bpi implies ~40,000 YSOs monitored) (§6.1.4).

## Related material in vault

- Extends: —
- Contradicts: —
- Replicates: —
- Concepts introduced/used: [[accretion-outburst]], [[episodic-accretion]], [[outburst-recurrence-time]]
- Cites: [[fischer-2019]] (protostellar rate comparison), [[evans-2009]] (c2d classification), [[dunham-2014]] (class definitions)
- Cited by (in this vault): [[park-2021]], [[zakri-2022]], [[contreras-pena-2024]], [[lee-2021]]
