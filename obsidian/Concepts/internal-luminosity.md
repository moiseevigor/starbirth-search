---
title: Internal luminosity
author: moiseevigor
language: en
domain: astrophysics
status: draft
tags:
  - agent/research
  - user/moiseevigor
  - domain/astrophysics
  - topic/embedded-low-luminosity-protostars
  - topic/protostar-observational-signatures
  - topic/radiative-transfer
  - concept
  - status/draft
introduced_in: ["[[dunham-2008]]"]
related_concepts: ["[[vello]]", "[[first-hydrostatic-core]]", "[[accretion-luminosity]]", "[[luminosity-problem]]", "[[bolometric-temperature]]"]
appears_in: ["[[evans-2009]]", "[[dunham-2008]]", "[[dunham-2014]]", "[[enoch-2010]]", "[[pineda-2011]]", "[[stutz-2013]]"]
---

# Internal luminosity

> **Concept hub.** This note exists as a shared anchor — multiple paper summaries link here via their `key_concepts` frontmatter, so reading this gives the cross-paper view of one idea. Keep it short and authoritative. Long discussions go in paper notes, not here.

## Definition

[[dunham-2008]] (Abstract): "The internal luminosity of a source, L_int, is the luminosity of the central source and excludes luminosity arising from external heating."

It differs from L_bol, which also includes envelope emission heated by the interstellar radiation field. For the faintest embedded sources the external term can dominate L_bol.

The standard observational proxy is the **L_int–F70 relation** ([[dunham-2008]] Eq. 2):

L_int = 3.3 × 10⁸ F70^0.94 L⊙, with F70 in erg cm⁻² s⁻¹ normalised to 140 pc.

It holds because 70 µm emission comes from envelope dust warmed by the central source and depends little on geometry, whereas 3–24 µm emission depends strongly on inclination and cavities.

## Why it matters

L_int turns a single 70 µm flux or upper limit into a central luminosity. This is how the faintest protostars, [[vello]]s and [[first-hydrostatic-core]] candidates are placed on a common scale. It also defines survey depth: c2d 70 µm maps reach L_int ≥ 4×10⁻³ (d/140 pc)² L⊙ ([[dunham-2008]]).

## Cross-paper view

- Per-Bolo 58: 0.012 L⊙ from full radiative-transfer modelling vs 0.014 L⊙ from the relation ([[enoch-2010]]).
- L1451-mm: 70 µm non-detection → L < 1.6×10⁻² L⊙ ([[pineda-2011]]).
- FHSC predicted L_int 10⁻⁴–10⁻¹ L⊙ ([[dunham-2014]]).
- A resolved 70 µm point source requires an internal heating source; external-heating starless-core models cannot reproduce PBRS SEDs ([[stutz-2013]]).
- [[evans-2009]] uses the c2d luminosities to frame the [[luminosity-problem]].

## Where it appears

- Introduced in: [[dunham-2008]]
- Appears in: [[evans-2009]], [[dunham-2008]], [[dunham-2014]], [[enoch-2010]], [[pineda-2011]], [[stutz-2013]]
- Related concepts: [[vello]], [[first-hydrostatic-core]], [[accretion-luminosity]], [[luminosity-problem]], [[bolometric-temperature]]

## Open questions

- The observational calibration rests on 11 modelled sources; the model grid carries the fit ([[dunham-2008]] quality note). How well does it hold at the 0.01 L⊙ level and beyond 140 pc, where beam blending adds flux?

## References

1. Dunham, M. M. et al. 2008, ApJS 179, 249 — [[dunham-2008]]
