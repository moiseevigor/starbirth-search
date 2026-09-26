---
title: "A Radiation Hydrodynamic Model for Protostellar Collapse. II. The Second Collapse and the Birth of a Protostar"
authors: Hirohiko Masunaga, Shu-ichiro Inutsuka
year: 2000
venue: The Astrophysical Journal 531, 350-365
url: https://doi.org/10.1086/308439
language: en
domain: astrophysics
status: draft
methodology_type: theoretical
citation_count: 391
citation_count_date: 2026-09-26
key_concepts: ["[[second-collapse]]", "[[first-hydrostatic-core]]", "[[class-0-protostar]]", "[[luminosity-problem]]", "[[prestellar-core]]", "[[bolometric-temperature]]", "[[accretion-luminosity]]", "[[free-fall-time]]"]
extends: ["[[larson-1969]]"]
contradicts: []
replicates: []
cites: ["[[larson-1969]]"]
cited_by: ["[[tomida-2013]]", "[[bhandare-2020]]", "[[young-2023]]", "[[pineda-2011]]"]
quality_notes: "Standard 1-D reference for the whole collapse-to-Class-I sequence with self-consistent, frequency-dependent RHD and SEDs. It is the calibration point that 3-D codes compare against (Tomida 2013, Table 2 row 'MI'). Its luminosity curve depends on the initial conditions: homogeneous and hydrostatic starts give qualitatively different curves (§3.2). Bhandare et al. 2020 (§5) cite its 0.73 M⊙ protostar mass as a value 'a few years after' second-core formation. In the paper, 0.73 M⊙ is the mass at the end of the calculation (§3.1.6), about 1.4×10⁵ yr later. Citation count is from Semantic Scholar. The first-core properties are in Paper I (Masunaga, Miyama & Inutsuka 1998) and are not repeated here."
author: moiseevigor
tags:
  - agent/research
  - user/moiseevigor
  - domain/astrophysics
  - topic/protostellar-collapse
  - topic/second-collapse
  - topic/first-hydrostatic-core
  - topic/radiation-hydrodynamics
  - topic/protostar-observational-signatures
  - topic/class-0-protostars
  - topic/evolutionary-lifetimes
  - topic/accretion-luminosity
  - topic/radiative-transfer
  - paper
  - status/draft
---

# A Radiation Hydrodynamic Model for Protostellar Collapse. II. The Second Collapse and the Birth of a Protostar

## Abstract

We carry out radiation hydrodynamic calculations to study physical processes in the formation of a 1 M⊙ protostar. Following our previous work, calculations pursue the whole evolution from the beginning of the first collapse to the end of the main accretion phase. The adiabatic core formed after the initial collapse (i.e., the first core) experiences further gravitational collapse triggered by dissociation of molecular hydrogen, which leads to the formation of the second core, i.e., the birth of a protostar. The protostar grows in mass as accreting the infalling material from the circumstellar envelope, while the protostar keeps its radius at ∼4 R⊙ during the main accretion phase. These typical features in the evolution are in good agreement with previous studies. We consider two different initial conditions for the density distribution: homogeneous and hydrostatic cloud cores with the same central density of 1.415 × 10⁻¹⁹ g cm⁻³. The homogeneous core has the total mass of 1 M⊙ while the hydrostatic core has 3.852 M⊙. For the initially homogeneous model, the accretion luminosity rapidly rises to the maximum value of ≈25 L⊙ just after the birth of a protostar, and declines gradually as the mass accretion rate decreases. In contrast, the luminosity increases monotonically with time for the initially hydrostatic model. This difference arises because the mass accretion rate varies depending on the inward acceleration at the initial stage, which affects the luminosity curve. A less massive hydrostatic core would possess the similar properties in the luminosity curve to the 3.852 M⊙ case, because a hydrostatic cloud core with mass lower than 3.852 M⊙ can be shown to provide a smaller mass accretion rate after the birth of a protostar and a more gradual rise in the luminosity curve. Our numerical code is designed to provide the evolution of the spectral energy distribution (SED) along with the dynamical evolution in our spherically symmetric calculations. We confirm that the SED evolves from a 10 K graybody spectrum to hotter spectra typical for class I and flat spectrum sources. The SED for the class 0 sources corresponds to the age of 2 × 10⁴ yr, which is smaller by an order of magnitude than the typical age of class I objects. Considering possible nonspherically symmetric effects, we suggest that observed class 0 sources should consist of the "genuine" class 0 objects, which are as young as 10⁴ yr, and more evolved protostars on edge-on view ("class 0–like class I" objects). The contamination of edge-on class I objects into class 0 sources are not negligible because they are more abundant than genuine class 0 objects. Since observations indicate that the class 0 sources are typically more luminous than class I sources, the initially hydrostatic model, where the luminosity increases monotonically with time, does not match the observations. The initially homogeneous model, in contrast, shows a tendency consistent with the observations. Compiling our results and other theoretical and observational evidence, we illustrate an evolutionary picture of protostar formation. In terms of the evolutionary time and the inclination to an observer, we find that protostellar objects are clearly categorized.

