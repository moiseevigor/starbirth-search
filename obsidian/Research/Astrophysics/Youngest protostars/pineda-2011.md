---
title: "The Enigmatic Core L1451-mm: A First Hydrostatic Core? Or a Hidden VeLLO?"
authors: Jaime E. Pineda, Héctor G. Arce, Scott Schnee, Alyssa A. Goodman, Tyler Bourke, Jonathan B. Foster, Thomas Robitaille, Joel Tanner, Jens Kauffmann, Mario Tafalla, Paola Caselli, Guillem Anglada
year: 2011
venue: The Astrophysical Journal 743, 201
url: https://arxiv.org/abs/1109.1207
language: en
domain: astrophysics
status: draft
methodology_type: empirical
citation_count: 91
citation_count_date: 2026-09-26
key_concepts: ["[[first-hydrostatic-core]]", "[[internal-luminosity]]", "[[prestellar-core]]", "[[statistical-lifetime]]", "[[luminosity-problem]]", "[[episodic-accretion]]", "[[bolometric-temperature]]", "[[accretion-luminosity]]", "[[vello]]"]
extends: ["[[enoch-2010]]", "[[dunham-2008]]"]
contradicts: []
replicates: []
cites: ["[[larson-1969]]", "[[masunaga-inutsuka-2000]]", "[[dunham-2008]]", "[[enoch-2008]]", "[[enoch-2010]]", "[[evans-2009]]"]
cited_by: ["[[stutz-2013]]", "[[dunham-2014]]", "[[young-2023]]"]
quality_notes: "Published in the main ApJ journal (743, 201), not ApJ Letters. The FHSC and YSO+disk models fit about equally well; the FHSC preference rests on the low luminosity plus the slow, poorly collimated CO outflow. The paper's own number-count estimate (≤0.2 FHSCs expected in Perseus) argues against all Perseus candidates being true FHSCs. Citation count from Semantic Scholar (91)."
author: moiseevigor
tags:
  - agent/research
  - user/moiseevigor
  - domain/astrophysics
  - topic/first-hydrostatic-core
  - topic/protostar-observational-signatures
  - topic/embedded-low-luminosity-protostars
  - topic/prestellar-cores
  - topic/sed-modeling
  - topic/evolutionary-lifetimes
  - topic/protostellar-outflows
  - topic/radiative-transfer
  - topic/accretion-luminosity
  - paper
  - status/draft
---

# The Enigmatic Core L1451-mm: A First Hydrostatic Core? Or a Hidden VeLLO?

## Abstract

(Verbatim from the arXiv v1 PDF.)

We present the detection of a dust continuum source at 3-mm (CARMA) and 1.3-mm (SMA), and ¹²CO (2–1) emission (SMA) towards the L1451-mm dense core. These detections suggest a compact object and an outflow where no point source at mid-infrared wavelengths is detected using Spitzer. An upper limit for the dense core bolometric luminosity of 0.05 L⊙ is obtained. By modeling the broadband SED and the continuum interferometric visibilities simultaneously, we confirm that a central source of heating is needed to explain the observations. This modeling also shows that the data can be well fitted by a dense core with a YSO and disk, or by a dense core with a central First Hydrostatic Core (FHSC). Unfortunately, we are not able to decide between these two models, which produce similar fits. We also detect ¹²CO (2–1) emission with red- and blue-shifted emission suggesting the presence of a slow and poorly collimated outflow, in opposition to what is usually found towards young stellar objects but in agreement with prediction from simulations of a FHSC. This presents the best candidate, so far, for a FHSC, an object that has been identified in simulations of collapsing dense cores. Whatever the true nature of the central object in L1451-mm, this core presents an excellent laboratory to study the earliest phases of low-mass star formation.

## TL;DR

L1451-mm (Per-Bolo 2) is a Perseus core with **no point source anywhere from J to 70 µm**: 24 µm < 1.5 mJy and 70 µm < 72 mJy at 3σ. It nevertheless shows a compact mm continuum source (SMA unresolved flux 27.0 mJy) and a **slow (~1.3 km s^-1), poorly collimated ¹²CO outflow**. The limits give **L_bol ≤ 0.05 L⊙ and T_bol ≤ 30 K**, and the 70 µm limit converts through the Dunham et al. (2008) relation to **L < 1.6 × 10^-2 L⊙**. Joint SED plus visibility fitting needs a central heat source. The YSO+disk model (L_int = 0.045 L⊙) fits slightly better than the FHSC model, but it needs an accretion rate about 100× below infall. So the authors prefer the FHSC, while noting that ≤ 0.2 FHSCs are expected in Perseus.

