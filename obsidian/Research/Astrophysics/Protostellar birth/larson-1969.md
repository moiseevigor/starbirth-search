---
title: "Numerical Calculations of the Dynamics of a Collapsing Proto-Star"
authors: Richard B. Larson
year: 1969
venue: Monthly Notices of the Royal Astronomical Society 145, 271-295
url: https://ui.adsabs.harvard.edu/abs/1969MNRAS.145..271L/abstract
language: en
domain: astrophysics
status: draft
methodology_type: theoretical
citation_count: 1197
citation_count_date: 2026-09-26
key_concepts: ["[[first-hydrostatic-core]]", "[[second-collapse]]", "[[prestellar-core]]", "[[accretion-luminosity]]", "[[free-fall-time]]"]
extends: []
contradicts: []
replicates: []
cites: []
cited_by: ["[[masunaga-inutsuka-2000]]", "[[tomida-2013]]", "[[bhandare-2020]]", "[[young-2023]]", "[[pineda-2011]]", "[[enoch-2010]]", "[[stutz-2013]]", "[[dunham-2014]]"]
quality_notes: "Foundational paper. Every later first/second-core simulation cites it, and its two-core sequence has never been overturned. The numbers are deliberately coarse (the stated accuracy goal is ~20 per cent, §3). The paper uses radiative diffusion everywhere, including optically thin gas, so the heating of the outer envelope is missed. It computes no SED; that is deferred to a 'forthcoming paper'. Citation count is from Semantic Scholar. Numbers below come from the ADS scan (OCR), checked by eye."
author: moiseevigor
tags:
  - agent/research
  - user/moiseevigor
  - domain/astrophysics
  - topic/protostellar-collapse
  - topic/first-hydrostatic-core
  - topic/second-collapse
  - topic/radiation-hydrodynamics
  - topic/protostar-observational-signatures
  - topic/accretion-luminosity
  - paper
  - status/draft
---

# Numerical Calculations of the Dynamics of a Collapsing Proto-Star

## Abstract