## TL;DR

This is the reference 1-D radiation-hydrodynamic calculation, with angle- and frequency-dependent transfer, from a 10 K cloud core through the second collapse to the end of main accretion. It is the first such calculation to output **SEDs and luminosity curves**.
- The second collapse starts at ρc ≈ 10⁻⁷ g cm⁻³ and Tc ≈ 2000 K. It lasts about 0.1 yr.
- The protostar settles at **~4 R⊙**.
- Luminosity is **<0.01 L⊙** during the first collapse. In the homogeneous model it rises to **~25 L⊙** and then declines. In the hydrostatic model it rises monotonically.
- The SED does not change during the first collapse. After birth, **T_bol jumps from 10 K to ~40 K** and climbs to 410 K. T_bol < 70 K corresponds to ≲2×10⁴ yr after birth.

## Problem

How does a protostar form and appear observationally, in SEDs, T_bol and luminosity, through the second collapse and main accretion? Where do starless cores, Class 0 and Class I sources sit on that timeline? Earlier calculations (Larson 1969; Winkler & Newman 1980; Stahler, Shu & Taam 1980) used simpler physics and did not produce SEDs (§1).

## Approach

- 1-D spherical RHD with the variable Eddington factor method. It solves the angle- and frequency-dependent transfer equation, so it is neither Eddington nor grey (§2.1).
- Includes H2 dissociation, H/He ionization, and the nonideal Saumon–Chabrier–Van Horn EOS. Specific heat of H2 is computed from the rotational and vibrational partition functions.
- Gas opacities: Iglesias & Rogers; Alexander & Ferguson. Dust opacities: Yorke, with three components (§2.1).
- Separate dust and gas temperatures (§2.1).
- Two initial conditions (§2.2):
  - **Homogeneous:** 1 M⊙, fixed boundary at R = 10⁴ AU, ρ = 1.415×10⁻¹⁹ g cm⁻³. Equivalent to [[larson-1969]].
  - **Hydrostatic:** same central density, boundary at 4×10⁴ AU, 3.852 M⊙.
- External radiation field: 2.7 K CMB plus diluted 6000 K starlight, and cosmic-ray heating (§2.3).
- SEDs are computed for an observer at 150 pc with a 10″ FWHM beam and no interstellar extinction (§3.3).
- T_bol follows Myers & Ladd: T_bol = 1.25×10⁻¹¹ ν̄ Hz⁻¹ K (eq. 8).

## Key result

**First collapse and first core (§3.1.1–3.1.2).** The central temperature dips to about 5 K and then rises. The evolution becomes fully adiabatic at τ ≈ 1, at ρc ≈ 10⁻¹² g cm⁻³. The first-core radius and mass agree with Paper I and are not repeated here.

