# Literature survey: catching a Hi-GAL prestellar clump turning into a protostar

Survey date: 2026-09-26. Every number below was checked against the abstract or
full text (arXiv/ADS/publisher) or queried live from IRSA / the Herschel Science
Archive (HSA). Anything that could not be checked is marked **UNVERIFIED**.
Numbers marked **(derived)** are this survey's own arithmetic on the cited inputs.

Terms, labels and metrics are defined in [GLOSSARY.md](GLOSSARY.md) (generated from `src/starbirth/glossary.py`).

## 1. Prior art

**Verdict: we found no published search that follows a catalogued starless or prestellar core or clump over time and reports it turning into a protostar.** The closest existing work falls into three groups:

1. **Reclassification by deeper data, not time evolution.** Spitzer c2d found that 15–25% of "starless" cores actually host low-luminosity protostars (L1014, L1521F, L328 and others). Dunham+2008 found 50 embedded sources with L_int < 1 L☉. PPVI later quotes 18–38% (Dunham+2014 §4.2.2). Herschel then found 55 new Orion protostar candidates that are faint or missing at 24 µm, including 18 PBRS (Stutz+2013).
2. **Mid-IR "appearance" events that turned out to be outbursts of existing protostars.** Three cases stand out:
   - **HOPS 383**, a Class 0 protostar, brightened ×35 at 24 µm between 2004 and 2008 and also brightened at 4.5 µm. It went from a faint source to an obvious protostar (Safron+2015). Fischer+2019 compared Spitzer and WISE photometry (6.5 yr apart) for 319 Orion protostars and recovered only HOPS 383 and V2775 Ori.
   - **WISEA J142238.82−611553.7** brightened by about 8 mag at 4.6 µm. It was already a Spitzer Class I source in 2004 (Lucas+2020).
   - The two catalogue-wide variability searches do not report non-detection-to-detection "births". Kulkarni+2026 covers ISO, Spitzer, WISE and NEOWISE from 1997 to 2024. Li & Wang 2024 found 641 unTimely variables with ΔW > 1 mag.
3. **Time-domain monitoring of starless samples, with null results.**
   - The JCMT Transient Survey monitored 190 starless submillimetre peaks for 4 years and found **none** variable. All 18 secular variables were protostars (Lee+2021).
   - Lu+2024 matched NEOWISE to ATLASGAL clumps. Only about 20% of the 248 "quiescent" clumps had a NEOWISE match, and 45 of those (18%) were variable. They did not look for new sources appearing.
   - The FHSC candidates (L1451-mm, Per-Bolo 58, B1-bN, Cha-MMS1, HOPS 404, …) have been discussed only in terms of static properties (SED, outflow, chemistry). **We found no report of any candidate changing state** (Young 2023 review; Dunham+2014). "Not found" is based on our searches; it is not a proof of absence.

**Implication:** the project's specific test (a Hi-GAL prestellar clump at the Herschel epoch, a persistent W1/W2 change point afterwards, and ruling out an outburst) appears to be new. The closest analogue in the literature, HOPS 383, was interpreted as an outburst, not a birth.

## 2. Candidate edge (what the literature says is possible)

- **Large parent sample.** The Hi-GAL 360° high-reliability catalogue contains **49,289 prestellar clumps**. 40,696 of them have distances, with median d = **4.31 kpc** (derived from an IRSA query). The Herschel epoch is known per tile: 2009-09 to 2013-03, and each observation has an ObsID and start time in the HSA. NEOWISE-R single exposures run from **2013-12-13 to 2024-08-01** (IRSA `neowiser_p1bs_frm` MJD 56639.8–60523.3). That gives a post-Herschel baseline of about 11–15 yr.
- **Transitions must occur statistically.** In steady state, the number of clumps crossing from starless to 70 µm-bright per year is N_proto / t_proto. With 35,186 protostellar clumps and a star-forming phase of 0.1–0.7 Myr (Battersby+2017), that is **≈0.05–0.35 transitions per yr** across the catalogue, or **≈0.6–5 over the NEOWISE-R baseline** (derived).
- **Galaxy-wide births.** The Milky Way SFR is 1.65–2.0 M☉/yr. Assuming a mean stellar mass of 0.5 M☉ (an assumption, not a sourced value), this gives **≈3–4 stars born per yr** in the whole Galaxy (derived).
- **Birth is energetically sharp.** After the second core forms, accretion luminosity takes over. The emergent L is predicted to be a few tens of L☉ for a 1 M☉ core (Masunaga & Inutsuka 2000, via Young 2023). During the FHSC stage, L_fc is only 0.003–0.1 L☉. In principle this jump should brighten the mid-IR at the stellar position.
- **Monitoring depth.** The unTimely per-epoch coadds reach 0.66 (W1) and 1.14 (W2) mag deeper than single exposures at 50% completeness (Meisner+2023). The VVV/VIRAC2 survey provides K_s light curves at higher resolution in the southern plane (Lucas+2024).

