---
title: "Insights into the first and second hydrostatic core stages from numerical simulations"
authors: Alison K. Young
year: 2023
venue: Frontiers in Astronomy and Space Sciences 10, 1288730
url: https://arxiv.org/abs/2312.03039
language: en
domain: astrophysics
status: draft
methodology_type: review
citation_count: 3
citation_count_date: 2026-09-26
key_concepts: ["[[first-hydrostatic-core]]", "[[second-collapse]]", "[[class-0-protostar]]", "[[prestellar-core]]", "[[statistical-lifetime]]", "[[accretion-luminosity]]"]
extends: []
contradicts: []
replicates: []
cites: ["[[larson-1969]]", "[[masunaga-inutsuka-2000]]", "[[tomida-2013]]", "[[bhandare-2020]]", "[[pineda-2011]]", "[[stutz-2013]]", "[[konyves-2015]]", "[[evans-2009]]"]
cited_by: []
quality_notes: "A concise, single-author review, and the most up-to-date compilation of first-core and second-core predictions and of first-core candidates (13 listed, 8 remaining). Where it summarises other papers, the primary sources in this folder are authoritative. Its SED statements lean on the author's own synthetic observations (Young et al. 2018, 2019). Semantic Scholar's count (3) is probably an undercount; treat it as a lower bound."
author: moiseevigor
tags:
  - agent/research
  - user/moiseevigor
  - domain/astrophysics
  - topic/first-hydrostatic-core
  - topic/second-collapse
  - topic/protostellar-collapse
  - topic/protostar-observational-signatures
  - topic/class-0-protostars
  - topic/evolutionary-lifetimes
  - topic/embedded-low-luminosity-protostars
  - topic/protostellar-outflows
  - topic/accretion-luminosity
  - paper
  - status/draft
---

# Insights into the first and second hydrostatic core stages from numerical simulations

## Abstract

The theory of how low mass stars form from the collapse of a dense molecular cloud core has been well-established for decades. Thanks to significant progress in computing and numerical modelling, more physical models have been developed and a wider parameter space explored to understand the early stages of star formation more fully. In this review, I describe the expected physical properties of the first and second core stages and how the inclusion of different physics affects those predicted characteristics. I provide an overview of chemical models and synthetic observations, looking towards the positive identification of the first core in nature, which remains elusive. However, there are a few likely candidate first cores, which are listed, and I briefly discuss the recent progress in characterising the youngest protostellar sources. Chemistry will be instrumental in the firm identification of the first core so we require robust theoretical predictions of the chemical evolution of protostellar cores, especially of the first and second core outflows. Looking ahead, simulations can shed light on how the protostellar collapse phase shapes the evolution of the protostellar disc. Simulations of dust evolution during protostellar core collapse show there is significant enhancement in grain size and abundance towards the centre of the core. Chemical models show that the warm, dense conditions of the first core drive chemical evolution. There is a wide scope for further study of the role that the first and second core stages play in determining the structure and composition of the protostellar disc and envelope and, of course, the eventual influence on the formation of planets.

## TL;DR

This review collects predicted first- and second-core properties across simulation types.
- **First core:** mass 0.005–0.2 M⊙, radius about 4–7 AU in 1-D and up to 50–100 AU as a rotating disc. Luminosity is 0.003–0.1 L⊙, likely ≳0.01 L⊙. The SED peaks at 100–200 µm. Lifetime is about 100 yr (ideal MHD), 200–600 yr (non-ideal MHD), up to a few thousand yr (rotating hydro), or >10⁴ yr for 0.1 M⊙ cores.
- **Second core:** about 0.0015 M⊙ and 1–4 R⊙ at birth. After birth the luminosity rises quickly to "a few tens L⊙", **but there is no immediate SED change** because the collapse happens inside the first core.
- **Numbers:** first cores should be 0.002–0.02 of Class 0 sources, i.e. at most 1–2 in nearby regions. Only 8 of 13 literature candidates remain.