**Second collapse (§3.1.3).** It begins "when the central density and the central temperature reach ρc ∼ 10⁻⁷ g cm⁻³ and Tc ∼ 2000 K", with γ_eff ≈ 1.1. H2 dissociation completes at ρc ≈ 10⁻² g cm⁻³ and Tc ≈ 10⁴ K, which is when the second core forms. The dynamical timescale is the free-fall time at 10⁻⁷ g cm⁻³, "which is 0.1 yr". Dust evaporates at ρc ≈ 3×10⁻⁷ g cm⁻³. The collapse halts at ρc ≈ 1 g cm⁻³.

**Timeline (Table 1, homogeneous model).** The second collapse begins at t₀ = 1.7526×10⁵ yr, close to t_ff = 1.77×10⁵ yr (eq. 2). Snapshots 9–13 fall at t − t₀ = 1.56×10⁻² yr, 19 yr, 4.93×10³ yr, 2.30×10⁴ yr and 1.38×10⁵ yr.

**Protostar (§3.1.4–3.1.6).**
- Radius is "settled at 2×10⁻² AU or 4 R⊙ during the main accretion phase".
- There is an off-centre temperature peak caused by partially degenerate electrons.
- The envelope follows ρ ∝ r⁻¹·⁵ inside and ρ ∝ r⁻² outside.
- The protostellar mass "monotonically reaches 0.73 M⊙ at the end of the calculation".

**Accretion rates (§3.1.7, §3.2).**
- Homogeneous model: Ṁ ≈ 10⁻⁵ M⊙ yr⁻¹ early in main accretion, falling to about 10⁻⁶ M⊙ yr⁻¹. Just after birth, Ṁ* = 1.3×10⁻⁵ M⊙ yr⁻¹. The time-averaged value is 5.7×10⁻⁶ M⊙ yr⁻¹ over 0 ≤ t − t₀ ≤ 1.4×10⁵ yr.
- Hydrostatic model: roughly constant at 5.3×10⁻⁶ M⊙ yr⁻¹.

**Luminosity curve (§3.2, Fig. 7; §4.1.3).**
- During the first collapse the luminosity stays ≲0.01 L⊙. It "rapidly rises when the second core, or a protostar, is born".
- Homogeneous model: the maximum is about 25 L⊙, followed by a gradual decline to about 10 L⊙ at the end, which the authors note is still too high for Class I (the "luminosity problem").
- §4.1.3 places the maximum of 25 L⊙ "at 2 × 10⁴ yr", i.e. the rise is resolved on a 10³–10⁴ yr scale, not in years. See Limitations.
- The luminosity is accretion-dominated: L_acc = GM*Ṁ*/R* (eq. 5).
- Hydrostatic model: no rapid rise and no maximum. The luminosity increases gradually and monotonically.

**SED evolution (§3.3, Fig. 8).**
- Initially the SED is optically thin ~10 K dust emission. It briefly gets colder (curves 2–3), then warms.
- The first-collapse stage (curves 1–6) "shows no apparent changes in SEDs", because the thick envelope reprocesses the central emission.
- A deep 10 µm silicate absorption feature appears. It is deepest just before near-IR emission emerges and becomes shallower as the envelope depletes.
- The source becomes near-IR-detectable only at curves 12–13 (t − t₀ ≈ 2.3×10⁴ and 1.4×10⁵ yr). Curve 12 looks Class I and curve 13 looks like a flat-spectrum source.
- In the hydrostatic model the mm/submm flux never decreases, because that model has more envelope mass. Shorter-wavelength emission is insensitive to the initial profile and the total mass (§3.3).

**Bolometric temperature (§4.1, Fig. 10).** T_bol "remains at 10 K before a protostar is formed" and "abruptly rises up to 40 K after t − t₀ exceeds 0". It then increases gradually to 410 K. Class 0 T_bol < 70 K corresponds to t − t₀ ≲ 2×10⁴ yr, the "genuine class 0" phase. T_bol is sensitive to missing high-frequency flux (upper cut-off at 3×10¹²–10¹³ Hz), so edge-on Class I sources can look like Class 0.

**Evolutionary picture (§4.2, Fig. 11).**
- Luminous, cold sources (L ≫ 1 L⊙, T_bol < 70 K) should be genuine Class 0.
- Less luminous cold sources are probably edge-on Class I.
- If outflows start at t₀, they must last to about 1.3×10⁵ yr to match the outflow statistics of Mardones et al. (1997).

