---
title: "Initial Performance of the NEOWISE Reactivation Mission"
authors: A. Mainzer, J. Bauer, R. M. Cutri, T. Grav, J. Masiero, R. Beck, P. Clarkson, T. Conrow, J. Dailey, P. Eisenhardt, B. Fabinsky, S. Fajardo-Acosta, J. Fowler, C. Gelino, C. Grillmair, I. Heinrichsen, M. Kendall, J. Davy Kirkpatrick, F. Liu, F. Masci, H. McCallon, C. R. Nugent, M. Papin, E. Rice, D. Royer, T. Ryan, P. Sevilla, S. Sonnett, R. Stevenson, D. B. Thompson, S. Wheelock, D. Wiemer, M. Wittman, E. Wright, L. Yan
year: 2014
venue: The Astrophysical Journal, 792, 30 (doi:10.1088/0004-637X/792/1/30)
url: https://arxiv.org/abs/1406.6025
language: en
domain: astrophysics
status: draft
methodology_type: empirical
citation_count: 291
citation_count_date: 2026-09-26
key_concepts: ["[[confusion-limit]]"]
extends: []
contradicts: []
replicates: []
cites: []
cited_by: ["[[meisner-2023]]", "[[park-2021]]", "[[lucas-2024]]", "[[lu-2024]]"]
quality_notes: "Mission-status paper written after ~3 months of reactivated operations; the solar-system science is the focus and the astrophysical data-quality numbers are mostly shown only as figures (single-exposure completeness, photometric RMS). Citation count is Semantic Scholar's (likely an undercount vs ADS). The operational reference for source-level quality flags (cc_flags, ph_qual, w?frtr, moon_masked, etc.) is the NEOWISE Explanatory Supplement (Cutri et al.), not this paper."
author: moiseevigor
tags:
  - agent/research
  - user/moiseevigor
  - domain/astrophysics
  - topic/wise-neowise
  - topic/time-domain-surveys
  - topic/survey-completeness-reliability
  - topic/survey-artefacts-and-contamination
  - paper
  - status/draft
---

# Initial Performance of the NEOWISE Reactivation Mission

## Abstract

NASA's Wide-field Infrared Survey Explorer (WISE) spacecraft has been brought out of hibernation and has resumed surveying the sky at 3.4 and 4.6 μm. The scientific objectives of the NEOWISE reactivation mission are to detect, track, and characterize near-Earth asteroids and comets. The search for minor planets resumed on December 23, 2013, and the first new near-Earth object (NEO) was discovered six days later. As an infrared survey, NEOWISE detects asteroids based on their thermal emission and is equally sensitive to high and low albedo objects; consequently, NEOWISE-discovered NEOs tend to be large and dark. Over the course of its three-year mission, NEOWISE will determine radiometrically-derived diameters and albedos for ∼2000 NEOs and tens of thousands of Main Belt asteroids. The 32 months of hibernation have had no significant effect on the mission's performance. Image quality, sensitivity, photometric and astrometric accuracy, completeness, and the rate of minor planet detections are all essentially unchanged from the prime mission's post-cryogenic phase.

## TL;DR

The reference paper for the NEOWISE-R (reactivation, from 2013 Dec) W1 (3.4 μm) / W2 (4.6 μm) survey. It fixes the cadence every NEOWISE-based variability study inherits — 7.7 s exposures every 11 s, ~12 exposures per sky position spread over ~1.5 days, every ~6 months, whole sky six times in the planned three years — and shows that photometry, astrometry (~0.67″) and single-exposure completeness match the 2010–2011 post-cryogenic phase. It gives no numerical per-exposure depth in the text (figure only); use [[meisner-2023]] for quantified L1b and per-epoch coadd depths.

## Problem

After 32 months of hibernation (warming to ~200 K), could WISE be passively re-cooled and resume a 3.4/4.6 μm survey with unchanged data quality, and what is the survey design and early performance of the NEOWISE reactivation?

## Approach

- Re-cooling by pointing near zenith from October 2013; telescope reached 74 K after ~3 months; first images 2013 Dec 7 at 76.5 K; regular survey with moving-object pipeline from 2013 Dec 23 (§II).
- Survey strategy unchanged from the prime mission: continuous great-circle scans at roughly constant ecliptic longitude, with a scan mirror freezing the sky on the focal planes (§II).
- Performance checks (§III.1): (i) W1/W2 profile-fit magnitudes in single exposures compared with the deeper AllWISE Catalog; (ii) positions compared with AllWISE; (iii) WISE Multiframe pipeline run on Atlas Tile 0368m197 (covered in both post-cryo and reactivated phases), restricted to sources with >10 exposure coverages, to compare photometric repeatability (RMS of single-exposure fluxes) and single-exposure completeness.
- **Single-exposure completeness** is defined in §III.1 as, per 0.2 mag bin, the ratio of the total number of times sources are detected with SNR > 2 to the total number of times they are observed.
- Astrometric precision independently measured from residuals of fits to numbered minor planets (§IV).

## Key result

Survey design / cadence (§II, §III):
- "a scan mirror freezes the sky on the focal planes for 9.9 seconds and returns to its starting position 1.1 seconds later"; simultaneous W1+W2 exposures "every 11 seconds with an exposure time of 7.7 seconds" (§II).
- "The 47x47 arcmin field of view scans at 92.5∘ solar elongation, with 10% overlaps in the in-scan direction. The scan path progresses 1∘/day" (§II).
- "On average, twelve independent exposures are collected for each point on the ecliptic"; ecliptic poles are densely covered (§II).
- Observing cadence gives "an average of ∼12 detections spaced evenly over ∼1.5 days" (§III); minor planets typically "∼10-12 observations spaced evenly over ∼36 hours" (§III.1).
- "Over the course of the three-year NEOWISE mission, the entire sky will be observed six times at 3.4 and 4.6 μm" (§III). (The mission was later extended; see [[meisner-2023]], which uses data to 2020 Dec.)
- First 3 months: coverage at least one frame deep over 60% of the sky (Dec 23, 2013 – Mar 30, 2014; §II, Fig. 5).
- Processing: only single-exposure processing is performed for NEOWISE; the scan/frame pipeline "flags sources that are positionally associated with the expected position of image artifacts" (§II) — this is the origin of the per-source artefact flags in the NEOWISE Single-Exposure Source Table.

