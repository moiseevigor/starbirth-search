---
title: "Radiation Magnetohydrodynamic Simulations of Protostellar Collapse: Protostellar Core Formation"
authors: Kengo Tomida, Kohji Tomisaka, Tomoaki Matsumoto, Yasunori Hori, Satoshi Okuzumi, Masahiro N. Machida, Kazuya Saigo
year: 2013
venue: The Astrophysical Journal 763, 6
url: https://arxiv.org/abs/1206.3567
language: en
domain: astrophysics
status: draft
methodology_type: theoretical
citation_count: 165
citation_count_date: 2026-09-26
key_concepts: ["[[second-collapse]]", "[[first-hydrostatic-core]]", "[[class-0-protostar]]", "[[free-fall-time]]"]
extends: ["[[larson-1969]]", "[[masunaga-inutsuka-2000]]"]
contradicts: []
replicates: []
cites: ["[[larson-1969]]", "[[masunaga-inutsuka-2000]]"]
cited_by: ["[[bhandare-2020]]", "[[young-2023]]"]
quality_notes: "First 3-D RMHD collapse from a cloud core through the second collapse without sink particles. It covers only about 0.4–1.25 yr after protostellar-core formation, so the protostellar-core radius (~10 R⊙) is a transient-expansion value, as the authors themselves stress. It uses grey FLD, not frequency-dependent transfer. No emergent luminosity or SED is computed. Citation count is from Semantic Scholar."
author: moiseevigor
tags:
  - agent/research
  - user/moiseevigor
  - domain/astrophysics
  - topic/protostellar-collapse
  - topic/second-collapse
  - topic/first-hydrostatic-core
  - topic/radiation-hydrodynamics
  - topic/protostellar-outflows
  - paper
  - status/draft
---

# Radiation Magnetohydrodynamic Simulations of Protostellar Collapse: Protostellar Core Formation

## Abstract

We report the first three-dimensional radiation magnetohydrodynamic (RMHD) simulations of protostellar collapse with and without Ohmic dissipation. We take into account many physical processes required to study star formation processes, including a realistic equation of state. We follow the evolution from molecular cloud cores until protostellar cores are formed with sufficiently high resolutions without introducing a sink particle. The physical processes involved in the simulations and adopted numerical methods are described in detail. We can calculate only about one year after the formation of the protostellar cores with our direct three-dimensional RMHD simulations because of the extremely short timescale in the deep interior of the formed protostellar cores, but successfully describe the early phase of star formation processes. The thermal evolution and the structure of the first and second (protostellar) cores are consistent with previous one-dimensional simulations using full radiation transfer, but differ considerably from preceding multi-dimensional studies with the barotropic approximation. The protostellar cores evolve virtually spherically symmetric in the ideal MHD models because of efficient angular momentum transport by magnetic fields, but Ohmic dissipation enables the formation of the circumstellar disks in the vicinity of the protostellar cores as in previous MHD studies with the barotropic approximation. The formed disks are still small (less than 0.35 AU) because we simulate only the earliest evolution. We also confirm that two different types of outflows are naturally launched by magnetic fields from the first cores and protostellar cores in the resistive MHD models.

## TL;DR

This is 3-D nested-grid RMHD with grey FLD, a realistic EOS and Ohmic dissipation, following a 1 M⊙ Bonnor–Ebert core down to the protostellar core. Main numbers:
- **First-core lifetimes are 650–950 yr**, radius 3–5 AU, mass about 3×10⁻² M⊙.
- The **second collapse lasts several years**.
- The protostellar core gains **~0.02 M⊙ within 0.7 yr** (Ṁ ≈ 2.7×10⁻² M⊙ yr⁻¹). It swells transiently to about 10 R⊙ in the spherical model.
- The protostellar core stays buried in the first-core remnant for about the first-core free-fall time, **~5.5 yr**. In the ~1 yr simulated, there is no radiative feedback on the first core.
- Ohmic models form discs smaller than 0.35 AU and drive jets of 6–15 km s⁻¹.

## Problem

Earlier multi-dimensional collapse studies used a barotropic EOS instead of radiation transfer. 3-D RMHD runs had stopped before the second collapse. The question is what realistic 3-D radiation, magnetic fields and non-ideal MHD give for first-core and protostellar-core formation, including their thermal structure, discs and outflows (§1).

## Approach