## 3. Caveats / failure modes (ordered by expected impact)

- **F1. Outbursts vastly outnumber births (main false positive).**
  - Measured rates: Class 0 protostars burst every **438 yr** (95% CI 161–1884; Zakri+2022). Protostars in general burst about every **1000 yr** (90% CI 690–40,300; Fischer+2019; Park+2021). Class I FUors recur every **1.75 (+1.12/−0.87) kyr**, and 2–3% of Class I sources are eruptive (Contreras Peña+2024).
  - Bursts last more than 9 yr and change by ≥2 mag at 3.6 or 4.5 µm (Zakri+2022). A long burst in the NEOWISE window looks exactly like a persistent turn-on.
  - Scale estimate: if 20% of the prestellar clumps hide a Class 0 protostar (F2), about **270 outbursts** would occur over 12 yr (49,289 × 0.2 × 12 / 438, derived). Compare this with ≲5 genuine transitions.
- **F2. "Prestellar" clumps already contain protostars.**
  - Elia+2021 notes that the classification misses 70 µm sources below about 0.2 Jy and says the class should be read as "candidate starless". The median 5σ PACS 70 µm limit for prestellar clumps is **0.138 Jy** (derived from the IRSA `ulim_70` column).
  - Using the Dunham+2008 relation L_int = 3.3×10⁸ F₇₀^0.94 L☉ (F₇₀ in erg cm⁻² s⁻¹ scaled to 140 pc), that limit hides a source of **L_int ≈ 0.4 / 1.4 / 5.8 L☉ at 1 / 2 / 4.3 kpc** (derived).
  - In the catalogue, **3,999** prestellar clumps have a MIPSGAL 24 µm counterpart and **4,742** have a WISE 22 µm counterpart (IRSA query). Infall and outflow signatures have also been seen in 70 µm-quiet clumps (Traficante+2017).
- **F3. A Hi-GAL transition is a threshold crossing, not a birth.** A clump changes class when a source crosses the 70 µm detection limit (several L☉ at kpc distances). A newborn second core with L below that limit can only be seen after it grows. A "turn-on" in a distant clump therefore most likely tracks accretion growth or a burst, not the second-collapse moment.
- **F4. Newborn protostars are faint or invisible at 3–5 µm.**
  - Emission from the first core below 850 µm is fully reprocessed by the envelope (Young 2023).
  - 8 of 18 PBRS are undetected even at Spitzer 24 µm. Some are seen at 3.6–8 µm only through scattered light or shocked gas in outflow cavities (Stutz+2013; Dunham+2014).
  - At the median distance of 4.3 kpc, a Class 0 source with L ≲ few L☉ is far below the NEOWISE single-exposure limits (W1 ≈ 15.8, W2 ≈ 14.3 mag at 90% completeness).
- **F5. Distance bias and confusion.**
  - Hi-GAL clumps beyond about 5 kpc are unresolved blends of cores and inter-core gas. The distance bias "can significantly affect … the classification" (Elia+2021 §4; Baldeschi+2017).
  - WISE has a ~6″ PSF. unTimely/crowdsource deblends nebulosity inconsistently between epochs: 9.5% of epochal catalogues are nebulosity-affected, and the authors advise avoiding `HAS_ANY_NEBULOSITY = 1` for rare-object searches (Meisner+2023).
  - About 32% of NEOWISE single-exposure rows lack an AllWISE match and are mostly spurious (NEOWISE Explanatory Supplement II.1.e).
- **F6. Starless timescales are model-dependent.** Every statistical lifetime assumes a steady state and a reference clock (Class II = 2 Myr, H II region or maser lifetimes). The results range over an order of magnitude and depend on mass (Svoboda+2016) and density (Könyves+2015).
- **F7. First cores are too short-lived to catch.** The FHSC lifetime is 0.5–50 kyr (quoted in PPVI) or a few hundred yr in non-ideal MHD models. That gives an expected FHSC:Class 0 ratio of 0.002–0.02, or at most 1–2 FHSCs among the ~10³ nearby Class 0 sources (Young 2023).

## 4. Key numbers

