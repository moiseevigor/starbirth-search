---
title: Statistical lifetime
author: moiseevigor
language: en
domain: astrophysics
status: draft
tags:
  - agent/research
  - user/moiseevigor
  - domain/astrophysics
  - topic/evolutionary-lifetimes
  - topic/prestellar-cores
  - topic/class-0-protostars
  - topic/clump-evolutionary-stages
  - topic/methanol-masers
  - concept
  - status/draft
introduced_in: ["[[evans-2009]]", "[[enoch-2008]]"]
related_concepts: ["[[prestellar-core]]", "[[class-0-protostar]]", "[[hi-gal-evolutionary-classification]]", "[[free-fall-time]]", "[[pacs-bright-red-source]]", "[[bolometric-temperature]]"]
appears_in: ["[[elia-2017]]", "[[elia-2021]]", "[[battersby-2017]]", "[[enoch-2008]]", "[[evans-2009]]", "[[konyves-2015]]", "[[kristensen-dunham-2018]]", "[[svoboda-2016]]", "[[young-2023]]", "[[dunham-2008]]", "[[dunham-2014]]", "[[enoch-2010]]", "[[pineda-2011]]", "[[stutz-2013]]"]
---

# Statistical lifetime

> **Concept hub.** This note exists as a shared anchor — multiple paper summaries link here via their `key_concepts` frontmatter, so reading this gives the cross-paper view of one idea. Keep it short and authoritative. Long discussions go in paper notes, not here.

## Definition

A statistical (number-count) lifetime is the duration of an evolutionary phase X inferred from how many objects are currently in X relative to a reference phase of assumed duration:

t_X = t_ref × N_X / N_ref

where N_X and N_ref are counts in the same survey volume and t_ref is the reference clock. The step from ratio to duration assumes steady state (continuous, constant-rate star formation) and a one-way sequence of phases. [[evans-2009]] (Abstract): "These lifetimes assume a continuous flow through the Class II phase".

## Why it matters

Almost every quoted duration for starless/prestellar cores, Class 0, Class I, PBRS or massive starless clumps is a statistical lifetime. It converts a snapshot census into a clock, and hence into expected numbers of rare phases (e.g. first cores, [[first-hydrostatic-core]]) and into burst-count statistics. It constrains only ratios; the absolute scale is entirely set by the reference clock.

## The Class II reference clock

In low-mass clouds the reference is the Class II phase, adopted as **2 ± 1 Myr** and interpreted as a half-life ([[evans-2009]]). The same clock underlies [[enoch-2008]] (through the c2d embedded lifetime of 5.4×10⁵ yr), [[konyves-2015]] (622 Class II YSOs, 2 Myr), [[dunham-2014]] (T_ClassII = 2 Myr) and [[stutz-2013]] (0.5 Myr protostellar lifetime from [[evans-2009]]). [[kristensen-dunham-2018]] show all derived half-lives scale linearly with t_1/2(Class II), varied from 1 to 4 Myr. A revision of the Class II clock therefore rescales the whole low-mass chain at once.

High-mass branch: the clock is instead a 6.7 GHz CH3OH maser lifetime ([[svoboda-2016]], [[battersby-2017]]; itself tied to the Galactic SFR, see [[chomiuk-povich-2011]]), a UCHII lifetime ([[battersby-2017]]) or the Mottram et al. (2011) H II-region lifetime relation ([[elia-2021]]). [[chomiuk-povich-2011]] notes that an assumed 2 Myr YSO lifetime is likely too long for intermediate-mass YSOs.

## Cross-paper values

| Phase | Lifetime (source) |
|---|---|
| Prestellar core | 4.5±0.8×10⁵ yr, factor-2 absolute ([[enoch-2008]]); ~0.5±0.1(±0.3) Myr ([[evans-2009]]); 1.2±0.3 Myr ([[konyves-2015]]) |
| Class 0 | 0.16 Myr, 0.10 extinction-corrected ([[evans-2009]]); 0.15–0.16 Myr ([[dunham-2014]]); half-life 47±4 kyr ([[kristensen-dunham-2018]]) |
| Class I / Class 0+I | Class I 0.54 Myr ([[evans-2009]]); Class 0+I 0.42–0.54 Myr ([[dunham-2014]]); Class I half-life 88±7 kyr ([[kristensen-dunham-2018]]) |
| PBRS | ~25 kyr, 5–80 kyr across Orion ([[stutz-2013]]) |
| Massive starless clumps | τ_SCC ≈ 0.37±0.08 Myr (10³ M⊙/M) ([[svoboda-2016]]); 0.2–1.7 Myr starless, 60–70% of the time ([[battersby-2017]]); ~60/40 pre-/protostellar split ([[elia-2021]]) |

## Known biases

- **Steady state:** non-steady-state (sequential-decay) modelling gives Class 0/I durations a factor ~2–3 shorter ([[kristensen-dunham-2018]]).
- **Density and mass dependence:** t_SL ∝ n^−1.2 ([[enoch-2008]]); ~1.4 Myr at 10⁴ cm⁻³ to ~t_ff at ≳10⁶ cm⁻³ ([[konyves-2015]]); lifetime ∝ M⁻¹ for clumps ([[svoboda-2016]]). See [[free-fall-time]].
- **Misclassification:** 15–25% of "starless" cores host protostars ([[dunham-2008]]; 18–38% in [[dunham-2014]]); the Hi-GAL 70 µm floor and beam blending bias clump counts in opposite directions ([[elia-2017]], [[hi-gal-evolutionary-classification]]); inclination mixes classes ([[furlan-2016]]).
- The 0.45 vs 1.2 Myr prestellar disagreement ([[enoch-2008]] vs [[konyves-2015]]) is largely a density-threshold and clock effect, not a contradiction ([[konyves-2015]] note).

## Where it appears

- Introduced in: [[evans-2009]], [[enoch-2008]]
- Appears in: [[elia-2017]], [[elia-2021]], [[battersby-2017]], [[enoch-2008]], [[evans-2009]], [[konyves-2015]], [[kristensen-dunham-2018]], [[svoboda-2016]], [[young-2023]], [[dunham-2008]], [[dunham-2014]], [[enoch-2010]], [[pineda-2011]], [[stutz-2013]]
- Related concepts: [[prestellar-core]], [[class-0-protostar]], [[hi-gal-evolutionary-classification]], [[free-fall-time]], [[pacs-bright-red-source]], [[bolometric-temperature]]

## Open questions

- How far from steady state are individual clouds, and can the cloud star-forming age ([[kristensen-dunham-2018]]: 1.2±0.1 Myr) be measured independently?
- Should lifetimes be quoted as distributions rather than single values ([[kristensen-dunham-2018]])?

## References

1. Evans, N. J. et al. 2009, ApJS 181, 321 — [[evans-2009]]
2. Enoch, M. L. et al. 2008 — [[enoch-2008]]
3. Kristensen, L. E. & Dunham, M. M. 2018 — [[kristensen-dunham-2018]]
