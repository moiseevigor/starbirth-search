---
title: "Constraining the Rate of Protostellar Accretion Outbursts in the Orion Molecular Clouds"
authors: William J. Fischer, Emily Safron, S. Thomas Megeath
year: 2019
venue: The Astrophysical Journal, 872, 183 (doi:10.3847/1538-4357/ab01dc)
url: https://arxiv.org/abs/1901.08062
language: en
domain: astrophysics
status: draft
methodology_type: empirical
citation_count: 44
citation_count_date: 2026-09-26
key_concepts: ["[[accretion-outburst]]", "[[episodic-accretion]]", "[[luminosity-problem]]", "[[class-0-protostar]]", "[[confusion-limit]]", "[[accretion-luminosity]]", "[[outburst-recurrence-time]]"]
extends: ["[[safron-2015]]"]
contradicts: []
replicates: []
cites: ["[[safron-2015]]", "[[furlan-2016]]", "[[evans-2009]]", "[[stutz-2013]]"]
cited_by: ["[[contreras-pena-2019]]", "[[park-2021]]", "[[zakri-2022]]", "[[contreras-pena-2024]]", "[[lee-2021]]", "[[lu-2024]]"]
quality_notes: "Rate rests on only 2 events (n_b = 2), so the 90% interval spans ~1.8 dex (690–40,300 yr). Zakri et al. 2022 show two further Class 0 bursts (HOPS 12, 124) were missed here because of WISE blending, so this is a lower bound on the burst rate for the sample."
author: moiseevigor
tags:
  - agent/research
  - user/moiseevigor
  - domain/astrophysics
  - topic/accretion-outbursts
  - topic/protostellar-variability
  - topic/time-domain-surveys
  - topic/spitzer-surveys
  - topic/wise-neowise
  - topic/class-0-protostars
  - topic/outburst-recurrence-rate
  - topic/herschel-protostar-surveys
  - topic/accretion-luminosity
  - paper
  - status/draft
---

# Constraining the Rate of Protostellar Accretion Outbursts in the Orion Molecular Clouds

## Abstract

Outbursts due to dramatic increases in the mass accretion rate are the most extreme type of variability in young stellar objects. We searched for outbursts among 319 protostars in the Orion molecular clouds by comparing 3.6, 4.5, and 24 µm photometry from the Spitzer Space Telescope to 3.4, 4.6, and 22 µm photometry from the Wide-field Infrared Survey Explorer (WISE) obtained ∼ 6.5 yr apart. Sources that brightened by more than two standard deviations above the mean variability at all three wavelengths were marked as burst candidates, and they were inspected visually to check for false positives due primarily to the reduced angular resolution of WISE compared to Spitzer. We recovered the known burst V2775 Ori (HOPS 223) as well as a previously unknown burst, HOPS 383, which we announced in an earlier paper. No other outbursts were found. With observations over 6.5 yr, we estimate an interval of about 1000 yr between bursts with a 90% confidence interval of 690 to 40,300 yr. The most likely burst interval is shorter than those found in studies of optically revealed young stellar objects, suggesting that outbursts are more frequent in protostars than in pre-main-sequence stars that lack substantial envelopes.

## TL;DR

Two-epoch (Spitzer 2004–05 vs AllWISE 2010, Δt ≈ 6.5 yr) search of the 319 HOPS protostars in Orion; a burst = brightening > mean + 2σ of the Spitzer−WISE magnitude difference in all three bands (1.01 / 1.54 / 1.25 mag at 3.6 / 4.5 / 24 µm) plus visual vetting. Only HOPS 223 (V2775 Ori) and HOPS 383 pass → most likely interval ≈ 1040 yr per protostar, 90% CI 690–40,300 yr. This is the canonical "~1000 yr" protostellar burst interval.

## Problem

How often does a given protostar undergo a large accretion outburst? Previous systematic estimates (Scholz et al. 2013: 5000–50,000 yr, mostly Class II) mixed evolutionary classes and had poorly constrained upper bounds (§1).

