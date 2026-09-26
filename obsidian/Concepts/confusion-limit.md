---
title: Confusion limit
author: moiseevigor
language: en
domain: astrophysics
status: draft
tags:
  - agent/research
  - user/moiseevigor
  - domain/astrophysics
  - topic/survey-completeness-reliability
  - topic/survey-artefacts-and-contamination
  - topic/hi-gal
  - topic/wise-neowise
  - concept
  - status/draft
introduced_in: ["[[elia-2017]]"]
related_concepts: ["[[hi-gal-evolutionary-classification]]", "[[accretion-outburst]]", "[[internal-luminosity]]"]
appears_in: ["[[elia-2017]]", "[[elia-2021]]", "[[molinari-2016]]", "[[kuhn-2021]]", "[[mainzer-2014]]", "[[meisner-2023]]", "[[robitaille-2017]]", "[[fischer-2019]]", "[[lu-2024]]", "[[lucas-2024]]", "[[zakri-2022]]"]
---

# Confusion limit

> **Concept hub.** This note exists as a shared anchor — multiple paper summaries link here via their `key_concepts` frontmatter, so reading this gives the cross-paper view of one idea. Keep it short and authoritative. Long discussions go in paper notes, not here.

## Definition

The confusion limit is the regime where overlapping sources within one beam and structured background emission (cirrus, nebulosity), rather than instrumental noise, set how faint a source can be reliably detected, separated and measured. In this vault it covers three related effects:

1. **Beam blending:** two or more sources inside one PSF are catalogued as one (more likely at large distance or low resolution).
2. **Structured background:** bright, variable diffuse emission hides faint compact sources ([[molinari-2016]]: "Hi-GAL DR1 images are cirrus-noise-limited").
3. **Epoch-dependent deblending:** in multi-epoch catalogues, the same blend is decomposed differently at each epoch, producing spurious variability ([[meisner-2023]]).

No single paper in the vault gives a canonical formula; the working definitions are survey-specific.

## Why it matters

Confusion biases counts in both directions. It merges starless and protostellar clumps into one "protostellar" clump, and it hides faint protostars under bright neighbours or nebulosity. In time-domain work it is the leading source of false outbursts and missed ones. Any statement about "a new source appearing" in the Galactic plane must first rule it out.

## Cross-paper view

- **Hi-GAL:** merging at the 18″ 250 µm beam raises the protostellar fraction with distance (0.005 kpc⁻¹; [[elia-2017]]); [[elia-2021]] (§2.1): classification "can be affected by confusion and/or lack of sensitivity at 70 µm"; CuTEx deblends point pairs to ~0.8 beam ([[molinari-2016]]).
- **WISE/NEOWISE (~6″):** confusion lowered NEO detection rates in the Galactic plane ([[mainzer-2014]]); nebulosity shredding and changing deblending between epochs ([[meisner-2023]]); only 8% of SPICY YSOs have reliable 22 µm WISE photometry ([[kuhn-2021]]); 10″ can enclose 2–3 NEOWISE sources ([[lu-2024]]).
- **Outburst searches:** blends and nebulosity in the larger WISE PSF produced all rejected false bursts ([[fischer-2019]]); WISE-based searches missed two Class 0 bursts because of blending with companions ([[zakri-2022]]); blends near the Galactic centre make YSO/giant discrimination ambiguous without spectra ([[lucas-2024]]).
- **SED fitting:** in distant/crowded regions only bulk properties remain meaningful ([[robitaille-2017]] §7.2).

## Where it appears

- Introduced in: [[elia-2017]] (clearest quantified treatment in the vault)
- Appears in: [[elia-2017]], [[elia-2021]], [[molinari-2016]], [[kuhn-2021]], [[mainzer-2014]], [[meisner-2023]], [[robitaille-2017]], [[fischer-2019]], [[lu-2024]], [[lucas-2024]], [[zakri-2022]]
- Related concepts: [[hi-gal-evolutionary-classification]], [[accretion-outburst]], [[internal-luminosity]]

## Open questions

- No paper here quantifies single-exposure W1/W2 completeness and reliability at |b| < 1° ([[mainzer-2014]] open question).
- What is the false-variability rate from epoch-dependent deblending in dense star-forming fields?

## References

1. Elia, D. et al. 2017 — [[elia-2017]]
2. Meisner, A. M. et al. 2023 — [[meisner-2023]]
3. Molinari, S. et al. 2016 — [[molinari-2016]]
