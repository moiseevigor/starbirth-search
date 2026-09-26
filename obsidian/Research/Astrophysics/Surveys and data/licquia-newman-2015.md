---
title: "Improved Estimates of the Milky Way's Stellar Mass and Star Formation Rate from Hierarchical Bayesian Meta-Analysis"
authors: Timothy C. Licquia, Jeffrey A. Newman
year: 2015
venue: The Astrophysical Journal 806, 96
url: https://arxiv.org/abs/1407.1078
language: en
domain: astrophysics
status: draft
methodology_type: methodology
citation_count: 502  # OpenAlex
citation_count_date: 2026-09-26
key_concepts: []
extends: ["[[chomiuk-povich-2011]]"]
contradicts: []
replicates: []
cites: ["[[chomiuk-povich-2011]]"]
cited_by: ["[[elia-2022]]"]
quality_notes: "Standard citation for the Milky Way SFR (1.65 ± 0.19). It adds no new data: it is a statistical combination of the Chomiuk & Povich (2011) normalised values, so it inherits their shared IMF and ionising-photon calibration."
author: moiseevigor
tags:
  - agent/research
  - user/moiseevigor
  - domain/astrophysics
  - topic/galactic-star-formation-rate
  - topic/sfr-imf-calibration
  - paper
  - status/draft
---

# Improved estimates of the Milky Way's stellar mass and SFR from hierarchical Bayesian meta-analysis

## Abstract

We present improved estimates of several global properties of the Milky Way, including its current star formation rate (SFR), the stellar mass contained in its disk and bulge+bar components, as well as its total stellar mass. We do so by combining previous measurements from the literature using a hierarchical Bayesian (HB) statistical method that allows us to account for the possibility that any value may be incorrect or have underestimated errors. We show that this method is robust to a wide variety of assumptions about the nature of problems in individual measurements or error estimates. Ultimately, our analysis yields a SFR for the Galaxy of Ṁ⋆ = 1.65 ± 0.19 M⊙ yr−1, assuming a Kroupa initial mass function (IMF). By combining HB methods with Monte Carlo simulations that incorporate the latest estimates of the Galactocentric radius of the Sun, R0, the exponential scale length of the disk, Ld, and the local surface density of stellar mass, Σ⋆(R0), we show that the mass of the Galactic bulge+bar is M⋆^B = 0.91 ± 0.07 × 10^10 M⊙, the disk mass is M⋆^D = 5.17 ± 1.11 × 10^10 M⊙, and their combination yields a total stellar mass of M⋆ = 6.08 ± 1.14 × 10^10 M⊙ (assuming a Kroupa IMF and an exponential disk profile). This analysis is based upon a new compilation of literature bulge mass estimates, normalized to common assumptions about the stellar initial mass function and Galactic disk properties, presented herein. We additionally find a bulge-to-total mass ratio for the Milky Way of B/T = 0.150 (+0.028/−0.019) and a specific star formation rate of Ṁ⋆/M⋆ = 2.71 ± 0.59 × 10^−11 yr^−1.

## TL;DR

The most-cited single number for the Milky Way SFR: **1.65 ± 0.19 M⊙ yr⁻¹** (Kroupa IMF). It comes from a hierarchical Bayesian (HB) combination of the nine normalised literature estimates tabulated by [[chomiuk-povich-2011]]. The HB analysis finds the inputs mutually consistent, so the result equals the inverse-variance weighted mean. The error bar does not include systematics common to all inputs, such as the IMF or the ionising-photon-to-SFR calibration.

## Problem

Published Milky Way SFR (and stellar mass) values scatter widely and have uneven error bars. How do you combine them into one consensus value with an honest uncertainty, when some measurements may be wrong or have underestimated errors (§1–2)?

## Approach

- **HB meta-analysis (§2).** Each literature value is a Gaussian (µᵢ, σᵢ). A fraction f_good of measurements is "good". The rest are "bad" and are modelled four ways:
  - errors scaled by n ("free-n");
  - Q·µ_MED added in quadrature ("free-Q");
  - a fractional error floor F ("free-F");
  - replaced by a flat distribution ("P_bad-flat").
  Models are compared by AIC, BIC and Bayes factor K. The formalism follows Press (1997).
