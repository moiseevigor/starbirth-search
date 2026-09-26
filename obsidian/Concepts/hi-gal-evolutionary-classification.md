---
title: Hi-GAL evolutionary classification
author: moiseevigor
language: en
domain: astrophysics
status: draft
tags:
  - agent/research
  - user/moiseevigor
  - domain/astrophysics
  - topic/hi-gal
  - topic/clump-evolutionary-stages
  - topic/massive-clumps
  - topic/prestellar-cores
  - topic/survey-completeness-reliability
  - concept
  - status/draft
introduced_in: ["[[elia-2017]]"]
related_concepts: ["[[prestellar-core]]", "[[statistical-lifetime]]", "[[confusion-limit]]", "[[internal-luminosity]]", "[[class-0-protostar]]"]
appears_in: ["[[elia-2017]]", "[[elia-2021]]", "[[elia-2022]]", "[[molinari-2016]]", "[[battersby-2017]]", "[[svoboda-2016]]"]
---

# Hi-GAL evolutionary classification

> **Concept hub.** This note exists as a shared anchor — multiple paper summaries link here via their `key_concepts` frontmatter, so reading this gives the cross-paper view of one idea. Keep it short and authoritative. Long discussions go in paper notes, not here.

## Definition

The photometric stage rule applied to Hi-GAL clumps ([[elia-2017]] §3.5; reused by [[elia-2021]] and [[elia-2022]]):

1. **Protostellar** — the clump has a 70 µm counterpart.
2. **Starless** — no 70 µm counterpart. Starless clumps split into
   - **pre-stellar (bound)** if M(r) > 460 M⊙ (r/pc)^1.9 (Larson's third relation), and
   - **unbound** otherwise.
3. **H II-region candidates** — protostellar clumps with L_bol/M ≥ 22.4 L⊙/M⊙.

The authors themselves call the scheme one that may "remain probably too clear-cut and surely affected by biases" ([[elia-2017]] §3.5), and [[elia-2021]] (§2.1) adds that "starless sources should be more rigorously named candidate starless clumps".

## Why it matters

It is the most widely used Galaxy-wide prestellar/protostellar split. Hi-GAL stage counts feed clump [[statistical-lifetime]]s ([[elia-2021]]) and the bottom-up Milky Way SFR, which sums only protostellar clumps ([[elia-2022]]).

## Cross-paper view

- **Counts:** 24,584 protostellar and 76,338 starless (16,667 bound) among 100,922 inner-Galaxy clumps ([[elia-2017]]); 35,412 protostellar = 23% of 150,223 across 360° ([[elia-2021]]).
- **70 µm floor:** typical PACS limit 0.2 Jy. Grey bodies with M ≤ 50 M⊙ and T ≤ 16 K are undetectable at d ≳ 5 kpc ([[elia-2017]] App. C1). Low-luminosity [[class-0-protostar]]s may be missed ([[elia-2021]]). The 70 µm catalogue depth comes from [[molinari-2016]], whose 70 µm completeness is nearly constant with longitude.
- **Blending:** merging sources closer than the 18″ 250 µm beam raises the protostellar fraction with distance (slope 0.005 kpc⁻¹; [[elia-2017]]). [[elia-2021]] reads the falling pre-/protostellar ratio with distance as blending dominating over 70 µm incompleteness. See [[confusion-limit]].
- **Independent checks:** in BGPS clumps the Hi-GAL 70 µm source is present in 88% of protostellar clumps and is the most sensitive indicator ([[svoboda-2016]]). [[battersby-2017]] avoids clump definitions by classifying pixels with GLIMPSE 8 µm contrast.
- ATLASGAL stages (quiescent → protostellar → YSO → H II; used by [[lu-2024]]) are a parallel scheme, not the same rule.

## Where it appears

- Introduced in: [[elia-2017]]
- Appears in: [[elia-2017]], [[elia-2021]], [[elia-2022]], [[molinari-2016]], [[battersby-2017]], [[svoboda-2016]]
- Related concepts: [[prestellar-core]], [[statistical-lifetime]], [[confusion-limit]], [[internal-luminosity]], [[class-0-protostar]]

## Open questions

- What fraction of Hi-GAL "starless" clumps host 70 µm-dark protostars below 0.2 Jy, as a function of distance? This sets the correction to both lifetimes and SFR.
- Can a lower PACS extraction threshold ([[molinari-2016]] suggests σc < 2) recover them at an acceptable false-positive rate?

## References

1. Elia, D. et al. 2017 — [[elia-2017]]
2. Elia, D. et al. 2021 — [[elia-2021]]
3. Molinari, S. et al. 2016 — [[molinari-2016]]