(The paper's "Summary", verbatim.)

Numerical calculations of the dynamics of a spherically symmetric collapsing proto-star of one solar mass have been made for various initial conditions. Calculations have also been made for masses of 2 M⊙ and 5 M⊙. In all cases the collapse is found to be extremely non-homologous and is such that a very small part of the cloud's mass at the centre reaches stellar densities and stops collapsing before most of the cloud has had time to collapse very far. The stellar core thus formed subsequently grows in mass as material falls into it, finally becoming an ordinary star when all of the proto-stellar material has been accreted. During most of this time the stellar core is completely obscured by the dust in the infalling cloud, the absorbed radiation reappearing in the infra-red as thermal emission from the dust grains. The resulting star is almost a conventional Hayashi pre-main sequence model, but it appears rather low on the Hayashi track. For masses much greater than about 2 M⊙ the convective Hayashi phase does not exist at all. It appears that certain properties of T Tauri stars may find explanation in the results of the present calculations.

In an appendix to the paper it is shown that limiting forms may be derived for the density and velocity distributions near the centre of an isothermally collapsing sphere. This may be shown to be possible also for a sphere with a polytropic equation of state. Numerical results are presented for the limiting solution in the isothermal case.

## TL;DR

This is the origin of the "two Larson cores" picture. A 1 M⊙ cloud at 10 K collapses non-homologously. When the centre becomes opaque at about 10⁻¹³ g cm⁻³, a **first core** forms (~10³¹ g, 6×10¹³ cm, 170 K). At about 2000 K H2 dissociation triggers a **second collapse**. That collapse forms a **stellar core** of ~1.5×10⁻³ M⊙, 1.3 R⊙ and 2×10⁴ K. The stellar core swells to 12 R⊙ within about 1 yr. Its luminosity becomes visible, reprocessed into the infrared by dust, and jumps to about **10 L⊙**. It peaks at **30 L⊙** at 8×10⁴ yr. The source stays dust-obscured until it is nearly on the Hayashi track, at about 10⁶ yr.

## Problem

Before 1969, pre-main-sequence models assumed that collapse was homologous or polytropic, and that stars started on the Hayashi track with very large radii and luminosities (~60 R⊙, ~600 L⊙; §4(g)). Larson asked what a direct numerical solution of the hydrodynamic and radiative equations for a collapsing proto-star actually predicts.

## Approach

- Spherically symmetric Eulerian hydrodynamics. There is no rotation, magnetic field or turbulence (§2(a)).
- Radiative diffusion with a constant Rosseland dust opacity of κ = 0.15 cm² g⁻¹ (§2(c)). Dust evaporates at 1400 K. Cox opacities are used above 2000 K, with log-linear interpolation between 1400 and 2000 K.
- Initial state: a uniform-density sphere at rest, T = 10 K, fixed outer boundary. For 1 M⊙, R_c = 1.63×10¹⁷ cm and ρ₀ = 1.10×10⁻¹⁹ g cm⁻³ (§2(f)).
- Shocks are treated with artificial viscosity early on. Later the stellar-core shock uses a "shock fitting" scheme with approximate radiative jump conditions (§3; Appendices A–B). Convection uses a mixing length equal to the scale height and a velocity of 1 km s⁻¹.
- The stated numerical accuracy goal is about 20 per cent (§3).
- Seven cases (§5, Tables I–II):
  - Case 1: fiducial, 1 M⊙.
  - Case 2: T₀ = 100 K.
  - Case 3: 10 K but denser.
  - Case 4: dust opacity ×10⁻².
  - Case 5: no H2.
  - Case 6: 2 M⊙.
  - Case 7: 5 M⊙.
- Appendix C derives the asymptotic isothermal similarity solution, later known as the Larson–Penston flow.

## Key result

**First core (Case 1, §4(b)).** The centre turns opaque at about 10⁻¹³ g cm⁻³ and the collapse becomes adiabatic. "The initial mass and radius of the core are about 10³¹ g and 6×10¹³ cm, respectively, and the central density and temperature at this time are about 2×10⁻¹⁰ g cm⁻³ and 170 °K". The core grows in mass while its radius shrinks through radiative losses. Pulsations have an amplitude of about 10–20 per cent in radius.

**Second collapse (§4(c)).** The trigger is the first core's mass roughly doubling and its radius halving, until "the central temperature reaches a value of about 2000 °K". H2 dissociation then pushes γ below 4/3.

**Second (stellar) core at formation (§4(c); Table I).**

| Case | t (yr) | M (g) | R (cm) | ρc (g cm⁻³) | Tc (K) |
|---|---|---|---|---|---|
| 1 | 3×10⁵ | 3×10³⁰ | 9×10¹⁰ | 2×10⁻² | 2.2×10⁴ |
| 2 | 9×10³ | 6×10³⁰ | 1.5×10¹¹ | 9×10⁻³ | 2.3×10⁴ |
| 7 (5 M⊙) | 5×10⁴ | 5×10³⁰ | 1.4×10¹¹ | 9×10⁻³ | x.3×10⁴ (first digit illegible in the scan) |

The Case 1 text gives "3×10³⁰ g (1.5×10⁻³ M⊙) and 9×10¹⁰ cm (1.3 R⊙)". Table I's t column is not defined in the OCR'd text. Read it as the time at which the stellar core forms.

**Early expansion, hidden phase (§4(d)).** The core radius grows roughly in proportion to its mass. It reaches a maximum of "12 R⊙ when the mass reaches 1.0×10⁻² M⊙", "about 1 yr after the formation of the stellar core". All shock luminosity is absorbed by the surrounding opaque material. The dashed track in Fig. 3 is "not an observationally significant quantity".

**Luminosity turn-on (§4(e)).** The trigger is the density outside the shock dropping to about 10⁻⁸ g cm⁻³. After that, "the luminosity of the proto-stellar object then increases rapidly from a very small value to a value of about 10 L⊙". The solid track in Fig. 3 starts where about 90 per cent of the core luminosity escapes the whole cloud. A Hayashi-like contraction follows, lasting about 10–100 yr after core formation. By the end of it the core mass is about 1.3×10⁻² M⊙ and all traces of the first core are gone.

**Observability.** "the infalling cloud remains optically thick until practically all of the material has fallen into the core". Energy therefore emerges as thermal infrared dust emission (§4(e)). The SED is deferred to a later paper.

**Main accretion (§4(f)–(g)).** The shock satisfies σTe⁴ = ½ρ₂|u₂|³ (eq. 9). The maximum surface temperature and luminosity are "about 8300 °K and 30 L⊙", reached "about 8×10⁴ years after the formation of the core, at which time the core mass is 0.56 M⊙". Luminosity then declines between about 10⁵ and 10⁶ yr.

**End state (§4(g); Table II).** The star appears on the Hayashi track at "about 2.0 R⊙, 4400 °K, and 1.3 L⊙" and "about 1.1×10⁶ years" after core formation. That is about 5 times the initial free-fall time. For 5 M⊙ (Case 7) there is no convective Hayashi phase. The surface layers become radiative 2.3×10⁴ yr after core formation, at M = 3.7 M⊙ (§5).

**Similarity solution (Appendix C, eq. C8).** For x ≪ 1: ξ = x/3, η = 1.667. For x ≫ 1: ξ = 3.28 and η = 8.86 x⁻², i.e. ρ ∝ r⁻² and the infall velocity tends to 3.28 times the sound speed. The central collapse time is 1.58 times the free-fall time (eq. C10).

## Assumptions

- Spherical symmetry. No rotation, magnetic fields or turbulence (§2(a)). The author concedes that rotation is "almost certainly important".
- Radiative diffusion is applied even where the gas is optically thin, which forces optically thin gas to 10 K (§3).
- Constant grey dust opacity. Gaustad composition, with hydrogen fully molecular at the start.
- Fixed outer boundary and a uniform initial density starting from rest (§2(e)–(f)).
- Convective velocity is a free parameter (1 km s⁻¹).

## Limitations / scope

- Coarse resolution with about 20 per cent accuracy (§3).
- No emergent spectrum is computed, so there is no SED or wavelength-dependent prediction. The only observational statements are total luminosity and "obscured, re-emitted in IR".
- The luminosity turn-on is reported only through the start of the solid Fig. 3 track. There is no light curve in physical units beyond the quoted 10 L⊙ and 30 L⊙ points.
- The heating of the envelope by the central source is missed because of the diffusion treatment (see [[young-2023]] §2.1).

## Replication evidence

Yes, qualitatively. The two-core sequence, the ~2000 K trigger, the initial second-core mass of order 10⁻³ M⊙ with a radius of a few R⊙, and the ρ ∝ r⁻² envelope have all been reproduced:
- 1-D frequency-dependent RHD: [[masunaga-inutsuka-2000]].
- 3-D RMHD: [[tomida-2013]].
- 1-D/2-D RHD over 0.5–100 M⊙: [[bhandare-2020]].
- Review: [[young-2023]].

The transient expansion of the young stellar core, to 12 R⊙ here, is also seen in [[tomida-2013]] (~10 R⊙) and [[bhandare-2020]].

## Why this paper matters

It defines the vocabulary used by every later paper on protostellar birth: first core, second collapse, stellar core, and the Larson–Penston flow. For a search for newborn protostars, the most useful points are these:
- The second collapse is effectively invisible when it happens. The stellar core's light is fully absorbed until the first-core remnant is accreted, of order 1–10 yr later.
- The emergent luminosity then rises from "very small" to about 10 L⊙ and grows to tens of L⊙ over 10⁴–10⁵ yr.
- The output always emerges as reprocessed dust emission.

## Quotes

1. > "the infalling cloud remains optically thick until practically all of the material has fallen into the core" — §4(e)
2. > "increases rapidly from a very small value to a value of about 10 L⊙" — §4(e)

## Open questions surfaced

- What is the emergent SED during and right after the luminosity turn-on? Larson deferred it; [[masunaga-inutsuka-2000]] computed it.
- How long does it take in physical time, not only in density, for the post-shock density to fall to about 10⁻⁸ g cm⁻³ so that the stellar-core luminosity escapes?
- How do rotation and magnetic fields change the sequence? Addressed by [[tomida-2013]].

## Related material in vault

- Extends: none
- Contradicts: none
- Replicates: none
- Concepts introduced/used: [[first-hydrostatic-core]], [[second-collapse]], [[prestellar-core]], [[accretion-luminosity]], [[free-fall-time]]
- Cites: none in vault
- Cited by (in this vault): [[masunaga-inutsuka-2000]], [[tomida-2013]], [[bhandare-2020]], [[young-2023]], [[pineda-2011]], [[enoch-2010]], [[stutz-2013]], [[dunham-2014]]
