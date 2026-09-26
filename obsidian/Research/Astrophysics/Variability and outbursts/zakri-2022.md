---
title: "The Rate, Amplitude and Duration of Outbursts from Class 0 Protostars in Orion"
authors: Wafa Zakri, S. T. Megeath, William J. Fischer, Robert Gutermuth, Elise Furlan, Lee Hartmann, Nicole Karnath, Mayra Osorio, Emily Safron, Thomas Stanke, Amelia M. Stutz, John J. Tobin, Thomas S. Allen, Sam Federman, Nolan Habel, P. Manoj, Mayank Narang, Riwaj Pokhrel, Luisa Rebull, Patrick D. Sheehan, Dan M. Watson
year: 2022
venue: The Astrophysical Journal Letters, 924, L23 (doi:10.3847/2041-8213/ac46ae)
url: https://arxiv.org/abs/2201.04647
language: en
domain: astrophysics
status: draft
methodology_type: empirical
citation_count: 32
citation_count_date: 2026-09-26
key_concepts: ["[[accretion-outburst]]", "[[class-0-protostar]]", "[[episodic-accretion]]", "[[luminosity-problem]]", "[[confusion-limit]]", "[[outburst-recurrence-time]]"]
extends: ["[[fischer-2019]]", "[[safron-2015]]"]
contradicts: []
replicates: []
cites: ["[[safron-2015]]", "[[fischer-2019]]", "[[park-2021]]", "[[contreras-pena-2019]]", "[[lee-2021]]", "[[furlan-2016]]", "[[stutz-2013]]", "[[dunham-2008]]"]
cited_by: ["[[contreras-pena-2024]]"]
quality_notes: "Class 0 vs Class I/FS rate difference (x4) is explicitly NOT statistically significant (p = 6-15% for Class 0 excess); intervals depend on a logarithmic prior (Appendix B). Only 3 Class 0 events. Amplitudes come from heterogeneous far-IR instruments with colour corrections."
author: moiseevigor
tags:
  - agent/research
  - user/moiseevigor
  - domain/astrophysics
  - topic/accretion-outbursts
  - topic/class-0-protostars
  - topic/protostellar-variability
  - topic/spitzer-surveys
  - topic/wise-neowise
  - topic/time-domain-surveys
  - topic/outburst-recurrence-rate
  - topic/accretion-luminosity
  - topic/herschel-protostar-surveys
  - paper
  - status/draft
---

# The Rate, Amplitude and Duration of Outbursts from Class 0 Protostars in Orion

## Abstract

At least half of a protostar's mass is accreted in the Class 0 phase, when the central protostar is deeply embedded in a dense, infalling envelope. We present the first systematic search for outbursts from Class 0 protostars in the Orion clouds. Using photometry from Spitzer/IRAC spanning 2004 to 2017, we detect three outbursts from Class 0 protostars with ≥ 2 mag changes at 3.6 or 4.5 µm. This is comparable to the magnitude change of a known protostellar FU Ori outburst. Two are newly detected bursts from the protostars HOPS 12 and 124. The number of detections implies that Class 0 protostars burst every 438 yr, with a 95% confidence interval of 161 to 1884 yr. Combining Spitzer and WISE/NEOWISE data spanning 2004-2019, we show that the bursts persist for more than nine years with significant variability during each burst. Finally, we use 19 − 100 µm photometry from SOFIA, Spitzer and Herschel to measure the amplitudes of the bursts. Based on the burst interval, a duration of 15 yr, and the range of observed amplitudes, 3–100% of the mass accretion during the Class 0 phase occurs during bursts. In total, we show that bursts from Class 0 protostars are as frequent, or even more frequent, than those from more evolved protostars. This is consistent with bursts being driven by instabilities in disks triggered by rapid mass infall. Furthermore, we find that bursts may be a significant, if not dominant, mode of mass accretion during the Class 0 phase.

## TL;DR

Spitzer/IRAC-only (2004 cryo → 2016–17 OrionTFE, plus YSOVAR 2009–10 and 2019 Spitzer Beyond) search of 319 Orion protostars with a ≥ 2 mag threshold at 3.6 or 4.5 µm: 5 bursts total, 3 in the 92 Class 0s (HOPS 12, 124 new; HOPS 383). Class 0 median burst interval 438 yr (95% CI 161–1884 yr) vs 1741 yr for Class I/flat; all protostars 879 yr (400–2515 yr). Bursts last > 9 yr (HOPS 383: ~15 yr total); far-IR luminosity amplitudes ×3.7, ×5.4, ×9.7.

