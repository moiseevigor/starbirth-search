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

Python 3.11+ (native arm64 on Apple Silicon — the system `python3` may be an old x86 build).

```bash
uv venv -p 3.12 .venv
uv pip install -p .venv -e '.[dev,research]'
.venv/bin/python -m pytest
```

## Layout

- `src/starbirth/` — library code; `glossary.py` is the single source of term definitions (-> `docs/GLOSSARY.md`)
- `research/` — experiment drivers (E-1, E1-pilot) and report writers
- `scripts/` — entry points / benchmarks · `tests/` — tests · `configs/` — run configs
- `docs/` — reports (`FEASIBILITY.md`, `LITERATURE.md`, …) with figures in `docs/figures/`
- `artifacts/` — machine outputs (CSV tables); `cache/` — gitignored downloads (Hi-GAL catalogue)

## Findings viewer

`viewer/index.html` is a standalone page with every result and real telescope imagery:
funnel, sky map of all 94,604 clumps, candidate explorer (NEOWISE light curves, per-visit
W2 image stacks and difference images, multi-survey cutouts), artefact gallery, experiment
charts, literature timescales and the paper library. Rebuild with
`.venv/bin/python research/build_viewer.py` (needs network for IRSA/CDS imagery), then open
`viewer/index.html` in a browser.

## Review desk (local)

A browsable classification catalog of all 19,219 searched clumps and a gallery of every
flagged birth-start candidate (with offset controls), each with its full evidence and a
review form. Decisions are saved to `reviews/reviews.jsonl` (append-only).

```bash
.venv/bin/python research/build_catalog.py      # after research/e7b_symmetric.py tier1/tier2/analyze
.venv/bin/python scripts/serve_catalog.py       # then open http://127.0.0.1:8792/catalog.html
```

## Current status

- **E1 full run** (19,219 prestellar clumps, 0 < d <= 4 kpc, NEOWISE 2014-2024): 4 persistent W2
  turn-ons (1 in the 60" offset control, a deblending artefact). All 4 had a young star already
  (Spitzer SPICY / AllWISE), i.e. accretion outbursts or large-amplitude variability, not births.
- **Literature** (`obsidian/`, 36 papers + synthesis): collapse models keep a newborn protostar
  dark at 3-5 um for ~1e4 yr, so a W1/W2 archive search is a burst search, not a birth search.
- Details: `docs/FEASIBILITY.md`, `docs/LITERATURE.md`, `viewer/index.html`.
