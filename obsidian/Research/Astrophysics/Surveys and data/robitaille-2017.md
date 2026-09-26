---
title: "A modular set of synthetic spectral energy distributions for young stellar objects"
authors: Thomas P. Robitaille
year: 2017
venue: Astronomy & Astrophysics, 600, A11 (doi:10.1051/0004-6361/201425486)
url: https://arxiv.org/abs/1703.05765
language: en
domain: astrophysics
status: draft
methodology_type: methodology
citation_count: 91
citation_count_date: 2026-09-26
key_concepts: ["[[confusion-limit]]"]
extends: []
contradicts: []
replicates: []
cites: ["[[stutz-2013]]", "[[evans-2009]]"]
cited_by: ["[[kuhn-2021]]"]
quality_notes: "Single-author model-grid release (v1.1); the author states the sets will not be expanded further. ~2% of models missing in v1.1 and some high-optical-depth power-law-envelope SEDs lack scattered dust emission — cite the version used. Citation count from Semantic Scholar (likely an undercount)."
author: moiseevigor
tags:
  - agent/research
  - user/moiseevigor
  - domain/astrophysics
  - topic/sed-modeling
  - topic/protostar-observational-signatures
  - topic/radiative-transfer
  - paper
  - status/draft
---

# A modular set of synthetic spectral energy distributions for young stellar objects

## Abstract

In this paper, I present a new set of synthetic spectral energy distributions (SEDs) for young stellar objects (YSOs) spanning a wide range of evolutionary stages, from the youngest deeply embedded protostars to pre-main-sequence stars with few or no disks. These models include significant improvements on the previous generation of published models: in particular, the new models cover a much wider and more uniform region of parameter space, do not include highly model-dependent parameters, and include a number of improvements that make them more suited to modeling far-infrared and sub-mm observations of forming stars. Rather than all being part of a single monolithic set of models, the new models are split up into sets of varying complexity. The aim of the new set of models is not to provide the most physically realistic models for young stars, but rather to provide deliberately simplified models for initial modeling, which allows a wide range of parameter space to be explored. I present the design of the model set, and show examples of fitting these models to real observations to show how the new grid design can help us better understand what can be determined from limited unresolved observations. The models, as well as a Python-based fitting tool are publicly available to the community.

## TL;DR

