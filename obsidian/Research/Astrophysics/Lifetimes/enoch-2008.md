---
title: "The Mass Distribution and Lifetime of Prestellar Cores in Perseus, Serpens, and Ophiuchus"
authors: Melissa L. Enoch, Neal J. Evans II, Anneila I. Sargent, Jason Glenn, Erik Rosolowsky, Philip Myers
year: 2008
venue: The Astrophysical Journal 684, 1240
url: https://arxiv.org/abs/0805.1075
language: en
domain: astrophysics
status: draft
methodology_type: empirical
citation_count: 259
citation_count_date: 2026-09-26
key_concepts: ["[[statistical-lifetime]]", "[[prestellar-core]]", "[[free-fall-time]]"]
extends: []
contradicts: []
replicates: []
cites: ["[[evans-2009]]", "[[dunham-2008]]"]
cited_by: ["[[evans-2009]]", "[[konyves-2015]]", "[[dunham-2008]]", "[[dunham-2014]]", "[[elia-2017]]", "[[enoch-2010]]", "[[pineda-2011]]"]
quality_notes: "Classic reference for the ~0.5 Myr dense prestellar-core lifetime. The embedded-phase clock (5.4e5 yr) is taken from Evans et al. 2008, then in prep. (published as evans-2009), so the two papers are not independent."
author: moiseevigor
tags:
  - agent/research
  - user/moiseevigor
  - domain/astrophysics
  - topic/evolutionary-lifetimes
  - topic/prestellar-cores
  - topic/spitzer-surveys
  - topic/protostellar-collapse
  - topic/core-mass-function
  - paper
  - status/draft
---

# The Mass Distribution and Lifetime of Prestellar Cores in Perseus, Serpens, and Ophiuchus

## Abstract

We present an unbiased census of starless cores in Perseus, Serpens, and Ophiuchus, assembled by comparing large-scale Bolocam 1.1 mm continuum emission maps with Spitzer c2d surveys. We use the c2d catalogs to separate 108 starless from 92 protostellar cores in the 1.1 mm core samples from Enoch et al. (2006), Young et al. (2006), and Enoch et al. (2007). A comparison of these populations reveals the initial conditions of the starless cores. Starless cores in Perseus have similar masses but larger sizes and lower densities on average than protostellar cores, with sizes that suggest density profiles substantially flatter than r^-2. By contrast, starless cores in Serpens are compact and have lower masses than protostellar cores; future star formation will likely result in lower mass objects than the currently forming protostars. Comparison to dynamical masses estimated from the NH_3 survey of Perseus cores by Rosolowsky et al. (2007) suggests that most of the starless cores are likely to be gravitationally bound, and thus prestellar. The combined prestellar core mass distribution includes 108 cores and has a slope of -2.3+/-0.4 for M>0.8 Msun. This slope is consistent with recent measurements of the stellar initial mass function, providing further evidence that stellar masses are directly linked to the core formation process. We place a lower limit on the core-to-star efficiency of 25%. There are approximately equal numbers of prestellar and protostellar cores in each cloud, thus the dense prestellar core lifetime must be similar to the lifetime of embedded protostars, or 4.5x10^5 years, with a total uncertainty of a factor of two. Such a short lifetime suggests a dynamic, rather than quasi-static, core evolution scenario, at least at the relatively high mean densities (n>2x10^4 cm^-3) to which we are sensitive.

## TL;DR

In three Gould Belt clouds, Bolocam 1.1 mm starless cores and Spitzer-identified embedded (Class 0+I) protostars occur in roughly equal numbers. Anchored to an embedded-phase lifetime of 5.4×10^5 yr, this gives a dense prestellar-core lifetime of **4.5×10^5 yr (±0.8×10^5 statistical; factor 2 absolute)**, which is only 1.5–3.9 free-fall times. The lifetime is shorter for denser cores (t_SL ∝ n^-1.2). This is the standard number for the prestellar lifetime at n ≳ 2×10^4 cm^-3.

## Problem

