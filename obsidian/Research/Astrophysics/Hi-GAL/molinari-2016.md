---
title: "Hi-GAL, the Herschel infrared Galactic Plane Survey: photometric maps and compact source catalogues. First data release for the inner Milky Way: +68° ≥ l ≥ −70°"
authors: S. Molinari, E. Schisano, D. Elia, M. Pestalozzi, A. Traficante, S. Pezzuto, B. M. Swinyard, A. Noriega-Crespo, J. Bally, T. J. T. Moore, et al.
year: 2016
venue: Astronomy & Astrophysics 591, A149
url: https://arxiv.org/abs/1604.05911
language: en
domain: astrophysics
status: draft
methodology_type: methodology
citation_count: 266  # OpenAlex; Semantic Scholar reports 525
citation_count_date: 2026-09-26
key_concepts: ["[[confusion-limit]]", "[[hi-gal-evolutionary-classification]]"]
extends: []
contradicts: []
replicates: []
cites: []
cited_by: ["[[elia-2017]]", "[[elia-2021]]", "[[elia-2022]]"]
quality_notes: "Reference data release: every Hi-GAL clump catalogue and the Hi-GAL SFR estimate are built on these single-band lists. The authors state that no single reliability flag could be defined for DR1 sources."
author: moiseevigor
tags:
  - agent/research
  - user/moiseevigor
  - domain/astrophysics
  - topic/hi-gal
  - topic/massive-clumps
  - topic/survey-completeness-reliability
  - topic/survey-artefacts-and-contamination
  - paper
  - status/draft
---

# Hi-GAL DR1: photometric maps and compact source catalogues (inner Milky Way)

## Abstract

Aims. We present the first public release of high-quality data products (DR1) from Hi-GAL, the Herschel infrared Galactic Plane Survey. Hi-GAL is the keystone of a suite of continuum Galactic Plane surveys from the near-IR to the radio, and covers five wavebands at 70, 160, 250, 350 and 500µm, encompassing the peak of the spectral energy distribution of cold dust for 8 ≲ T ≲ 50K. This first Hi-GAL data release covers the inner Milky Way in the longitude range 68° ≳ ℓ ≳ −70° in a |b| ≤ 1° latitude strip.
Methods. Photometric maps have been produced with the ROMAGAL pipeline, that optimally capitalizes on the excellent sensitivity and stability of the bolometer arrays of the Herschel PACS and SPIRE photometric cameras, to deliver images of exquisite quality and dynamical range, absolutely calibrated with Planck and IRAS, and recovering extended emission at all wavelengths and all spatial scales, from the point-spread function to the size of an entire 2° × 2° "tile" that is the unit observing block of the survey. The compact source catalogues have been generated with the CuTEx algorithm, specifically developed to optimize source detection and extraction in the extreme conditions of intense and spatially varying background that are found in the Galactic Plane in the thermal infrared.
Results. Hi-GAL DR1 images are cirrus-noise-limited, reaching the 1σ-rms predicted by the Herschel Time Estimators for parallel-mode observations at 60″ s−1 scanning speed only in relatively low cirrus emission regions. Hi-GAL DR1 images will be accessible via a dedicated web-based image cutout service. The DR1 Compact Source Catalogues are delivered as single-band photometric lists containing, in addition to source position, peak and integrated flux and source sizes, a variety of parameters useful to assess the quality and reliability of the extracted sources; caveats and hints to help this assessment are provided. Flux completeness limits in all bands are determined from extensive synthetic source experiments and greatly depend on the specific line of sight along the Galactic Plane, due to the greatly varying background as a function of Galactic longitude. Hi-GAL DR1 catalogues contain 123210, 308509, 280685, 160972 and 85460 compact sources in the five bands, respectively.

(Inequality symbols and the arcsecond sign were garbled in the arXiv PDF text layer and are restored here.)

## TL;DR

The Hi-GAL first data release (DR1). It gives calibrated 70/160/250/350/500 µm maps and five single-band CuTEx compact-source lists for the inner Galactic plane (|b| ≤ 1°). The 70 µm band is the most uniform: its completeness is almost constant with longitude. The SPIRE bands lose depth towards the Galactic Centre, where the background is brighter. Read this paper when you need the observing log (tile dates), the 90% flux-completeness limits, or the reliability caveats behind every later Hi-GAL clump or protostar count.

