---
title: "Birth of convective low-mass to high-mass second Larson cores"
authors: Asmita Bhandare, Rolf Kuiper, Thomas Henning, Christian Fendt, Mario Flock, Gabriel-Dominique Marleau
year: 2020
venue: Astronomy & Astrophysics 638, A86
url: https://arxiv.org/abs/2004.12419
language: en
domain: astrophysics
status: draft
methodology_type: theoretical
citation_count: 12
citation_count_date: 2026-09-26
key_concepts: ["[[second-collapse]]", "[[first-hydrostatic-core]]", "[[prestellar-core]]", "[[accretion-luminosity]]"]
extends: ["[[larson-1969]]", "[[masunaga-inutsuka-2000]]", "[[tomida-2013]]"]
contradicts: []
replicates: []
cites: ["[[larson-1969]]", "[[masunaga-inutsuka-2000]]", "[[tomida-2013]]", "[[dunham-2014]]"]
cited_by: ["[[young-2023]]"]
quality_notes: "Semantic Scholar's count (12) is probably an undercount for an A&A paper of this profile; treat it as a lower bound. Table 2 lists Msc = 8.31e-03 M⊙ for the 12 M⊙ core, which breaks the monotonic trend (5.73e-01 at 10 M⊙, 1.17e+00 at 14 M⊙) and is probably a typo for about 8.31e-01. §5 says Masunaga & Inutsuka (2000) found 0.73 M⊙ 'a few years' after second-core formation. In that paper 0.73 M⊙ is the end-of-calculation mass. Grey FLD, ideal-gas EOS without electron degeneracy, and no rotation or magnetic fields."
author: moiseevigor
tags:
  - agent/research
  - user/moiseevigor
  - domain/astrophysics
  - topic/protostellar-collapse
  - topic/second-collapse
  - topic/first-hydrostatic-core
  - topic/radiation-hydrodynamics
  - topic/prestellar-cores
  - topic/accretion-luminosity
  - paper
  - status/draft
---

# Birth of convective low-mass to high-mass second Larson cores

## Abstract

Context. Stars form as an end product of the gravitational collapse of cold, dense gas in magnetized molecular clouds. This fundamentally multi-scale scenario occurs via the formation of two quasi-hydrostatic Larson cores and involves complex physical processes, which require a robust, self-consistent numerical treatment.
Aims. The primary aim of this study is to understand the formation and evolution of the second hydrostatic Larson core and the dependence of its properties on the initial cloud core mass.
Methods. We used the PLUTO code to perform high resolution, one- and two-dimensional radiation hydrodynamic (RHD) core collapse simulations. We include self-gravity and use a grey flux-limited diffusion approximation for the radiative transfer. Additionally, we use for the gas equation of state density- and temperature-dependent thermodynamic quantities (heat capacity, mean molecular weight, etc.) to account for the effects such as dissociation of molecular hydrogen, ionisation of atomic hydrogen and helium, and molecular vibrations and rotations. Properties of the second core are investigated using one-dimensional studies spanning a wide range of initial cloud core masses from 0.5 M⊙ to 100 M⊙. Furthermore, we expand to two-dimensional (2D) collapse simulations for a selected few cases of 1 M⊙, 5 M⊙, 10 M⊙, and 20 M⊙. We follow the evolution of the second core for ≥ 100 years after its formation, for each of these non-rotating cases.
Results. Our results indicate a dependence of several second core properties on the initial cloud core mass. Molecular cloud cores with a higher initial mass collapse faster to form bigger and more massive second cores. The high-mass second cores can accrete at a much faster rate of ≈ 10⁻² M⊙ yr⁻¹ compared to the low-mass second cores, which have accretion rates as low as 10⁻⁵ M⊙ yr⁻¹. For the first time, owing to a resolution that has not been achieved before, our 2D non-rotating collapse studies indicate that convection is generated in the outer layers of the second core, which is formed due to the gravitational collapse of a 1 M⊙ cloud core. Additionally, we find large-scale oscillations of the second accretion shock front triggered by the standing accretion shock instability (SASI), which has not been seen before in early evolutionary stages of stars. We predict that the physics within the second core would not be significantly influenced by the effects of magnetic fields or an initial cloud rotation.
Conclusions. In our 2D RHD simulations, we find convection being driven from the accretion shock towards the interior of the second Larson core. This supports an interesting possibility that dynamo-driven magnetic fields may be generated during the very early phases of low-mass star formation.

## TL;DR

