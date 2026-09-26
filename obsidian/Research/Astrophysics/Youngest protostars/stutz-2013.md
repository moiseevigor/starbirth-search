---
title: "A Herschel and APEX Census of the Reddest Sources in Orion: Searching for the Youngest Protostars"
authors: Amelia M. Stutz, John J. Tobin, Thomas Stanke, S. Thomas Megeath, William J. Fischer, Thomas Robitaille, Thomas Henning, Babar Ali, James di Francesco, Elise Furlan, Lee Hartmann, Mayra Osorio, Thomas L. Wilson, Lori Allen, Oliver Krause, P. Manoj
year: 2013
venue: The Astrophysical Journal 767, 36
url: https://arxiv.org/abs/1302.1203
language: en
domain: astrophysics
status: draft
methodology_type: empirical
citation_count: 115
citation_count_date: 2026-09-26
key_concepts: ["[[class-0-protostar]]", "[[statistical-lifetime]]", "[[first-hydrostatic-core]]", "[[internal-luminosity]]", "[[bolometric-temperature]]", "[[pacs-bright-red-source]]"]
extends: ["[[dunham-2008]]"]
contradicts: []
replicates: []
cites: ["[[larson-1969]]", "[[dunham-2008]]", "[[enoch-2010]]", "[[pineda-2011]]", "[[evans-2009]]"]
cited_by: ["[[dunham-2014]]", "[[safron-2015]]", "[[kristensen-dunham-2018]]", "[[fischer-2019]]", "[[lee-2021]]", "[[zakri-2022]]", "[[young-2023]]", "[[furlan-2016]]", "[[robitaille-2017]]"]
quality_notes: "Defines the PBRS ('PACS Bright Red sources') class, later written PBRS in dunham-2014 and HOPS follow-ups. The PBRS lifetime (~25 kyr) is a constant-SFR number-ratio estimate that varies 16x between Orion A and B, so it is not a robust phase duration. Nearly half of the 55 new 70 µm candidates are classified as extragalactic contamination. Citation count from Semantic Scholar (115)."
author: moiseevigor
tags:
  - agent/research
  - user/moiseevigor
  - domain/astrophysics
  - topic/class-0-protostars
  - topic/embedded-low-luminosity-protostars
  - topic/evolutionary-lifetimes
  - topic/spitzer-surveys
  - topic/sed-modeling
  - topic/yso-catalogs
  - topic/protostar-observational-signatures
  - topic/herschel-protostar-surveys
  - topic/survey-artefacts-and-contamination
  - topic/radiative-transfer
  - paper
  - status/draft
---

# A Herschel and APEX Census of the Reddest Sources in Orion: Searching for the Youngest Protostars

## Abstract

(Verbatim from the arXiv v1 PDF.)

We perform a census of the reddest, and potentially youngest, protostars in the Orion molecular clouds using data obtained with the PACS instrument onboard the Herschel Space Observatory and the LABOCA and SABOCA instruments on APEX as part of the Herschel Orion Protostar Survey (HOPS). A total of 55 new protostar candidates are detected at 70 µm and 160 µm that are either too faint (m24 > 7 mag) to be reliably classified as protostars or undetected in the Spitzer/MIPS 24 µm band. We find that the 11 reddest protostar candidates with log λFλ70/λFλ24 > 1.65 are free of contamination and can thus be reliably explained as protostars. The remaining 44 sources have less extreme 70/24 colors, fainter 70 µm fluxes, and higher levels of contamination. Taking the previously known sample of Spitzer protostars and the new sample together, we find 18 sources that have log λFλ70/λFλ24 > 1.65; we name these sources "PACS Bright Red sources", or PBRs. Our analysis reveals that the PBRs sample is composed of Class 0 like sources characterized by very red SEDs (Tbol < 45 K) and large values of sub–millimeter fluxes (Lsmm/Lbol > 0.6%). Modified black–body fits to the SEDs provide lower limits to the envelope masses of 0.2 M⊙ to 2 M⊙ and luminosities of 0.7 L⊙ to 10 L⊙. Based on these properties, and a comparison of the SEDs with radiative transfer models of protostars, we conclude that the PBRs are most likely extreme Class 0 objects distinguished by higher than typical envelope densities and hence, high mass infall rates.

## TL;DR

