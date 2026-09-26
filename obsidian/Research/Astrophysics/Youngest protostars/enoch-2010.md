---
title: "A Candidate Detection of the First Hydrostatic Core"
authors: Melissa L. Enoch, Jeong-Eun Lee, Paul Harvey, Michael M. Dunham, Scott Schnee
year: 2010
venue: The Astrophysical Journal Letters 722, L33
url: https://arxiv.org/abs/1009.0536
language: en
domain: astrophysics
status: draft
methodology_type: empirical
citation_count: 77
citation_count_date: 2026-09-26
key_concepts: ["[[first-hydrostatic-core]]", "[[internal-luminosity]]", "[[prestellar-core]]", "[[statistical-lifetime]]", "[[class-0-protostar]]", "[[vello]]"]
extends: ["[[dunham-2008]]", "[[enoch-2008]]"]
contradicts: []
replicates: []
cites: ["[[larson-1969]]", "[[dunham-2008]]", "[[enoch-2008]]", "[[evans-2009]]"]
cited_by: ["[[pineda-2011]]", "[[stutz-2013]]", "[[dunham-2014]]"]
quality_notes: "Four-page Letter; the FHSC identification is explicitly tentative (a protostar with L_int ~0.01 L⊙ fits equally well). Per-Bolo 58's candidacy was later weakened: stutz-2013 places its 70/24 colour with VeLLOs, and dunham-2014 lists it among nine candidates and judges it very unlikely that all nine are true FHSCs. Citation count from Semantic Scholar (77)."
author: moiseevigor
tags:
  - agent/research
  - user/moiseevigor
  - domain/astrophysics
  - topic/first-hydrostatic-core
  - topic/protostar-observational-signatures
  - topic/embedded-low-luminosity-protostars
  - topic/prestellar-cores
  - topic/spitzer-surveys
  - topic/sed-modeling
  - topic/radiative-transfer
  - topic/protostellar-outflows
  - paper
  - status/draft
---

# A Candidate Detection of the First Hydrostatic Core

## Abstract

(Verbatim from the arXiv v1 PDF.)

The first hydrostatic core (FHSC) represents a very early phase in the low-mass star formation process, after collapse of the parent core has begun but before a true protostar has formed. This large (few AU), cool (100 K), pressure supported core of molecular hydrogen is expected from theory, but has yet to be observationally verified. Here we present observations of an excellent candidate for the FHSC phase: Per-Bolo 58, a dense core in Perseus that was previously believed to be starless. The 70 µm flux of 65 mJy, from new deep Spitzer MIPS observations, is consistent with that expected for the FHSC. A low signal-to-noise detection at 24 µm leaves open the possibility that Per-Bolo 58 could be a very low luminosity protostar, however. We utilize radiative transfer models to determine the best-fitting FHSC and protostar models to the spectral energy distribution and 2.9 mm visibilities of Per-Bolo 58. The source is consistent with a FHSC with some source of lower opacity through the envelope allowing 24 µm emission to escape; a small outflow cavity or a cavity in the envelope are both possible. While we are unable to rule out the presence of a protostar, if present it would be one of the lowest luminosity protostellar objects yet observed, with an internal luminosity of ∼ 0.01L⊙.

## TL;DR

Deep Spitzer 70 µm imaging (5σ ≈ 7.5 mJy, about 10× deeper than c2d) of 7 selected "starless" cores found one detection: **Per-Bolo 58 in Perseus/NGC 1333, with F70 = 65 ± 6 mJy and a marginal F24 = 0.88 ± 0.24 mJy**. SED plus CARMA 2.9 mm visibility modelling gives **L_int = 0.012 L⊙**. The fit works equally well for a 100 K, 1.7 AU FHSC (with an envelope cavity or outflow to let 24 µm out) and for a 3000 K protostar. The Dunham et al. (2008) relation gives 0.014 L⊙. It is a deep-70-µm-selected FHSC candidate, and it shows that FHSCs and extreme VeLLOs are not separable from continuum data alone.

## Problem

