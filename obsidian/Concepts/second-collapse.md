---
title: Second collapse
author: moiseevigor
language: en
domain: astrophysics
status: draft
tags:
  - agent/research
  - user/moiseevigor
  - domain/astrophysics
  - topic/second-collapse
  - topic/protostellar-collapse
  - topic/radiation-hydrodynamics
  - topic/accretion-luminosity
  - concept
  - status/draft
introduced_in: ["[[larson-1969]]"]
related_concepts: ["[[first-hydrostatic-core]]", "[[accretion-luminosity]]", "[[free-fall-time]]", "[[class-0-protostar]]"]
appears_in: ["[[larson-1969]]", "[[masunaga-inutsuka-2000]]", "[[tomida-2013]]", "[[bhandare-2020]]", "[[young-2023]]", "[[dunham-2014]]"]
---

# Second collapse

> **Concept hub.** This note exists as a shared anchor — multiple paper summaries link here via their `key_concepts` frontmatter, so reading this gives the cross-paper view of one idea. Keep it short and authoritative. Long discussions go in paper notes, not here.

## Definition

The second collapse is the dynamical collapse inside the [[first-hydrostatic-core]] triggered when its central temperature reaches ~2000 K. H2 dissociation absorbs energy and drops the effective adiabatic index below 4/3 (Γ ≈ 1.1), so pressure can no longer support the core. The collapse ends when dissociation is complete (ρc ≈ 10⁻² g cm⁻³, Tc ≈ 10⁴ K), forming the second (stellar, protostellar) core: the moment of protostellar birth.

[[masunaga-inutsuka-2000]] §3.1.3: the second collapse begins "when the central density and the central temperature reach ρc ∼ 10⁻⁷ g cm⁻³ and Tc ∼ 2000 K".

## Why it matters

It is the physical definition of when a protostar is "born". Every model agrees the event is hidden: the new core sits inside the first-core remnant and an optically thick envelope, so the emergent SED does not change immediately ([[young-2023]]: "There is no immediate change in the SED after the formation of the second core"). The observable consequence is the later rise of the [[accretion-luminosity]].

## Cross-paper view

| Quantity | Values (source) |
|---|---|
| Onset | Tc ≈ 2000 K ([[larson-1969]]); ρc ≈ 10⁻⁷ g cm⁻³ ([[masunaga-inutsuka-2000]]); ρc ≈ 10⁻⁸ g cm⁻³ ([[tomida-2013]]) |
| Duration | ~0.1 yr, the free-fall time at 10⁻⁷ g cm⁻³ ([[masunaga-inutsuka-2000]]); "several years", t_ff ≈ 0.67 yr at 10⁻⁸ g cm⁻³ ([[tomida-2013]]) |
| Second core at birth | 1.5×10⁻³ M⊙, 1.3 R⊙, ~2×10⁴ K ([[larson-1969]]); ≈0.0015 M⊙, 1–4 R⊙ ([[young-2023]]) |
| Early growth | swells to 12 R⊙ within ~1 yr ([[larson-1969]]); settles at ~4 R⊙ ([[masunaga-inutsuka-2000]]); ~0.02 M⊙ within 0.7 yr, transient ~10 R⊙ ([[tomida-2013]]); 1 M⊙ core: 54 R⊙ and 0.044 M⊙ at 188 yr ([[bhandare-2020]]) |
| Burial time | ~5.5 yr, the first-core free-fall time ([[tomida-2013]]); optically thick second cores ([[bhandare-2020]]) |
| Luminosity emergence | 10 L⊙ within ~10–100 yr, peak 30 L⊙ at 8×10⁴ yr ([[larson-1969]]); peak ~25 L⊙ at ~2×10⁴ yr ([[masunaga-inutsuka-2000]]) |

[[dunham-2014]] places the second collapse in the observational context of FHSC candidates and Class 0 statistics.

**Inconsistency to watch:** the time for the luminosity to become visible differs between [[larson-1969]] (tens of years) and [[masunaga-inutsuka-2000]] (rise resolved on 10³–10⁴ yr). [[young-2023]]'s "tomida 0.02 M⊙ is probably high" also shows second-core mass depends on when it is measured.

## Where it appears

- Introduced in: [[larson-1969]]
- Appears in: [[larson-1969]], [[masunaga-inutsuka-2000]], [[tomida-2013]], [[bhandare-2020]], [[young-2023]], [[dunham-2014]]
- Related concepts: [[first-hydrostatic-core]], [[accretion-luminosity]], [[free-fall-time]], [[class-0-protostar]]

## Open questions

- How long after the second collapse does any observable (mid-IR, 160 µm, chemistry such as CS or CO sublimation) change measurably? [[young-2023]] gives ~200 yr for CO/CS chemistry.
- Does the second-core radius evolution (expansion vs contraction, set by the Kelvin–Helmholtz to accretion time ratio in [[bhandare-2020]]) affect the early luminosity?

## References

1. Larson, R. B. 1969 — [[larson-1969]]
2. Masunaga, H. & Inutsuka, S. 2000 — [[masunaga-inutsuka-2000]]
3. Tomida, K. et al. 2013 — [[tomida-2013]]