A Herschel/PACS 70 + 160 µm search of HOPS fields in Orion (~420 pc) for protostars that Spitzer missed, i.e. faint (m24 > 7) or undetected at 24 µm. It found **55 new candidates: 34 faint at 24 µm and 21 with no 24 µm detection**. About **47% of these are extragalactic contamination**, but sources with no IRAC and no 24 µm detection are the most reliably protostellar. **18 sources with log(λFλ70/λFλ24) > 1.65** are defined as PBRS: Class 0 objects with dense envelopes (T_bol < 45 K, L_bol ~0.7–10 L⊙), not FHSCs. They make up **~5% of Orion protostars (~25 kyr at a 0.5 Myr protostellar lifetime)**, ranging from 1% in Orion A to 17% in Orion B.

## Problem

Spitzer protostar catalogues required m24 < 7 mag to suppress background galaxies (Kryukova et al. 2012; Megeath et al. 2012). That cut excludes the faintest and reddest, and possibly youngest, protostars. The question is how many protostars were missed at 24 µm, what they are (young Class 0, FHSC, edge-on, or galaxy), and whether the reddest can be tied to extreme youth rather than geometry.

## Approach

- **Data (§2)**: HOPS PACS 70/160 µm scan maps (5′ or 8′ fields), with 70 µm aperture correction 0.7331 and 160 µm 0.6602 and a 10% systematic error floor. Also Herschel GBS 100 µm, APEX SABOCA 350 µm (7.3″) and LABOCA 870 µm (19″), and the Spitzer Orion survey (Megeath et al. 2012: 488 protostars; HOPS targets ~300 with a 70 µm detection).
- **Source finding (§3)**: PhotVis at 70 µm with SNR ≥ 7. Sources were removed if they matched a Spitzer protostar brighter than 7 mag within 8″, if 70 µm FWHM was > 7.8″, or if 160 µm was not detected. This left 127 point sources, then 55 with 160 µm detections. 24 µm upper limits come from artificial-star tests at the 90% completeness level.
- **Contamination triage (§3.2)**: α_{5.8–8} ≥ 3 with α_{3.6–4.5} ≤ 0.5 flags PAH galaxies. α_{3.6–160} > 1.2 marks high-probability protostars (flag 1), with lower-probability, extragalactic, "other" (photosphere plus cold dust) and no-IRAC flags as 2–5.
- **PBRS definition (§5)**: log λFλ70/λFλ24 > 1.65 in the combined Spitzer plus new sample.
- **Modelling (§6)**: an Ali et al. (2010) rotating-collapse grid with outflow cavities at 87° inclination to set a floor on envelope density. Hyperion 1-D "external only", "star" and "star+external" models. Modified black-body fits for λ ≥ 70 µm with 2000-draw Monte-Carlo errors.

## Key result

- **Census (§8)**: of the 55 candidates, 27% (15) are reliable protostars, 18% (10) lower-probability protostars, 47% (26) extragalactic contamination including AGN, 3 have stellar photospheres plus cold dust, and 1 has no IRAC coverage. Sources without a 24 µm detection outnumber the others among the most reliable protostars by a factor of ~3. All 6 sources with neither IRAC nor 24 µm detections have strong submm detections and sit in dense, filamentary gas (§3.2).
- **PBRS (§5, §8)**: 18 sources with 70/24 > 1.65, 11 of them new from Herschel. Twelve of 18 show 4.5 µm outflow emission, 4/18 look highly inclined, and 13/18 lie in filamentary regions (§5.1). Eight PBRS are undetected at 24 µm ([[dunham-2014]] §4.2.3).
- **Evolutionary indicators**: T_bol < 45 K and L_smm/L_bol > 0.6% (Abstract). The extreme values are HOPS358 (L_bol = 30.6 L⊙, T_bol = 44.2 K) and 091016 (L_bol = 0.65 L⊙, T_bol = 29 K) (Fig. 12). Every new candidate that has an L_smm estimate, except one, exceeds the André et al. (2000) Class 0 threshold L_smm/L_bol > 0.5% (§7).
- **Envelope density floor (§6.1)**: no model in the grid gives 70/24 > 1.65 below log ρ1/(g cm^-3) ~ −13.4, equivalent to Ṁ_env = 5.4 × 10^-6 M⊙ yr^-1. Inclination alone cannot make PBRS colours.
- **Internal source required (§8)**: externally heated starless-core models cannot reproduce the SEDs. A 70 µm point source requires a dense envelope with an embedded protostar.
- **Phase duration (§5.3)**: about 5% of Orion protostars are PBRS. At constant SFR with a 0.5 Myr protostellar lifetime ([[evans-2009]]), that gives ~25,000 yr, ranging from 5,000 yr in Orion A to 80,000 yr in Orion B. The PBRS fraction is 1% in Orion A and 17% in Orion B.
- **FHSC comparison (§4)**: the new candidates' colours match Class 0 sources and VeLLOs, not the FHSC model colours of Commerçon et al. (2012). Per-Bolo 58 ([[enoch-2010]]) has a VeLLO-like 70/24 colour. B1-bS is as red as the reddest PBRS but more than 10× fainter at 70 µm.

