# Compute plan

## Principle

Move spatial filtering to the survey archives. The laptop should receive only rows/cutouts around target coordinates.

## M2-class laptop

Good fits:
- catalog joins and feature engineering with Arrow/Parquet;
- change-point scans over tens of millions of measurements;
- 64–96 pixel cutout PSF fitting in streaming batches;
- PyTorch MPS for image injection / batched convolutions.

Avoid:
- downloading the ~200-billion-row NEOWISE source database;
- downloading all 26.9 million NEOWISE image sets;
- keeping all candidate cutouts in unified memory at once.

## Storage envelopes

Assuming ~49k targets and ~21 WISE/NEOWISE epochs:

- epoch-level light curves: well below 1 GB with a compact schema;
- single-exposure matched rows: order 1–8 GB depending on retained columns/format;
- 64x64 W1/W2 epoch cutouts, image+variance+mask for every target: ~76 GB uncompressed-equivalent;
- same cutouts for top 1,000 candidates: ~1.5 GB;
- same cutouts for top 5,000 candidates: ~7.6 GB.

Therefore the recommended local working set is 20–50 GB, not the whole archive.

## GPU

The catalog stage is memory-bandwidth/I/O dominated and usually faster/simpler on CPU.
GPU/MPS becomes useful for:
- PSF convolution and source injection;
- joint scene fitting in batches;
- image differencing;
- optional CNN/artifact classifier.

The code should select `mps`, `cuda`, or `cpu` at runtime and benchmark actual throughput on the host.
