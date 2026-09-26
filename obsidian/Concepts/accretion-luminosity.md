---
title: Accretion luminosity
author: moiseevigor
language: en
domain: astrophysics
status: draft
tags:
  - agent/research
  - user/moiseevigor
  - domain/astrophysics
  - topic/accretion-luminosity
  - topic/second-collapse
  - topic/protostellar-collapse
  - topic/accretion-outbursts
  - concept
  - status/draft
introduced_in: ["[[larson-1969]]", "[[masunaga-inutsuka-2000]]"]
related_concepts: ["[[luminosity-problem]]", "[[episodic-accretion]]", "[[accretion-outburst]]", "[[second-collapse]]", "[[internal-luminosity]]"]
appears_in: ["[[evans-2009]]", "[[bhandare-2020]]", "[[larson-1969]]", "[[masunaga-inutsuka-2000]]", "[[young-2023]]", "[[fischer-2019]]", "[[dunham-2008]]", "[[dunham-2014]]", "[[pineda-2011]]"]
---

# Accretion luminosity

> **Concept hub.** This note exists as a shared anchor — multiple paper summaries link here via their `key_concepts` frontmatter, so reading this gives the cross-paper view of one idea. Keep it short and authoritative. Long discussions go in paper notes, not here.

## Definition

The luminosity released by material falling onto the protostar's surface:

L_acc = G M* Ṁ / R* ([[masunaga-inutsuka-2000]] Eq. 5; same form in [[bhandare-2020]] §3.2)

with M* the protostellar mass, Ṁ the accretion rate and R* the protostellar radius. [[fischer-2019]] writes L_acc = η G M* Ṁ / R*, with η the fraction of the energy radiated. During the embedded phase L_acc dominates the internal luminosity.

## Why it matters

It is the link between accretion rate and observable luminosity. It defines the [[luminosity-problem]] (observed L below the L_acc of a constant rate), makes bursts visible as luminosity jumps, and is the quantity that should rise after the [[second-collapse]].

## Cross-paper view

- **Theory after birth:** jump to ~10 L⊙, peak 30 L⊙ at 8×10⁴ yr ([[larson-1969]]); peak ~25 L⊙ at ~2×10⁴ yr, homogeneous model ([[masunaga-inutsuka-2000]]); 1.65 L⊙ at ~188 yr for a 1 M⊙ core, up to 2.12×10⁴ L⊙ for 100 M⊙ ([[bhandare-2020]]); "a few tens L⊙" ([[young-2023]]).
- **Reference numbers:** 2×10⁻⁶ M⊙ yr⁻¹ onto 0.08 M⊙, 3 R⊙ gives ~1.6 L⊙ ([[dunham-2008]], [[evans-2009]]); 10⁻⁵ M⊙ yr⁻¹ onto 0.25 M⊙, 3 R⊙ gives ~25 L⊙ ([[dunham-2014]]).
- **Observed tensions:** IRAM 04191 L_acc ~2 L⊙ from its outflow vs L_int ~0.08 L⊙ ([[dunham-2008]]); L1451-mm expected 6 L⊙ vs fitted 0.045 L⊙ ([[pineda-2011]]).
- **Bursts:** HOPS 223 rose ×12 to ~51 L⊙ (Ṁ ~10⁻⁶ → 10⁻⁵ M⊙ yr⁻¹); HOPS 383 ×35 ([[fischer-2019]]).
- **Efficiency:** the second accretion shock is subcritical, so accretion energy goes into the core rather than being radiated ([[bhandare-2020]]); [[dunham-2014]] lists inefficient shocks (f_acc < 1) among luminosity-problem solutions.

**Inconsistency to watch:** peak post-birth luminosity and its timing differ between 1-D models (30 L⊙ at 8×10⁴ yr vs 25 L⊙ at 2×10⁴ yr) and depend on the initial density profile (the hydrostatic model of [[masunaga-inutsuka-2000]] has no peak).

## Where it appears

- Introduced in: [[larson-1969]], [[masunaga-inutsuka-2000]]
- Appears in: [[evans-2009]], [[bhandare-2020]], [[larson-1969]], [[masunaga-inutsuka-2000]], [[young-2023]], [[fischer-2019]], [[dunham-2008]], [[dunham-2014]], [[pineda-2011]]
- Related concepts: [[luminosity-problem]], [[episodic-accretion]], [[accretion-outburst]], [[second-collapse]], [[internal-luminosity]]

## Open questions

- What value of η (or f_acc) applies in the embedded phase, and does it change between quiescence and bursts?

## References

1. Masunaga, H. & Inutsuka, S. 2000 — [[masunaga-inutsuka-2000]]
2. Larson, R. B. 1969 — [[larson-1969]]
