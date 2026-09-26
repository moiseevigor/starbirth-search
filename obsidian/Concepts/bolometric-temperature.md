---
title: Bolometric temperature
author: moiseevigor
language: en
domain: astrophysics
status: draft
tags:
  - agent/research
  - user/moiseevigor
  - domain/astrophysics
  - topic/class-0-protostars
  - topic/protostar-observational-signatures
  - topic/evolutionary-lifetimes
  - concept
  - status/draft
introduced_in: ["[[furlan-2016]]", "[[masunaga-inutsuka-2000]]"]
related_concepts: ["[[class-0-protostar]]", "[[pacs-bright-red-source]]", "[[statistical-lifetime]]", "[[internal-luminosity]]"]
appears_in: ["[[evans-2009]]", "[[masunaga-inutsuka-2000]]", "[[furlan-2016]]", "[[dunham-2008]]", "[[dunham-2014]]", "[[pineda-2011]]", "[[stutz-2013]]"]
---

# Bolometric temperature

> **Concept hub.** This note exists as a shared anchor — multiple paper summaries link here via their `key_concepts` frontmatter, so reading this gives the cross-paper view of one idea. Keep it short and authoritative. Long discussions go in paper notes, not here.

## Definition

T_bol is the temperature of a blackbody with the same mean frequency as the observed SED (Myers & Ladd 1993; as defined in [[furlan-2016]] §III.3):

T_bol = 1.25 × 10⁻¹¹ ⟨ν⟩ K Hz⁻¹, with ⟨ν⟩ = ∫ν S_ν dν / ∫S_ν dν.

Class boundaries (Chen et al. 1995): Class 0 T_bol < 70 K, Class I 70–650 K, Class II 650–2800 K. The 70 K Class 0/I boundary is used by [[dunham-2014]] and [[furlan-2016]].

## Why it matters

T_bol is the standard one-number evolutionary indicator for embedded protostars and the basis of Class 0 counts, hence of Class 0 [[statistical-lifetime]]s. Theory shows it jumps at protostellar birth, so it is a potential birth marker.

## Cross-paper view

- **Theory clock:** T_bol "remains at 10 K before a protostar is formed", then "abruptly rises up to 40 K after t − t₀ exceeds 0" and climbs to 410 K; T_bol < 70 K corresponds to ≲2×10⁴ yr after birth ([[masunaga-inutsuka-2000]] §4.1).
- **Empirical clock:** T_bol = 25 K + C (t/10⁵ yr)^1.8, C = 51 K ([[evans-2009]] §7.1, quoting Enoch et al.).
- **Values:** HOPS median 146 K, nine sources within ±5% of 70 K ([[furlan-2016]]); PBRS T_bol < 45 K ([[stutz-2013]]); L1451-mm T_bol ≤ 30 K ([[pineda-2011]]); Class 0 fraction by T_bol 0.30–0.32 ([[dunham-2014]]); BLT (L_bol–T_bol) diagram of low-luminosity sources ([[dunham-2008]]).
- **Bias:** T_bol is sensitive to missing high-frequency flux, so edge-on Class I sources can look like Class 0 ([[masunaga-inutsuka-2000]]); inclination moves sources between classes ([[furlan-2016]]); ISRF heating can raise L_bol of faint Class 0 sources ([[dunham-2008]]).

## Where it appears

- Introduced in: [[furlan-2016]] (definition as used), [[masunaga-inutsuka-2000]] (theoretical T_bol evolution)
- Appears in: [[evans-2009]], [[masunaga-inutsuka-2000]], [[furlan-2016]], [[dunham-2008]], [[dunham-2014]], [[pineda-2011]], [[stutz-2013]]
- Related concepts: [[class-0-protostar]], [[pacs-bright-red-source]], [[statistical-lifetime]], [[internal-luminosity]]

## Open questions

- How much does sparse or non-simultaneous photometry (variable sources, [[robitaille-2017]] §7.3) shift T_bol near the 70 K boundary?

## References

1. Myers, P. C. & Ladd, E. F. 1993, ApJ 413, L47 (definition; not in vault)
2. Chen, H. et al. 1995, ApJ 445, 377 (class boundaries; not in vault)
3. Masunaga, H. & Inutsuka, S. 2000 — [[masunaga-inutsuka-2000]]