- **SFR dataset (§3.1).** Table 1 of [[chomiuk-povich-2011]], all normalised to the Kroupa IMF and Starburst99 v5.1. Smith et al. (1978) and Güsten & Mezger (1982) are dropped because Mezger (1987) superseded them. The Misiriotis et al. (2006) value is given an assumed 50% error (0.95 M⊙ yr⁻¹). This leaves nine studies.
- **Prior (§3.2).** Uniform SFR on 0–6 M⊙ yr⁻¹.
- **Robustness tests (§3.3).** Robitaille & Whitney (2010) with doubled errors; Bennett et al. (1994) excluded; a bootstrap drawing one measurement per method.
- **Stellar mass (§4).** HB combined with Monte Carlo over R₀ = 8.33 ± 0.35 kpc and the Bovy & Rix (2013) disk, with L_d = 2.15 ± 0.14 kpc.

## Key result

- **SFR (§3.3, Table 1).** Every model converges to f_good ≈ 1 and Ṁ⋆ ≈ 1.66. The fiducial all-"good" model has the largest Bayes factor and gives **Ṁ⋆ = 1.65 ± 0.19 M⊙ yr⁻¹**, identical to the inverse-variance weighted mean (χ² = 3.83; 95% expected range [2.18, 17.53]). Other models give 1.65–1.69 with ±0.20–0.26.
- **Robustness (§3.3).** Down-weighting or excluding Robitaille & Whitney (2010) changes the consensus by at most 0.17 M⊙ yr⁻¹. The bootstrap standard deviation of the mean is 0.22 with one measurement per method and 0.25 for random draws, so variation between methods is negligible.
- **Stellar mass (Abstract, Table 6).** Bulge+bar 0.91 ± 0.07 × 10¹⁰ M⊙, disk 5.17 ± 1.11 × 10¹⁰ M⊙, total 6.08 ± 1.14 × 10¹⁰ M⊙. B/T = 0.150 (+0.028/−0.019). Specific SFR = 2.71 ± 0.59 × 10⁻¹¹ yr⁻¹. The SFR does not depend on R₀ or L_d (∂Ṁ⋆/∂R₀ = 0).

## Assumptions

- Kroupa IMF, and the Kennicutt (1998) Lyman-continuum-to-SFR relation reduced by a factor of 1.44 for Kroupa. These are the [[chomiuk-povich-2011]] normalisations (§3.3).
- The input measurements are independent. Bennett et al. (1994) and McKee & Williams (1997) share COBE data but are treated as independent (§3.3).
- Flat prior on SFR in [0, 6] M⊙ yr⁻¹ (§3.2).

## Limitations / scope

- No new data. The result is only as good as the renormalised inputs and inherits any systematic common to them (IMF shape, ionising-photon calibration, O-star models). The authors argue these cancel when the Milky Way is compared with other galaxies calibrated the same way, but not for absolute rates (§3.3).
- It does not use the far-IR clump approach later taken by [[elia-2022]] (2.0 ± 0.7, consistent), nor the factor ~2–3 star-count offset flagged by [[chomiuk-povich-2011]] §4.
- I read the full text of §1–§3, §4 intro and §5. The bulge-mass compilation (§4.3) was skimmed.

## Replication evidence

Partial. The weighted-mean nature means any re-analysis of the same inputs reproduces it. The independent Hi-GAL clump-based value of 2.0 ± 0.7 M⊙ yr⁻¹ ([[elia-2022]]) is consistent within errors.

## Why this paper matters

It supplies the default "Milky Way SFR ≈ 1.65 M⊙ yr⁻¹" and the Milky Way stellar mass used when placing the Galaxy among external galaxies. For star-birth statistics, it gives the Galactic normalisation: roughly how many solar masses of new stars form per year. It should be quoted together with its caveat that the ±0.19 is a statistical combination and excludes the common IMF and calibration systematics.

## Quotes

1. > "yields a SFR for the Galaxy of Ṁ⋆ = 1.65 ± 0.19 M⊙ yr−1" — Abstract
2. > "common-mode systematics do not have a large impact" — §3.3

## Open questions surfaced

- How large are the common-mode (IMF, Lyman-continuum calibration) systematics that the HB error excludes? [[chomiuk-povich-2011]] suggests absolute SFRs could be low by factors of 2–3.
- How do independent bottom-up estimates (YSO counts, far-IR clumps) with separate systematics shift the consensus?

## Related material in vault

- Extends: [[chomiuk-povich-2011]]
- Contradicts: none
- Replicates: none
- Concepts introduced/used: none of the current hubs
- Cites: [[chomiuk-povich-2011]]
- Cited by (in this vault): [[elia-2022]]
