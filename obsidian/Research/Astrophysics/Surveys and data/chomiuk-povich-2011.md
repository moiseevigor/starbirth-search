---
title: "Toward a Unification of Star Formation Rate Determinations in the Milky Way and Other Galaxies"
authors: Laura Chomiuk, Matthew S. Povich
year: 2011
venue: The Astronomical Journal 142, 197
url: https://arxiv.org/abs/1110.4105
language: en
domain: astrophysics
status: draft
methodology_type: review
citation_count: 348  # OpenAlex
citation_count_date: 2026-09-26
key_concepts: []
extends: []
contradicts: []
replicates: []
cites: []
cited_by: ["[[licquia-newman-2015]]", "[[elia-2022]]", "[[battersby-2017]]", "[[svoboda-2016]]"]
quality_notes: "Its Table 1 (literature SFRs renormalised to Kroupa IMF + Starburst99) is the dataset behind licquia-newman-2015 and the comparison table in elia-2022."
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

# Toward a unification of SFR determinations in the Milky Way and other galaxies

## Abstract

The star formation rate (SFR) of the Milky Way remains poorly known, with often-quoted values ranging from 1 to 10 M⊙ yr−1. This situation persists despite the potential for the Milky Way to serve as the ultimate SFR calibrator for external galaxies. We show that various estimates for the Galactic SFR are consistent with one another once they have been normalized to the same initial mass function (IMF) and massive star models, converging to 1.9 ± 0.4 M⊙ yr−1. However, standard SFR diagnostics are vulnerable to systematics founded in the use of indirect observational tracers sensitive only to high-mass stars. We find that absolute SFRs measured using resolved low/intermediate-mass stellar populations in Galactic H II regions are systematically higher by factors of ∼2 − 3 as compared with calibrations for SFRs measured from mid-IR and radio emission. We discuss some potential explanations for this discrepancy and conclude that it could be allayed if (1) the power-law slope of the IMF for intermediate-mass (1.5 M⊙ < m < 5 M⊙) stars were steeper than the Salpeter slope, or 2) a correction factor was applied to the extragalactic 24 µm SFR calibrations to account for the duration of star formation in individual mid-IR–bright H II regions relative to the lifetimes of O stars. Finally, we present some approaches for testing if a Galactic SFR of ∼2 M⊙ yr−1 is consistent with what we would measure if we could view the Milky Way as external observers. Using luminous radio supernova remnants and X-ray point sources, we find that the Milky Way deviates from expectations at the 1–3σ level, hinting that perhaps the Galactic SFR is overestimated or extragalactic SFRs need to be revised upwards.

## TL;DR

The literature Milky Way SFRs (1–10 M⊙ yr⁻¹) collapse to **1.9 ± 0.4 M⊙ yr⁻¹** once they are renormalised to one IMF (Kroupa) and one set of massive-star models (Starburst99 v5.1). The often-quoted 4–5 M⊙ yr⁻¹ is an IMF/model artefact. There is a caveat on absolute scale: star counts in Galactic H II regions such as M17 give SFRs a factor ~2–3 higher than the indirect ionising-photon and mid-IR tracers.

## Problem

Why do Milky Way SFR estimates disagree by an order of magnitude? Is the Galaxy consistent with the SFR calibrations used for external galaxies (§1)?

## Approach

- **Common inputs (§2).** Kroupa broken power-law IMF, φ(log m) ∝ m^−Γ with Γ = 0.3 for 0.1–0.5 M⊙ and Γ = 1.3 for 0.5–100 M⊙. Starburst99 v5.1 at solar metallicity. Lyman-continuum calibration Eq. 4: SFR [M⊙ yr⁻¹] = 7.5 × 10⁻⁵⁴ N_c [phot s⁻¹]. This is the Kennicutt (1998) Salpeter value of 9.26 × 10⁵² phot s⁻¹ per M⊙ yr⁻¹, rescaled by 1.44 for Kroupa. Steady state needs star formation lasting at least ~8 Myr, the lifetime of a late O star. For the supernova-rate method, a SFR of 1 M⊙ yr⁻¹ corresponds to 0.85 supernovae per century (progenitors 10–100 M⊙).
- **Renormalisation of 11 literature estimates (§3, Table 1).** Methods: ionisation rate (radio free-free, COBE N II 205 µm, WMAP free-free), supernova rate (O/B star counts, INTEGRAL ²⁶Al), dust heating (COBE far-IR), and YSO counts (Spitzer GLIMPSE, MSX/RMS).
- **Calibration test against direct star counts (§4).** Resolved low- and intermediate-mass populations in Galactic H II regions, with M17 as the case study, compared against mid-IR and radio SFR diagnostics.
- **External-observer consistency tests (§5).** The brightest radio supernova remnant and luminous young X-ray point sources, compared with extragalactic L_max–SFR and L_YXP–SFR relations.

