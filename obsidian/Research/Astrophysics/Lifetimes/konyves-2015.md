---
title: "A census of dense cores in the Aquila cloud complex: SPIRE/PACS observations from the Herschel Gould Belt survey"
authors: V. Könyves, Ph. André, A. Men'shchikov, P. Palmeirim, D. Arzoumanian, N. Schneider, A. Roy, P. Didelon, A. Maury, Y. Shimajiri, J. Di Francesco, S. Bontemps, N. Peretto, M. Benedettini, J.-Ph. Bernard, D. Elia, M. J. Griffin, T. Hill, J. Kirk, B. Ladjelate, K. Marsh, P. G. Martin, F. Motte, Q. Nguyen Luong, S. Pezzuto, H. Roussel, K. L. J. Rygl, S. I. Sadavoy, E. Schisano, L. Spinoglio, D. Ward-Thompson, G. J. White
year: 2015
venue: Astronomy & Astrophysics 584, A91
url: https://arxiv.org/abs/1507.05926
language: en
domain: astrophysics
status: draft
methodology_type: empirical
citation_count: 338
citation_count_date: 2026-09-26
key_concepts: ["[[statistical-lifetime]]", "[[prestellar-core]]", "[[free-fall-time]]"]
extends: ["[[enoch-2008]]"]
contradicts: []
replicates: []
cites: ["[[enoch-2008]]", "[[evans-2009]]", "[[dunham-2008]]"]
cited_by: ["[[elia-2017]]", "[[young-2023]]"]
quality_notes: "Largest single-cloud prestellar census at the time (446 candidate / 292 robust prestellar cores). Its lifetime rests on starless-core vs. Class II counts with the evans-2009 2 Myr clock. The result depends on the adopted distance (260 vs. 415 pc; Appendix C)."
author: moiseevigor
tags:
  - agent/research
  - user/moiseevigor
  - domain/astrophysics
  - topic/prestellar-cores
  - topic/evolutionary-lifetimes
  - topic/core-mass-function
  - topic/herschel-protostar-surveys
  - paper
  - status/draft
---

# A census of dense cores in the Aquila cloud complex: SPIRE/PACS observations from the Herschel Gould Belt survey

## Abstract

(Verbatim from the A&A-accepted arXiv v1 PDF. The arXiv listing abstract is slightly shorter.)

We present and discuss the results of the Herschel Gould Belt survey (HGBS) observations in a ∼11 deg² area of the Aquila molecular cloud complex at d ∼ 260 pc, imaged with the SPIRE and PACS photometric cameras in parallel mode from 70 µm to 500 µm. Using the multi-scale, multi-wavelength source extraction method getsources, we identify a complete sample of starless dense cores and embedded (Class 0-I) protostars in this region, and analyze their global properties and spatial distributions. We find a total of 651 starless cores, ∼ 60% ± 10% of which are gravitationally bound prestellar cores, and they will likely form stars in the future. We also detect 58 protostellar cores. The core mass function (CMF) derived for the large population of prestellar cores is very similar in shape to the stellar initial mass function (IMF), confirming earlier findings on a much stronger statistical basis and supporting the view that there is a close physical link between the stellar IMF and the prestellar CMF. The global shift in mass scale observed between the CMF and the IMF is consistent with a typical star formation efficiency of ∼40% at the level of an individual core. By comparing the numbers of starless cores in various density bins to the number of young stellar objects (YSOs), we estimate that the lifetime of prestellar cores is ∼ 1 Myr, which is typically ∼ 4 times longer than the core free-fall time, and that it decreases with average core density. We find a strong correlation between the spatial distribution of prestellar cores and the densest filaments observed in the Aquila complex. About 90% of the Herschel-identified prestellar cores are located above a background column density corresponding to A_V ∼ 7, and ∼ 75% of them lie within filamentary structures with supercritical masses per unit length ≳ 16 M⊙/pc. These findings support a picture wherein the cores making up the peak of the CMF (and probably responsible for the base of the IMF) result primarily from the gravitational fragmentation of marginally supercritical filaments. Given that filaments appear to dominate the mass budget of dense gas at A_V > 7, our findings also suggest that the physics of prestellar core formation within filaments is responsible for a characteristic "efficiency" SFR/M_dense ∼ 5^{+2}_{−2} × 10^−8 yr^−1 for the star formation process in dense gas.