## Assumptions

- Distance ~420 pc for all of Orion.
- Constant star-formation rate and a 0.5 Myr protostellar lifetime for the duration estimate.
- Central mass 0.5 M⊙ when converting ρ1 to infall rate.
- The density-floor grid fixes Ṁ_disk = 10^-8 M⊙ yr^-1, R_disk,max = 5 AU and L = 1 L⊙.
- Foreground A_V up to 40 mag was shown not to change L_bol, T_bol or L_smm.

## Limitations / scope

- Red 70/24 colours are degenerate between envelope density, inclination, cavity opening and foreground or filament extinction (§7). The 70/24 cut does not select every dense envelope.
- L_bol and T_bol are upper limits for sources not detected at 24 µm.
- The faint candidates with 70/24 < 1.65 need confirmation before they can constrain the faint end of the luminosity function.
- The PBRS "lifetime" varies 16× between clouds, which points to either environment or a recent burst, not a universal phase length.
- A 7 mag cut at 24 µm with 8″ matching could misassign sources in crowded fields. PACS photometry can be affected by blending in nebulous Orion.

## Replication evidence

**Partial.** [[dunham-2014]] (§4.2.3) summarizes the PBRS results with the same numbers (18 PBRS, ~5%, ~25 kyr, 1% vs 17%). [[safron-2015]] uses the HOPS PACS/APEX photometry and modified black-body method from this paper to place the outbursting Class 0 source HOPS 383 against the PBRS (its 70/24 ratio is at the low end of the PBRS range). Later HOPS/ALMA PBRS follow-up papers were not read for this note.

## Why this paper matters

It shows directly that **Spitzer 24 µm cuts miss the reddest protostars** and that far-IR (70 µm) point sources recover them, but only with heavy extragalactic contamination among faint sources. The most reliable new protostars were those with no 3.6–24 µm detection at all. This is the empirical basis for treating "70 µm point source, dark at 24 µm" as a youth signature, and for being cautious about faint 70 µm-only sources.

The PBRS number-ratio duration (~25 kyr) is one of few observational constraints on the length of the earliest Class 0 sub-phase. Its 1% to 17% spread between clouds is a warning against applying a single duration everywhere. The paper also concludes that its candidates are not FHSCs by colour, which narrows where FHSCs might still hide: below PACS sensitivity at Orion's distance.

## Quotes

1. > "we conclude that the PBRs are most likely extreme Class 0 objects" — Abstract
2. > "sources with no short–wavelength detections ... are much less likely to be of extragalactic origin" — §8

## Open questions surfaced

- Are the faint candidates with 70/24 < 1.65 real low-luminosity cold protostars? They would populate the faint end of the protostellar luminosity function (§8).
- Why are PBRS 17× more common in Orion B? Is it a recent burst or an environmental effect on PBRS duration (§5.3)?
- What are the inclinations and outflow opening angles? ALMA and mm line maps are needed to break the density–inclination degeneracy (§7).
- Should nearby Gould Belt clouds hold comparable numbers of very red protostars once Herschel GBS data are analyzed with careful galaxy rejection (§8)?

## Related material in vault

- Extends: [[dunham-2008]]
- Contradicts: —
- Replicates: —
- Concepts introduced/used: [[class-0-protostar]], [[statistical-lifetime]], [[first-hydrostatic-core]], [[internal-luminosity]], [[bolometric-temperature]], [[pacs-bright-red-source]]
- Cites: [[larson-1969]], [[dunham-2008]], [[enoch-2010]], [[pineda-2011]], [[evans-2009]]
- Cited by (in this vault): [[dunham-2014]], [[safron-2015]], [[kristensen-dunham-2018]], [[fischer-2019]], [[lee-2021]], [[zakri-2022]], [[young-2023]], [[furlan-2016]], [[robitaille-2017]]
