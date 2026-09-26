# Numerical experiments

## E0 — Pipeline sanity and synthetic false-alarm calibration

Goal: determine a detection threshold before looking at unknown objects.

1. Simulate NEOWISE-like cadence.
2. Inject persistent steps spanning 0–5 sigma per exposure.
3. Add heteroscedastic noise, missing epochs, upper limits, and correlated epoch systematics.
4. Measure detection completeness, change-time error, and false-positive rate.
5. Repeat after adding nuisance models: sinusoidal variables, one-epoch flares, slow drifts, centroid contamination.

Deliverable: threshold table `P(detect | amplitude, cadence, confusion)` and a target false discovery rate.

## E1 — Catalog-level full-sample search

Parent sample: Hi-GAL high-reliability prestellar objects.

For each target:
- attach exact Herschel observation time;
- query WISE/NEOWISE detections within a conservative radius;
- form ~6-month epoch bins (and preserve single exposures for shortlisted sources);
- estimate local crowding and centroid stability;
- fit constant, persistent-step, monotonic-ramp, flare/outburst, and periodic nuisance models;
- rank by model evidence / BIC plus persistence.

This experiment should run before any GPU-heavy work.

## E2 — Injection/recovery in real Galactic-plane images

For a stratified sample of real backgrounds:
- select empty locations near the Hi-GAL targets;
- inject PSF-shaped sources with W1/W2 colors and rise times;
- process with the same forced-photometry and difference-imaging code;
- measure completeness as a function of background, crowding, flux, and distance from bright neighbors.

This is the experiment where MPS/CUDA acceleration is worthwhile.

## E3 — Candidate forced photometry

Top ~1,000 E1 candidates:
- fetch 64x64 or 96x96 W1/W2 epoch cutouts;
- fit scene model jointly across epochs;
- hold neighbor positions fixed while allowing candidate flux to vary;
- compare direct aperture/PSF photometry with difference imaging;
- require spatially stable emergence at the core location.

## E4 — Historical vetoes

For top ~100:
- Spitzer GLIMPSE/MIPSGAL pre-event search;
- WISE 2010 W3/W4 where available;
- VVV/VVVX histories;
- SIMBAD/Gaia/2MASS source and variability checks;
- reject known YSOs or evidence for an already-existing protostar.

## E5 — Multi-wavelength confirmation

For top ~10:
- VLASS epoch comparison for a new compact radio source;
- ALMA/VLA/JCMT/JWST archive search;
- SED before/after reconstruction;
- fit explicit competing models `birth` vs `accretion burst`.

## E6 — Population-level null result

Even if no robust birth is found, injection/recovery gives a quantitative upper limit on the rate of observable prestellar-to-protostar transitions in the surveyed sample.