## Approach

- **Sample:** 319 protostars (Class 0, I, flat-spectrum) from Furlan et al. (2016) HOPS SED catalogue ([[furlan-2016]]) (§2).
- **Epochs:** Spitzer IRAC 3.6/4.5 µm and MIPS 24 µm (2004–2005; 5σ limits ~17 mag IRAC, ~9 mag MIPS) vs AllWISE W1/W2/W4 (2010 Mar; W1/W2 again 2010 Sep; 5σ 16.9 / 15.9 / 8.0 mag). PSF FWHM ~2″ (IRAC), ~6″ (MIPS, W1/W2), ~12″ (W4) (§2).
- **Matching:** 227 auto-matched within 1″; 32 no WISE source within 10″; 60 intermediate inspected by eye, 44 kept → 271/319 with WISE counterparts (§2).
- **Baseline scatter (Table 2):** mean Spitzer−WISE difference −0.283 / 0.356 / 0.013 mag; std. dev. 0.646 / 0.590 / 0.620 mag at 3.6 / 4.5 / 24 µm (positive = brighter in WISE).
- **Detection threshold:** brightening > mean + 2σ in all three bands = 1.01 / 1.54 / 1.25 mag; or threshold met in 1–2 bands with non-detection → detection in the other(s). These correspond to luminosity increases of ~2.5–4× (§3).
- **Physical justification:** L_acc = ηGM*Ṁ/R*; total L ratio is a lower limit on Ṁ ratio; SED shape changes slowly with L (peak λ ∝ L^−1/12, Kenyon et al. 1993), so all three bands should brighten together (§3).
- **Rate statistics:** r_b = n_b/(N_p Δt); Poisson per star, binomial across stars: P(n_b | I_b, N_p, Δt) = C(N_p, n_b) (1 − e^(−Δt/I_b))^(n_b) (e^(−Δt/I_b))^(N_p − n_b), uniform prior → posterior on the burst interval I_b (Eq. 2, §6).

## Key result

- **Outbursts found:** only HOPS 223 and HOPS 383 (§5, Table 3).

| HOPS | Δ3.6 µm | Δ4.5 µm | Δ24 µm |
|---|---|---|---|
| 223 (V2775 Ori, flat-spectrum) | 1.69 | 2.23 | 1.77 mag (flux ×4.7, ×7.9, ×5.3; 2.8–3.2σ) |
| 383 (Class 0) | >2.9 | 2.40 | 3.96 mag (≥4.9σ, 3.5σ, 6.4σ) |

- **Luminosity amplitudes:** HOPS 223 rose 4.5 → ~51 L⊙ (×12) between 2005 Apr 2 and 2007 Mar 12; Ṁ ~10⁻⁶ → 10⁻⁵ M⊙ yr⁻¹; HOPS 383 0.2 → 7.5 L⊙ (×35) (§5.1–5.2, §7.2).
- **Rate:** r_b = 9.65 × 10⁻⁴ yr⁻¹, I_b = 1036.75 yr; posterior peaks at 27.2% for 1033.50 yr, adopted 1040 yr; "The 90% confidence interval ... is from 690 to 40,300 yr" (§6).
- **Denominator sensitivity:** using N_p = 271 (only WISE-matched) → 880 yr, 90% CI 586–34,200 yr (~15% shorter) (§6).
- **Implication:** with a 5 × 10⁵ yr protostellar lifetime ([[evans-2009]]), "several hundred outbursts" per protostar (§6).
- **Evolutionary comparison:** shorter than Class II estimates (Scholz et al. 2013: 5000–50,000 yr; Carpenter et al. 2001 lower limit 5400 yr) — "outbursts are frequent in the protostellar stage, occuring once every ∼10³ yr" vs ~10⁴ yr in disk-dominated stage (§7.1, §8).
- **Mass fraction toy model:** M_b/M = A f_b / [(A − 1) f_b + 1], f_b = d_b/I_b. HOPS 223-like (×15, 20–40 yr → 0.02 < f_b < 0.04) → 23–38% of mass in bursts; HOPS 383-like (×40) → > 50% for f_b > 0.024 (§7.2).
- **Duration:** not constrained; both bursts still elevated ~a decade after onset (SOFIA) → "typically longer than a decade" (§7.2, §8).

