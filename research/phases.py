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
]
