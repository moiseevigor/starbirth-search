"""Catalog-level NEOWISE turn-on classifier.

Rows: NEOWISE-R single-exposure detections within a search radius of each
target (columns tid, t_ra, t_dec, ra, dec, mjd, w2snr, cc_flags).
"""
from __future__ import annotations

import numpy as np
import pandas as pd

NEO_START_MJD = 56640.0  # 2013-12-13, NEOWISE-R survey start
N_VISITS = 22            # ~6-month visits through 2024-08
VISIT_DAYS = 182.625


def _sep_arcsec(ra1, dec1, ra2, dec2):
    # ponytail: small-angle separation; fine at arcsec scales away from the poles
    dra = (np.asarray(ra1) - np.asarray(ra2) + 180) % 360 - 180
    return 3600 * np.hypot(dra * np.cos(np.radians(dec2)), np.asarray(dec1) - np.asarray(dec2))


def clean(rows: pd.DataFrame, min_snr: float = 5.0) -> pd.DataFrame:
    """W2 >= min_snr, W2 contamination flag '0'. qual_frame is NOT cut (it drops real detections)."""
    ok = (rows.w2snr >= min_snr) & (rows.cc_flags.astype(str).str[1] == "0")
    return rows[ok]


def track(rows: pd.DataFrame, assoc_arcsec: float = 3.0, track_arcsec: float = 2.0) -> pd.DataFrame:
    """Follow the source nearest each target instead of a fixed aperture.

    Centre = median position of clean detections within assoc_arcsec of the
    target; keep detections within track_arcsec of that centre. A steady source
    sitting on the aperture edge is then either tracked in every visit or not
    at all — it can no longer flicker in/out and fake a turn-on.
    """
    g = clean(rows)
    g = g.assign(sep=_sep_arcsec(g.ra, g.dec, g.t_ra, g.t_dec))
    near = g[g.sep <= assoc_arcsec]
    if near.empty:
        return g.iloc[:0]
    c = near.groupby("tid")[["ra", "dec"]].median().rename(columns={"ra": "c_ra", "dec": "c_dec"})
    g = g.join(c, on="tid", how="inner")
    return g[_sep_arcsec(g.ra, g.dec, g.c_ra, g.c_dec) <= track_arcsec]


def visit_table(tracked: pd.DataFrame, min_exp: int = 3) -> pd.DataFrame:
    """tid x visit boolean: detected in >= min_exp exposures of that visit.

    A visit has ~12 exposures; a real SNR>=10 source is detected in most of
    them, while single-exposure detections are mostly spurious (E1-pilot
    offset-control tids 177, 1463: 1 of ~12 exposures per visit).
    """
    n = pd.crosstab(tracked.tid.values, _visit(tracked.mjd).values)
    return n.ge(min_exp).reindex(columns=range(N_VISITS), fill_value=False)


def _visit(mjd):
    return ((mjd - NEO_START_MJD) // VISIT_DAYS).astype(int).clip(0, N_VISITS - 1)


def classify(rows: pd.DataFrame, n_targets: int, min_pre: int = 3, min_post: int = 3,
             min_post_frac: float = 0.8, min_post_snr: float = 10.0,
             confusion_arcsec: float = 6.0, max_pre_busy: float = 0.5) -> pd.Series:
    """none / steady / turn_on / confused / other per target id 0..n_targets-1.

    rows: raw detections (any flags) within >= confusion_arcsec of each target.

    turn_on: first detected visit >= min_pre, >= min_post detected visits,
    detected in >= min_post_frac of visits from onset, and post-onset median
    SNR >= min_post_snr (so earlier non-detections imply >= ~0.75 mag rise).
    confused: would be turn_on, but >= max_pre_busy of the pre-onset visits
    already have ANY W2 detection (w2snr >= 3, flags ignored) within
    confusion_arcsec (~W2 PSF FWHM). Flags grade measurement quality, not
    existence: a steady star with halo/spike flags (h/H/d/D) in most exposures
    and rare clean ones mimics a sporadic late source (E1-pilot tids 362, 1242,
    1862); a steady neighbour's astrometric outliers do too (tid 1768).
    ponytail: assumes every visit covers the position (NEOWISE ~6-month cadence);
    upgrade = coverage from neowiser_p1bs_frm to turn gaps into upper limits.
    """
    tracked = track(rows)
    vt = visit_table(tracked)
    c = rows[rows.w2snr >= 3]
    c = c[_sep_arcsec(c.ra, c.dec, c.t_ra, c.t_dec) <= confusion_arcsec]
    busy = pd.crosstab(c.tid.values, _visit(c.mjd).values).gt(0).reindex(columns=range(N_VISITS), fill_value=False)
    snr = tracked.groupby("tid").w2snr.median()
    out = pd.Series("none", index=range(n_targets))
    for tid, row in vt.iterrows():
        det = np.flatnonzero(row.values)
        if len(det) == 0:
            continue
        first = det[0]
        if (first >= min_pre and len(det) >= min_post and row.values[first:].mean() >= min_post_frac
                and snr[tid] >= min_post_snr):
            out[tid] = "confused" if busy.loc[tid].values[:first].mean() >= max_pre_busy else "turn_on"
        elif first < min_pre and row.values.mean() >= min_post_frac:
            out[tid] = "steady"
        else:
            out[tid] = "other"
    return out
