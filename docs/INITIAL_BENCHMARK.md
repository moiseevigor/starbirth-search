# Initial synthetic benchmark

The first implementation used a naive change-point scan and was too slow. It was replaced by a prefix-sum implementation whose work is linear in the number of light-curve samples.

A 3,000-trial-per-amplitude synthetic run (21 NEOWISE-like epochs x 12 exposures, Delta-BIC threshold 20) produced:

| injected persistent step | detection rate | localization within one epoch |
|---:|---:|---:|
| 0.0 sigma | 0.0000 | 0.0000 |
| 0.5 sigma/exposure | 0.0563 | 0.0430 |
| 1.0 sigma/exposure | 0.9583 | 0.9180 |
| 1.5 sigma/exposure | 1.0000 | 0.9963 |
| 2.0 sigma/exposure | 1.0000 | 0.9997 |
| 3.0 sigma/exposure | 1.0000 | 1.0000 |
| 5.0 sigma/exposure | 1.0000 | 1.0000 |

This is **not an astrophysical sensitivity result**. The simulation presently assumes independent Gaussian noise and a perfect permanent step. Real Galactic-plane data have crowding, correlated systematics, missing observations, blends, upper limits, artifacts, and astrophysical variables. The table is only a software/sanity benchmark and motivates E0/E2 injection-recovery calibration on real backgrounds.

The entire 21,000-curve run completed in about 2.85 s on the development runtime after the O(n) rewrite. Use `scripts/benchmark_host.py` on the target Mac to obtain a real M2 throughput number.
