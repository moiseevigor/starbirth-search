---
title: "HOPS 383: An Outbursting Class 0 Protostar in Orion"
authors: Emily J. Safron, William J. Fischer, S. Thomas Megeath, Elise Furlan, Amelia M. Stutz, Thomas Stanke, Nicolas Billot, Luisa M. Rebull, John J. Tobin, Babar Ali, Lori E. Allen, Joseph Booker, Dan M. Watson, T. L. Wilson
year: 2015
venue: The Astrophysical Journal Letters, 800, L5 (doi:10.1088/2041-8205/800/1/L5)
url: https://arxiv.org/abs/1501.00492
language: en
domain: astrophysics
status: draft
methodology_type: empirical
citation_count: 71
citation_count_date: 2026-09-26
key_concepts: ["[[accretion-outburst]]", "[[class-0-protostar]]", "[[episodic-accretion]]", "[[luminosity-problem]]"]
extends: []
contradicts: []
replicates: []
cites: ["[[stutz-2013]]", "[[dunham-2008]]", "[[dunham-2014]]", "[[evans-2009]]"]
cited_by: ["[[fischer-2019]]", "[[zakri-2022]]", "[[park-2021]]", "[[furlan-2016]]", "[[lee-2021]]", "[[lu-2024]]"]
quality_notes: "Discovery letter; the outburst is independently recovered in Fischer et al. 2019 (Spitzer vs WISE) and its full ~15 yr light curve is shown in Zakri et al. 2022. Pre-outburst luminosity (0.2 L_sun) is an inference from the 24 um flux ratio, not a measured SED."
author: moiseevigor
tags:
  - agent/research
  - user/moiseevigor
  - domain/astrophysics
  - topic/accretion-outbursts
  - topic/class-0-protostars
  - topic/protostellar-variability
  - topic/spitzer-surveys
  - topic/wise-neowise
  - topic/sed-modeling
  - topic/accretion-luminosity
  - topic/herschel-protostar-surveys
  - paper
  - status/draft
---

# HOPS 383: An Outbursting Class 0 Protostar in Orion

## Abstract

We report the dramatic mid-infrared brightening between 2004 and 2006 of HOPS 383, a deeply embedded protostar adjacent to NGC 1977 in Orion. By 2008, the source became a factor of 35 brighter at 24 µm with a brightness increase also apparent at 4.5 µm. The outburst is also detected in the submillimeter by comparing APEX/SABOCA to SCUBA data, and a scattered-light nebula appeared in NEWFIRM Ks imaging. The post-outburst spectral energy distribution indicates a Class 0 source with a dense envelope and a luminosity between 6 and 14 L⊙. Post-outburst time-series mid- and far-infrared photometry shows no long-term fading and variability at the 18% level between 2009 and 2012. HOPS 383 is the first outbursting Class 0 object discovered, pointing to the importance of episodic accretion at early stages in the star formation process. Its dramatic rise and lack of fading over a six-year period hint that it may be similar to FU Ori outbursts, although the luminosity appears to be significantly smaller than the canonical luminosities of such objects.

## TL;DR

First accretion outburst ever found in a Class 0 protostar: HOPS 383 (Orion) brightened ×35 at 24 µm (MIPS, 2004 → 2008) and by ~2 mag at 4.5 µm, with onset bracketed to 2004 Oct 12 – 2006 Oct 20; post-outburst L ≈ 6–14 L⊙ (best fit 8.7 L⊙) versus an inferred ~0.2 L⊙ before. Extinction clearing is ruled out because the source also brightened in the sub-mm (≥ ×2). It is the anchor event for all later Orion outburst-rate estimates.

## Problem

Protostars are under-luminous relative to steady-accretion expectations (the [[luminosity-problem]]); [[episodic-accretion]] resolves this if mass is delivered in bursts. Before 2015 outbursts were known only in Class II and Class I objects. Can outbursts occur in the earliest, envelope-dominated (Class 0) phase? (§1)

## Approach

- Found in a Spitzer (2004–2005, 3.6/4.5/24 µm) vs WISE (2010, 3.4/4.6/22 µm) comparison of Orion protostars (full search deferred to Fischer et al. 2019) (§2).
- Pre-outburst: SQIID K (2000 Dec 12), IRAC 4.5 µm (2004 Mar 9 & Oct 12), MIPS 24 µm (2004 Mar 20), SCUBA 450 µm (1998) (§2.1).
- Post-outburst: IRS peak-up 15.8/22.3 µm (2006 Oct 20), MIPS 24 µm (2008 Apr 19), NEWFIRM Ks (2009 Nov 25), YSOVAR IRAC 3.6/4.5 µm (81 epochs fall 2009, 11 epochs fall 2010), WISE (2010 Mar & Sep), Herschel/PACS 70/100/160 µm incl. 18 PACS 70 µm epochs 2011 Feb 25 – 2012 Aug 27, APEX SABOCA 350 µm (2011) and LABOCA 870 µm (2010) (§2.2).
- SED fitted with the HOPS grid of 3040 Whitney et al. (2003) radiative-transfer models; goodness-of-fit statistic R = log-deviation in units of fractional uncertainty (§3.2).
- Class 0 diagnostics: L_smm/L_bol (Class 0 if > 0.5%) and bolometric temperature T_bol (Class 0 if < 70 K) (§3.2).

## Key result

Amplitudes by band (§3.1, §3.3, Table 1):