| Quantity | Value | Source |
|---|---|---|
| Hi-GAL 360° entries (SEDs fitted) | 150,223 (94,604 high-reliability + 55,619 low) | Elia+2021 §2, Tables 1–2 |
| High-rel. prestellar / protostellar / unbound | **49,289 / 35,186 / 10,129** | Elia+2021 Table 1; reproduced by IRSA `evol_flag` counts |
| High-rel. with distance | 77,489 (Table 1) / 77,488 with `dist>0` on IRSA | Elia+2021; IRSA query |
| Prestellar with distance; median d | 40,696; 4.31 kpc (47% within 4 kpc; 1,929 within 1 kpc) | IRSA query (derived) |
| Median 5σ 70 µm limit, prestellar | 0.138 Jy | IRSA `ulim_70` (derived) |
| Hi-GAL catalogue hosting | **Not in VizieR** (`J/MNRAS/504/2742` returns "not found"). Hosted as IRSA TAP `higal360clump` (high-reliability only) and a VIALACTEA tarball. Paper I (inner Galaxy) is VizieR `J/MNRAS/471/100` (`hcatalog`, `lcatalog`). | VizieR/IRSA queries; Elia+2021 Data Availability |
| Key columns | `DIST` (kpc, null −999), `D_FLAG` (1 = kinematic from V_LSR), `VLSR`, `EVOL_FLAG` (0 unbound, 1 prestellar, 2 protostellar), `F70`, `ULIM_70`, `F22`, `F24`, `MASS` (<0 = computed at 1 kpc), `TEMP`, `L_BOL`, `T_BOL`, `LRATIO` | Elia+2021 App. A; IRSA schema |
| Reliability | No reliability column. Reliability is carried by which table you use (the IRSA table is high-reliability only). | IRSA schema |
| Hi-GAL inner-Galaxy tile dates | 2009-09-03 → 2011-11-05 (per-tile date, OD, ObsID) | Molinari+2016 tile table |
| Molinari HSA proposals | SDP 2009-10-23/24; KPOT_smolinar_1 2010-01-08→2011-11-05; OT1_smolinar_5 2011-05-05→2013-03-01; OT2_smolinar_7 2012-04-11→2012-11-15; DDT 2012-10/11 | HSA TAP `hsa.v_active_observation`. The mapping of each proposal to Hi-GAL fields is **UNVERIFIED**. |
| Prestellar core lifetime, Aquila (low mass) | **1.2 ± 0.3 Myr** (~4 t_ff). Falls from ~1.4 Myr at n > 10⁴ cm⁻³ to a few 10⁴ yr at the highest densities. Clock: 622 Class II YSOs at 2 Myr. | Könyves+2015 §5.1 |
| Prestellar core lifetime, Per/Ser/Oph | **0.45 Myr** (N_pre ≈ N_proto; 108 starless vs 92 protostellar cores) | Enoch+2008 |
| Prestellar core lifetime (review) | 2–5 free-fall times | Ward-Thompson+2007 (PPV) |
| Massive BGPS starless clumps | **0.37 ± 0.08 (M/10³ M☉)⁻¹ Myr** for M > 10³ M☉; 2,223 (47.5%) starless | Svoboda+2016 |
| High-mass starless phase | **0.2–1.7 Myr** (60–70% of lifetime); star-forming phase 0.1–0.7 Myr | Battersby+2017 |
| ATLASGAL clumps | 23% (up to 31%) star-forming. The first ~70% of the lifetime is starless. | Heyer+2016 |
| Hi-GAL prestellar:protostellar ratio | ~1.5 for M ≲ 10³ M☉ → 60% / 40% of time. Absolute lifetimes ~1–4×10⁵ yr (read from Fig. 14, approximate). | Elia+2021 §3.5 |
| Class 0+I lifetime | **~0.5 Myr** (0.42–0.54); Class 0 **0.15–0.16 Myr** (30–32% of protostars) | Dunham+2014 Tables 1, 3 |
| Class 0 / Class I lifetimes | 0.10–0.16 / 0.44–0.54 Myr | Evans+2009 |
| Class 0 / I / Flat half-lives | **47 ± 4 / 88 ± 7 / 87 ± 8 kyr** (for a 2 Myr Class II half-life) | Kristensen & Dunham 2018 |
| PBRS phase | ~25 kyr (~5% of Orion protostars) | Dunham+2014 §4.2.3 |
| FHSC luminosity; lifetime | 0.003–0.1 L☉ (likely ≳0.01); 0.5–50 kyr, or a few hundred yr in MHD | Young 2023; Dunham+2014 |
| Second core at birth | ≈0.0015 M☉ (0.02 M☉ in Tomida+2013); R = 1–4 R☉; L rises to a few ×10 L☉ | Young 2023 (citing Larson 1969, MI2000, Vaytet+2013, Bhandare+2020) |
| NEOWISE single-exposure SNR = 10 | W1 = 15.0, W2 = 13.5 mag (unconfused sky) | NEOWISE Expl. Suppl. II.1.c.iii |
| NEOWISE single-exposure SNR = 5 | ≈ W1 15.75, W2 14.25 (derived as SNR10 + 0.75 mag, background-limited). **UNVERIFIED** against the supplement's SNR = 5 table. | derived |
| NEOWISE 90% completeness | W1 = 15.8, W2 = 14.2–14.4 mag (year 11: 14.3) | Expl. Suppl. II.1.e.i |
| NEOWISE saturation | W1 ≈ 8.0, W2 ≈ 7.0 mag | Expl. Suppl. II.1.c.iv |
| NEOWISE detection threshold | Combined W1+W2 SNR > 3; about 32% of rows have no AllWISE match (mostly spurious) | Expl. Suppl. II.1 / II.1.e.ii |
| unTimely per epoch (COSMOS, ecliptic latitude β = 10°) | 50% complete: W1 17.14, W2 16.08. 90% reliable: 16.81, 15.34. Single-exposure comparison: 16.48/14.94 and 15.35/13.55. Covers 2010–2020 (~16 epochs). | Meisner+2023 §4 |
| IRSA TAP tables | `neowiser_p1bs_psd` (sources), `neowiser_p1bs_frm` (frame metadata), `neowiser_p1bm_frm` (image inventory), `allwise_p3as_mep` (AllWISE multi-epoch), `allwise_p3as_psd`, `allsky_4band_p1bs_psd`, `higal360clump`, `mipsgalc`, `spicy` | IRSA `TAP_SCHEMA.tables` |
| Outburst interval, Class 0 | **438 yr** (95% CI 161–1884); lasts > 9 yr; ΔM ≥ 2 mag at 3.6/4.5 µm | Zakri+2022 |
| Outburst interval, protostars | **~1000 yr** (90% CI 690–40,300) | Fischer+2019 |
| FUor recurrence, Class I (VVV) | **1.75 (+1.12/−0.87) kyr**; 2–3% of ~7,000 Class I sources are eruptive | Contreras Peña+2024 |
| FUor recurrence, Class II | 112 kyr (68% CI 74–180) | Contreras Peña+2019 |
| NEOWISE YSO variability | ~1,700 of ~5,400 YSOs variable; ~55% of protostars variable; FUor recurrence ~1000 yr (embedded) | Park+2021 |
| Milky Way SFR | **1.65 ± 0.19** M☉/yr; 1.9 ± 0.4; **2.0 ± 0.7** (Hi-GAL; 1.7 ± 0.6 from clumps with distances) | Licquia & Newman 2015; Chomiuk & Povich 2011; Elia+2022 |
| Births per yr, Galaxy | ≈3–4 stars/yr at an assumed mean mass of 0.5 M☉ (assumption **UNVERIFIED**) | derived |
| Expected Hi-GAL transitions | ≈0.05–0.35 per yr, or ≈0.6–5 over 2013–2024 | derived: 35,186 / (0.1–0.7 Myr) |