## Problem

Can a core with no mid-IR source still hide a central object, and if so, is it a first hydrostatic core or a very low luminosity protostar (VeLLO)? It had been classified as starless by [[enoch-2008]] because Spitzer IRAC and MIPS showed no point source (§2). The paper is also a test of how well SED plus interferometric-visibility modelling can separate FHSCs from young protostars.

## Approach

- **Archival IR (§2, Table 1)**: deep J/H/Ks and Spitzer IRAC/MIPS aperture photometry, all non-detections except a 2.7σ 160 µm signal (880 ± 330 mJy). 3σ limits: 3.6 µm < 0.048 mJy, 4.5 µm < 0.012 mJy, 8.0 µm < 0.030 mJy, 24 µm < 1.5 mJy, 70 µm < 72 mJy. IRAM 1.2 mm flux 70 ± 7 mJy.
- **New data (§3)**: IRAM-30m MAMBO 1.2 mm; VLA NH3 (1,1)/(2,2); CARMA 3 mm continuum plus N2H+ and NH2D; SMA 1.3 mm continuum and ¹²CO/¹³CO/C¹⁸O/N2D+ in compact and extended configurations (~1.2″ × 0.9″).
- **Modelling (§4.4)**: simultaneous χ² fit to SED and binned 1.3 mm visibilities, χ² = (1 − Q)χ²_SED + Qχ²_vis with Q = 0.5. The fit uses a genetic algorithm and a Monte-Carlo radiative transfer code (Robitaille, in prep.). Three models: (a) an isothermal starless core n ∝ r^-p; (b) an Ulrich envelope plus a passive flared disk plus a 3000 K YSO (7 free parameters); (c) the Masunaga et al. (1998) model M3a FHSC density/temperature profile (R* ~ 5 AU, L_int ≈ 0.03 L⊙) with only core mass and radius free.
- **Outflow energetics (§4.6)**: optically thin ¹²CO, T_ex = 20 K, Cabrit & Bertout (1990) momentum and energy.

## Key result

- **Luminosity limits (§2)**: L_bol ≤ 0.05 L⊙ and T_bol ≤ 30 K, treating upper limits as detections. This is lower than any Class 0 source in Enoch et al. (2009b) and any VeLLO in [[dunham-2008]]. The 70 µm non-detection with the [[dunham-2008]] L_int–F70 relation gives L < 1.6 × 10^-2 L⊙.
- **Compact source (§4.1, §4.3)**: CARMA 3 mm point-source fit 4 ± 2 mJy. SMA 1.3 mm point source 27.0 ± 0.4 mJy on baselines > 40 kλ, giving M_1.3mm = 0.024 M⊙ at 30 K; the disk-to-core mass ratio is ≈ 0.1. The core mass within 4,200 AU is 0.3 M⊙ (MAMBO), and the core is more compact than most starless cores.
- **Gas temperature (§2)**: GBT NH3 gives T_kin ≈ 9.7 K and σ_v ≈ 0.15 km s^-1, and shows no evidence of heating by a central source. The VLA NH3 T_kin map is flat, with no rise at the continuum peak (Fig. 5).
- **Model fits (Table 11)**:
  - The starless core needs n ∝ r^-2.8 to fit, which is unphysical.
  - YSO+disk: L_int = 0.0450 L⊙, Ṁ_infall = 7.1 × 10^-6 M⊙ yr^-1, M_disk = 0.086 M⊙, R_disk = 107 AU, i = 64.9°, M_core = 0.146 M⊙, R_env = 1007 AU.
  - FHSC: M_core = 0.56 M⊙, R_env = 2543 AU.
- **Accretion inconsistency (§4.4)**: for the YSO model, the expected L_acc is 6 L⊙, 100× more than the fitted luminosity allows. Matching the fitted luminosity needs Ṁ_acc = 2.45 × 10^-8 M⊙ yr^-1, against an infall rate of 7.1 × 10^-6 M⊙ yr^-1. A hidden YSO therefore requires extremely inefficient or episodic accretion (§5).
- **Outflow (Table 12)**: mass 1.2 × 10^-5 M⊙; momentum 1.7 × 10^-5 M⊙ km s^-1; energy 3.1 × 10^38 erg; characteristic velocity 1.3 km s^-1; dynamical time 2.0 × 10^3 yr; mechanical luminosity 1.3 × 10^-6 L⊙. The authors call it the weakest outflow found so far. It is unbound (it would need ≈ 0.53 M⊙ to bind, about twice the core mass). The authors describe it as consistent with RMHD FHSC outflows of ≲ 3 km s^-1 (Machida et al. 2008; Tomida et al. 2010).
- **Expected FHSC number (§5, Eq. 17)**: N_FHSC = N_Class0 · τ_FHSC/τ_Class0. With τ_FHSC ~ 10^3 yr, N_Class0 = 20–35 in Perseus and τ_Class0 = 2–5 × 10^5 yr, the expected number of FHSCs in Perseus is ≤ 0.2. Class I statistics from [[evans-2009]] give a similar answer. Three of the four known candidates are in Perseus. If all are confirmed, either Perseus is in a star-formation burst or FHSCs live longer (up to 10^4 yr; Tomida et al. 2010).

