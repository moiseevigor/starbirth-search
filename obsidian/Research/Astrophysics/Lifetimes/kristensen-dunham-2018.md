---
title: "Protostellar half-life: new methodology and estimates"
authors: L. E. Kristensen, M. M. Dunham
year: 2018
venue: Astronomy & Astrophysics 618, A158
url: https://arxiv.org/abs/1807.11262
language: en
domain: astrophysics
status: draft
methodology_type: methodology
citation_count: 36
citation_count_date: 2026-09-26
key_concepts: ["[[statistical-lifetime]]", "[[class-0-protostar]]", "[[episodic-accretion]]"]
extends: ["[[evans-2009]]"]
contradicts: ["[[evans-2009]]"]
replicates: []
cites: ["[[evans-2009]]", "[[dunham-2014]]", "[[stutz-2013]]"]
cited_by: []
quality_notes: "Short methodological paper (8 pp.). The half-lives are not fits: they are solutions of a degenerate system closed by assuming a Class II half-life of 2 Myr. The numbers scale linearly with that assumption. The Class 0/I split of the 0+I counts is fixed at 35%/65% rather than measured per cloud."
author: moiseevigor
tags:
  - agent/research
  - user/moiseevigor
  - domain/astrophysics
  - topic/evolutionary-lifetimes
  - topic/class-0-protostars
  - topic/spitzer-surveys
  - topic/yso-catalogs
  - paper
  - status/draft
---

# Protostellar half-life: new methodology and estimates

## Abstract

(Verbatim from the arXiv v1 PDF. The arXiv listing shows an abridged version.)

Protostellar systems evolve from prestellar cores, through the deeply embedded stage and then disk-dominated stage, before they end up on the main sequence. Knowing how much time protostellar systems spend in each stage is crucial for understanding how stars and associated planetary systems form, because a key constraint is the time available to form such systems. Equally important is understanding what the spread or uncertainty in these inferred time scales is. The most commonly used method for inferring protostellar ages is to assume the lifetime of one evolutionary stage, and then scale this lifetime to the relative number of protostars in the other stages, i.e., the method assumes populations are in steady state. The number-counting method does not take into account the underlying age distribution and apparent stochasticity of star formation, nor that star formation is sequential, i.e., populations are not in steady state. To overcome this, we propose a new scheme where the lifetime of each protostellar stage follows a distribution based on the formalism of sequential nuclear decay. In this formalism, the main assumptions are: Class 0 sources follow a straight path to Class III sources, the age distribution follows a binomial distribution, and the star-formation rate is constant throughout. The results are that the half-life of Class 0, Class I, and Flat sources are (2.4±0.2)%, (4.4±0.3)%, and (4.3±0.4)% of the Class II half-life, respectively, which translates to 47±4, 88±7, and 87±8 kyr, respectively, for a Class II half-life of 2 Myr for protostars in the Gould Belt clouds with more than 100 protostars. The mean age of these clouds is 1.2±0.1 Myr, and the total inferred star formation rate is (8.3±0.5)×10^−4 M⊙ yr^−1 for a mean protostellar mass of 0.5 M⊙. The critical parameters in arriving at these numbers are the assumed half-life of the Class II stage, and the assumption that the star-formation rate and half-lives are constant. This method presents a first step in moving from steady-state to non-steady-state solutions of protostellar populations.

## TL;DR

This paper replaces steady-state number-count lifetimes with a sequential-decay model: modified Bateman equations with constant Class 0 injection, exponential "decay" between classes, and no steady state. Applied to Gould Belt Spitzer counts, it gives half-lives of **Class 0 = 47 ± 4 kyr, Class I = 88 ± 7 kyr, Flat = 87 ± 8 kyr** (for a 2 Myr Class II half-life). These are a factor ~2–3 shorter than the steady-state c2d values. The cloud star-forming age comes out at 1.2 ± 0.1 Myr.

## Problem

Number-count lifetimes (e.g., [[evans-2009]]) assume populations are in steady state, where every class has reached its equilibrium count. Clouds that started forming stars only ~1–2 Myr ago, with a Class II lifetime of ~2 Myr, cannot be in steady state. The method also returns a single number instead of a lifetime distribution.

## Approach

- **Model** (§2): Class 0 objects form at a constant rate λ_SF. Each class "decays" into the next with a constant rate λ_i (half-life t_1/2 = ln 2 / λ_i): Class 0 → I → Flat → II → III. Class III is the stable end state.
  - dN_0/dt = λ_SF − λ_0 N_0
  - dN_I/dt = λ_0 N_0 − λ_I N_I, and so on for Flat and II (Eqs. 2–5). The initial condition is N_i(0) = 0.
  - Analytic Bateman-type solution: N_D(t) = (λ_SF/λ_D) [1 − Σ_i c_i e^(−λ_i t)], with c_i = Π_{j≠i} λ_j/(λ_j − λ_i) (Eqs. 10–11).
- **Boundary conditions**: N_i(t_0) = N_i^obs, where t_0 is the unknown star-forming time of the cloud. There are six unknowns (λ_SF, λ_0, λ_I, λ_Flat, λ_II, t_0) and five observables. The degeneracy is closed by fixing **λ_II = ln(2)/2 Myr = 0.347 Myr^-1**.
- **Data**: class counts from Dunham et al. (2015) for Gould Belt clouds with N_tot > 100 (Perseus, Serpens, Aquila, Auriga/CMC, Cepheus, IC5146, Ophiuchus; 1988 YSOs in total). The 0+I counts are split 35%/65% into Class 0/I following Enoch et al. (2009). Aquila Class III counts are corrected for 90% AGB contamination.
- **Uncertainties**: 1000 binomial resamplings of each cloud's class populations, re-solved by an iterative bisection method.