## Key result

- **Normalised Table 1 (M⊙ yr⁻¹).** Smith et al. 1978: 0.35. Güsten & Mezger 1982: 2.0 ± 0.6. Mezger 1987: 1.6 ± 0.5. Bennett et al. 1994: 2.6 ± 1.3. McKee & Williams 1997: 2.0 ± 1.0. Reed 2005: 1.8 ± 0.6. Diehl et al. 2006: 2.0 ± 1.2. Misiriotis et al. 2006: 1.9 ± 0.8 (50% error assumed). Murray & Rahman 2010: 2.4 ± 1.2 (50% error assumed). Robitaille & Whitney 2010: 1.1 ± 0.4. Davies et al. 2011: 1.8 ± 0.3.
- **Consensus (§3.4).** The estimates average **1.9 ± 0.4 M⊙ yr⁻¹**, excluding Smith et al. (1978) and Güsten & Mezger (1982), which Mezger (1987) superseded. The largest outlier is Robitaille & Whitney (2010), argued to be a lower limit: an assumed 2 Myr YSO lifetime is likely too long for intermediate-mass YSOs, and a factor ~2 correction would reconcile it. The commonly quoted 4–5 M⊙ yr⁻¹ differs only because of IMF and model choices. On the Starburst99/Kroupa scale the Galactic SFR is 2 M⊙ yr⁻¹.
- **Absolute calibration offset (§4, §6).** SFRs from direct star counts in H II regions are higher than indirect-tracer SFRs by factors of ~2–3. Since only lower limits on the star-count SFRs were derived, the true discrepancy may be larger. Two proposed explanations: an intermediate-mass IMF steeper than Salpeter for 1.5–5 M⊙, or overestimated star-formation durations for mid-IR-bright H II regions, which are younger than O-star lifetimes by factors ≳ 1.6.
- **External-observer tests (§5.3).** The Milky Way deviates from both extragalactic relations at 1–3σ. This hints that the Galactic SFR is overestimated, or extragalactic SFRs underestimated, by a factor of a few. The authors call the result noisy and marginal.

## Assumptions

- Kroupa IMF and Starburst99 v5.1 are adopted as a common scale, not as the true inputs. Relative comparisons are robust, but absolute values inherit these choices (§4 intro).
- Steady-state star formation over O-star lifetimes for ionisation-based diagnostics (§2).
- Differences in the assumed Milky Way structural model (e.g. R☉) are not homogenised (§3.1).

## Limitations / scope

- The 1.9 ± 0.4 is a simple average of heterogeneous, partly non-independent estimates, several with assumed 50% errors. [[licquia-newman-2015]] later formalises the combination (1.65 ± 0.19).
- The star-count calibration rests mainly on M17 and a few H II regions. Low-mass regions (< 3,000 M⊙) suffer from stochastic IMF sampling (§6).
- I read the full text of §1–§3, §5.3 and §6. The M17 X-ray luminosity-function analysis (§4.1–§4.3) was skimmed via the Abstract and Conclusions.

## Replication evidence

Partial. [[licquia-newman-2015]] re-combined the same Table 1 with a hierarchical Bayesian method and found the inputs mutually consistent (1.65 ± 0.19). The independent far-IR clump method of [[elia-2022]] gives 2.0 ± 0.7, consistent. The factor ~2–3 star-count offset was not examined by either.

## Why this paper matters

It is the origin of the modern "Milky Way SFR ≈ 2 M⊙ yr⁻¹" and the homogenised dataset every later consensus uses. For star-birth work it matters for two reasons. First, the global normalisation (~2 M⊙ yr⁻¹) sets the expected Galactic birth rate. Second, it warns that the absolute SFR scale is uncertain by a factor ~2–3, because high-mass tracers are extrapolated through the IMF.

## Quotes

1. > "converging to 1.9 ± 0.4 M⊙ yr−1" — Abstract
2. > "systematically higher by factors of ∼2 − 3" — Abstract

## Open questions surfaced

- Is the intermediate-mass IMF steeper than Salpeter? That would raise all absolute SFRs, Galactic and extragalactic.
- Is the Milky Way really a 1–3σ outlier from extragalactic SFR relations, or is this small-number noise in the supernova-remnant and X-ray tests?
- How do bottom-up census methods (YSO counts, far-IR clumps) that do not rely on ionising photons compare on the same IMF scale?

## Related material in vault

- Extends: none
- Contradicts: none
- Replicates: none
- Concepts introduced/used: none of the current hubs
- Cites: none in this vault list
- Cited by (in this vault): [[licquia-newman-2015]], [[elia-2022]], [[battersby-2017]], [[svoboda-2016]]