## Problem

What do current numerical models predict for the physical and observable properties of the first and second hydrostatic cores? How does that depend on the physics included (radiative transfer, dimensionality, magnetic fields, chemistry)? Why has no first core been confirmed yet?

## Approach

A literature review of RHD, RMHD, chemical and synthetic-observation models, and ALMA/Herschel observations of candidates:
- §2: developments since 1969.
- §3: predicted properties.
- §4: predicted observables.
- §5: observed candidates and the youngest protostars.
- §6: outlook.

## Key result

**First core: masses and radii (§3.1.1–3.1.2; Table 1).**
- Initial first-core mass is 0.01 M⊙ ([[larson-1969]]).
- 1-D frequency-dependent models give M_fc ≈ 0.04 M⊙ and r_fc ≈ 7 au for 0.2 ≤ M_cc ≤ 8 M⊙ (Vaytet & Haugbølle 2017).
- In RHD, rotation raises the first-core mass from about 0.005 M⊙ (β = 0) to about 0.22 M⊙ (β = 0.01) (Bate 2011). With magnetic fields it is 0.02–0.05 M⊙.
- Rotating first cores reach 10–20 au, compared with about 5 au for spherical ones.
- There is no real first-core phase for M_cc ≥ 40 M⊙ (Bhandare et al. 2018).

**Second core (§3.1.1).**
- "The initial mass of the second core is ≈ 0.0015 M⊙ (Larson, 1969)".
- The initial radius is 1–4 R⊙, with rapid growth and transient expansions ([[tomida-2013]]).
- [[tomida-2013]]'s 0.02 M⊙ is probably high because part of the first core had already been accreted when it was measured.
- [[bhandare-2020]]: 0.03 M⊙ for a 0.5 M⊙ cloud and >10 M⊙ for clouds >80 M⊙ after ≥100 yr.

**First-core lifetime (§3.1.4; Table 1).**

| Model type | Maximum lifetime |
|---|---|
| Ideal MHD | ~100 yr |
| Non-ideal MHD | 200–600 yr ([[tomida-2013]] et al.) |
| Rotating hydro | up to a few 1000 yr |
| Radiative-transfer hydro vs barotropic | up to 3000 yr vs 1500 yr (Bate 2011) |

- Lifetime scales as t_fc ∝ M⁻⁰·⁵ for M_cc < 10 M⊙ and as ∝ M⁻²·⁵ above that (Bhandare et al. 2018).
- Very-low-mass (0.1 M⊙) cores give first cores that may last "> 10⁴ years" and may be brighter in the mid-IR.

**Outflows (§3.1.3).**
- First-core outflows are ≲ a few km s⁻¹, "most likely < 3", with an extent of at most a few hundred au.
- Second-core outflows range from 1.5 to 30–40 km s⁻¹, and up to about 100 km s⁻¹ within 2000 yr.
- [[tomida-2013]] get 6 and 15 km s⁻¹ for slow and fast rotation.

**Luminosity and SED (§4.1).**
- First-core luminosity: "0.003 ≲ Lfc ≲ 0.1 L⊙". It is likely ≳0.01 L⊙ once heating at second-core formation is included.
- After second-core formation: "The emergent luminosity is predicted to be a few tens L⊙, increasing quickly as the accretion rate increases after second core formation" ([[masunaga-inutsuka-2000]]; Jones & Bate 2018).
- The first-core SED peaks at 100–200 µm. The peak shifts gradually to shorter wavelengths.
- The 160 µm flux "rises quickly after first core formation" (Young et al. 2018).
- The envelope is optically thick below 850 µm. Emission at 20–100 µm is significant only for face-on, flattened, rotating cores.
- 24 µm is probably too faint except for the lowest-mass cores. 70 µm could be detectable with Herschel for evolved, fast-rotating, pole-on cores.
- "There is no immediate change in the SED after the formation of the second core despite the rapid increase in the central temperature".
- Unattenuated external heating erases the SED evolution: the "catch-22".