## Key result

- Table 2 (total sample): λ_0 = 14.7 ± 1.1, λ_I = 7.9 ± 0.6, λ_Flat = 8.0 ± 0.7 Myr^-1. The half-lives are **47 ± 4, 88 ± 7, 87 ± 8 kyr**, which are 2.4 ± 0.2%, 4.4 ± 0.3% and 4.3 ± 0.4% of the Class II half-life.
- Per-cloud λ_0 ranges from 7.4 ± 2.2 (Auriga/CMC) to 23.2 ± 6.2 Myr^-1 (Ophiuchus). The "decay rates are remarkably similar for all clouds" (§2).
- Table 3: cloud star-forming times range from 0.97 ± 0.17 Myr (Perseus) to 2.00 ± 0.30 Myr (Serpens), and are 1.20 ± 0.08 Myr for the total. SFR is 831 ± 53 M☉ Myr^-1 (mean mass 0.5 M☉).
- Embedded fraction (§3.1.7): "protostars spend ∼ 10% of their time on average in the embedded phase (Class 0, I, Flat stages)".
- Comparison to steady state (§3.1.7): most studies find Class 0 lifetimes "exceeding 0.1 Myr, i.e., a factor of at least two greater than the half-life reported here". The Class 0+I duration of ~0.5 Myr is "three times longer than reported here".
- Population dynamics (§2, Fig. 3): the Class 0, I and Flat numbers become constant after < 0.5 Myr. After that, "about twice as many Class I and Flat sources as Class 0 sources". The star-forming time is constrained by the Class II+III numbers relative to 0/I/Flat.
- Sensitivity tests:
  - Ophiuchus with its observed Class 0/I split: Class 0 half-life 10 kyr (vs. 30 kyr with 35/65).
  - Flat sources split per Heiderman & Evans (2015): Class 0/I half-lives rise to 54/99 kyr.
  - Delta-function (fixed-duration) decay: recovers steady-state lifetimes but needs a 3.2 Myr star-forming time (§3.1.4).
  - All half-lives scale linearly with t_1/2(Class II), which was varied from 1 to 4 Myr (Fig. 4).

## Assumptions

Listed in §2:
1. Star formation is continuous at a constant (core-formation) rate over the cloud's star-forming time.
2. Half-lives depend only on time, "not on mass, environment, or other factors".
3. Evolution is strictly sequential, 0 → I → Flat → II → III.
4. SFR and half-lives are constant (constant decay probability, i.e., exponential/Poisson).
5. Populations are complete above a luminosity limit.
6. No main-sequence stars are included. Class III is the stable final state.
7. Class II half-life is 2 Myr (the reference clock; §3.1.7 notes that Dunham et al. 2015 prefer a combined II+III half-life of 3 Myr).

## Limitations / scope

- The half-lives are for observational **Classes**, not physical **Stages**. Edge-on disks and episodic accretion can move sources between classes (§3.1.3).
- Constant decay probability is one extreme and a fixed-duration delta function is the other. The authors expect the truth between them, i.e., lifetimes shorter than the steady-state values and star-forming times longer (§3.1.4).
- No mass dependence can be tested, because protostellar masses are unknown at the embedded stage (§3.1.2).
- Completeness: the number of PACS Bright Red Sources (PBRS; [[stutz-2013]]) is argued to be negligible (≪1%) in the Gould Belt clouds (§3.1.5).
- The Ophiuchus Class 0 deficit suggests its SFR may be declining, a case the constant-SFR model cannot handle (§3.1.2).
- The Gould Belt sample is biased: all clouds are young, rich, and contain Class 0 sources.

## Replication evidence

None known within the vault. The paper re-analyses the same Gould Belt Spitzer counts that underlie the steady-state lifetimes of [[evans-2009]] and Dunham et al. 2015. The disagreement comes from the model, not the data.

## Why this paper matters

This is the main published critique of the steady-state assumption behind every [[statistical-lifetime]] in this folder. It makes explicit that number counts constrain only ratios of half-lives to the Class II clock, and that in young clouds sequential filling of later classes shortens the inferred early-phase durations. The Class 0 value (~50 kyr) is about half the commonly quoted ~0.1–0.16 Myr. Any rate calculation built on Class 0 duration (e.g., expected numbers of Class 0 births or first cores in a survey) inherits this factor-of-2–3 systematic.

The paper also introduces the concept of a lifetime *distribution*: stochastic dwell times with a spread, rather than one deterministic duration.

## Quotes

1. > "the method assumes populations are in steady state" — Abstract
2. > "the average protostar will spend ∼ 50,000 years as a Class 0 object" — §3.2

## Open questions surfaced

- What is the real dwell-time distribution, between exponential and delta-function? Can it be constrained from age spreads or kinematics?
- Can the main-sequence population of a cloud (e.g., from Gaia co-moving members) be used to solve for λ_III and remove the Class II clock? This is proposed in §3.1.6.
- How would a declining SFR with a cut-off time (as suggested for Ophiuchus) change the Class 0 half-life?
- Do half-lives depend on protostellar mass or environment? Testing this requires mass estimates for embedded sources.

## Related material in vault

- Extends: [[evans-2009]] (develops its "half-life" interpretation into a non-steady-state model)
- Contradicts: [[evans-2009]] (Class 0 and embedded-phase durations a factor ~2–3 shorter than steady-state values)
- Replicates: —
- Concepts introduced/used: [[statistical-lifetime]], [[class-0-protostar]], [[episodic-accretion]]
- Cites: [[evans-2009]], [[dunham-2014]], [[stutz-2013]]
- Cited by (in this vault): —