## Problem

Far-IR/sub-mm maps of the Galactic plane from 70 to 500 µm cover the dust SED peak. They can therefore constrain both dust temperature and mass. But compact sources sit on a bright, structured cirrus background, usually brighter than the sources themselves. Threshold-on-intensity and high-pass-filter extraction methods fail there. The paper produces the maps and catalogues and measures their sensitivity, completeness, false-positive behaviour and flux corrections (§1, §4).

## Approach

- **Observations (§2, Table 1).** The survey was split into square tiles of about 2.2°, observed with PACS and SPIRE simultaneously in parallel mode (pMode). Each tile has two nearly orthogonal scan passes, executed back to back. The scan speed was 60″ s⁻¹. PACS/SPIRE sampling rates were 40/10 Hz. On-board co-adding of 8 (70 µm) and 4 (160 µm) frames elongates the PACS PSFs to 5.8″×12.1″ and 11.4″×13.4″. Nominal beams are ≃[6.0, 12.0, 18.0, 24.0, 35.0]″ at [70, 160, 250, 350, 500] µm. The whole survey used slightly more than 900 hours, the largest Herschel programme.
- **Tile dates (Table 1).** DR1 tiles run from ℓ = 290.4° (field "290") to ℓ = 66.0° (field "66"). Dates span 2009-09-03 (tile 299, Performance Verification, OD 112) to 2011-11-05 (OD 905). Two Science Demonstration Phase tiles (30, 59) date from 2009-10-24/23 (OD 163/162). Tiles 303, 305, 312 and 323 are from 2010-01. Most tiles are from 2010-08 to 2010-10 and 2011-02 to 2011-05. Tiles 48, 50, 52, 63 and 66, plus the "30filler" and "59filler" strips, are from 2011-10/11. OD 1 = 14 May 2009. Standard tiles are 2°×2° with scan durations of 9490 s and 10189 s. The three tiles nearest the Galactic Centre (358, 0, 2) used SPIRE "bright-source" mode, which avoids saturation but greatly reduces sensitivity.
- **Map making (§3).** The ROMAGAL generalised-least-squares (GLS) map maker plus weighted post-processing of the GLS maps (WGLS) to remove cross/stripe artefacts. Pixel sizes are [3.2, 4.5, 6.0, 8.0, 11.5]″. Astrometry is tied to Spitzer/MIPSGAL 24 µm, with residual source-coordinate scatter of ~0.9″ (PACS) and ~1.7″ (SPIRE). Zero-point offsets come from Planck/IRIS with DustEM colour corrections.
- **Extraction (§4).** CuTEx (Curvature Thresholding Extractor) runs on second-derivative (curvature) images and fits elliptical Gaussians plus a planar background. The threshold is σc = 2, where σc is in units of the local curvature r.m.s. This value was chosen from synthetic-source runs on tiles at ℓ = 19°, 30° and 59°. The 90% completeness is measured by injecting 1000 sources per band into roughly one tile in every 2–3, iterated 10 times.

## Key result