The FHSC was predicted by [[larson-1969]] but had never been verified observationally. Its expected signature is an increase in 40–100 µm emission over a starless core, with no emission at λ ≲ 24 µm (§1–2, citing Boss & Yorke 1995 and Young & Evans 2005). The c2d 70 µm survey was too shallow for such sources. Any FHSC would therefore sit in the "starless" core census of [[enoch-2008]].

## Approach

- **Target selection (§2)**: from the 108-core starless census of [[enoch-2008]] (complete to M_core ≳ 0.2 M⊙), 7 cores in Perseus, Serpens and Ophiuchus were chosen by one or more of three criteria: (1) faint emission below 5σ in the c2d 70 µm maps; (2) mass-to-size ratio above the critical Bonnor–Ebert value (M/FWHM > 31.9 M⊙ pc^-1 at 10 K); (3) spatial compactness at 1.1 mm or in CARMA 2.9 mm maps. The authors state that the sample is neither complete nor unbiased.
- **Observations (§3)**: deep MIPS 70 µm maps taken 2008 Oct 20–27 with 1100–2000 s pixel^-1 integration and a **5σ limit ~7.5 mJy**. That depth was chosen to detect FHSCs with mass ≳ 0.015 M⊙ at 250–260 pc (Omukai 2007 models). The SED also uses 4.5, 24 and 160 µm c2d data, SHARC-II 350 µm, SCUBA 850 µm, Bolocam 1.1 mm and CARMA 2.9 mm (Table 1).
- **Modelling (§4.1)**: RADMC 2-D radiative transfer with a rotating, infalling (Ulrich) envelope plus an outflow cavity of opening angle α. M_env is fixed at 1.2 M⊙ (from the 1.1 mm flux at T = 8 K), with Ossenkopf & Henning (1994) thin-ice opacities and an ISRF 3× Black–Draine. The FHSC grid varies L_int ∈ {0.006, 0.012, 0.025} L⊙, R_out, R_cent, α and i, with T_eff = 100 K. The protostar grid is the same with T_eff = 3000 K and R ~ 1 R⊙. The fit is by χ² to the SED, with the 2.9 mm visibilities constraining R_out.

## Key result

- **Detection (§3)**: the 70 µm flux of Per-Bolo 58 is 65 ± 6 mJy. A 24 µm counterpart has 0.88 ± 0.24 mJy, below c2d's 7σ catalogue threshold. A 4.5 µm source (0.024 ± 0.007 mJy) lies 10″ offset and is treated as an upper limit. F160 ≈ 2.8 Jy with ~50% uncertainty.
- **Best FHSC model (§4.2)**: L_int = 0.012 L⊙, T_eff = 100 K, R = 1.7 AU, R_cent = 50 AU, R_out = 8000 AU, α = 0°, i = 25°. Every good fit needs either R_cent ≥ 50 AU or α ≥ 20°, because models with no cavity cannot reproduce the 24 µm point.
- **Best protostar model (§4.3)**: L_int = 0.012 L⊙, R_cent = 50 AU, R_out = 8000 AU, α = 10°, i = 30°. At high inclination (i > α) this model is essentially indistinguishable from the FHSC fit. Protostar models at low inclination are ruled out because they give far too much near-IR emission.
- **Cross-check with the L_int–F70 relation (§4.3)**: using L_int = 3.3 × 10^8 F70^0.94 L⊙ from [[dunham-2008]] gives **L_int = 0.014 L⊙**. If Per-Bolo 58 is a protostar, it is among the faintest known, with L_int ~ 0.01 L⊙.
- **Expected FHSC numbers (§1)**: an FHSC lifetime of t ~ 10^3–3 × 10^4 yr set against a protostellar lifetime of 5.4 × 10^5 yr ([[evans-2009]]) predicts only one FHSC for every 18 to 540 protostars. Perseus, Serpens and Ophiuchus each hold 30–70 embedded protostars.
- **Detectability (§2)**: an unambiguous FHSC detection requires compact 70 µm emission and no emission at λ ≲ 24 µm. The c2d 70 µm limit, approximately 75 mJy (5σ), sits above typical FHSC fluxes.
- **Proposed discriminants (§4.4)**: outflow speed (FHSC v ~ 3 km s^-1 against 10–20 km s^-1 for protostars) and warm-gas chemistry. The FHSC envelope peaks at T ~ 80 K, while protostar models reach up to 300 K in the inner few AU and would sublimate water ice, giving ALMA H2O/HDO lines near 300 and 240 GHz.