- **Equations and method (§2–3):**
  - Comoving-frame grey RHD with flux-limited diffusion (FLD).
  - Ideal or Ohmic MHD with the HLLD solver.
  - Self-gravity on a nested grid.
  - Tabulated EOS with H2, H, H⁺, He, He⁺, He²⁺ and e⁻, X = 0.7, Y = 0.28, ortho:para = 3:1.
  - Opacities from Semenov, Seaton and Ferguson. Resistivity from Umebayashi & Nakano, plus thermal ionization of K.
- **Initial core (§4):** an unstable Bonnor–Ebert sphere at T = 10 K, M ≈ 1 M⊙, R ≈ 8800 AU, ρc = 1.2×10⁻¹⁸ g cm⁻³ (A₀ = 0.2). Free-fall time t_ff ≈ 6.08×10⁴ yr.
- **Models (Table 1):**
  - SP: spherical, no rotation, no field.
  - IS and IF: ideal MHD, slow and fast rotation.
  - RS and RF: resistive (Ohmic) MHD, slow and fast rotation.
  - Magnetised models have B₀ = 20 µG and mass-to-flux ratio µ₀ ≈ 3.8.
- **Clock and resolution (§4):**
  - t = 0 is when ρc first exceeds 10⁻³ g cm⁻³.
  - Runs stop at Tc ≈ 10⁵ K.
  - The finest resolution is about 6.6×10⁻⁵ AU, roughly 0.014 R⊙.

## Key result

**Thermal path (§5.1.1).**
- The collapse is isothermal below about 10⁻¹³ g cm⁻³.
- Γ ≈ 5/3 below about 100 K, then ≈ 7/5.
- At Tc ≈ 2000 K, H2 dissociation drops Γ to about 1.1, which starts the second collapse.
- H and He ionization cause no "third collapse".
- All models share essentially the same central thermal evolution (§5.2.1).

**First core (§5.1.2; §5.2.1; Table 2).**
- Forms at t ≈ −650 yr, when ρc ≈ 10⁻¹² g cm⁻³.
- Radius "initially about ~5.4 AU, and it contracts gradually to ~3 AU".
- The dust evaporation front sits at about 1.2 AU at the end of the first-core phase.
- Lifetimes are "about 650, 720, 800, 850 and 950 years in SP, IS, IF, RS and RF, respectively".
- For the free-fall estimate the authors use M_FC ≈ 3×10⁻² M⊙, R_FC ≈ 3 AU and ρ_FC = 1.5×10⁻¹⁰ g cm⁻³ (§5.1.3).

**Second collapse and protostellar core (§5.1.3).**
- The second collapse begins at ρc ≈ 10⁻⁸ g cm⁻³. The free-fall time at that density "is only about 0.67 years". The protostellar core forms "in the short dynamical timescale of several years".
- "Within 0.7 years after the formation of the protostellar core, it acquires MPC ∼ 2 × 10⁻² M⊙ and the averaged accretion rate is very high, 2.7 × 10⁻² M⊙ yr⁻¹."
- The accretion shock is almost adiabatic ("hot accretion"), so the core expands.
- R_PC ≈ 0.047 AU ≈ 10 R⊙ at the end, "about 2.5 times larger" than the ~4 R⊙ of [[masunaga-inutsuka-2000]], and still growing.
- The energy released, GM²/2R ≈ 6.8×10⁴³ erg, matches the H2 dissociation energy of about 5.7×10⁴³ erg.
- The expansion lasts until the first core is accreted, which takes about the first core's mean free-fall time: t_ff,FC ≈ 5.5 yr.

**Protostellar-core summary (Table 2).** Columns: first-core lifetime τ_FC, first-core radius R_FC, outflow distance D_OF, protostellar-core radius R_PC, protostellar-core mass M_PC, jet velocity V_Jet.

| Model | τ_FC (yr) | R_FC (AU) | D_OF (AU) | R_PC (R⊙) | M_PC (M⊙) | V_Jet (km s⁻¹) |
|---|---|---|---|---|---|---|
| SP | 650 | 3 | 0 | 10* | 0.02 | 0 |
| IS | 720 | 3 | 55 | 10* | 0.02 | 0 |
| IF | 800 | 3 | 70 | 17* | 0.02 | 0 |
| RS | 850 | 5 | 60 | 45 | 0.02 | 5 |
| RF | 950 | 5 | 80 | 75 | 0.02 | 15 |
| MI (Masunaga & Inutsuka 2000, snapshot 10 = 19 yr) | 650 | 3 | 0 | 4 | 0.016 | 0 |

