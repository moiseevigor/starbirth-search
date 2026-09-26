# starbirth-search

Search archival time-domain surveys for the transition from a Hi-GAL prestellar core to a newly formed protostar.

## Scientific target

The project searches for sources that are consistent with being prestellar (or first-hydrostatic-core-like) at the Herschel/Hi-GAL epoch and later develop a persistent compact infrared source, with optional radio/sub-mm corroboration.

The primary hypothesis test is:

- **H0:** no persistent protostar turn-on; variability/confusion/noise only.
- **H1:** a persistent change point appears after the Hi-GAL epoch and is spatially associated with the cold core.
- **Hburst:** an already-existing protostar underwent an accretion burst.

The discovery pipeline is deliberately staged so that the full NEOWISE image archive is never downloaded.

## Pipeline

1. Build the high-reliability Hi-GAL prestellar target list (~49k objects).
2. Recover the exact Herschel observation epoch per target/tile.
3. Query WISE/NEOWISE measurements server-side around those coordinates.
4. Build per-target W1/W2 light curves and upper-limit/coverage records.
5. Rank persistent post-Herschel change points.
6. Run forced photometry and difference imaging only for the top candidates.
7. Add Spitzer, VVV/VVVX, SPHEREx, and VLASS evidence.
8. Compare `birth` vs `accretion_burst` vs `confusion/artifact` hypotheses.

## First numerical experiment

`starbirth.experiments.synthetic_turnon` generates WISE-like cadence, injects a persistent turn-on into noisy data, and applies a weighted change-point scan. It is intended to answer:

> For a given post-birth flux jump and noise level, how often can the pipeline recover the event while controlling false alarms?

Run:

```bash
python -m starbirth.experiments.synthetic_turnon --trials 5000 --seed 42
```

## Environment

Python 3.11+.

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e '.[dev]'
pytest
```

The catalog phase is CPU/I/O-oriented. Later image experiments can use PyTorch MPS on Apple Silicon or CUDA on NVIDIA GPUs.

See:
- `docs/EXPERIMENTS.md`
- `docs/DATASETS.md`
- `docs/COMPUTE.md`