**Chemistry (§4.3).**
- About 200 yr after second-core formation, the CO sublimation radius moves from about 60 au to about 150 au.
- CS becomes detectable within "a couple of hundred years" of second-core formation (Young 2019).
- Redshifted CO absorption at 0.5–1.5 km s⁻¹ is a first-core signature.

**Candidates and statistics (§5.1, §6.2; Table 2).**
- 13 candidates are listed and 8 remain. [[pineda-2011]]'s L1451-mm is still listed, and HOPS 404 is from the [[stutz-2013]] PBRS sample.
- The working definition of a candidate is L < 0.1 L⊙, faint or undetected below 70 µm, and no outflow faster than 10 km s⁻¹. The author argues the outflow limit should be tightened.
- Class 0 lifetime is taken as a few ×10⁴ yr to 1–3×10⁵ yr ([[evans-2009]]; Dunham et al. 2015). First cores should therefore be 0.002–0.02 of Class 0 sources. With about 10³ Class 0 sources, that means "at most 1 or 2 first cores in total in the nearby star forming regions".

## Assumptions

It is a review, so it inherits the assumptions of the cited models, mostly isolated cores. The first-core fraction estimate assumes a steady state and that lifetimes scale with number counts, i.e. a [[statistical-lifetime]] argument.

## Limitations / scope

- It gives no new calculations.
- Second-core-phase observables are covered briefly. The post-birth luminosity rise is stated qualitatively ("a few tens L⊙", "increasing quickly") without a timescale.
- The SED statements rest largely on Young et al. (2018), which uses 1 M⊙ models at particular inclinations.
- High-mass first and second cores are treated only through [[bhandare-2020]]-type monolithic collapse, which the author considers unrealistic.

## Replication evidence

Not applicable (review). It consolidates agreement across 1-D and 3-D codes on the qualitative sequence and on initial second-core masses and radii. It also records the model disagreements on first-core lifetime (factor of about 10–30 across physics choices) and on outflow speeds.

## Why this paper matters

It is the most recent single place that ties the physics to what a survey could see. For a search for protostellar birth, the decisive statements are:
1. Second-core formation produces **no immediate SED change**, because the event is buried inside the first core and the inner envelope sets the SED.
2. The emergent luminosity then climbs to **tens of L⊙**.
3. First cores are so short-lived that only about 1–2 should exist in all nearby star-forming regions.
4. Near- and mid-IR (<70 µm) is the wrong place to look for first cores. The far-IR and submm (100–200 µm SED peak, and the rise at 160 µm) and molecular-line chemistry are the diagnostics.

## Quotes

1. > "There is no immediate change in the SED after the formation of the second core" — §4.1
2. > "we would expect to find at most 1 or 2 first cores" — §6.2

## Open questions surfaced

- How fast does the emergent far-IR luminosity rise after second-core formation? The review gives no timescale.
- Chemical models of the first and second core stages that include complex organic molecules, and grain growth beyond 100 µm (§6.1).
- Do large grains grown in the first core survive second-core formation, and where do they end up?
- Deep sub-100 au ALMA observations of the eight remaining candidates, plus interferometric searches for outflows in Aqu-MM1 and K242.
- The role of JWST/MIRI in detecting face-on oblate first cores, and the loss of a far-IR capability after the SPICA cancellation.

## Related material in vault

- Extends: none (review)
- Contradicts: none
- Replicates: none
- Concepts introduced/used: [[first-hydrostatic-core]], [[second-collapse]], [[class-0-protostar]], [[prestellar-core]], [[statistical-lifetime]], [[accretion-luminosity]]
- Cites: [[larson-1969]], [[masunaga-inutsuka-2000]], [[tomida-2013]], [[bhandare-2020]], [[pineda-2011]], [[stutz-2013]], [[konyves-2015]], [[evans-2009]]
- Cited by (in this vault): none known
