"""Research log: one entry per phase, rendered as a visual report in the viewer.

Single source of truth for the scientific narrative (question -> hypothesis ->
test -> result -> verdict -> caveats -> next). Add a phase here in the same
change that adds its experiment; `figs` names figure renderers in viewer/app.html.
verdict: confirmed | refuted | partial | null | pending
"""

PHASES = [
    dict(
        id="L", title="Literature survey", date="2026-09-26", verdict="confirmed",
        question="Has anyone caught a starless core turning into a protostar, and what should the birth look like?",
        hypothesis="If birth were observable in archival IR data, the literature would contain either a detection "
                   "or a model predicting a prompt (years) mid-IR brightening at second-core formation.",
        test="36 papers read in full (birth physics, first-core candidates, lifetimes, Hi-GAL, outbursts, survey "
             "methods) into the research vault, with a synthesis.",
        result="No published detection. Every collapse model keeps the newborn inside an opaque envelope: luminosity "
               "grows over ~1e2-1e4 yr and near-IR light escapes only after 2e4-1.4e5 yr (Masunaga & Inutsuka 2000); "
               "'no immediate change in the SED' (Young 2023). Accretion bursts of existing protostars recur every "
               "~0.4-2 kyr and mimic a turn-on.",
        caveats="No model gives the observable light curve over the first 10-1e3 yr; outflow cavities could open a "
                "faster mid-IR path. Lifetimes are uncertain by factors of 2-3.",
        next="Quantify expected births vs burst impostors for the Hi-GAL sample (E-1).",
        figs=["timescales", "bursts"]),
    dict(
        id="E0", title="Synthetic change-point calibration", date="2026-09-26", verdict="confirmed",
        question="Can a change-point test recover a persistent step in WISE-like cadence?",
        hypothesis="A weighted two-level BIC scan detects steps of >= 1 sigma per exposure with near-zero false "
                   "alarms on 21 epochs x 12 exposures.",
        test="2,000 synthetic light curves per amplitude, Gaussian noise, random onset epoch; detection = "
             "delta-BIC >= 20 and positive step.",
        result="0% false alarms at 0 sigma, 96% detection at 1 sigma, ~100% at >= 1.5 sigma. 49k curves take ~3 s "
               "on the M2 Pro.",
        caveats="Independent Gaussian noise overstates significance: real NEOWISE errors are correlated within a "
                "visit, and real turn-ons are high-SNR (the problem is confusion, not noise).",
        next="Check whether the post-birth state is visible at 4.6 um at all (E-1B).",
        figs=["e0"]),
    dict(
        id="E-1B", title="Is a young protostar visible at 4.6 um?", date="2026-09-26", verdict="confirmed",
        question="Do Hi-GAL protostellar clumps (the post-transition state) show a W2 source above chance?",
        hypothesis="Excess W2 match rate (clump position minus 60\" offset) > 0.05 for the youngest protostellar "
                   "clumps.",
        test="AllWISE crossmatch of 4,000 prestellar + 4,000 protostellar clumps (3\", W2 SNR >= 5), with a 60\" "
             "offset control; protostellar split by L/M quartile.",
        result="Youngest quartile excess df_W2 = 0.26 (chance rate 4.4%); matched sources are bright (median "
               "W2 = 10.2). Prestellar clumps already show a 2.3% excess (vetoed).",
        caveats="Hi-GAL protostellar clumps are older and more luminous than a fresh second core: df_W2 is an "
                "optimistic upper bound for a true birth.",
        next="Turn detectability into expected counts against the burst background (E-1A).",
        figs=["w2vis", "ratio"]),
    dict(
        id="E-1A", title="Expected births vs burst impostors", date="2026-09-26", verdict="partial",
        question="Is the expected number of observable births large enough, and larger than bursts?",
        hypothesis="Y (observable births in 12 yr) >= 0.1 and exceeds the burst background B.",
        test="Steady state N_T = N_proto * dt / tau_proto; Y = N_T * df_W2 * (1 - f_prehost); "
             "B = N_pre * f_hidden * dt / burst_interval * p_lift, over literature ranges.",
        result="Y ~ 0.06-0.4 within 4 kpc (0.15-1.1 for all distances) but B ~ 1-53: signal/background 0.003-0.35. "
               "A W2 turn-on alone cannot claim a birth.",
        caveats="p_lift is a guess; Y ignores the literature result (L) that births are dark at 3-5 um for ~1e4 yr, "
                "which drives Y towards zero.",
        next="Measure the empirical turn-on rate directly (E1).",
        figs=["yield"]),
    dict(
        id="E1-pilot", title="NEOWISE turn-on pilot, 2,000 clumps", date="2026-09-26", verdict="null",
        question="Do prestellar clumps show catalog-level W2 turn-ons above an offset control?",
        hypothesis="Prediction from E-1: excess ~1e-4-3e-3 per clump, i.e. undetectable in 2,000 clumps unless "
                   "artefacts dominate.",
        test="NEOWISE-R single exposures within 6\" of 2,000 prestellar clumps (d <= 4 kpc) and offset positions; "
             "tracked-source classifier; injection-recovery on real steady light curves.",
        result="0 turn-ons on and off at every threshold; completeness 0.83-0.91 (SNR >= 10); 95% upper limit "
               "1.7e-3 per clump. Hand-checking every near-candidate exposed 4 artefact classes, each now fixed and "
               "tested.",
        caveats="Coverage assumed complete every visit; faint (SNR < 10) turn-ons excluded by design.",
        next="Scale to all 19,219 clumps within 4 kpc (E1-full).",
        figs=["sweep", "artefacts"]),
    dict(
        id="E1-full", title="Full turn-on search, 19,219 clumps", date="2026-09-26", verdict="partial",
        question="Across every prestellar clump within 4 kpc, how many persistent W2 turn-ons appear 2014-2024?",
        hypothesis="Turn-ons occur at the burst-background rate; births contribute ~0.",
        test="Same classifier and offset control as the pilot on 19,219 clumps (1.25M NEOWISE exposures on-source, "
             "1.16M off).",
        result="4 turn-ons on-source vs 1 in the offset control (a flat-flux deblending artefact). Count excess alone "
               "is not significant (P = 0.19 for >= 4 of 5); the archival vetting (E3) separates them.",
        caveats="The confusion veto costs ~10-20% completeness in crowded fields.",
        next="Vet every event against its archival history (E3).",
        figs=["classes", "funnel"]),
    dict(
        id="E3", title="Archival vetting of every event", date="2026-09-26", verdict="refuted",
        question="Is any turn-on a birth, i.e. with no young star at that position before?",
        hypothesis="H_birth: no Spitzer/AllWISE source before onset. H_burst: a catalogued YSO was already there.",
        test="Per event: NEOWISE coverage within 60\", AllWISE 2010, Spitzer GLIMPSE I/II/3D, MIPSGAL, SPICY, "
             "SIMBAD, per-visit W2 image stacks and difference images.",
        result="H_birth refuted for all 4: three were SPICY YSOs (flat-spectrum, Class II, Class I; each within "
               "0.8\" of the NEOWISE centroid) and one a known AllWISE YSO. Amplitudes 1.1-3.3 mag; G354.23+0.51 is a FUor-like 3.3 mag outburst with a 2-yr rise and "
               "8-yr plateau. Best follow-up: G261.89-2.24, a faint red source with an 8-yr brightening episode.",
        caveats="Pre-existing-source checks depend on survey footprints (GLIMPSE misses |b| > 1 deg outside 3D).",
        next="Use the events as a burst-rate measurement and compare with published intervals (E4).",
        figs=["explorer"]),
    dict(
        id="E4", title="Burst-rate calibration against the literature", date="2026-09-27", verdict="pending",
        question="Do the E1 turn-ons of catalogued YSOs occur at the published protostellar burst rate?",
        hypothesis="Implied interval tau = N_eff * dt_eff * completeness / k lies inside published confidence "
                   "intervals (Zakri+2022, Park+2021, Contreras Pena+2024).",
        test="SPICY YSOs within 3\" of the 19,219 clumps; N_eff = hosts not steadily detected by NEOWISE (only these "
             "can register a turn-on); dt_eff = 8 yr; exact Poisson CI on k.",
        result="(computed at build time from artifacts/e4/burst_calibration.json)",
        caveats="Small k; hosts within 3\" include chance alignments (still YSOs); SPICY misses Class 0 sources.",
        next="E5: test whether SPICY classes of hosts inside cold clumps are reliable (SED refit with W1-W4 "
             "and Herschel), then faint (SNR < 10) turn-ons with forced photometry on unTimely epochal coadds.",
        figs=["e4"]),
    dict(
        id="E5", title="Are YSO classes reliable inside clumps?", date="2026-09-27", verdict="partial",
        question="E4 found a Class II burst rate far above the published one. Are SPICY classes trustworthy for "
                 "YSOs sitting inside cold Hi-GAL clumps?",
        hypothesis="SPICY 'Class II' hosts of prestellar clumps are redder in IRAC [3.6]-[4.5] than Class II "
                   "sources in protostellar clumps or in the field (i.e. extincted or mislabelled protostars).",
        test="Fraction of Class II with [3.6]-[4.5] > 0.7 (the Gutermuth+2009 Class I colour condition), bootstrap "
             "95% CI, for SPICY hosts within 3\" of prestellar clumps, of protostellar clumps (both d <= 4 kpc), "
             "and a field sample (every 20th SPICY id, |b| < 1 deg).",
        result="(computed at build time from artifacts/e5/host_colours.json)",
        caveats="[3.6]-[4.5] mixes extinction (E([3.6]-[4.5]) ~ 0.13 A_K) with intrinsic envelope emission and "
                "4.5 um shocked-H2 emission; a colour-colour test against the reddening vector is needed to "
                "separate them.",
        next="E6: deredden hosts along the reddening vector ([3.6]-[4.5] vs [4.5]-[5.8]) to separate extinction "
             "from envelope emission; then forced photometry for faint turn-ons (unTimely).",
        figs=["e5"]),
    dict(
        id="E6", title="Extinction or envelope?", date="2026-09-27", verdict="partial",
        question="E5 found clump-hosted YSOs strongly reddened. Is that dust in front of them (extinction) or "
                 "their own envelopes (intrinsically younger objects)?",
        hypothesis="H_ext: the extinction law is flat from 4.5 to 8 um (Indebetouw+2005: A_4.5 = A_5.8 = A_8.0 = "
                   "0.43 A_K, A_3.6 = 0.56 A_K), so clump hosts should be redder than the field in [3.6]-[4.5] but "
                   "not in [4.5]-[5.8] (|delta median| < 0.1 mag). H_env: both colours shift.",
        test="Median colour differences, clump Class II hosts minus field Class II, with bootstrap 95% intervals, "
             "for [3.6]-[4.5], [4.5]-[5.8] and [4.5]-[8.0]; implied A_K = delta([3.6]-[4.5]) / 0.13.",
        result="(computed at build time from artifacts/e6/colour_colour.json)",
        caveats="Above A_K ~ 1 the IRAC extinction law flattens towards the Weingartner & Draine R_V = 5.5 model "
                "(Chapman+2009), which is not exactly flat from 4.5 to 5.8 um; PAH emission at 6.2 and 7.7 um "
                "enters [5.8] and [8.0] in bright regions.",
        next="E7: faint (SNR < 10) turn-ons with forced photometry on unTimely epochal coadds, to reach below the "
             "catalog threshold where very young, low-luminosity sources would first appear.",
        figs=["e6"]),
    dict(
        id="E7", title="Faint turn-ons with forced photometry", date="2026-09-27", verdict="superseded",
        question="Below the NEOWISE catalog threshold, do prestellar clumps show faint persistent brightenings that "
                 "the catalog-level search (E1) could not see?",
        hypothesis="Rises (positive change point, onset 2015.5-2023.5) at clump positions exceed the offset-control "
                   "rate once the delta-BIC threshold is set to a 1% false-positive rate on the offsets.",
        test="Forced aperture photometry (r = 5.5\", sky annulus 11-19\") on every NEOWISE-R W2 frame at 685 "
             "'other'/'confused'/'turn_on' positions plus 500 random 'none' positions and their 60\" offsets; "
             "per-visit medians; E0 change-point scan. Self-check: G354, G337 and G261 recovered blind "
             "(delta-BIC 5666 / 3010 / 414), offsets flat.",
        result="(computed at build time from artifacts/e7/summary.json)",
        caveats="Fixed-aperture photometry is blended with neighbours in crowded fields; a varying neighbour inside "
                "5.5\" mimics a rise. 'From nothing' uses pre-onset flux < 3 sigma, not a true upper limit.",
        next="Superseded by E7b after an adversarial review: clump positions were preselected for variability "
             "while offsets were not, photometry errors ignored masks and visit systematics, and 'from nothing' "
             "did not require a post-onset detection.",
        figs=["e7"]),
    dict(
        id="E7b", title="Faint rises, symmetric re-test", date="2026-09-27", verdict="pending",
        question="Correcting the three E7 flaws, is there a clump-associated excess of faint W2 rises, and does any "
                 "rise start from nothing?",
        hypothesis="Pre-registered: confirmed only if the bootstrap 95% lower bound of the population-weighted rise "
                   "rate (clumps minus offsets) is above zero, using rises confirmed with mask and uncertainty images.",
        test="Both arms classified by the same E1 rule on their own detections and sampled per stratum (all "
             "variable, 500 none, 300 steady); rates weighted by stratum size. Frames with qual_frame = 0 or moon "
             "< 15 deg dropped; per-visit error = max(propagated, robust scatter) plus a systematic floor calibrated "
             "on offsets (median reduced chi^2 = 1); threshold = population-weighted 99th percentile of offsets "
             "(>= 20). Tier 2 remeasures every rise with L1b mask (fatal bits) and uncertainty images. "
             "Injection-recovery on real clump light curves. 'From nothing' needs pre-onset flux < 3 sigma, no "
             "catalog detection before onset, post-onset >= 5 sigma and a >= 5 sigma difference-image source.",
        result="(computed at build time from artifacts/e7b/results.json)",
        caveats="Aperture photometry still blends neighbours within ~6\"; the offset arm samples the Galactic field, "
                "not clump backgrounds, so the FPR calibration is approximate at structured positions.",
        next="Human review of every flagged candidate in the local review desk (scripts/serve_catalog.py); "
             "the far-IR/sub-mm two-epoch test remains the only route to a birth signal.",
        figs=["e7b"]),
    dict(
        id="E8", title="Which dust hides a newborn at 4.6 um? (scenario)", date="2026-09-27", verdict="partial",
        question="The literature says a newborn protostar is dark at 3-5 um. Is it the clump's own beam-averaged "
                 "dust column (which Hi-GAL measures) or the unresolved inner envelope, and how much is simply "
                 "distance?",
        hypothesis="Per luminosity L in {1, 5, 25, 100} L_sun. H_dist(L): with zero extinction, fewer than half the "
                   "clumps are close enough for the source to reach W2 = 14.3. H_clump(L): distance alone leaves "
                   "a majority detectable but the clump column pushes the majority below the limit.",
        test="Per prestellar clump (0 < d <= 4 kpc): A_4.5 from the catalogue surface density (Sigma -> N_H2 -> "
             "A_V -> A_K -> A_4.5, half the column for a central source); unextincted W2 scaled from the HOPS "
             "Class 0 median ([4.5] = 12.16 at 420 pc for 5.5 L_sun, F_4.5 ~ L); fraction detectable with and "
             "without clump extinction for L = 1, 5, 25, 100 L_sun.",
        result="(computed at build time from artifacts/e8/extinction_budget.json)",
        caveats="This is a scenario on an observed anchor, not a decomposition: the HOPS [4.5] values already "
                "contain envelope, geometry and Orion foreground extinction, so the inner-envelope term cannot be "
                "isolated and 'distance' vs 'clump column' are relative shifts. F_4.5 ~ L is crude (scattered/shocked "
                "light). A fresh newborn (no near-IR for ~2e4 yr per Masunaga & Inutsuka 2000) is fainter than any HOPS "
                "source, so all fractions are upper bounds. Sigma is beam-averaged (Hi-GAL 250 um beam ~18\").",
        next="Human review of every flagged candidate (review desk), then the far-IR/sub-mm two-epoch test that "
             "the literature identifies as the band where a birth first shows.",
        figs=["e8"]),
    dict(
        id="G1", title="Event gallery by prominent feature", date="2026-09-28", verdict="partial",
        question="Beyond the rise-only test, what kinds of variability do the clump positions show, and which "
                 "events are strongest?",
        hypothesis="Events at clump positions outnumber offset-control events in every feature class that involves "
                   "a pre-existing source (brightening, fade, ramp), while the 'appearance' class, the only one "
                   "compatible with a birth, is not enriched.",
        test="Every forced light curve (both arms; E7b design, all steady-stratum positions, offset twins) is scanned "
             "for the best step in either direction at the E7b threshold, then classified by amplitude (mag), shape "
             "(step / ramp / flare / fade / dip), rise time, W1-W2 change and prior counterpart. Strength = "
             "log10(delta-BIC) + |amplitude| + 1 if tier-2 confirmed.",
        result="(computed at build time from artifacts/gallery/events.json and the review catalog)",
        caveats="The extended steady-stratum sample is not part of the pre-registered E7b population estimate; the "
                "classifier's amplitude needs a positive pre-onset flux, so 'appearance' and 'unusable' are limits, "
                "not measurements. Offset-arm coverage is smaller (E7b design + twins), so the on/off ratio per "
                "class is indicative, not a rate comparison.",
        next="Human review of the strongest events per class in the desk; sub-mm follow-up of the strongest fades "
             "and outbursts.",
        figs=["gallery"]),
    dict(
        id="E9", title="Alternative explanations for every event", date="2026-09-28", verdict="pending",
        question="Is each event better explained by a known star, an evolved Galactic object, dust, a blend or an "
                 "artefact than by a new star?",
        hypothesis="Every clump event has at least one archival alternative explanation; no event is left "
                   "'unexplained by the archives' after the tests, and the offset controls show the same mix.",
        test="Per event: SIMBAD stellar / variable / AGB types within the 5.5\" aperture; SPICY YSO; Gaia DR3 "
             "sources within 2\" with their variability class (vari_classifier_result); Lomb-Scargle on the forced "
             "light curve for P = 150-1500 d (FAP < 0.01; heavily aliased at 6-month cadence, so only "
             "'sinusoid-consistent'); extinction rule from the W1-W2 change (fade + redder, or brightening + bluer); "
             "blend from clustered NEOWISE catalog positions; artefact from unusable baselines, rising offset twins "
             "or low-coverage onsets; prior AllWISE/GLIMPSE/MIPSGAL source. One best alternative by priority.",
        result="(computed at build time from artifacts/e9/alternatives.json)",
        caveats="'Unexplained by the archives' means no archival counterpart or effect was found, not that a new "
                "star is required: the pre-onset forced flux and the E7b stratum still apply. Gaia is optical and "
                "misses embedded sources by construction; SIMBAD types are heterogeneous.",
        next="Human review in the desk with the alternative explanation shown on each card; sub-mm follow-up of "
             "any clump event that stays unexplained and passes the checklist.",
        figs=["e9"]),
]
