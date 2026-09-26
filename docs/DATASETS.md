# Dataset plan

## Tier 0 — target definition

### Hi-GAL physical compact-source catalogue
- Role: parent sample and pre-birth state.
- Bands: 70, 160, 250, 350, 500 um.
- Primary sample: high-reliability prestellar sources.
- Critical metadata to recover: exact Herschel observation date/ObsID for each tile.
- Main systematic: a source labelled starless because it lacks a 70 um counterpart can still hide a faint protostar, especially at larger distances/crowded backgrounds.

## Tier 1 — discovery time series

### WISE / NEOWISE
- W1/W2: 3.4/4.6 um.
- Strategy: IRSA TAP table upload, server-side spatial filtering.
- Do not download the all-sky source database or complete image archive.
- First pass: catalog detections + exposure/epoch coverage.
- Second pass: forced photometry on time-resolved coadds / image cutouts.
- Strength: long time baseline and repeated full-sky coverage.
- Weakness: ~6 arcsec PSF and severe Galactic-plane confusion; deeply embedded newborn protostars can be invisible at 3–5 um.

## Tier 2 — historical and high-resolution checks

### Spitzer GLIMPSE / MIPSGAL
- Role: pre-Herschel baseline, deeper/higher-resolution mid-IR evidence.
- Query cutouts/catal­ogs only.
- Particularly valuable: MIPSGAL 24 um non-detection before the candidate turn-on.

### VVV / VVVX / VIRAC2
- Role: high-cadence/high-resolution near-IR variability where the footprint overlaps.
- Query source and light-curve tables server-side.
- Also inspect reject/transient-prone tables for candidates rather than bulk downloading.

## Tier 3 — confirmation

### SPHEREx
- Role: 0.75–5 um spectral confirmation and continuing monitoring from 2025 onward.
- Useful for spectral/ice/emission-line changes, not the historical 2010s turn-on by itself.

### VLASS
- Role: compact radio source / jet appearance.
- Low cadence but strong independent evidence.

### ALMA / VLA / JCMT / JWST archives
- Role: expensive per-candidate confirmation only.