## TL;DR

A Herschel census of Aquila (651 starless cores, 446 candidate and 292 robust prestellar cores, 58 protostellar cores) counted against 622 Spitzer Class II YSOs with a 2 Myr Class II clock. It gives a prestellar-core lifetime of **t_pre = 1.2 ± 0.3 Myr** (~4 t_ff). The lifetime falls from **~1.4 Myr at n ≳ 10^4 cm^-3 to a few ×10^4 yr at n ≳ 10^5–10^6 cm^-3**. Cores above ~2–3 M☉ are denser and likely evolve faster.

## Problem

What is the lifetime of prestellar cores, and how does it depend on core density and mass, when counted in a complete Herschel census? Herschel reaches lower-density cores than the Bolocam-based [[enoch-2008]] (floor ≳ 2×10^4 cm^-3). A second question is how prestellar cores relate to filaments and to the IMF.

## Approach

- **Data** (§2–4): HGBS SPIRE/PACS parallel-mode maps (70–500 µm) of ~11 deg² of Aquila at d = 260 pc. Cores extracted with getsources.
- **Classification**: starless if no candidate 70 µm YSO lies within the core's half-power contour, protostellar otherwise. "Prestellar" means bound according to a Bonnor–Ebert mass ratio. The "candidate" set uses a looser criterion than the "robust" set.
- **Statistical lifetime** (§5.1): the Beichman et al. (1986) technique. N(starless or prestellar) / N(Class II YSOs) × t(Class II). Class II counts are 622 from the c2d + Gould Belt Spitzer surveys (Dunham et al. 2013; Allen et al. in prep.).
- **Reference clock**: "Adopting a reference lifetime of 2 Myr for Class II YSOs ([[evans-2009]])".
- **Density dependence**: lifetime computed in bins of average volume density (core mass / deconvolved volume) and plotted against t_ff and 10 t_ff in a "JWT" plot after Jessop & Ward-Thompson (2000) (Fig. 9).

## Key result

- Global lifetimes (§5.1): "∼ 2 Myr, ∼ 1.4 Myr, and ∼ 0.9 Myr for the global populations of Herschel starless cores, candidate prestellar cores, and robust prestellar cores, respectively". Best estimate: "t_pre = 1.2 ± 0.3 Myr".
- **Density dependence** (§5.1): the lifetime "decreases from ∼1.4 Myr for cores with average volume density ≳ 10^4 cm^−3 to a few times 10^4 yr for cores with average volume density ≳ 10^5-10^6 cm^−3". At the median density ~4×10^4 cm^−3 the lifetime is "∼ 0.75 Myr or ∼ 4–5 t_ff". All points lie between 1 t_ff and 10 t_ff (a rough ambipolar-diffusion timescale).
- Densest cores (§5.1): cores with deconvolved densities ≳ 10^6 cm^−3 have "a much shorter lifetime ∼ 0.02–0.05 Myr or ∼ t_ff", possibly in near-free-fall collapse.
- **Mass dependence** (§5.1, §6): core density correlates weakly and positively with core mass above ~2–3 M☉. So "prestellar cores more massive than ∼ 2–3 M⊙ may evolve on significantly shorter timescales" than the 0.1–2 M☉ majority. Weighting the CMF by 1/t_ff(M) leaves the peak at ~0.5 M☉ and flattens the high-mass end to dN/dlogM ∝ M^−1.0±0.2.
- Distance systematics (Appendix C): at d = 415 pc, candidate and robust prestellar lifetimes rise to ~1.8 and ~1.3 Myr, "leading to t_pre = 1.5 ± 0.3 Myr".
- Other: ~90% of prestellar cores lie above A_V^bg ~ 7. The CMF peaks at 0.45 ± 0.2 M☉ (observed), implying ε_core ~ 0.4. The star-formation efficiency of dense gas is SFR/M_dense ~ 5^{+2}_{−2}×10^−8 yr^−1.