## How outbursts were separated from other variability

- Thresholds set at 2σ of the population scatter to exceed typical 0.1–0.6 mag rotational / inner-disk variability and Spitzer/WISE bandpass differences; explicitly "should not be considered the statistical significance of the bursts" (§3).
- Requiring simultaneous brightening at 3–5 µm **and** 24 µm (colour-coherent, luminosity-driven).
- Visual inspection: all single- and two-band candidates (e.g. HOPS 370: +3.9/+2.7 mag at 3.6/4.5 but −0.1 at 24 µm; HOPS 28; HOPS 335) rejected as blends/nebulosity in the larger WISE PSF (§4.1) — the [[confusion-limit]] of WISE dominates false positives.

## Assumptions

- All protostars share one burst rate (single mechanism); Poisson-distributed bursts (§6).
- Δt = 6.5 yr for all (311/319 have 6.53–6.59 yr; 8 in L1622 have 4.90 yr) (§6).
- Missing WISE counterparts count as "no burst" (§6).
- Spitzer and WISE bandpasses directly comparable (weak colour dependence) (§2).

## Limitations / scope

- n_b = 2 → very broad CI; authors (citing Hillenbrand & Findeisen 2015) say an order-of-magnitude larger sample or baseline is needed (§7.3).
- Two-epoch design misses bursts that rose and decayed within the gap, and bursts hidden by blending — [[zakri-2022]] later found HOPS 12 and HOPS 124 missed for exactly that reason.
- Pre-existing bursts (V1647 Ori, Reipurth 50, V883 Ori) excluded from the statistic (§5.3).

## Replication evidence

Partial / yes. [[park-2021]] (NEOWISE, 735–1059 protostars in 20 regions, 6.5 yr) gets τ ≈ 478–2295 yr depending on k, "very similar to the work of Fischer et al. (2019)". [[zakri-2022]] (Spitzer 2004–2017, 13 yr) finds 879 yr for all Orion protostars (95% CI 400–2515 yr) and 438 yr for Class 0 alone. [[contreras-pena-2019]] finds Class II outbursts ~10⁵ yr, consistent with the protostar/Class II contrast.

## Why this paper matters

It is the first survey-based burst rate restricted to protostars, and its ~1000 yr figure became the reference value for protostellar episodic accretion. It also documents the key systematic of any Spitzer-vs-WISE comparison: the larger WISE beam converts nebulosity and neighbours into false brightenings, making visual vetting mandatory.

## Quotes

1. > "Visual inspection is a crucial step to identify false outbursts" — §4.1
2. > "the two-sigma threshold should not be considered the statistical significance" — §3

## Open questions surfaced

- Burst duration d_b (both events still ongoing in 2019) — the key missing input for the mass fraction.
- Does the rate depend on class within protostars (Class 0 vs I)? — addressed by [[zakri-2022]].
- Larger samples (to ~2 kpc) via VVV / UKIDSS / WFIRST and far-IR/sub-mm monitoring to shrink the CI (§7.3).

## Related material in vault

- Extends: [[safron-2015]]
- Contradicts: —
- Replicates: —
- Concepts introduced/used: [[accretion-outburst]], [[episodic-accretion]], [[luminosity-problem]], [[class-0-protostar]], [[confusion-limit]], [[accretion-luminosity]], [[outburst-recurrence-time]]
- Cites: [[safron-2015]], [[furlan-2016]] (sample + SED fits), [[evans-2009]] (lifetime 5×10⁵ yr), [[stutz-2013]] (HOPS)
- Cited by (in this vault): [[contreras-pena-2019]], [[park-2021]], [[zakri-2022]], [[contreras-pena-2024]], [[lee-2021]], [[lu-2024]]
