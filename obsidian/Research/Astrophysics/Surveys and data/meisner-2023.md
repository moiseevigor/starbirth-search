---
title: "unTimely: a Full-sky, Time-domain unWISE Catalog"
authors: Aaron M. Meisner, Dan Caselden, Edward F. Schlafly, Frank Kiwy
year: 2023
venue: The Astronomical Journal, 165, 36 (doi:10.3847/1538-3881/aca2ab)
url: https://arxiv.org/abs/2209.14327
language: en
domain: astrophysics
status: draft
methodology_type: methodology
citation_count: 41
citation_count_date: 2026-09-26
key_concepts: ["[[confusion-limit]]"]
extends: ["[[mainzer-2014]]"]
contradicts: []
replicates: []
cites: ["[[mainzer-2014]]"]
cited_by: ["[[lucas-2024]]"]
quality_notes: "Catalog/data-release paper; completeness and reliability are calibrated only in COSMOS (high Galactic latitude, |beta| = 10.1 deg), so Galactic-plane performance is not measured. Citation count from Semantic Scholar."
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

# unTimely: a Full-sky, Time-domain unWISE Catalog

## Abstract

We present the unTimely Catalog, a deep time-domain catalog of detections based on Wide-field Infrared Survey Explorer (WISE) and NEOWISE observations spanning the 2010 through 2020 time period. Detections are extracted from 'time-resolved unWISE coadds', which stack together each biannual sky pass of WISE imaging to create a set of ∼16 all-sky maps (per band), each much deeper and cleaner than individual WISE exposures. unTimely incorporates the W1 (3.4 μm) and W2 (4.6 μm) channels, meaning that our data set effectively consists of ∼32 full-sky unWISE catalogs. We run the crowdsource crowded-field point source photometry pipeline on each epochal coadd independently, with low detection thresholds: S/N = 4.0 (2.5) in W1 (W2). In total, we tabulate and publicly release 23.5 billion (19.9 billion) detections at W1 (W2). unTimely is ∼1.3 mag deeper than the WISE/NEOWISE Single Exposure Source Tables near the ecliptic, with further enhanced depth toward higher ecliptic latitudes. The unTimely Catalog is primarily designed to enable novel searches for faint, fast-moving objects, such as Y dwarfs and/or late-type (T/Y) subdwarfs in the Milky Way's thick disk or halo. unTimely will also facilitate other time-domain science applications, such as all-sky studies of quasar variability at mid-infrared wavelengths over a decade-long time baseline.

## TL;DR

Per-sky-pass (≈6-monthly) unWISE coadds of W1/W2 from 2010–2020, catalogued independently per epoch with crowdsource PSF photometry. Quantified depth in COSMOS: per-epoch 50% completeness W1 = 17.14, W2 = 16.08 mag (Vega) vs 16.48 / 14.94 for NEOWISE single exposures; 90% reliability 16.81 / 15.34 vs 15.35 / 13.55. Key caveats for Galactic-plane YSO light curves: epoch-to-epoch deblending changes (spurious variability), nebulosity decomposed into point sources (flag via HAS_ANY_NEBULOSITY), ~2% first-epoch zero-point offset, astrometry uncalibrated to Gaia (systematics up to ~250 mas).

## Problem

WISE/NEOWISE single-exposure (L1b) source tables are shallow and contaminated by cosmic rays and satellite streaks, while static full-depth coadd catalogs (unWISE, CatWISE) smear out fast motion and variability. Is there a catalog that trades sub-day time resolution for ~1.3 mag of depth while preserving the ~6-month cadence over a decade?

## Approach

- **Input** (§II): "time-resolved unWISE coadds" — all ≳12 single exposures per sky location in each ~6-month sky pass stacked into one coadd epoch per band. Tiles are 2048 × 2048 pixels at 2.75″/pix (1.56° on a side, 2.45 deg²). Data span 2010 January – 2020 December 13; "Most sky locations have a time baseline of 10.5 years", with the 2011–2013 hibernation gap.
- **Epochs** (§II): typically 16 coadd epochs per band; "never fewer than 15"; up to 295 near the ecliptic poles. 616,838 single-band coadds, ≈33.8 all-sky equivalents over 18,240 tile footprints. 15-epoch longitudes are those hit by the 2014 April WISE command-timing anomaly (Fig. 1).
- **Photometry** (§III): crowdsource crowded-field PSF photometry run independently on each coadd (no forced photometry, no multi-band). Detection thresholds S/N = 4.0 (W1), 2.5 (W2). Unlike the unWISE Catalog, the neural-network nebulosity classifier was **not** used, so FLAGS_INFO bit 25 (nebulosity) is always 0.
- **Completeness / reliability** (§IV): comparison with Spitzer S-COSMOS (FWHM ≈ 1.7″), 2″ cross-match radius. *Differential completeness* = fraction of truth-catalog sources in a narrow magnitude bin recovered by unTimely; *differential reliability* = fraction of unTimely detections in a narrow unTimely-magnitude bin that have a counterpart in the deeper truth catalog (footnote 5). Compared with WISE/NEOWISE L1b tables using the "moderate filtering" (w?frtr like '00%') approach.
- **Zero points** (§V): bright unsaturated stars (W1 9.5–10.5, W2 8.7–10.5 mag; FLAGS_UNWISE = 0, FLAGS_INFO = 0, FRACFLUX > 0.99, PRIMARY = 1) in four COSMOS tiles (~10 deg²); per-epoch median flux ratio to static unWISE Catalog.

## Key result

Depth (§IV, COSMOS, Vega mag):