## Assumptions

Stated in §5.1:
1. "all starless cores will evolve into YSOs in the future". For the all-starless figure (2 Myr), unbound cores are assumed to still be growing (footnote 14).
2. "star formation proceeds at a roughly constant rate, at least when averaged over an entire cloud".
3. Class II lifetime is 2 Myr ([[evans-2009]]).
4. Lifetime ∝ free-fall time when inferring the mass dependence (§5.1).
5. Distance is 260 pc (see Appendix C for 415 pc).

## Limitations / scope

- The main error sources named (§5.1) are "failed cores" that disperse before collapsing, and uncertainty in the number and lifetime of Class II YSOs in Aquila.
- The reference is Class II rather than embedded protostars, so the result inherits the full Class II-clock uncertainty (2 ± 1 Myr in [[evans-2009]]). It is not directly comparable to [[enoch-2008]]'s Class 0+I-anchored value.
- Fig. 9 error bars reflect √N counting only.
- Distance ambiguity (260 vs. 415 pc) moves masses by a factor of 2.5 and t_pre from 1.2 to 1.5 Myr.
- Only the lifetime part of this paper was studied in depth for this note. The filament and CMF sections were read but are summarized briefly.

## Replication evidence

Partial and consistent. The trend of lifetime decreasing with density reproduces [[enoch-2008]] (t_SL ∝ n^−1.2) and the Ward-Thompson et al. (2007) compilation. The longer global value (~1.2 Myr vs. ~0.45 Myr) is consistent with Herschel's lower density floor. The authors compare their result to the literature in the JWT plot.

## Why this paper matters

This paper supplies the "~1 Myr, ~4 free-fall times" prestellar lifetime used by the Herschel Gould Belt community. It is also the best-sampled demonstration that the prestellar lifetime is not one number: it runs from ~1.4 Myr at 10^4 cm^-3 to ~t_ff at ≳10^6 cm^-3.

Read together with [[enoch-2008]], the apparent disagreement (0.45 vs. 1.2 Myr) is largely a density-threshold and reference-clock effect rather than a contradiction. The paper also quantifies how a mass-dependent lifetime would bias the observed CMF.

## Quotes

1. > "best estimate of the global lifetime of the prestellar core phase" — §5.1 (value: t_pre = 1.2 ± 0.3 Myr)
2. > "core evolution may also be mass dependent" — §5.1

## Open questions surfaced

- How much of the factor-of-~2.5 gap with Bolocam-based lifetimes is due to density floor, and how much to the Class II vs. embedded-protostar reference clock?
- Do the densest (~10^6 cm^-3) cores really collapse on ~t_ff, or is their short inferred lifetime an artefact of small numbers per bin?
- What fraction of "candidate" prestellar cores are failed cores that will disperse? This sets the upper bound on the lifetime.
- Are the positive density–mass correlation, and hence faster evolution of cores above 2–3 M☉, general across HGBS clouds?

## Related material in vault

- Extends: [[enoch-2008]] (same counting method, Herschel depth, density-binned)
- Contradicts: —
- Replicates: —
- Concepts introduced/used: [[statistical-lifetime]], [[prestellar-core]], [[free-fall-time]]
- Cites: [[enoch-2008]], [[evans-2009]] (Class II 2 Myr clock), [[dunham-2008]]
- Cited by (in this vault): [[elia-2017]], [[young-2023]]