Successor to the Robitaille et al. (2006) YSO SED grid ("R06"): 18 modular model sets of increasing complexity (star only → star + passive disk + Ulrich envelope + bipolar cavities + inner hole + ambient medium), parameters sampled uniformly (log or linear) without evolutionary-track or collapse-model assumptions, computed with Hyperion (Monte Carlo radiative transfer) for 9 random stratified viewing angles and 20 apertures (10²–10⁶ au), 0.01 μm–5 mm, with large envelope outer radii to capture 10–20 K dust for Herschel. Model-set choice is done by a Bayesian "fraction of good fits" score (Occam's razor), not best χ². Explicit general limits: models are misspecified (χ² only relative), blending in distant regions, and non-simultaneous photometry of variable YSOs.

## Problem

The widely used R06 grid (≈20,000 models × 10 angles × 50 apertures, 14 parameters) had: (i) model-dependent parameters (mass/age via evolutionary tracks; infall rate via Ulrich collapse), (ii) unevenly sampled, built-in parameter correlations, (iii) fixed complexity (no embedded models without disks), (iv) envelopes too small to include cold dust at long wavelengths, (v) poor S/N at long wavelengths (§2). How should a YSO SED grid be designed so users can ask which *components* are required, and fit Herschel/sub-mm data?

## Approach

- **Components** (§3.2): spherical central source defined by R★ and T★ (Castelli & Kurucz ≥ 4000 K, PHOENIX < 4000 K); passive flared disk; spherically symmetric power-law envelope ρ ∝ r^γ or rotationally flattened Ulrich (1976) envelope; bipolar cavities; variable inner radius ("hole"); constant-density ambient medium; interstellar dust. Accretion not explicitly modelled.
- **Parameter ranges** (Table 1): R★ 0.1–100 R☉ (log); T★ 2000–30,000 K (log); disk dust mass 10⁻⁸–0.1 M☉ (log); disk inner radius R_sub–1000 R_sub; disk outer radius 50–5000 AU; flaring power β 1–1.3; surface-density power p −2 to 0; scaleheight at 100 AU 1–20 AU; envelope dust density ρ₀^env 10⁻²⁴–10⁻¹⁶ g cm⁻³ (log); envelope power γ −2 to −1; centrifugal radius R_c 50–5000 AU; cavity dust density 10⁻²³–10⁻²⁰ g cm⁻³; cavity opening angle 0°–60°; cavity power c 1–2.
- **Model sets** (Table 2, §3.3): 18 sets named by 7 characters — s (star), p (passive disk), p/u (power-law/Ulrich envelope), b (bipolar cavities), s/h (inner radius at sublimation / variable hole), m (ambient medium), i (interstellar dust). Number of models per set n_models = 10,000 × 2^max[n_var − 9, 0]: 10,000 for sets with ≤ 9 variables, 40,000 (spubsmi, 11 variables), 80,000 (spubhmi, 12 variables). (Researcher's arithmetic from Table 2: 16 × 10,000 + 40,000 + 80,000 = 280,000 models, × 9 viewing angles.)
- **Dust** (§3.4): single Draine (2003) / Weingartner & Draine (2001) Milky Way R_V = 5.5 dust everywhere; no PAHs or transiently heated grains.
- **Radiative transfer** (§4.1): Hyperion v0.9.5; 400 radial (×300 polar for 2-d) cells; modified random walk and raytracing for long-wavelength S/N.
- **SEDs** (§4.2): 250 log-spaced wavelengths 0.01 μm–5 mm; full Stokes I, Q, U, V; 9 viewing angles by stratified random sampling (one per 10° bin); 20 apertures interpolated to log-spaced 10²–10⁶ au; background ambient-medium surface brightness subtracted; fluxes < 0.1% of largest-aperture SED masked for λ > 10 μm in small apertures.
- **Fitting tool** (§4.3): new Python sedfitter (BSD); good fits defined by χ² − χ²_best < 3 n_data (Fig. 3) or, for cross-set comparison, χ² − χ²₀,best < 9 n_data with a common best (Fig. 4).
- **Model comparison** (§5.4.4): Bayes factor K = P(D|M₁)/P(D|M₂); with uniform priors P(D|M) is approximated by the fraction of models in a set providing a good fit — a formal Occam's razor.

## Key result

- Computation (§5.1): ≈640,000 CPU hours on 120 cores; "just below 2%" of models terminated (extreme optical depth) and missing from v1.1; for two power-law-envelope sets some SEDs recomputed without scattered light — between 2 and 14 μm, for 90% of models the omission is a < 10% effect.
- Worked example (§5.4, NGC 2264 Source 20, d = 869–961 pc, A_V 0–40): most sets with a disk and/or envelope fit acceptably; relative scores (Table 3) favour a simple star + passive disk (sp--s-i, fraction of good fits 0.3167%, χ²_best 2.71, score 7.600) over the same with ambient medium (sp--smi, χ²_best 2.28 but score 1.947) — i.e. a lower χ² does not make a set more probable if fewer of its models fit.
- For the preferred set, stellar temperature and disk mass remain very uncertain: without sub-mm detections disk mass is only lower-bounded by mid-IR fluxes; T★ is degenerate with extinction (§5.4.5).
- Envelope outer radii now large enough "to include 10-20K dust that is essential for modeling Herschel observations" (§8).

## Assumptions

- Single, spatially uniform dust model; single central heating source; no interstellar radiation field; no explicit accretion luminosity (passive disks approximate accreting ones except in UV/optical) (§3.2.2, §6).
- Uniform sampling means some combinations are unphysical; the user decides which to discard (§3.1, §6 item 5).
- Only directly sampled parameters are uniformly distributed; derived ones (e.g. luminosity) are not (§6 item 7).

## Limitations / scope

- **Misspecification** (§7.1): real YSOs are 3-d; χ² can only be a relative measure — absolute probabilities from exp(−χ²/2) are not meaningful.
- **Blending and confusion** (§7.2): distant/crowded regions contain unresolved multiples; only bulk properties (luminosity, maybe dust mass) remain meaningful — population synthesis may be preferable to per-source fitting.
- **Variability** (§7.3): archival SEDs combine epochs years apart; wavelength-dependent YSO variability causes SED discontinuities a static model cannot fit.
- Photosphere shapes accurate to ~10% in some cases (§6 item 6); v1.1 missing ~2% of models (§6 item 8).
- No new astrophysical measurements; the worked example is one source.
- Read in full via arXiv HTML; Table 3 partially parsed (first 8 rows); arXiv abstract used verbatim (A&A structured-abstract headings omitted).

## Replication evidence

Not applicable in the usual sense (model release). Used downstream in this vault by [[kuhn-2021]] (SED shapes of silicate-absorption YSO candidates, Fig. 17). No independent validation of the grid against resolved protostars is recorded in this vault.

## Why this paper matters

This is the current public reference grid for fitting YSO SEDs (sedfitter + Zenodo models) and is the natural successor to R06, which underlies many GLIMPSE-era YSO classifications. Its methodological contribution — asking first *which components are required* via the fraction of acceptable fits, then examining parameters within the favoured set — directly addresses over-interpretation of multi-parameter SED fits. The explicit statements on misspecification, blending in distant regions, and non-simultaneous photometry of variable YSOs define where SED-derived physical parameters for Galactic-plane protostars should not be trusted.

## Quotes

1. > "the models are wrong compared to the real density distributions" — §7.1
2. > "the simpler model should be favored because more complex models require more fine tuning" — §5.4.4

## Open questions surfaced

- How well can deeply embedded (Class 0-like) protostars be distinguished from edge-on disks or ambient-medium-dominated sources when only near/mid-IR + a few far-IR points exist? (Compare the degeneracies in [[furlan-2016]].)
- Effect of adding an interstellar radiation field and variable dust (grain growth, PAHs) on inferred envelope densities — flagged as future work (§6).
- Population-synthesis alternatives for blended, distant sources (§7.2) — not implemented.
- Time-dependent SED fitting for variable YSOs with non-simultaneous photometry (§7.3).

## Related material in vault

- Extends: —
- Contradicts: —
- Replicates: —
- Concepts introduced/used: [[confusion-limit]]
- Cites: [[stutz-2013]], [[evans-2009]]
- Cited by (in this vault): [[kuhn-2021]]