## Assumptions

- Spherical symmetry. No rotation, magnetic field or disc (§4.1.3 and §4.2 discuss non-spherical effects qualitatively).
- No convection and no nuclear burning. The authors argue that deuterium burning would not change R* much (§5).
- No mass inflow through the outer boundary. The end of accretion is therefore set by exhausting the finite reservoir (§3.2).
- The Class 0/Class I comparison uses observed mean luminosities: 5.7 L⊙ for Class 0 (Gregersen et al. 1997) and about 1 L⊙ for Class I (Kenyon et al. 1990).

## Limitations / scope

- The phrase "rapidly rises ... just after the birth" in the abstract should not be read as a rise over years. The luminosity maximum is quoted at about 2×10⁴ yr in §4.1.3, and Fig. 7 spans 0–5×10⁴ yr. The early light curve at t − t₀ < 100 yr is not reported numerically, and the Fig. 7 values could not be read from the text extraction.
- Snapshot 10 (t − t₀ = 19 yr) is quoted in [[tomida-2013]] Table 2 as R = 4 R⊙ and M = 0.016 M⊙. That quote comes from Tomida, not from a table in this paper.
- In 1-D, the hot inner envelope cannot be seen along low-column sightlines, so near/mid-IR detectability is pessimistic compared with a rotating, cavity-bearing geometry.
- The initial conditions strongly affect the luminosity curve. The authors' preference for the homogeneous model rests on observed mean Class 0 and Class I luminosities, which are themselves uncertain (§4.1.3).

## Replication evidence

Partial.
- The ~4 R⊙ main-accretion radius agrees with Winkler & Newman and with Stahler, Shu & Taam (§3.1.4).
- The thermal evolution was reproduced in 3-D RMHD by [[tomida-2013]], who find a larger transient radius (~10 R⊙) at t < 1 yr and attribute the difference to an early expansion phase.
- [[bhandare-2020]] reproduce the off-centre temperature peak with a different EOS and give a different explanation for it.
- The luminosity-curve dependence on initial conditions has not been independently re-tested in these vault papers.

## Why this paper matters

For a "watch the protostar switch on" search, this is the key quantitative prediction. In spherical symmetry, second-core formation produces **no immediate SED change**. What changes is:
- bolometric luminosity, from ≲0.01 L⊙ to tens of L⊙ on a ≲10⁴ yr scale in the homogeneous case;
- T_bol, from 10 K to about 40 K right after birth.

The near-IR stays dark for about 10⁴–10⁵ yr. Any detectable brightening right after birth therefore has to appear in the far-IR/submm luminosity, not the near/mid-IR. The initial-condition dependence of the light curve (rise-and-decline versus monotonic rise) is also a key caveat for any statistical interpretation of Class 0 luminosities.

## Quotes

1. > "the first collapse stage (curves 1–6) shows no apparent changes in SEDs" — §3.3
2. > "it abruptly rises up to 40 K after t − t₀ exceeds 0" — §4.1

## Open questions surfaced

- What is the emergent light curve during the first ~10–10³ yr after second-core formation, at the resolution needed for a multi-epoch search? It is not reported numerically.
- How do rotation and outflow cavities change near/mid-IR detectability of genuine Class 0 sources? Treated qualitatively in §4.2 only.
- Which initial condition (dynamical or hydrostatic) is realised in nature? That decides whether Class 0 luminosity peaks early.

## Related material in vault

- Extends: [[larson-1969]]
- Contradicts: none
- Replicates: none
- Concepts introduced/used: [[second-collapse]], [[first-hydrostatic-core]], [[class-0-protostar]], [[luminosity-problem]], [[prestellar-core]], [[bolometric-temperature]], [[accretion-luminosity]], [[free-fall-time]]
- Cites: [[larson-1969]]
- Cited by (in this vault): [[tomida-2013]], [[bhandare-2020]], [[young-2023]], [[pineda-2011]]
