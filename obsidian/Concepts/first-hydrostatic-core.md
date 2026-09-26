---
title: First hydrostatic core
author: moiseevigor
language: en
domain: astrophysics
status: draft
tags:
  - agent/research
  - user/moiseevigor
  - domain/astrophysics
  - topic/first-hydrostatic-core
  - topic/protostellar-collapse
  - topic/protostar-observational-signatures
  - concept
  - status/draft
introduced_in: ["[[larson-1969]]"]
related_concepts: ["[[second-collapse]]", "[[prestellar-core]]", "[[vello]]", "[[internal-luminosity]]", "[[statistical-lifetime]]", "[[free-fall-time]]"]
appears_in: ["[[larson-1969]]", "[[masunaga-inutsuka-2000]]", "[[tomida-2013]]", "[[bhandare-2020]]", "[[young-2023]]", "[[dunham-2014]]", "[[enoch-2010]]", "[[pineda-2011]]", "[[stutz-2013]]"]
---

# First hydrostatic core

> **Concept hub.** This note exists as a shared anchor — multiple paper summaries link here via their `key_concepts` frontmatter, so reading this gives the cross-paper view of one idea. Keep it short and authoritative. Long discussions go in paper notes, not here.

## Definition

The first hydrostatic core (FHSC, "first core", first Larson core) is the quasi-hydrostatic, optically thick, molecular-hydrogen object that forms when the centre of a collapsing dense core becomes opaque (ρc ≈ 10⁻¹³–10⁻¹² g cm⁻³) and the collapse turns adiabatic. It grows by accretion until its central temperature reaches ~2000 K, when H2 dissociation triggers the [[second-collapse]].

Larson's original numbers ([[larson-1969]] §4(b)): "The initial mass and radius of the core are about 10³¹ g and 6×10¹³ cm, respectively, and the central density and temperature at this time are about 2×10⁻¹⁰ g cm⁻³ and 170 °K".

## Why it matters

The FHSC is the first object in the collapse sequence and the earliest possible "birth" signature. Its predicted observables (a cold SED with nothing below ~20–50 µm, internal luminosity ≲0.1 L⊙, very slow outflows) overlap with those of the faintest protostars ([[vello]]), so FHSC searches double as tests of how young the youngest observed protostars are. Expected FHSC counts in a cloud scale as N_Class0 × τ_FHSC / τ_Class0 ([[pineda-2011]] Eq. 17), so the FHSC lifetime directly links theory to survey statistics ([[statistical-lifetime]]).

## Cross-paper view

| Property | Values (source) |
|---|---|
| Mass | ~10³¹ g ≈ 0.005 M⊙ at formation ([[larson-1969]]); ~3×10⁻² M⊙ ([[tomida-2013]]); max 0.04–0.05 M⊙, 0.01–0.1 with rotation ([[dunham-2014]]); 0.005–0.2 M⊙ across models ([[young-2023]]) |
| Radius | ~4 AU ([[larson-1969]]); 3–5 AU ([[tomida-2013]]); ~5 AU, ≳10–20 AU with rotation ([[dunham-2014]]); 4–7 AU in 1-D, up to 50–100 AU as a rotating disc ([[young-2023]]) |
| Lifetime | 650–950 yr (3-D RMHD, [[tomida-2013]]); ~10³ yr ([[pineda-2011]], up to 10⁴ yr); 10³–3×10⁴ yr ([[enoch-2010]]); 0.5–50 kyr ([[dunham-2014]]); ~100 yr ideal MHD to >10⁴ yr for 0.1 M⊙ cores ([[young-2023]]); ~10⁴ yr for a 1 M⊙, 3000 au core (Bhandare et al. 2018, quoted in [[bhandare-2020]]) |
| Luminosity | 10⁻⁴–10⁻¹ L⊙ ([[dunham-2014]]); 0.003–0.1 L⊙, likely ≳0.01 L⊙ ([[young-2023]]) |
| SED / outflow | no emission below ~20–50 µm ([[dunham-2014]]); SED peak 100–200 µm, outflows "most likely < 3" km s⁻¹ ([[young-2023]]); slow first-core outflows reaching 55–80 AU ([[tomida-2013]]) |
| Expected numbers | 1 per 18–540 protostars ([[enoch-2010]]); ≤0.2 in Perseus ([[pineda-2011]]); 0.07–7 in Perseus ([[dunham-2014]]); 0.002–0.02 of Class 0, "at most 1 or 2" nearby ([[young-2023]]) |
| Candidates | Per-Bolo 58 ([[enoch-2010]]); L1451-mm ([[pineda-2011]]); 9 candidates ([[dunham-2014]]); 13 listed, 8 remain ([[young-2023]]); PBRS are *not* FHSCs ([[stutz-2013]]) |

[[masunaga-inutsuka-2000]] reproduces the first-core mass and radius of its Paper I and shows the SED does not change during the first-collapse stage.

## Where it appears

- Introduced in: [[larson-1969]]
- Appears in: [[larson-1969]], [[masunaga-inutsuka-2000]], [[tomida-2013]], [[bhandare-2020]], [[young-2023]], [[dunham-2014]], [[enoch-2010]], [[pineda-2011]], [[stutz-2013]]
- Related concepts: [[second-collapse]], [[prestellar-core]], [[vello]], [[internal-luminosity]], [[statistical-lifetime]], [[free-fall-time]]

## Open questions

- The lifetime spans more than two orders of magnitude across physics choices (ideal vs non-ideal MHD, rotation, core mass). Expected counts inherit this spread, so a single candidate count cannot yet test the models.
- No continuum-only discriminant separates an FHSC from an extreme VeLLO ([[enoch-2010]]). Outflow speed and warm-gas chemistry are the proposed discriminants.

## References

1. Larson, R. B. 1969, MNRAS 145, 271 — [[larson-1969]]
2. Young, A. K. 2023, review of first- and second-core properties — [[young-2023]]
3. Dunham, M. M. et al. 2014, PPVI — [[dunham-2014]]