## Problem

Is the burst rate higher in the Class 0 phase (where most mass is accreted) than in Class I/flat-spectrum, and what are the amplitudes and durations needed to compute the fraction of mass accreted in bursts? (§1)

## Approach

- **Sample:** 319 HOPS protostars ([[furlan-2016]]): 92 Class 0, 227 Class I/flat-spectrum (FS) (§4.1).
- **Data (§2.1):** Spitzer IRAC cryo 2004 (two epochs ~6 months apart; extensions 2007/2009); YSOVAR ~80 epochs in 2009–2010 (ONC only; campaigns 2009 Oct 23–Dec 01 and 2010 Oct 29–Dec 09); OrionTFE two epochs 2016–2017 duplicating cryo fields; Spitzer Beyond 2019 for sources varying ≥ 1 mag. Aperture photometry, 2.4″ radius, sky 2.4–7.2″.
- **WISE/NEOWISE (§2.2):** HOPS 12 from All-Sky, 3-Band Cryo and NEOWISE-R single exposures averaged per week; HOPS 124 via PSF fitting on unWISE epochs (2010–2017) to separate HOPS 125. For HOPS 12, Spitzer images convolved to WISE resolution (12.4″ aperture) for comparison.
- **Far-IR amplitudes (§2.3–2.4, §3.2):** MIPS 24/70 µm (pre), PACS 70/100 µm (2010), SOFIA FORCAST 19.7–37.1 µm (2016, 2019) and HAWC+ 89 µm (2019), with bandpass colour corrections (Appendix A).
- **Rate statistics (§4.1, Appendix B):** posterior on burst interval from Eq. 2 of [[fischer-2019]] (also Hillenbrand & Findeisen 2015; [[contreras-pena-2019]]) with a logarithmic prior; baseline 13 yr; p-values from Eq. B5.

## Key result

**Detection threshold and rationale (§3):** ≥ 2 mag at 3.6 or 4.5 µm, chosen because V2775 Ori (HOPS 223) is "one of the lowest amplitude FU Ori outbursts known", and "in the Orion sample, only bursts show variations at 3.6 or 4.5 µm that exceed 2 mag".

**Mid-IR amplitudes and durations (§3.1):**

| Source | Class | Δ3.6 µm | Δ4.5 µm | Duration / behaviour |
|---|---|---|---|---|
| HOPS 12 (West) | 0 | 1.66 mag (×4.6) | 2.09 mag (×6.8) | rose 2004–2009, sustained through 2017, faded ~0.5 mag by 2019; NEOWISE fluctuations with peaks ~2 yr apart |
| HOPS 124 | 0 | 2.2 mag (×7.5) | 2.3 mag (×8.2) | rising during 2010 WISE, peaked 2015, ~0.5 mag fade 2017–2019 |
| HOPS 383 | 0 | — | 3.6 mag (×22) | entire burst ~15 yr, ended |

- Both new bursts "have lasted for 9 yr", with "> 0.5 mag variability during the bursts" (§3.1).
- **Colour test vs extinction:** [3.6]−[4.5] became ~0.5 mag **redder** during bursts — "the opposite of what one would expect if the brightening were due to a decrease in extinction" (§3.1).

**Luminosity amplitudes from 19–100 µm (§3.2):** HOPS 12: 70 µm 3.6 → 13.4 Jy after deblending → ×3.7 (24 µm ×2.5, taken during decline); HOPS 124: 24 µm ×5.4 (likely underestimate); HOPS 383: faded ×9.7 at 89 µm (PACS-interpolated 20.9 Jy in 2010 vs HAWC+ 2019), whereas 24–25 µm gave ×35 (2004→2008) and ×40 (2016 FORCAST vs 2004) — discrepancy "not understood"; ×9.7 adopted as conservative.

**Burst intervals (Table 3; median and 95% CI, log prior, 13 yr baseline):**

| Sample | Median (yr) | 95% CI (yr) |
|---|---|---|
| Class 0 | 438 | 161 – 1884 |
| Class I/FS | 1741 | 527 – 12011 |
| Class 0 in ONC | 199 | 60 – 1393 |
| Class I/FS in ONC (1 burst; prior-dominated) | 823 | 155 – 21694 |
| All protostars | 879 | 400 – 2515 |
| All protostars in ONC | 341 | 126 – 1468 |