How long does a dense starless core last before it forms a protostar? The answer separates quasi-static evolution (magnetic support with ambipolar diffusion, t_AD ~ 10^7 yr) from dynamic evolution (a few free-fall times). Published values before this paper spanned two orders of magnitude, "from a few times 10^5 yr to 10^7 yr" (§6).

## Approach

- **Sample** (§2–3): Bolocam 1.1 mm core catalogs of Perseus, Serpens and Ophiuchus (30″ beam), cross-matched with Spitzer c2d IRAC/MIPS catalogs. The result is 108 starless and 92 protostellar cores.
- **Statistical lifetime** (§6): t_SL = t_emb (N_SL / N_emb). Here N_SL is the number of starless cores and N_emb = N_Class0 + N_ClassI is the number of embedded protostars, classified by bolometric temperature (Class 0: T_bol < 70 K; Class I: 70 < T_bol < 650 K) and required to have 1.1 mm emission. This makes the sample complete to embedded sources with M_env ≳ 0.1 M☉.
- **Reference clock**: t_emb = 5.4×10^5 yr ("Evans et al. 2008, in prep" → [[evans-2009]]). That value is itself derived from Class 0+I / Class II counts with a Class II lifetime of 2×10^6 yr.
- **Free-fall comparison**: t_ff = sqrt(3π / (32 G ⟨n⟩ μ_p m_H)) with μ_p = 2.33 (Eq. 8). ⟨n_1e4⟩ is the mean density in a fixed 10^4 AU aperture.

## Key result

- Starless-to-embedded ratios (§6): "N_SL/N_emb = 1.0 in Perseus, 0.4 in Serpens, and 0.8 in Ophiuchus". These imply prestellar core lifetimes of "5 × 10^5 yr in Perseus, 2 × 10^5 yr in Serpens, and 5 × 10^5 yr in Ophiuchus".
- Table 3 (verbatim):

| Cloud | N_SL/N_emb | t_SL (yr) | ⟨n_1e4⟩_SL (cm^-3) | t_ff (yr) | t_SL/t_ff |
|---|---|---|---|---|---|
| Perseus | 67/66 = 1.0 | 5×10^5 | 1.4×10^5 | 1.4×10^5 | 3.9 |
| Serpens | 15/35 = 0.4 | 2×10^5 | 1.2×10^5 | 1.5×10^5 | 1.5 |
| Ophiuchus | 26/28 = 0.9 | 5×10^5 | 1.6×10^5 | 1.3×10^5 | 3.9 |
| Combined | 108/129 = 0.8 | 4.5×10^5 | 1.7×10^5 | 1.4×10^5 | 3.2 |
| "low density" (n_1e4 < 2×10^5) | 78/129 = 0.6 | 3.3×10^5 | 1.3×10^5 | 1.5×10^5 | 2.2 |
| "high density" (n_1e4 > 2×10^5) | 30/129 = 0.2 | 1.3×10^5 | 2.8×10^5 | 1.0×10^5 | 1.3 |

- Combined lifetime (§6): "Taking all three clouds together yields a prestellar core lifetime of 4.5 × 10^5 yr". The count uncertainty (±10 cores) gives "approximately 0.8 × 10^5 yr".
- **Density dependence** (§6.1): the lifetime falls "at a faster rate than n^−0.5". The observed trend is "t_SL ∝ n^−1.2", closer to the n^−0.85 of Jessop & Ward-Thompson (2000).
- **Mass dependence** (§6, §5.4): the N_SL/N_emb ratio is lowest in Serpens, "which has the highest mass cores on average". Higher-mass cores "tend to be protostellar, possibly because they collapse on a shorter timescale".
- Conclusion (§7): "The three-cloud average is 4.5±0.8×10^5 yr (with an absolute uncertainty of a factor of two)". The ambipolar-diffusion timescale t_AD ~ 7×10^6 yr is "more than an order of magnitude longer".
- Prestellar core mass distribution (CMD) slope α = −2.3 ± 0.4 above 0.8 M☉. The core-to-star efficiency is ≥ 25%.

