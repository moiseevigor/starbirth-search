---
title: "The Spitzer c2d Legacy Results: Star Formation Rates and Efficiencies; Evolution and Lifetimes"
authors: Neal J. Evans II, Michael M. Dunham, Jes K. Jørgensen, Melissa L. Enoch, Bruno Merín, Ewine F. van Dishoeck, Juan M. Alcalá, Philip C. Myers, Karl R. Stapelfeldt, Tracy L. Huard, Lori E. Allen, Paul M. Harvey, Tim van Kempen, Geoffrey A. Blake, David W. Koerner, Lee G. Mundy, Deborah L. Padgett, Anneila I. Sargent
year: 2009
venue: The Astrophysical Journal Supplement Series 181, 321
url: https://arxiv.org/abs/0811.1059
language: en
domain: astrophysics
status: draft
methodology_type: empirical
citation_count: 1270
citation_count_date: 2026-09-26
key_concepts: ["[[statistical-lifetime]]", "[[class-0-protostar]]", "[[prestellar-core]]", "[[luminosity-problem]]", "[[episodic-accretion]]", "[[internal-luminosity]]", "[[bolometric-temperature]]", "[[accretion-luminosity]]"]
extends: ["[[enoch-2008]]"]
contradicts: []
replicates: []
cites: ["[[enoch-2008]]", "[[dunham-2008]]"]
cited_by: ["[[enoch-2008]]", "[[konyves-2015]]", "[[kristensen-dunham-2018]]", "[[contreras-pena-2019]]", "[[contreras-pena-2024]]", "[[dunham-2014]]", "[[enoch-2010]]", "[[fischer-2019]]", "[[furlan-2016]]", "[[kuhn-2021]]", "[[lee-2021]]", "[[lucas-2024]]", "[[park-2021]]", "[[pineda-2011]]", "[[robitaille-2017]]", "[[safron-2015]]", "[[stutz-2013]]", "[[young-2023]]"]
quality_notes: "Highly cited (~1270, Semantic Scholar). This is the standard source of the 'Class II = 2 Myr' reference clock and of the c2d Class 0 (0.10–0.16 Myr) and Class I (0.44–0.54 Myr) lifetimes. Superseded in part by Dunham et al. 2015 (Gould Belt) and challenged by the non-steady-state treatment of kristensen-dunham-2018."
author: moiseevigor
tags:
  - agent/research
  - user/moiseevigor
  - domain/astrophysics
  - topic/evolutionary-lifetimes
  - topic/class-0-protostars
  - topic/prestellar-cores
  - topic/spitzer-surveys
  - topic/yso-catalogs
  - topic/accretion-outbursts
  - topic/accretion-luminosity
  - paper
  - status/draft
---

# The Spitzer c2d Legacy Results: Star Formation Rates and Efficiencies; Evolution and Lifetimes

## Abstract

(Verbatim from the arXiv v1 PDF. The arXiv listing shows an abridged version.)

The c2d Spitzer Legacy project obtained images and photometry with both IRAC and MIPS instruments for five large, nearby molecular clouds. Three of the clouds were also mapped in dust continuum emission at 1.1 mm, and optical spectroscopy has been obtained for some clouds. This paper combines information drawn from studies of individual clouds into a combined and updated statistical analysis of star formation rates and efficiencies, numbers and lifetimes for SED classes, and clustering properties. Current star formation efficiencies range from 3% to 6%; if star formation continues at current rates for 10 Myr, efficiencies could reach 15% to 30%. Star formation rates and rates per unit area vary from cloud to cloud; taken together, the five clouds are producing about 260 M⊙ of stars per Myr. The star formation surface density is more than an order of magnitude larger than would be predicted from the Kennicutt relation used in extragalactic studies, reflecting the fact that those relations apply to larger scales, where more diffuse matter is included in the gas surface density. Measured against the dense gas probed by the maps of dust continuum emission, the efficiencies are much higher, with stellar masses similar to masses of dense gas, and the current stock of dense cores would be exhausted in 1.8 Myr on average. Nonetheless, star formation is still slow compared to that expected in a free fall time, even in the dense cores. The derived lifetime for the Class I phase is 0.54 Myr, considerably longer than some estimates. Similarly, the lifetime for the Class 0 SED class, 0.16 Myr, with the notable exception of the Ophiuchus cloud, is longer than early estimates. If photometry is corrected for estimated extinction before calculating class indicators, the lifetimes drop to 0.44 Myr for Class I and to 0.10 for Class 0. These lifetimes assume a continuous flow through the Class II phase and should be considered median lifetimes or half-lives. Star formation is highly concentrated to regions of high extinction, and the youngest objects are very strongly associated with dense cores. The great majority (90%) of young stars lie within loose clusters with at least 35 members and a stellar density of 1 M⊙ pc^−3. Accretion at the sound speed from an isothermal sphere over the lifetime derived for the Class I phase could build a star of about 0.25 M⊙, given an efficiency of 0.3. Building larger mass stars by using higher mass accretion rates could be problematic, as our data confirm and aggravate the "luminosity problem" for protostars. At a given T_bol, the values for L_bol are mostly less than predicted by standard infall models and scatter over several orders of magnitude. These results strongly suggest that accretion is time variable, with prolonged periods of very low accretion. Based on a very simple model and this sample of sources, half the mass of a star would be accreted during only 7% of the Class I lifetime, as represented by the eight most luminous objects.