Values marked * are "strongly affected by the transient expansion". The runs stop 1.05, 0.44, 0.90 and 1.25 yr after protostellar-core formation in IF, IS, RF and RS respectively (§5.2.3).

**Discs and outflows (§5.2.2–5.2.3).**
- Resistive models build rotationally supported discs within about 1 yr: about 0.35 AU in RF and 0.2 AU in RS.
- Slow, loosely collimated first-core outflows reach 55–80 AU.
- Protostellar-core jets reach about 15 km s⁻¹ in RF and 6 km s⁻¹ in RS, and the jets are kink-unstable.
- Ideal-MHD protostellar cores are essentially non-rotating and launch no protostellar outflow.

**Feedback (§5.2.3, §6).** "radiation feedback from the protostellar core formation on the first core and outer envelope is not significant" within the simulated ~1 yr. The protostellar core is "still deeply obscured in the remnants of the first cores". The expected feedback timescale is the first-core free-fall time, about 5 yr. A 15 km s⁻¹ jet would reach the first-core surface in about 1.5 yr.

## Assumptions

- Grey FLD radiation transfer, with gas and radiation assumed in LTE for opacities.
- Only Ohmic dissipation. Ambipolar diffusion and the Hall effect are omitted (§2).
- Chemical equilibrium EOS with a fixed ortho:para ratio of 3:1. The authors note that the ortho:para choice affects the first and protostellar core properties (§5.1.1).
- Isolated Bonnor–Ebert core with the field aligned to the rotation axis, and parameters chosen so the first cores do not fragment (§4).

## Limitations / scope

- It covers only about 1 yr after protostellar-core formation, because timesteps shrink below 1 minute (§6). It says nothing about luminosity evolution over 10–10⁴ yr.
- No emergent luminosity, SED or synthetic observation is computed.
- The protostellar-core radii are transient values. They should not be used as settled protostellar radii.
- Grey FLD. Frequency-dependent effects are absent.

## Replication evidence

- The first-core thermal evolution and structure agree with the 1-D non-grey RHD of [[masunaga-inutsuka-2000]] and Masunaga et al. (1998), and with the 3-D SPH of Whitehouse & Bate (2006) (§5.1.2).
- The transient expansion agrees with [[larson-1969]] (12 R⊙) and Stahler et al. (1986). [[bhandare-2020]] find an expansion to about 54 R⊙ at about 188 yr in 1-D.
- The absence of radiative feedback differs from RHD without magnetic fields (Bate 2010, 2011; Schönke & Tscharnuter 2011). The authors attribute this to magnetic fields and to the short run duration (§6).

## Why this paper matters

It anchors the first-core lifetime in magnetised 3-D models at **several hundred years**. [[young-2023]] quotes ~200–600 yr for non-ideal MHD. It also shows that the second collapse and protostellar-core formation happen on a **year** timescale, deep inside an opaque first-core remnant. For observational searches, this means:
- Second-core formation itself is a sub-decade internal event.
- Any external signal is delayed by at least the first-core free-fall time (~5 yr), and more for reprocessing through the envelope.
- Jets of 6–15 km s⁻¹ from the protostellar core start almost immediately in resistive models.

## Quotes

1. > "the protostellar cores are still deeply obscured in the remnants of the first cores" — §6
2. > "Therefore this expansion is a highly transient phenomenon." — §5.1.3

## Open questions surfaced

- When, after second-core formation, does the accretion luminosity break out of the first-core remnant (the ~5 yr estimate), and what does the emergent light curve look like?
- Does magnetic braking suppress the radiation-heating-driven first-core outflow seen by Bate (2011)? This needs runs longer than about 15 yr.
- What is the settled protostellar radius after the transient expansion? It is the initial condition for stellar-evolution models.
- Ambipolar diffusion and the Hall effect were not included.

## Related material in vault

- Extends: [[larson-1969]], [[masunaga-inutsuka-2000]]
- Contradicts: none
- Replicates: none
- Concepts introduced/used: [[second-collapse]], [[first-hydrostatic-core]], [[class-0-protostar]], [[free-fall-time]]
- Cites: [[larson-1969]], [[masunaga-inutsuka-2000]]
- Cited by (in this vault): [[bhandare-2020]], [[young-2023]]
