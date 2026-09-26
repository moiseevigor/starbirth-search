---
title: Outburst recurrence time
author: moiseevigor
language: en
domain: astrophysics
status: draft
tags:
  - agent/research
  - user/moiseevigor
  - domain/astrophysics
  - topic/outburst-recurrence-rate
  - topic/accretion-outbursts
  - topic/time-domain-surveys
  - concept
  - status/draft
introduced_in: ["[[contreras-pena-2019]]", "[[fischer-2019]]"]
related_concepts: ["[[accretion-outburst]]", "[[episodic-accretion]]", "[[statistical-lifetime]]"]
appears_in: ["[[contreras-pena-2019]]", "[[contreras-pena-2024]]", "[[fischer-2019]]", "[[park-2021]]", "[[zakri-2022]]"]
---

# Outburst recurrence time

> **Concept hub.** This note exists as a shared anchor — multiple paper summaries link here via their `key_concepts` frontmatter, so reading this gives the cross-paper view of one idea. Keep it short and authoritative. Long discussions go in paper notes, not here.

## Definition

The mean interval τ between [[accretion-outburst]]s of a single source, estimated from a survey that sees k bursts among N sources over a baseline t, assuming bursts are a Poisson process with the same rate for every source.

[[contreras-pena-2019]] (§6, Eqs. 6–9): P(k|R) = (Rt)^k e^(−Rt)/k!, with τ = 1/(RN). With a flat prior the posterior mode is τ = Nt/k. With the preferred 1/τ prior (equal probability per decade),

p(τ|k) = (Nt)^k e^(−Nt/τ) / [(k−1)! τ^(k+1)], mode **τ = N t / (k + 1)**.

[[fischer-2019]] (Eq. 2) uses the equivalent binomial form across stars, P(n_b | I_b, N_p, Δt) = C(N_p, n_b)(1 − e^(−Δt/I_b))^(n_b)(e^(−Δt/I_b))^(N_p − n_b), with a uniform prior on the interval I_b. [[zakri-2022]] uses the same with a logarithmic prior.

## Why it matters

τ turns a small number of detected bursts into a rate that can be compared across evolutionary classes and with theory, and combined with burst amplitude and duration to estimate the mass accreted in bursts. For archival searches it also predicts how many bursts a survey of N sources over t years should contain.

## Cross-paper values

| Sample | τ (interval) | Source |
|---|---|---|
| Orion protostars, Spitzer vs WISE | ~1040 yr (90% CI 690–40,300 yr) | [[fischer-2019]] |
| Gould Belt protostars, NEOWISE | 683 yr (90% 356–1579 yr; N = 735, k = 6); 478–2295 yr over k and N | [[park-2021]] |
| Orion Class 0, Spitzer | 438 yr (95% CI 161–1884 yr) | [[zakri-2022]] |
| Orion, all protostars | 879 yr (95% CI 400–2515 yr) | [[zakri-2022]] |
| Galactic Class I, VVV | 1.75 (+1.12/−0.87) kyr | [[contreras-pena-2024]] |
| Class I (by-product) | 3–13 kyr | [[contreras-pena-2019]] |
| Class II, plates vs Gaia | 112 (+68/−38) kyr (68%) | [[contreras-pena-2019]] |

Reading: bursts become more frequent at younger stages (Class 0 → I → II), but [[zakri-2022]] cannot rule out a common rate for all protostars (p = 6–15%).

## Caveats

- **Small k:** most estimates rest on 2–9 events; the result depends on the prior (flat vs 1/τ vs log) and on which candidates are counted ([[park-2021]], [[zakri-2022]]).
- **Denominator:** N depends on the class definition and contamination (e.g. N = 319 → 271 gives 1040 → 880 yr in [[fischer-2019]]; α-threshold choices in [[contreras-pena-2024]]).
- **Universality:** the estimator assumes every source takes part in bursts ([[contreras-pena-2024]] §6.3).
- **Different intervals:** CIs are quoted at 68%, 90% or 95%, and thresholds/bands differ, so values are not directly comparable.

## Where it appears

- Introduced in: [[contreras-pena-2019]] (the τ = Nt/(k+1) formalism), [[fischer-2019]] (binomial form)
- Appears in: [[contreras-pena-2019]], [[contreras-pena-2024]], [[fischer-2019]], [[park-2021]], [[zakri-2022]]
- Related concepts: [[accretion-outburst]], [[episodic-accretion]], [[statistical-lifetime]]

## Open questions

- A joint analysis of all protostellar samples with one threshold, one prior and one CI level is missing.

## References

1. Contreras Peña, C. et al. 2019 — [[contreras-pena-2019]]
2. Fischer, W. J. et al. 2019 — [[fischer-2019]]