This is a 1-D and 2-D grey-FLD RHD survey of second-core formation. It covers **0.5–100 M⊙ cloud cores**, each 3000 au across at 10 K, and follows each for about 100–500 yr after the second core forms.
- More massive cloud cores collapse faster and form bigger, more massive second cores.
- Initial second-core accretion is **~10⁻² M⊙ yr⁻¹**, falling to a few ×10⁻⁵ M⊙ yr⁻¹ at the low-mass end.
- For a 1 M⊙ core, about 188 yr after second-core formation: R_sc ≈ 54 R⊙ (0.253 au), M_sc = 0.044 M⊙, **L_acc ≈ 1.65 L⊙**.
- In 2-D the young 1 M⊙ second core becomes convective in its outer layers.
- The second cores are optically thick, "extremely difficult to detect".

## Problem

How do the properties of the second (stellar) Larson core depend on the initial cloud-core mass, from low-mass to high-mass star formation? What does its internal structure look like when resolved in multi-D?

## Approach

- PLUTO grid code with grey FLD radiation transport and self-gravity (§2).
- EOS from D'Angelo & Bodenheimer (2013). It includes H2 dissociation, H and He ionisation, and H2 rotation and vibration, but not electron degeneracy (§3.1).
- Dust opacities from Ossenkopf & Henning; gas opacities from Malygin et al.
- Dust and gas temperatures are perfectly coupled (§2.1).
- Initial state: a Bonnor–Ebert-like profile (ξ = 6.45) with R_cloud = 3000 au and T₀ = 10 K. The cloud is gravity-dominated because T₀ is below T_BE (Table 1). For 1 M⊙, ρc = 2.33×10⁻¹⁷ g cm⁻³.
- 1-D runs cover 17 masses from 0.5 to 100 M⊙ with 4416 cells from 10⁻⁴ to 3000 au. The smallest cell is 3.09×10⁻⁵ au (§2.2).
- 2-D axisymmetric runs cover 1, 5, 10 and 20 M⊙. The smallest cell is 8.77×10⁻⁵ au, with no rotation (§2.3).
- The second-core radius is defined by the accretion-shock position. Second-core onset (t = 0) is when a prominent second accretion shock appears (§3.2).

## Key result

**Second-core properties at the final 1-D snapshot (Table 2).** The snapshot is taken when ρc ≈ 0.5–0.8 g cm⁻³. t_final is counted from the start of the simulation. T_sc is the second-core temperature listed in the table.

| M₀ (M⊙) | t_final (yr) | R_sc (au) | M_sc (M⊙) | T_sc (K) | Ṁ_sc (M⊙ yr⁻¹) | L_acc (L⊙) |
|---|---|---|---|---|---|---|
| 0.5 | 38039.76 | 0.203 | 3.36e-02 | 2.07e+03 | 3.23e-05 | 7.78e-01 |
| 1.0 | 18635.00 | 0.253 | 4.40e-02 | 1.79e+03 | 6.52e-05 | 1.65e+00 |
| 2.0 | 11543.76 | 0.329 | 6.58e-02 | 1.67e+03 | 1.52e-04 | 4.43e+00 |
| 5.0 | 6860.80 | 0.405 | 1.65e-01 | 1.54e+03 | 5.53e-04 | 3.27e+01 |
| 10.0 | 4909.00 | 0.876 | 5.73e-01 | 1.56e+03 | 1.71e-03 | 1.64e+02 |
| 20.0 | 3610.66 | 1.914 | 2.01e+00 | 8.99e+03 | 5.17e-03 | 7.93e+02 |
| 100.0 | 1655.55 | 5.206 | 1.31e+01 | 1.16e+04 | 5.78e-02 | 2.12e+04 |

The accretion luminosity is L_acc = G M_sc Ṁ_sc / R_sc, with Ṁ_sc = 4π R_sc² ρ_sc u_sc (§3.2).

**Accretion rate (§3.2).** "Initially, material from the first core accretes onto the second core at a much faster rate of ≈ 10⁻² M⊙ yr⁻¹. The accretion rate slows down over time and can decrease to roughly a few times 10⁻⁵ M⊙ yr⁻¹ in the low-mass end."

**Radius evolution (§3.2, Fig. 3).** The second core first expands and then contracts. The switch is set by the ratio of Kelvin–Helmholtz time to accretion time: a large ratio means expansion.

**1 M⊙ comparison (§5).**
- At ρc = 9.6×10⁻² g cm⁻³: R_sc ≈ 4 R⊙, M = 5.12×10⁻³ M⊙.
- 188.2 yr after second-core formation, at ρc = 0.85 g cm⁻³: R_sc ≈ 54 R⊙, M = 4.40×10⁻² M⊙.
- Vaytet & Haugbølle (2017) report ≈1 R⊙ and 2.62×10⁻³ M⊙ at a similar central density.

**Shock character (§3.1).** The second accretion shock is subcritical: "the accretion energy is transferred onto the second core and not radiated away".