## TL;DR

The c2d synthesis (1024 YSOs in five clouds) set the standard statistical lifetimes: **Class I 0.54 Myr (0.44 extinction-corrected), Flat 0.40 (0.35), Class 0 0.16 Myr (0.10), prestellar cores ~0.5 ± 0.1 (±0.3) Myr** at n ≳ 2×10^4 cm^-3. All are anchored to an adopted **Class II lifetime of 2 ± 1 Myr** (interpreted as a half-life) and assume continuous star formation. The same data sharpen the protostellar luminosity problem and argue for episodic accretion.

## Problem

What are the durations of the YSO SED classes (Class 0, I, Flat, II, III) and of the prestellar-core phase, measured in a large, uniformly observed sample rather than in single clouds of 50–100 sources? Earlier estimates ranged from 0.01 Myr for Class 0 (André et al. 1993) to 0.1–0.4 Myr for Class I (§5.2).

## Approach

- **Data** (§1–3): Spitzer IRAC+MIPS photometry of five clouds (Serpens, Perseus, Ophiuchus, Lupus, Cha II), plus Bolocam 1.1 mm maps of three of them (Per, Ser, Oph).
- **Classification**: SED classes by infrared spectral index α (Greene et al. 1994), with and without extinction correction (α′). Class 0 vs. I uses T_bol = 70 K (Chen et al. 1995). Prestellar cores are 1.1 mm cores without a Spitzer source ([[enoch-2008]]).
- **Statistical lifetime** (§5.3): "taking the ratios of number counts in each class, and multiplying by the lifetime for Class II". Earlier phases are bootstrapped. The Class 0+I lifetime (0.54 Myr) is split using the Class 0 / Class I counts among mm-detected sources. Prestellar = (starless cores / embedded protostars) × t(0+I).
- **Reference clock** (§5.3): the Class II duration is set at 2 ± 1 Myr. Evidence: disk-fraction studies (Haisch et al. 2001; Cieza et al. 2007), IC348 ages, Cha II mean age ~2 Myr. The paper stresses that the transition marker is the point where half the stars lack IR excess, so 2 Myr is "best thought of as a half-life".

## Key result

- Class fractions (§5.3): "60% of our YSOs are in Class II, with 16% in Class I, 12% in Flat, and 12% in Class III". With extinction correction: Class I 14%, Flat 9%, Class II 64%.
- Class I / Flat (§5.3): "t(I) = 0.54 Myr, with an additional t(F) = 0.40 Myr". Extinction-corrected: "t′(I) = 0.44 Myr and t′(F) = 0.35 Myr".
- Cloud-to-cloud spread (§5.3): t(I) ranges from "0.2 Myr (Cha II and Lupus) to t(I) = 0.77 Myr in Perseus". Excluding Perseus, ⟨t(I)⟩ = 0.40 Myr.
- Class 0 (§7.1): "a mean lifetime for Class 0 of 0.16 Myr for all three clouds combined". Extinction-corrected t′(0) = 0.10 Myr. Cloud by cloud: "from Ophiuchus with t(0) = 0.043 Myr to Perseus with 0.32 Myr".
- Prestellar (§7.1): t(pre) = 0.46 Myr (extinction-corrected 0.47). Per cloud: 0.23 (Serpens) to 0.78 (Perseus) Myr. With SCUBA (Jørgensen et al. 2008): 0.55 Myr in Perseus, 0.75 Myr in Ophiuchus. Adopted: "about 0.5 ± 0.1(±0.3) Myr" above ~2×10^4 cm^-3, where the parenthetical term is the cloud-to-cloud range.
- **Density dependence** (§7.1, quoting [[enoch-2008]]): for mean densities below and above 2×10^5 cm^-3, the inferred lifetimes are 0.32 Myr and 0.11 Myr. Lifetimes decrease "toward, but not yet reaching, the free-fall time" as density rises.
- T_bol clock (§7.1, from Enoch et al. 2008a): T_bol = 25 K + C (t/10^5 yr)^1.8 with C = 51 K.
- Luminosity problem (§9.2): 59% of Class 0/I sources with mm emission have L_bol < 1.6 L☉, the luminosity expected from standard Shu accretion (2×10^-6 M☉ yr^-1) onto a 0.08 M☉, 3 R☉ protostar. In a toy model, half the final mass accretes during "0.039 Myr (7% of the Class I lifetime)" (§9.3).
- Dense-gas depletion: the current dense cores would be exhausted in 1.8 Myr on average. Total star formation rate (SFR) of the five clouds is ~260 M☉ Myr^-1.