| Band | Pre (date) | Post (date) | Change |
|---|---|---|---|
| 24 µm (MIPS) | 5.34 mJy (2004 Mar 20) | 187 mJy (2008 Apr 19) | "a factor of 35 brighter" |
| 22 µm | — | 80.5 mJy (IRS 2006 Oct 20); 198 mJy (WISE 2010) | IRS 2006 close to 2008 MIPS → onset before 2006 Oct 20 |
| 4.5 µm (IRAC) | 1.30 mJy (2004) | 6.34 mJy (2009 Oct 23) | "the 2 mag jump at 4.5 µm between 2004 and 2009" |
| K / Ks (4.8″ aperture) | 0.374 mJy (2000) | 0.850 mJy (2009) | "an increase of 0.476 mJy at K"; point source undetected both epochs, nebula appears |
| 350/450 µm | SCUBA 450 µm (1998) | SABOCA 350 µm (2011) | source ratio ~4 vs extended ~2.1 → "increase in brightness of ≥ 2" |

- **Timing:** "the outburst began between 2004 October 12 and 2006 October 20, with a subsequent rise in luminosity up to 2008" (§3.1).
- **Luminosity:** post-outburst L_bol = 7.5 L⊙; assuming ΔL equals the ×35 24 µm change → pre-outburst ≈ 0.2 L⊙ (§3.2). Best-fit model total luminosity 8.7 L⊙ (R = 1.7), inclination 41°, cavity 25°; acceptable fits (R < 2.1) span 6–14 L⊙ (§3.2).
- **Class 0 status:** L_smm/L_bol = 1.4%, T_bol = 43 K, modified-blackbody peak 106 µm, envelope mass ≥ 0.2 M⊙ (SED) or 0.7 M⊙ within 4000 AU (870 µm) (§3.2).
- **Post-outburst variability:** YSOVAR 2009 "remarkably constant" (slopes 0.07 mag at 3.6 µm, 0.08 mag at 4.5 µm); 2010 dimming 0.20 mag (3.6) and 0.15 mag (4.5); PACS 70 µm "variability at the 18% level", 13% decline 2010 Sep → 2012 Mar then recovery (§3.3).
- **Distinguishing outburst from extinction change:** ×35 at 24 µm would need a column drop of 1.3×10²³ cm⁻², "an implausible reduction in A_V of 70"; and the sub-mm brightening cannot result from lower extinction (§4).
- **Distinguishing FUor-like from EXor-like:** elevation persisted 2006 → 2012, "inconsistent with the short-term EX Lup events"; no spectrum, so class is not confirmed (§4).

## Assumptions

- Distance 420 pc for all of Orion (§2).
- Nebular contamination in the 4.8″ K aperture is constant between epochs (Table 1 note).
- Fractional change in luminosity ≈ fractional change in 24 µm flux (justified by Dunham et al. 2008 flux–luminosity correlation tightening with wavelength) (§3.2).
- Color corrections: MIPS +5% for red source; WISE −18%, −6.1%, +1.3%, −12% in W1–W4 (§2).

## Limitations / scope

- Single object; no rate estimate here (deferred to [[fischer-2019]]).
- Sparse pre-outburst SED (no pre-outburst 70 µm), so the ×35 luminosity jump is an assumption, and later work ([[zakri-2022]]) finds a far-IR amplitude of only ×9.7 (70–89 µm).
- No near-IR spectrum → FUor vs EXor classification not established.
- Onset window is 2 yr wide; peak epoch unconstrained.

## Replication evidence

Yes — recovered blind by [[fischer-2019]] (Δ = >2.9 / 2.40 / 3.96 mag at 3.6/4.5/24 µm); [[zakri-2022]] shows the full burst (~15 yr, ending by ~2019; 3.6 mag at 4.5 µm) consistent with Grosso et al. (2020) that the outburst ended; [[park-2021]] uses it as one of two spectroscopically confirmed FUor-type protostellar bursts in NEOWISE.

## Why this paper matters

It moved the outburst phenomenon into the Class 0 phase, where most stellar mass is thought to be accreted, and supplied one of two events (with V2775 Ori) on which the ~1000 yr Orion protostellar burst interval rests. It also establishes the diagnostic template used afterwards: multi-band mid-IR brightening plus sub-mm brightening to exclude extinction, and T_bol / L_smm/L_bol to confirm evolutionary class.

## Quotes

1. > "HOPS 383 is the first outbursting Class 0 object discovered" — Abstract
2. > "an implausible reduction in AV of 70" — §4

## Open questions surfaced

- True pre-outburst bolometric luminosity (no far-IR pre-burst data) and hence the real accretion-rate amplification (×35 at 24 µm vs ×9.7 in far-IR later).
- FUor vs EXor nature — requires spectroscopy of a deeply embedded source.
- Why the luminosity (6–14 L⊙) is far below canonical FUor luminosities.

## Related material in vault

- Extends: —
- Contradicts: —
- Replicates: —
- Concepts introduced/used: [[accretion-outburst]], [[class-0-protostar]], [[episodic-accretion]], [[luminosity-problem]]
- Cites: [[stutz-2013]] (PACS Bright Red Sources, Herschel photometry), [[dunham-2008]] (flux–luminosity correlation), [[dunham-2014]] (Class 0 definition), [[evans-2009]] (median luminosities)
- Cited by (in this vault): [[fischer-2019]], [[zakri-2022]], [[park-2021]], [[furlan-2016]], [[lee-2021]], [[lu-2024]]