## 5. Open questions / next tests

1. **Predict W1/W2 fluxes for a newborn.** Run radiative transfer on Class 0 envelopes at 1–5 kpc to predict the W1/W2 flux of a newborn protostar. This decides whether H1 is detectable at all, or whether the search is really a search for young bursts (F3, F4).
2. **Restrict to a near subsample.** Limit the sample to d < 2 kpc (6,547 prestellar clumps) and drop clumps with 22/24 µm counterparts. Then quantify the burst background using the Zakri and Fischer rates, applied to the protostellar clumps as a control sample.
3. **Look up the Herschel epoch for every target.** Use `hsa.v_active_observation` so that each change point is timed relative to that target's own Herschel non-detection.
4. **Use JCMT/SCUBA-2 as a discriminator.** A burst heats an existing envelope, so the submillimetre flux rises with the mid-IR (Contreras Peña+2020). A birth in a prestellar clump should first show up as a compact 70 µm or submillimetre source.

## References

- Baldeschi A. et al. 2017, MNRAS 466, 3682 — Hi-GAL distance biases (not re-read in this pass).
- Battersby C., Bally J., Svoboda B. 2017, ApJ 835, 263 — arXiv:1702.02199
- Chomiuk L., Povich M. S. 2011, AJ 142, 197 — arXiv:1110.4105
- Contreras Peña C., Naylor T., Morrell S. 2019, MNRAS 486, 4590 — https://ui.adsabs.harvard.edu/abs/2019MNRAS.486.4590C
- Contreras Peña C. et al. 2020, MNRAS 495, 3614 — mid-IR vs sub-mm variability of embedded protostars
- Contreras Peña C. et al. 2023, JKAS 56, 253 — arXiv:2311.18187 (new eruptive YSOs from SPICY + WISE)
- Contreras Peña C., Lucas P. W., Guo Z., Smith L. 2024, MNRAS 528, 1823 — arXiv:2401.14472
- Dunham M. M. et al. 2008, ApJS 179, 249 — arXiv:0806.1754
- Dunham M. M. et al. 2014, Protostars & Planets VI, 195 — arXiv:1401.1809
- Elia D. et al. 2017, MNRAS 471, 100 (Hi-GAL Paper I; VizieR J/MNRAS/471/100)
- Elia D. et al. 2021, MNRAS 504, 2742 — arXiv:2104.04807; data: http://vialactea.iaps.inaf.it/vialactea/public/HiGAL_360_clump_catalogue.tar.gz
- Elia D. et al. 2022, ApJ 941, 162 — arXiv:2211.05573
- Enoch M. L. et al. 2008, ApJ 684, 1240 — arXiv:0805.1075
- Evans N. J. II et al. 2009, ApJS 181, 321 — arXiv:0811.1059
- Fischer W. J., Safron E., Megeath S. T. 2019, ApJ 872, 183 — arXiv:1901.08062
- Furlan E. et al. 2016, ApJS 224, 5 — https://ui.adsabs.harvard.edu/abs/2016ApJS..224....5F
- Heyer M. et al. 2016, A&A 588, A29 — arXiv:1601.06875
- Könyves V. et al. 2015, A&A 584, A91 — arXiv:1507.05926
- Kristensen L. E., Dunham M. M. 2018, A&A 618, A158 — arXiv:1807.11262
- Kuhn M. A. et al. 2021, ApJS 254, 33 (SPICY, 117,446 YSO candidates)
- Kulkarni C. S. et al. 2026, ApJ (accepted) — arXiv:2601.21013
- Lee Y.-H. et al. 2021, ApJ 920, 119 (JCMT Transient 4-yr summary) — arXiv:2107.10750. The volume/page is **UNVERIFIED**; DOI 10.3847/1538-4357/ac1679.
- Li J., Wang T. 2024, MNRAS 532, 2683 — arXiv:2406.18303
- Licquia T. C., Newman J. A. 2015, ApJ 806, 96 — arXiv:1407.1078
- Lu Y. et al. 2024, ApJS 272, 44 — doi:10.3847/1538-4365/ad41e2
- Lucas P. W. et al. 2020, MNRAS 499, 1805 — arXiv:2007.12056
- Lucas P. W. et al. 2024, MNRAS 528, 1789 — doi:10.1093/mnras/stad3929 (222 VVV sources with ΔK_s ≥ 4 mag)
- Mainzer A. et al. 2014, ApJ 792, 30 — arXiv:1406.6025
- Masunaga H., Inutsuka S. 2000, ApJ 531, 350 — doi:10.1086/308439
- Meisner A. M., Caselden D., Schlafly E. F., Kiwy F. 2023, AJ 165, 36 — arXiv:2209.14327
- Molinari S. et al. 2016, A&A 591, A149 — arXiv:1604.05911
- NEOWISE Explanatory Supplement, §II.1 — https://wise2.ipac.caltech.edu/docs/release/neowise/expsup/sec2_1.html
- Park W. et al. 2021, ApJ 920, 132 — arXiv:2107.10751
- Safron E. J. et al. 2015, ApJL 800, L5 — arXiv:1501.00492
- Stutz A. M. et al. 2013, ApJ 767, 36 — arXiv:1302.1203
- Svoboda B. E. et al. 2016, ApJ 822, 59 — arXiv:1511.08810
- Tomida K. et al. 2013, ApJ 763, 6 — arXiv:1206.3567 (the volume/page is **UNVERIFIED**)
- Traficante A. et al. 2017, MNRAS 470, 3882 — 70 µm-quiet clumps with embedded star formation
- Vaytet N. et al. 2013, A&A 557, A90 — doi:10.1051/0004-6361/201321423; Bhandare A. et al. 2020, A&A 638, A86
- Ward-Thompson D. et al. 2007, Protostars & Planets V, 33 — arXiv:astro-ph/0603474
- Young A. K. 2023, Front. Astron. Space Sci. 10, 1288730 — arXiv:2312.03039
- Zakri W. et al. 2022, ApJL 924, L23 — arXiv:2201.04647 (the volume/page is **UNVERIFIED**; DOI 10.3847/2041-8213/ac46ae)