## Assumptions

- The census is complete, and star formation has been "continuous ... at a steady rate for longer than the dwell time in the slowest phase considered" (§5.2).
- All objects of all masses behave identically, with no other variables entering importantly (§5.3). No dependence on core mass (§7.1).
- Class II lifetime is 2 Myr. Every lifetime scales linearly with this value.
- SED class maps onto physical stage (discussed in §5.1, §6; edge-on disks and extinction blur this).
- All starless Bolocam cores are prestellar, i.e., gravitationally bound.

## Limitations / scope

- The authors call the continuous-formation assumption "dubious" (§5.3). A decline in SFR within the last 2 Myr underestimates t(I)/t(F), and a recent increase overestimates them. The cloud-to-cloud scatter (Perseus vs. Cha II/Lupus; Ophiuchus Class 0) is attributed to this.
- The Ophiuchus Class 0 lifetime "rests on three Class 0 sources, two of which are borderline" (§7.1). A star-formation decline "beginning 0.16 Myr ago" would explain it.
- Losing substellar Class II sources to the galaxy-confusion region biases t(I) upward by up to 10–30% (§5.3).
- Stellar ages at these epochs are uncertain by factors of ~2, so the Class II clock is 2 ± 1 Myr.
- The prestellar lifetime applies only to cores dense enough for Bolocam (≳ 2×10^4 cm^-3).
- Class counts from α are sensitive to wavelength range (IRAC-only vs. 2–24 µm fits, §6.1).

## Replication evidence

Partial. The prestellar value agrees with the SCUBA-based estimates of Jørgensen et al. (2008) and Hatchell et al. (2007) (§7.1). Dunham et al. 2015 recomputed the classes for the full Gould Belt (not in vault). [[kristensen-dunham-2018]] re-analyses the Gould Belt counts without steady state and finds half-lives a factor ~2–3 shorter than the steady-state values (Class 0 47 kyr, Class I 88 kyr). [[konyves-2015]] reuses the 2 Myr Class II clock.

## Why this paper matters

This is the reference that fixes the "reference clock" of the whole statistical-lifetime chain: Class II ≈ 2 Myr, interpreted as a half-life. It also produced the widely quoted Class 0 ≈ 0.1–0.16 Myr and Class 0+I ≈ 0.5 Myr durations, overturning the earlier 10^4 yr Class 0 estimate from Ophiuchus. Almost every later lifetime paper in this folder either rescales from it ([[konyves-2015]], [[enoch-2008]]) or argues against its steady-state framing ([[kristensen-dunham-2018]]).

Its second legacy is observational support for the [[luminosity-problem]] and [[episodic-accretion]]. The L_bol spread of 2–3 dex at fixed T_bol practically requires non-steady accretion (§9.2), beginning in Class 0. This links the lifetime question to outburst statistics.

## Quotes

1. > "These lifetimes assume a continuous flow through the Class II phase" — Abstract
2. > "In particular, the continuous formation assumption is dubious." — §5.3

## Open questions surfaced

- How sensitive are the Class 0/I lifetimes to non-steady star formation histories? [[kristensen-dunham-2018]] takes this up.
- Does the Class 0 lifetime vary genuinely between clouds (Ophiuchus 0.043 vs. Perseus 0.32 Myr), or is the variation a star-formation-history artefact?
- How does episodic accretion move sources back and forth across the Class 0/I boundary, and how does that bias class-count lifetimes (§9.3)?
- Is there a mass dependence of prestellar-core lifetimes (Clark et al. 2007 vs. Hatchell & Fuller 2008, §7.1)?

## Related material in vault

- Extends: [[enoch-2008]] (re-derives its prestellar lifetime with the final c2d source list)
- Contradicts: —
- Replicates: —
- Concepts introduced/used: [[statistical-lifetime]], [[class-0-protostar]], [[prestellar-core]], [[luminosity-problem]], [[episodic-accretion]], [[internal-luminosity]], [[bolometric-temperature]], [[accretion-luminosity]]
- Cites: [[enoch-2008]] (as Enoch et al. 2008b), [[dunham-2008]]
- Cited by (in this vault): [[enoch-2008]] (as in prep.), [[konyves-2015]], [[kristensen-dunham-2018]], [[contreras-pena-2019]], [[contreras-pena-2024]], [[dunham-2014]], [[enoch-2010]], [[fischer-2019]], [[furlan-2016]], [[kuhn-2021]], [[lee-2021]], [[lucas-2024]], [[park-2021]], [[pineda-2011]], [[robitaille-2017]], [[safron-2015]], [[stutz-2013]], [[young-2023]]