- **Catalogue counts (Table 2, §4.3).** 123,210 (70 µm), 308,509 (160 µm), 280,685 (250 µm), 160,972 (350 µm), 85,460 (500 µm).
- **Sensitivity (§3.1).** Maps are cirrus-noise-limited for λ ≥ 160 µm. The predicted pMode 1σ instrument noise is reached only in low-cirrus regions, mainly at the ends of the longitude range. At 70 µm the diffuse brightness falls off much faster away from the Galactic Centre.
- **Completeness (§4.4, Figs. 8–9).** 90% completeness in integrated flux depends strongly on longitude. At 70 µm it is almost constant along the plane. At 160 µm it is higher for |ℓ| ≤ 40°. In the SPIRE bands it rises towards the Galactic Centre. Worked example: 3 Jy at 250 µm for the ℓ = 41° tile. The per-tile numbers are shown only in Fig. 9, not in a table. Elia et al. 2017 later quote the extreme 350 µm limits read from this analysis: 13.08 Jy and 0.65 Jy. The authors call the limits conservative, because injected sources were spread over whole tiles, including the bright mid-plane band.
- **Extraction limits (§4.1, §4.5).** Point sources are damped to ~40% in the curvature image and 2.5×PSF sources to ~10%. CuTEx misses most sources larger than 3×PSF and is completely insensitive beyond ~5×PSF. It deblends point-like pairs down to ~0.8 beam and extended pairs beyond ~1.25 beam.
- **Photometric corrections (§4.6).** PACS integrated fluxes are corrected for non-Gaussian pMode PSFs with factors calibrated on α Boo. The catalogue gives both FINT and FINT_UNCORR. The SPIRE corrections stay within 10%. Calibration accuracy is ~5% (PACS) and 4% (SPIRE).
- **Reliability (§5.1).** Most sources have SNR ≥ 3 but rarely above ~10. Source peak flux is typically a factor of a few below the local background. The authors could not define a single quality flag. Detection in ≥ 2 adjacent bands is the best available reliability criterion.
- **Extragalactic contamination (§5.2).** ≤1% at 250 µm, ≤0.7% at 350 µm and ≤0.3% at 500 µm, restricted to F < 0.4 Jy at 250 µm. About 4% at 160 µm, falling to ≤1% after scaling to pMode depth. Negligible at 70 µm.
- **Source sizes (§5.3).** Sizes span 1–2×PSF for most sources. Axis ratios peak at 1.2–1.3. Only the 70 µm band shows a clear peak at the PSF size.
- **Latitude (§6).** The median source latitude is ~−0.06°, below the nominal midplane, in agreement with ATLASGAL.

## Assumptions

- Compact sources are well described by 2-D elliptical Gaussians on a 2nd-order background surface (§4, §4.6).
- Completeness can be characterised from a subset of tiles, using injected sources whose sizes and axis ratios match the extracted population (§4.4).
- The false-positive rate rises faster than the true-detection rate below σc ≈ 2. This is inferred from the change of slope in the N–σc relation plus earlier simulations. It is not measurable on the real maps (§4.2).

## Limitations / scope

- DR1 covers only 68° ≳ ℓ ≳ −70°, |b| ≤ 1°. The outer Galaxy came in later releases (used by [[elia-2021]]).
- There is no reliability flag. Sources below SNR 3 can be real, and high-SNR sources can have low contrast (§5.1).
- Completeness is quoted per band and per longitude, not per background level within a tile. Sources more than 0.3–0.4° off the midplane are detected below the quoted limits.
- The three Galactic-Centre tiles have much shallower SPIRE data because of bright-source mode.
- The extraction is blind to structures larger than ~3–5×PSF, so extended clumps and filaments are excluded by construction.
- I read the full arXiv v1 text. The per-tile completeness values (Fig. 9) were not extractable as numbers.

## Replication evidence

Partial. The later 360° extension (Molinari et al., in prep. at the time; used by [[elia-2021]]) applied the same pipeline and extraction. No independent re-extraction of Hi-GAL was examined here.

## Why this paper matters

This is the foundation for every Hi-GAL-based count of prestellar and protostellar clumps. The "70 µm-detected = protostellar" rule of [[hi-gal-evolutionary-classification]] depends on the depth of this 70 µm catalogue. Here the 70 µm catalogue is the most uniform band in longitude. The SPIRE bands, which set whether a clump enters the physical catalogue at all, degrade strongly towards the inner Galaxy. The observing log (Table 1) dates each tile to 2009–2011, which fixes the epoch of Hi-GAL fluxes for any comparison with later data.

## Quotes

1. > "there is no easy shortcut to identify the most reliable sources" — §5.1
2. > "Hi-GAL DR1 images are cirrus-noise-limited" — Abstract

## Open questions surfaced

- The authors suggest pushing the PACS threshold below σc = 2, especially at low |ℓ|. How many real faint 70 µm sources (low-luminosity protostars) would that recover, and at what false-positive cost?
- The authors propose a machine-learning reliability classifier trained on expert inspection (§5.1). It was not built in this paper.
- Completeness as a function of local background within a tile, promised for later releases.

## Related material in vault

- Extends: none
- Contradicts: none
- Replicates: none
- Concepts introduced/used: [[confusion-limit]], [[hi-gal-evolutionary-classification]]
- Cites: none in this vault list
- Cited by (in this vault): [[elia-2017]], [[elia-2021]], [[elia-2022]]
