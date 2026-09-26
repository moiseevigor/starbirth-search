---
title: Accretion outburst
author: moiseevigor
language: en
domain: astrophysics
status: draft
tags:
  - agent/research
  - user/moiseevigor
  - domain/astrophysics
  - topic/accretion-outbursts
  - topic/protostellar-variability
  - topic/time-domain-surveys
  - topic/survey-artefacts-and-contamination
  - concept
  - status/draft
introduced_in: ["[[fischer-2019]]"]
related_concepts: ["[[episodic-accretion]]", "[[outburst-recurrence-time]]", "[[accretion-luminosity]]", "[[luminosity-problem]]", "[[confusion-limit]]"]
appears_in: ["[[furlan-2016]]", "[[contreras-pena-2019]]", "[[contreras-pena-2024]]", "[[fischer-2019]]", "[[lee-2021]]", "[[lu-2024]]", "[[lucas-2024]]", "[[park-2021]]", "[[safron-2015]]", "[[zakri-2022]]", "[[dunham-2014]]"]
---

# Accretion outburst

> **Concept hub.** This note exists as a shared anchor — multiple paper summaries link here via their `key_concepts` frontmatter, so reading this gives the cross-paper view of one idea. Keep it short and authoritative. Long discussions go in paper notes, not here.

## Definition

An accretion outburst (burst) is a large, sustained brightening of a young stellar object caused by a sharp rise in its mass accretion rate. [[fischer-2019]] (Abstract): "Outbursts due to dramatic increases in the mass accretion rate are the most extreme type of variability in young stellar objects."

Classical sub-types: **FUor** (FU Orionis-like; rise over months to years, lasting decades) and **EXor** (EX Lupi-like; shorter, often repeating). Photometric surveys usually cannot confirm the type without spectra ([[safron-2015]], [[contreras-pena-2024]]).

## Why it matters

Outbursts are the direct evidence for [[episodic-accretion]], and their rate constrains how much protostellar mass is gained in bursts. For archival searches they are also the main astrophysical false positive and confusion case for "new source" detections.

## Operational definitions differ by survey

| Paper | Data | Threshold |
|---|---|---|
| [[fischer-2019]] | Spitzer vs WISE, 6.5 yr | brightening > mean + 2σ in all of 3.6/4.5/24 µm, then visual vetting |
| [[zakri-2022]] | Spitzer IRAC, 13 yr | ≥ 2 mag at 3.6 or 4.5 µm |
| [[park-2021]] | NEOWISE, 6.5 yr | ΔW1 or ΔW2 > 1 mag, then multi-survey vetting |
| [[contreras-pena-2019]] | plates vs Gaia, ~55 yr | ΔR ≥ 1 mag, long-lasting (> ~10 yr) |
| [[contreras-pena-2024]] | VVV/VIRAC2, 9 yr | ΔK_s > 2 mag; long / intermediate / short durations |
| [[lucas-2024]] | VVV/VIRAC2, 9 yr | ΔK_s ≥ 4 mag, blind search |

## Cross-paper view

- **Anchor events:** HOPS 383, first Class 0 outburst, ×35 at 24 µm ([[safron-2015]]); HOPS 223 (V2775 Ori), 4.5 → ~51 L⊙ ([[fischer-2019]]; its SED in [[furlan-2016]] mixes pre- and post-outburst epochs).
- **Durations:** "typically longer than a decade" ([[fischer-2019]]); > 9 yr, HOPS 383 ~15 yr total ([[zakri-2022]]); ≥ 5 yr with 600–1000 d rises at ΔK_s ≥ 4 mag ([[lucas-2024]]).
- **False positives:** extinction changes (ruled out for HOPS 383 by sub-mm brightening, [[safron-2015]]; colour test, [[zakri-2022]]); WISE blends and nebulosity ([[fischer-2019]], [[confusion-limit]]); non-YSOs, fewer than 1 in 5 sources at ΔK_s ≥ 4 mag are YSOs ([[lucas-2024]]); ~11% evolved-star contamination of Class I colour samples ([[contreras-pena-2024]]).
- **Other regimes:** no single-epoch sub-mm bursts in 4 yr ([[lee-2021]]); 104 bursts among 2230 NEOWISE-matched massive clumps ([[lu-2024]]).
- The PPVI review of burst evidence before these surveys is [[dunham-2014]] §5.

## Where it appears

- Introduced in: [[fischer-2019]] (vault reference definition)
- Appears in: [[furlan-2016]], [[contreras-pena-2019]], [[contreras-pena-2024]], [[fischer-2019]], [[lee-2021]], [[lu-2024]], [[lucas-2024]], [[park-2021]], [[safron-2015]], [[zakri-2022]], [[dunham-2014]]
- Related concepts: [[episodic-accretion]], [[outburst-recurrence-time]], [[accretion-luminosity]], [[luminosity-problem]], [[confusion-limit]]

## Open questions

- Thresholds differ in band, amplitude and baseline, so rates are not directly comparable across papers. A common injection-recovery framework is missing.
- Are high-amplitude short and long events one population ([[contreras-pena-2019]] finds amplitude does not always imply a long outburst)?

## References

1. Fischer, W. J. et al. 2019 — [[fischer-2019]]
2. Safron, E. J. et al. 2015 — [[safron-2015]]
3. Contreras Peña, C. et al. 2019 — [[contreras-pena-2019]]