**Observability (§3.1).** "The radial profiles of the optical depth indicates that the second cores are optically thick, which makes it extremely difficult to detect them observationally".

**2-D, 1 M⊙ (§4.1).**
- Followed for about 312 yr after second-core formation. Tc ≈ 40 000 K.
- An entropy inversion below the accretion shock gives ∇_act > ∇_ad. Convection grows inward from the shock. The energy flux is still dominated by radiation.
- The 5, 10 and 20 M⊙ runs show turbulent patterns but no clear convective criterion. They are shown at 128, 91.4 and 86.4 yr respectively (§4.2).
- The standing accretion shock instability (SASI) may drive large-scale shock oscillations, but convection seems to be the main source of turbulence (§4.3).

**First core (from the Introduction, citing Bhandare et al. 2018).** "The process of formation and evolution of the first core lasts for about 10⁴ years, for the collapse of a 3000 au cloud core in marginal hydrostatic equilibrium, with an initial mass of 1 M⊙ and 10 K temperature".

## Assumptions

- No rotation or magnetic fields. The authors argue these would not change the second-core internals much (§4.4).
- Grey FLD with gas, dust and radiation temperatures equal.
- Ideal-gas EOS without electron degeneracy. Because of this, the authors attribute the off-centre temperature peak to changing thermal ionisation, unlike [[masunaga-inutsuka-2000]] (§3.1).
- Isolated 3000 au cloud at 10 K for all masses. More massive cores are therefore increasingly unstable, since M_BE/M₀ falls from 1.05 to 0.0176 at 30 M⊙ (Table 1).
- 2-D axisymmetry with midplane symmetry. 3-D at the same resolution is not feasible (§4.4).

## Limitations / scope

- No SED or emergent-luminosity calculation. L_acc is the accretion luminosity at the second-core shock, not what an observer sees through the first-core remnant and envelope.
- Runs cover about 100–500 yr after second-core formation, far short of the Class 0 phase.
- High-mass cases assume monolithic collapse of a single isolated 3000 au core. [[young-2023]] notes this is unlikely in nature.
- Table 2 anomaly: see quality_notes.

## Replication evidence

Partial.
- The 1 M⊙ numbers are compared directly with [[masunaga-inutsuka-2000]], [[tomida-2013]] and Vaytet & Haugbølle (2017) (§5). Second-core radii differ by factors of several across codes and times: ≈1 R⊙ (VH17), ≈4 R⊙ (here, early; MI00), ≈10 R⊙ (Tomida, at <1 yr) and ≈54 R⊙ (here, 188 yr). The authors attribute this to EOS, opacity and grid differences, and to comparing different evolutionary times.
- The convective second core has not been independently confirmed in the papers in this vault.

## Why this paper matters

It extends the second-core picture across the stellar mass range and shows how different a newborn second core can look depending on its birth environment:
- Accretion rates span 10⁻⁵ to 10⁻² M⊙ yr⁻¹.
- Accretion luminosities range from about 1 L⊙ at 0.5–1 M⊙ to about 2×10⁴ L⊙ at 100 M⊙, a few hundred years after birth.
- Time from the start of collapse ranges from about 1.7×10³ to 3.8×10⁴ yr.

For low-mass cores, the L_acc of about 1–2 L⊙ at about 200 yr after birth is well below the ~25 L⊙ peak of [[masunaga-inutsuka-2000]]. That peak is reached much later and under different initial conditions. So the size of the luminosity jump right after birth depends on the model.

## Quotes

1. > "makes it extremely difficult to detect them observationally and trace this evolutionary stage" — §3.1
2. > "Molecular cloud cores with a higher initial mass collapse faster" — Abstract

## Open questions surfaced

- How much of L_acc escapes the first-core remnant and envelope, and when? That would give the observable light curve over the first 10–10³ yr.
- Does convection, and a possible early dynamo, survive with rotation and magnetic fields? A follow-up paper was promised (§4.4).
- Does the expansion to about 54 R⊙ at 1 M⊙ reverse into the ~4 R⊙ state of [[masunaga-inutsuka-2000]] once the Kelvin–Helmholtz to accretion time ratio drops?
- How do the mass-dependent timescales change with more realistic, non-isolated initial conditions such as filament-fed cores?

## Related material in vault

- Extends: [[larson-1969]], [[masunaga-inutsuka-2000]], [[tomida-2013]]
- Contradicts: none
- Replicates: none
- Concepts introduced/used: [[second-collapse]], [[first-hydrostatic-core]], [[prestellar-core]], [[accretion-luminosity]]
- Cites: [[larson-1969]], [[masunaga-inutsuka-2000]], [[tomida-2013]], [[dunham-2014]]
- Cited by (in this vault): [[young-2023]]
