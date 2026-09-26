"""Single source of truth for terms, metrics and labels used in reports.

`python -m starbirth.glossary` regenerates docs/GLOSSARY.md; report writers
call `markdown()` and append it.
"""
from __future__ import annotations

from pathlib import Path

GLOSSARY: dict[str, str] = {
    # physics
    "FHSC": "First hydrostatic core: ~AU-scale, ~1000 K pressure-supported gas core that precedes H2 dissociation; lives ~10^2-10^3 yr.",
    "second core / birth": "Second hydrostatic core, formed after H2 dissociation triggers a second collapse; conventionally the birth of the protostar.",
    "Class 0": "Youngest protostellar class: envelope mass > stellar mass, SED peaking in the far-IR/sub-mm (T_bol < 70 K).",
    "T_bol": "Bolometric temperature: temperature of a blackbody with the same mean frequency as the SED.",
    "L_int": "Internal luminosity of the central source only, excluding external heating.",
    "VeLLO": "Very low luminosity object: embedded protostar with L_int <= 0.1 L_sun (Dunham+2008).",
    "PBRS": "PACS Bright Red Source: Orion protostar with log(lambda F_lambda(70)/lambda F_lambda(24)) > 1.65 (Stutz+2013).",
    "FUor / EXor": "Long (decades) / short (months) accretion outbursts, named after FU Ori / EX Lup.",
    "half-life": "Kristensen & Dunham 2018's statistically inferred phase duration.",
    "statistical lifetime": "t_X = (N_X / N_ref) * t_ref; assumes steady state and that every X evolves into the reference class.",
    "accretion burst": "Episodic luminosity increase of an already-existing protostar (FUor/EXor-like); the main astrophysical false positive.",
    # data
    "Hi-GAL": "Herschel infrared Galactic Plane Survey (70-500 um, observed 2009-2013). Clump catalogue: Elia et al. 2021, IRSA table `higal360clump` (94,604 high-reliability rows).",
    "prestellar (evol_flag=1)": "Hi-GAL clump that is gravitationally bound and has no 70 um counterpart (49,289 clumps).",
    "protostellar (evol_flag=2)": "Hi-GAL clump with a 70 um counterpart (35,186 clumps).",
    "high-reliability": "Hi-GAL SED fitted with >=4 Herschel bands and T not at the 5/40 K grid edge (Elia+2021 Sec. 2); the IRSA table holds only these.",
    "unbound starless (evol_flag=0)": "Hi-GAL starless clump below the Larson-mass threshold (10,129 clumps).",
    "W1 / W2": "WISE bands at 3.4 / 4.6 um; magnitudes are Vega (`w1mpro`, `w2mpro`).",
    "AllWISE": "WISE+NEOWISE-cryo coadded catalogue (epochs 2010-2011), IRSA `allwise_p3as_psd`; used as the ~Herschel-epoch baseline.",
    "NEOWISE": "Reactivated WISE W1/W2 survey 2013-12 to 2024-08, ~1-day visits every ~6 months; single exposures in IRSA `neowiser_p1bs_psd`.",
    # method / experiments
    "E-1": "Feasibility experiment: expected number of observable turn-ons before building the pipeline.",
    "E0": "Synthetic change-point calibration on WISE-like cadence (docs/EXPERIMENTS.md).",
    "W2 match": "An AllWISE source with w2snr >= 5 within 3 arcsec of the clump position (nearest kept).",
    "offset control": "Same targets shifted +60 arcsec in Dec; its W2 match rate f_off is the chance-alignment baseline.",
    "f_on / f_off": "Fraction of clumps with a W2 match at the clump position / at the offset position.",
    "df_W2": "Detectability of the post-birth state = f_on - f_off for the youngest-quartile (lowest L_bol/M) protostellar clumps.",
    "f_prehost": "f_on - f_off for prestellar clumps: fraction already hosting a W2 source at the Herschel epoch (vetoed).",
    "L/M": "Clump bolometric luminosity over mass (L_sun/M_sun); low L/M = earlier evolutionary stage.",
    "tau_pre / tau_proto": "Lifetimes (Myr) of the Hi-GAL prestellar / protostellar clump phases. Steady state: N_pre/tau_pre = N_proto/tau_proto.",
    "dt": "Search window: 12 yr (Hi-GAL epoch 2010-2012 to NEOWISE end 2024-08, minus 2 epochs needed to confirm persistence).",
    "N_T": "Expected prestellar->protostellar transitions in the window: N_T = N_proto * dt / tau_proto.",
    "Y": "Expected observable W2 turn-ons: Y = N_T * df_W2 * (1 - f_prehost).",
    "B": "Expected accretion-burst background from protostars hidden in prestellar clumps: B = N_pre * f_hidden * dt / burst_interval.",
    "NEOWISE visit": "~6-month bin of NEOWISE-R data counted from 2013-12-13 (visit 0) to 2024-08 (visit 21); a position is observed ~once per visit for ~1 day.",
    "tracking": "Following the source nearest the clump (centre = median of clean detections within 3\"; keep detections within 2\" of it) instead of a fixed aperture.",
    "turn_on / steady / other / none": "Catalog light-curve classes: turn_on = first detection after visit 3, >=3 detected visits, detected in >= min_post_frac of visits from onset, post-onset median SNR >= 10; steady = detected from the start in >= 80% of visits; other = sporadic; none = never detected.",
    "confused": "Light-curve class: would be a turn_on, but >= 50% of pre-onset visits already have any W2 detection (flags ignored) within 6\" (~W2 PSF FWHM).",
    "E1 full run": "Turn-on search over all 19,219 prestellar clumps with 0 < d <= 4 kpc (plus 60\" offset control), NEOWISE-R 2013-12 to 2024-08.",
    "E3-lite vetting": "Per-candidate archival history: NEOWISE coverage within 60\", AllWISE, GLIMPSE I/II/3D, MIPSGAL, SPICY, SIMBAD (research/e3_vet_candidate.py).",
    "coverage proxy": "Number of NEOWISE detections of any source within 60\" in a visit; > 0 means the position was imaged in that visit.",
    "W2 stack": "Median of up to 8 NEOWISE W2 single-exposure frames of one visit, reprojected to a common 64x64 grid at 1.5\"/px (96\" field); one brightness scale per target for all epochs.",
    "difference image": "W2 stack of a visit minus the median of the first three visits (2014-15); red = brighter, blue = fainter, white = no change.",
    "burst rate (E1)": "Completeness-corrected turn-on rate of pre-existing YSOs: k_on / (N searched * mean injection completeness), per clump over the NEOWISE window.",
    "SPICY": "Spitzer/IRAC Candidate YSO catalogue (Kuhn+2021, 117,446 sources); requires 3.6 and 4.5 um detections, so it misses the youngest Class 0 objects.",
    "[3.6]-[4.5]": "Spitzer IRAC colour (Vega mag) between 3.6 and 4.5 um; > 0.7 is part of the Gutermuth+2009 Class I criteria. Extinction adds E([3.6]-[4.5]) ~ 0.13 A_K (Indebetouw+2005).",
    "SPICY host": "A SPICY YSO within 3\" of a clump position (E4/E5).",
    "red fraction (E5)": "Fraction of SPICY Class II sources with [3.6]-[4.5] > 0.7 mag; 95% CI from 2,000 bootstrap resamples.",
    "[4.5]-[5.8]": "Spitzer IRAC colour (mag); nearly extinction-free (A_4.5 = A_5.8 = 0.43 A_K, Indebetouw+2005), so it tracks intrinsic envelope emission.",
    "Gutermuth Class I cut": "[3.6]-[4.5] > 0.7 and [4.5]-[5.8] > 0.7 mag (simplified from Gutermuth+2009).",
    "A_K": "Extinction in the K band (mag); A_V ~ 10 A_K. Implied A_K (E6) = delta median([3.6]-[4.5]) / 0.13.",
    "min_post_frac": "Minimum fraction of visits (from onset onward) in which a turn_on source must be detected.",
    "95% UL (Poisson)": "Upper limit on a rate with k=0 events in n trials: 3/n (from -ln 0.05 ~ 3).",
    # metrics
    "sigma per exposure": "Injected step amplitude in units of the per-exposure Gaussian noise sigma (synthetic E0 only).",
    "delta_BIC": "BIC(constant) - BIC(step); BIC = chi^2 + k ln n with k=1 (constant) or 3 (two levels + change index). Detection if >= 20 and step > 0.",
    "detection rate": "Fraction of simulated curves with delta_BIC >= threshold and positive step.",
    "localization rate": "Fraction of simulated curves detected AND with change index within +/-1 epoch (12 exposures) of truth.",
    "SNR": "Signal-to-noise ratio; SNR = 5 is a 5-sigma detection (`w2snr`).",
    "binomial SE": "Standard error of a fraction p over n trials: sqrt(p(1-p)/n).",
}


def markdown() -> str:
    lines = ["## Glossary", "", "| term | definition |", "|---|---|"]
    lines += [f"| {k} | {v} |" for k, v in GLOSSARY.items()]
    return "\n".join(lines) + "\n"


if __name__ == "__main__":
    out = Path(__file__).resolve().parents[2] / "docs" / "GLOSSARY.md"
    out.write_text("# Glossary\n\n" + markdown().split("\n", 2)[2])
    print(f"wrote {out}")