## Assumptions

Stated in §6:
1. All starless cores are prestellar, i.e., bound and will form stars or brown dwarfs.
2. Star formation has been steady in time for at least the last 2 Myr, because the clock is ultimately calibrated on the Class II phase (2×10^6 yr).
3. There is "no significant evolutionary dependence on source mass". The paper's own §5.4 hints that this is violated.
4. The embedded-phase lifetime is 5.4×10^5 yr (from [[evans-2009]]).

## Limitations / scope

Additional uncertainties (§6.2), each quantified:
- **Unequal sensitivity**: the protostellar mass completeness limit is lower by a factor of ~2, so the lifetime "should perhaps be increased by a factor of 1.3".
- **Multiplicity**: N_emb/N_PS = 1.2, 1.8 and 1.6 in Per, Ser and Oph. If unresolved starless cores are also multiple, lifetimes rise by these factors.
- **Unbound starless cores**: extrapolating from the six cores with M_dust/M_vir < 0.5 would decrease the lifetime by a factor of 1.2.
- **Contaminated Class I**: if many Class I sources are edge-on T Tauri disks, t_emb could be as low as 2.8×10^5 yr, which halves the prestellar lifetime.
- **Continuous-star-formation assumption**: acknowledged as possibly wrong. Averaging over three clouds is the only mitigation. No correction factors are applied, and the absolute uncertainty is stated as a factor of 2 either way.
- **Density floor**: the survey is sensitive only to n ≳ 2–3×10^4 cm^-3. Earlier, lower-density evolution could still be quasi-static (§6, §7).

## Replication evidence

Partial. Jørgensen et al. (2007) and Hatchell et al. (2007) (SCUBA + c2d, Perseus) find approximately equal starless and embedded lifetimes (quoted in §6). [[evans-2009]] re-derives t(pre) = 0.46 Myr with a slightly different source list and combines it with SCUBA results to give 0.5 ± 0.1 (±0.3) Myr. [[konyves-2015]] (Herschel, Aquila, lower density floor) finds a longer ~1.2 Myr, which is consistent with the lifetime–density trend reported here.

## Why this paper matters

This is the canonical "prestellar lifetime ≈ embedded lifetime ≈ 0.5 Myr" result. It uses unbiased mm and IR censuses of whole clouds instead of targeted core samples. By expressing the result as t_SL/t_ff = 1.5–3.9, it made the dynamic-versus-quasi-static argument quantitative, and it established the density dependence later reproduced with Herschel.

The number is not independent of the c2d Class 0/I lifetime. The whole chain rests on the Class II ~2 Myr clock and on steady state. Any revision of those, e.g. [[kristensen-dunham-2018]]'s non-steady-state half-lives, propagates directly.

## Quotes

1. > "argues for a dynamic, rather than quasi-static, core evolutionary scenario" — §6
2. > "sampling only the densest end stage in a longer core evolutionary picture" — §6

## Open questions surfaced

- Does the lifetime–density law t_SL ∝ n^−1.2 hold across more clouds and below n ~ 2×10^4 cm^-3? [[konyves-2015]] tests this.
- How large is the mass dependence of the prestellar lifetime (Serpens suggests massive cores evolve faster), and how much does it distort the CMD-to-IMF mapping?
- How much of the "starless" sample hides very-low-luminosity embedded sources below c2d sensitivity? See [[dunham-2008]].

## Related material in vault

- Extends: —
- Contradicts: —
- Replicates: —
- Concepts introduced/used: [[statistical-lifetime]], [[prestellar-core]], [[free-fall-time]]
- Cites: [[evans-2009]] (as "Evans et al. 2008, in prep": source of t_emb), [[dunham-2008]] (as "Dunham et al. 2008, in prep": low-luminosity completeness)
- Cited by (in this vault): [[evans-2009]], [[konyves-2015]], [[dunham-2008]], [[dunham-2014]], [[elia-2017]], [[enoch-2010]], [[pineda-2011]]