- Simple rate: 3 / 92 / 13 yr = 2.5 × 10⁻³ yr⁻¹ → ~400 yr (§4.1).
- **Significance:** assuming t_b = 879 yr, P(n ≥ 3) = 15% (Class 0 clouds) and P(n ≥ 2) = 6% (ONC); P(n ≤ 2) = 35%, P(n ≤ 1) = 86% for Class I/FS → "we cannot rule out that protostars of all classes have the same burst interval" (§4.1).
- **Mass fraction (§4.2):** M_b/M = (A d_b/I_b) / [(A − 1) d_b/I_b + 1] with I_b = 438 yr, d_b = 15 yr: 12, 16, 26% (A = 3.7, 5.4, 9.7); I_b = 199 yr: 23, 31, 44%; I_b = 1884 yr: 3, 4, 7%; bounded range 3–39% (HOPS 12) to 7–100% (HOPS 383).
- Comparable to outflow-knot spacing 310 ± 150 yr (CARMA-7, Class 0) and shorter than 1–3 kyr knot spacing for more evolved sources; longer 2400 yr prediction from N₂H⁺/HCO⁺ chemistry (Hsieh et al. 2019) (§4.1).

## Assumptions

- All protostars in a class share one Poisson burst rate; no multiple mechanisms or binarity dependence (§4.1).
- 70–100 µm flux scales ~linearly with luminosity; all luminosity is accretion luminosity for the A estimate (§3.2, §4.2).
- HOPS 12 East constant between epochs in the 70 µm deblend (§3.2).
- Class 0 contamination by inclined/extincted Class I is < 10% (Stutz & Kainulainen 2015; only 4/75 Class 0 edge-on in HST) (§4.1).

## Limitations / scope

- Sparse cadence outside the ONC: a burst rising and decaying between 2004 and 2016 would be missed (why the ONC-only rates are shorter).
- Only ≥ 2 mag bursts counted; lower-amplitude events deferred to a companion paper.
- 3 Class 0 events → Class 0/Class I difference suggestive, not conclusive (§5).
- Far-IR amplitude for HOPS 383 disagrees with 24 µm by ×4 (unexplained).

## Replication evidence

Partial. The all-protostar interval (879 yr) is consistent with [[fischer-2019]] (~1000 yr) and [[park-2021]] (NEOWISE). The Class 0 enhancement has not been independently confirmed within this paper's statistics. HOPS 383's end of burst agrees with Grosso et al. (2020, NEOWISE).

## Why this paper matters

It extends the outburst census to the Class 0 phase with a higher-resolution, longer (13 yr) Spitzer-only baseline and shows that WISE-based searches ([[fischer-2019]], [[park-2021]]) missed two Class 0 bursts because of blending with companions — a direct demonstration of the [[confusion-limit]] bias in WISE time-domain work. It is also one of the few papers to measure all three ingredients (interval, duration, amplitude) of the burst mass fraction.

## Quotes

1. > "bursts may be a significant, if not dominant, mode of mass accretion" — Abstract
2. > "only bursts show variations at 3.6 or 4.5 µm that exceed 2 mag" — §3

## Open questions surfaced

- Is the Class 0 burst interval truly ~4× shorter than Class I/FS? Needs larger samples / denser cadence.
- Why do 24 µm and 70–89 µm amplitudes disagree for HOPS 383?
- Contribution of < 2 mag bursts, fluctuations and fades (companion paper, "W. Zakri et al., in prep.").
- Role of disk gravitational instability (HOPS 124 Toomre-Q unstable; HOPS 383 disk near stability limit) vs binaries.

## Related material in vault

- Extends: [[fischer-2019]], [[safron-2015]]
- Contradicts: —
- Replicates: —
- Concepts introduced/used: [[accretion-outburst]], [[class-0-protostar]], [[episodic-accretion]], [[luminosity-problem]], [[confusion-limit]], [[outburst-recurrence-time]]
- Cites: [[safron-2015]], [[fischer-2019]], [[park-2021]], [[contreras-pena-2019]] (rate statistics), [[lee-2021]] (JCMT low-amplitude accretion ~12% of Class 0 mass, redefined), [[furlan-2016]], [[stutz-2013]], [[dunham-2008]]
- Cited by (in this vault): [[contreras-pena-2024]]