## Assumptions

- Perseus distance ~250 pc.
- Upper limits are treated as detections for L_bol and T_bol.
- Dust opacities are Ossenkopf & Henning (1994) thick-ice.
- In the YSO model, accretion rate equals infall rate, with M* = M_disk = 0.086 M⊙ and R* = 3 R⊙.
- The FHSC model is taken directly from the 1-D RHD structure of Masunaga et al. (1998), not refit.
- Outflow parameters are not corrected for inclination.

## Limitations / scope

- FHSC and YSO+disk fits are almost indistinguishable (§6). The FHSC model fits the visibilities worse but has only 2 free parameters against 7.
- No mid-IR detections: the SED is constrained only at 160 µm, 1.2 mm and the interferometric points. The authors predict detection by the Herschel Gould Belt Survey.
- Outflow inclination is unknown. If it lies near the plane of the sky, the true speed is higher; if near the line of sight, the dynamical time is longer. Either reading changes the FHSC argument.
- The FHSC counting argument depends on τ_FHSC, which spans 0.5–50 kyr across models (Table 4 of [[dunham-2014]]).

## Replication evidence

**Partial.** [[dunham-2014]] (§4.2.2) lists L1451-mm among nine FHSC candidates found through (sub)millimetre detections of outflows from "starless" cores. It concludes that some, possibly all, are very young protostars. [[young-2023]] tabulates L1451-mm among observed first-core candidates. Later L1451-mm follow-up papers (a 2016 kinematics study; a 2022 SiO/CH3OH outflow confirmation; titles seen in an arXiv search only) are not in this vault and were not read.

## Why this paper matters

L1451-mm is the example of a core with a central heat source, a disk-like compact component and an outflow, yet **nothing at 3.6–70 µm at Spitzer c2d depth**. Any mid-IR/far-IR search for the earliest objects has to reckon with this: at L_int ≲ 0.02 L⊙ and 250 pc, a Spitzer-depth 70 µm non-detection does not make a core starless. The paper's joint SED plus visibility method, and its Eq. 17 count of expected FHSCs, became standard tools in later candidate papers.

It also restates the luminosity problem at its most extreme. If the central object is a protostar, it must be accreting about 300× below the infall rate, which makes L1451-mm either an FHSC or a strong case for episodic accretion.

## Quotes

1. > "the expected number of FHSC in Perseus is ≤ 0.2 objects" — §5
2. > "This presents the best candidate, so far, for a FHSC" — Abstract

## Open questions surfaced

- Is the unresolved 1.3 mm component a disk or the FHSC itself? Longer baselines were proposed to test this (§5).
- Is the CO outflow warm? ¹²CO(3–2) would give the gas temperature (§5).
- Outflow inclination and cavity geometry would pin down the dynamical time and collimation (Huard et al. 2006-style imaging).
- Herschel detection or non-detection would settle L_int (predicted detectable by the HGBS).
- How can ≥ 3 FHSC candidates in Perseus be reconciled with ≤ 0.2 expected: a longer FHSC lifetime, a recent SFR burst, or misidentified protostars?

## Related material in vault

- Extends: [[enoch-2010]], [[dunham-2008]]
- Contradicts: —
- Replicates: —
- Concepts introduced/used: [[first-hydrostatic-core]], [[internal-luminosity]], [[prestellar-core]], [[statistical-lifetime]], [[luminosity-problem]], [[episodic-accretion]], [[bolometric-temperature]], [[accretion-luminosity]], [[vello]]
- Cites: [[larson-1969]], [[masunaga-inutsuka-2000]], [[dunham-2008]], [[enoch-2008]], [[enoch-2010]], [[evans-2009]]
- Cited by (in this vault): [[stutz-2013]], [[dunham-2014]], [[young-2023]]