## Assumptions

- Distance 250–260 pc (Perseus/Serpens).
- M_env = 1.2 M⊙ is fixed from the 1.1 mm flux at T_dust = 8 K.
- The ISRF is 3× Black–Draine, justified by the bright NGC 1333 environment.
- ISRF back-scattering is subtracted up to 40 µm, following Dunham et al. (2010).
- The FHSC is modelled as a 100 K blackbody inside an Ulrich envelope, not as an RHD first core.

## Limitations / scope

- The paper itself states that it cannot distinguish an FHSC from a very low luminosity protostar.
- The 24 µm detection is low-SNR, and it is inconsistent with a spherically symmetric FHSC, so the model has to add an envelope cavity or outflow that simple FHSC physics does not predict.
- The sample is small and hand-picked (7 cores). Non-detection in the other 6 cores does not measure FHSC incidence.
- No outflow was detected; the Hatchell & Dunham (2009) HARP CO 3–2 search was not sensitive to FHSC-speed outflows.
- A Letter: the modelling details defer to Enoch et al. (2009b).

## Replication evidence

**Partial / contested.** Dunham et al. (2011) detected a collimated slow CO outflow from Per-Bolo 58 (cited in [[pineda-2011]] and [[dunham-2014]]; not in this vault). [[stutz-2013]] (§4) places Per-Bolo 58's 70/24 colour with VeLLOs and suggests it may be an extremely low-mass protostar. [[dunham-2014]] (§4.2.2) lists it among nine FHSC candidates. In Perseus that review expects only 0.07–7 first cores, so at least some candidates are probably young protostars.

## Why this paper matters

This was the first FHSC candidate found by the method most relevant to archival searches: **a compact 70 µm point source in a core with nothing at ≤ 24 µm**, deep enough to reach L_int ~ 0.01 L⊙ at 250 pc. It defined the detectability threshold, since c2d's ~75 mJy (5σ) at 70 µm misses FHSC-level fluxes and ~7.5 mJy is needed. It also shows the central degeneracy: once envelope reprocessing dominates, a 100 K FHSC and a 3000 K protostar of equal L_int produce almost the same SED and visibilities.

It is a useful reminder of what counts as evidence. Even a well-fitted SED only constrains L_int. Deciding the evolutionary state needs kinematic (outflow speed) or chemical (warm water) information. The paper also notes that VeLLOs are defined by luminosity alone, so some objects called VeLLOs may be FHSCs.

## Quotes

1. > "we expect only one FHSC for every 18 to 540 protostars" — §1
2. > "we are unable to rule out the presence of a protostar" — Abstract

## Open questions surfaced

- Is Per-Bolo 58 an FHSC or a VeLLO? The paper proposes outflow velocity (millimetre or Herschel spectroscopy) and ALMA H2O/HDO warm-gas tracers as tests (§4.4).
- What physically makes the low-opacity path needed for the 24 µm leak: an FHSC outflow (as in Machida et al. 2008), a binary, or a cavity?
- How many FHSCs hide among "starless" cores when surveys are as deep as 7.5 mJy at 70 µm but uniform, not hand-picked?
- If the FHSC lifetime reaches ~10^4 yr (Tomida et al. 2010), is one candidate in NGC 1333 consistent with the 1:18–540 expected ratio?

## Related material in vault

- Extends: [[dunham-2008]], [[enoch-2008]]
- Contradicts: —
- Replicates: —
- Concepts introduced/used: [[first-hydrostatic-core]], [[internal-luminosity]], [[prestellar-core]], [[statistical-lifetime]], [[class-0-protostar]], [[vello]]
- Cites: [[larson-1969]], [[dunham-2008]], [[enoch-2008]], [[evans-2009]]
- Cited by (in this vault): [[pineda-2011]], [[stutz-2013]], [[dunham-2014]]