| Quantity | unTimely W1 | unTimely W2 | NEOWISE L1b W1 | NEOWISE L1b W2 |
|---|---|---|---|---|
| 50% differential completeness | 17.14 | 16.08 | 16.48 | 14.94 |
| 90% differential reliability | 16.81 | 15.34 | 15.35 | 13.55 |

- "unTimely pushes 0.66 mag (1.14 mag) fainter than the Single Exposure Source Tables in terms of 50% completeness in W1 (W2), and 1.46 mag (1.79 mag) fainter in terms of 90% reliability." Gains grow with |β| because frame coverage per pass increases (COSMOS is at |β| = 10.1°), except very near the ecliptic poles (|β| > 80°) where some epochs have low/zero coverage (§IV).
- The nominal coadd gain is "∼1.3 magnitudes (2.5×log10√12)" (§I).

Volume (§III): 43,459,534,445 detections — 23,538,460,814 (W1), 19,921,073,631 (W2); median per coadd 56,010 (W1) / 50,574 (W2); max 272,062 / 238,767. W1 source density ~18% higher than W2 overall; Galactic plane clearly visible in density maps (Fig. 2). 226,620 CPU hours; 4.3 TB release (§VII).

Photometric stability (§V):
- First WISE sky pass: W1 (W2) bright stars "∼1.8% (∼2.5%) brighter than in all following sky passes, which remain consistent with one another at the ≲1% level." Bright-end scatter ≲1%. Users needing zero-point consistency better than ±2% (±3%) in W1 (W2) should compute per-(band, epoch, coadd_id) recalibration offsets.

Nebulosity / artefact flags (§VII–VIII):
- Nebulosity is supplied in the index table as NEBULOSITY_BITMASK (8 × 8 grid of 256 × 256-pix patches per tile, from the 6-year unWISE Catalog mask) and HAS_ANY_NEBULOSITY; "9.5% of all unTimely epochal catalogs correspond to a coadd_id with at least one of its 64 sectors affected by nebulosity." Because crowdsource "attempts to aggressively decompose nebulosity into a sum of point sources, which are likely deblended differently from one epoch to the next", avoiding HAS_ANY_NEBULOSITY = 1 is advised for rare-object searches and population studies.
- Residual cosmic rays: for S/N > 10 sources in uncrowded fields, "SPREAD_MODEL < −0.021 identifies residual cosmic ray imprints reasonably well."
- FLAGS_INFO bit 21 marks overlap with large (d25 ≳ 7″) HyperLeda galaxies.
- Low/zero coverage: use NM and index columns N_PIX_COV[0-2] / FRAC_COV[0-2].
- Astrometry inherits L1b astrometry, not recalibrated to Gaia; "These astrometric systematics can reach levels of up to ∼250 mas per coordinate."
- No cross-epoch or cross-band object grouping in the release.
- Data release excludes 2021 NEOWISE year (released 2022 March).

## Assumptions

- COSMOS (high Galactic latitude, near ecliptic) is "representative of 'typical' sky locations" (§IV) — explicitly not representative of the Galactic plane.
- Sub-day variability is sacrificed; each epoch is an average over the ~1-day pass. Motion within a pass is negligible (10″/yr → 27 mas smear per epoch; §VI.1.1).
- Point-source-only modelling (no extended profiles) (§VIII).

## Limitations / scope

- No completeness/reliability measurement in crowded or nebulous Galactic-plane fields — the regime where protostars live. The 9.5% nebulosity statistic is sky-wide; the affected fraction in the plane will be much higher (not quantified in paper).
- Independent per-epoch detection means light curves of near-threshold sources are subject to selection bias: detections are more likely when the source is brighter or noise fluctuates upward (§VIII) — relevant for burst searches using non-detection → detection transitions.
- Deblending differs between epochs → "spurious variability signatures in light curves" (§VIII); requires visual checks (WiseView recommended).
- Low S/N thresholds (W2 2.5σ) imply many spurious detections at the faint end unless users cut (e.g. S/N > 5).
- Read in full via arXiv HTML; figures inspected via captions only.

## Replication evidence

No independent replication within this vault; the depth comparison is internal to the authors (using NEOWISE team completeness data supplied by R. Cutri). [[lucas-2024]] uses the catalog in a Galactic-plane VVV-variability context (cites it).

## Why this paper matters

For multi-epoch mid-IR searches, unTimely defines the practical trade-off between the NEOWISE L1b single-exposure tables (sub-day sampling, shallow, artefact-prone) and per-epoch coadds (≈1 mag deeper, cleaner, ~6-monthly). Its explicit caveat list — epoch-dependent deblending, nebulosity shredding, zero-point offset of the first pass, Gaia-uncalibrated astrometry — is effectively a checklist of false-positive sources for any variable/transient search in dusty star-forming regions.

## Quotes

1. > "unTimely Catalog deblending can be different from one epoch to another" — §VIII
2. > "it may be advisable to avoid catalogs with HAS_ANY_NEBULOSITY = 1" — §VII

## Open questions surfaced

- What are unTimely's completeness and reliability in the Galactic plane (|b| < 1°), in nebulous vs non-nebulous patches, measured against GLIMPSE/Spitzer truth?
- How large is the spurious-variability rate (fraction of stationary sources with epoch-to-epoch ΔW2 > X mag from deblending alone) in crowded fields?
- Can forced photometry at fixed positions (suggested in §IX) suppress deblending-driven false variability for YSO light curves?
- Per-epoch zero-point recalibration table (proposed, not provided; §V, §VIII).

## Related material in vault

- Extends: [[mainzer-2014]]
- Contradicts: —
- Replicates: —
- Concepts introduced/used: [[confusion-limit]]
- Cites: [[mainzer-2014]]
- Cited by (in this vault): [[lucas-2024]]