Instrument / data quality (§III.1):
- Masked high-dark-current pixels: "3.3% and 4.3% of pixels in bands W1 and W2" after reactivation vs "1.9% and 2.5%" in the post-cryogenic phase.
- Photometric zero points: "essentially no shifts in zero points for either band or flux-dependent biases over most of the brightness range" vs AllWISE; W2 shows a systematic deviation of "0.03-0.04 mag" over "7<W2<14 mag"; "Systematic changes in W1 are <0.01 mag".
- Saturation: "dramatic flux overestimation of NEOWISE fluxes brighter than the saturation levels", consistent with the post-cryogenic phase (numbers not given in text).
- Faint end: the systematic overestimation at the faint end relative to AllWISE is the Eddington bias — noise-driven upward scatter preferentially lifts faint sources over the detection threshold, so measured fluxes near threshold are biased high (§III.1).
- No RA/Dec offsets vs AllWISE as a function of W1 (Fig. 7).
- Photometric repeatability and single-exposure completeness "essentially identical" to the post-cryogenic phase (Figs. 8–9; values only graphical).

Astrometry (§IV):
- Residuals of fits to numbered minor planets: "the root sum square of the medians of these, ∼0.67 arcsec, is identical to that observed during all phases of the prime mission."

Confusion (§IV):
- "The NEO detection rate has been lowered due to the effects of confusion in the galactic plane in March 2014"; minor-planet detections decrease while the scan circle crosses the Galactic Center (Fig. 11).

## Assumptions

- Data quality assessed on a single Atlas tile (0368m197) and one reactivated scan (Figs. 6–8); generalisation to the whole sky, and in particular to the Galactic plane, is assumed rather than tested.
- Completeness defined with an SNR > 2 per-exposure detection criterion (§III.1), a lower threshold than typical catalogue-quality cuts.
- Passive cooling assumed to keep dark current approximately stable; the paper notes dark current "could change slightly if temperature varies with seasons" (§III.1).

## Limitations / scope

- Solar-system focused: stellar-variability use is mentioned only as a future application (§III).
- No numerical per-exposure 5σ limits, saturation magnitudes, or completeness magnitudes in the text — only figures (Figs. 6, 8, 9). Researcher did not digitise figures.
- Quality-flag semantics (cc_flags diffraction spikes / persistence / halos / ghosts, ph_qual, moon masking, SAA) are not described here; they are in the NEOWISE Explanatory Supplement, not ingested in this vault.
- Galactic-plane performance (source confusion, nebulosity, saturation of bright YSOs) is only noted as reducing NEO detection rates; not quantified for stationary sources.
- Early-mission snapshot (first ~90 days); later degradation (orbit drift, increased scattered light, end of mission) is outside scope.
- Read in full via arXiv HTML (v1, text + captions); tables of NEO photometry not examined.

## Replication evidence

Partial / indirect. The data-quality claims were re-examined by later users: [[meisner-2023]] measured NEOWISE Single Exposure (L1b) Source Table 50% differential completeness of 16.48 mag (W1) / 14.94 mag (W2) and 90% reliability of 15.35 / 13.55 mag in COSMOS, and found a ~2% zero-point offset of the very first WISE sky pass relative to later passes — consistent with, but more quantitative than, this paper's "no zero-point shift" statement. Multi-year NEOWISE light-curve studies ([[park-2021]], [[lucas-2024]]) rely on the cadence described here.

## Why this paper matters

This is the canonical citation for the NEOWISE reactivation data stream that underpins almost all decade-baseline mid-IR variability work (protostellar bursts, YSO variability, AGN, brown-dwarf motion). Its value for star-formation work is operational: it fixes the sampling function (~12 exposures within ~1–1.5 days, repeated at ~6-month intervals), the precision floor (~0.67″ astrometry, ≲0.04 mag photometric systematics), and flags two failure modes relevant to the Galactic plane — confusion and saturation-driven flux overestimation — plus Eddington bias at the faint end.

It does not provide the quantitative depth numbers; for those, the unWISE/unTimely work ([[meisner-2023]]) and the NEOWISE Explanatory Supplement are the working references.

## Quotes

1. > "The 32 months of hibernation have had no significant effect on the mission's performance." — Abstract
2. > "the root sum square of the medians of these, ∼0.67 arcsec" — §IV

## Open questions surfaced

- What are the single-exposure W1/W2 completeness and reliability limits in the Galactic plane (|b| < 1°), where confusion and nebulosity dominate, as opposed to the high-latitude test tile used here?
- How much does the ~6.5″ PSF blend close YSO pairs and clustered protostars in single exposures, and how does that bias multi-epoch amplitude estimates?
- At what W1/W2 magnitudes do saturation-driven flux overestimates begin, and how do they propagate into bright-YSO light curves?
- How does the faint-end Eddington bias propagate into variability amplitudes for sources near threshold (cf. the selection-bias caveat in [[meisner-2023]] §VIII)?

## Related material in vault

- Extends: —
- Contradicts: —
- Replicates: —
- Concepts introduced/used: [[confusion-limit]]
- Cites: —
- Cited by (in this vault): [[meisner-2023]], [[park-2021]], [[lucas-2024]], [[lu-2024]]
