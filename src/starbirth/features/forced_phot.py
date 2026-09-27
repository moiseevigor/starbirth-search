"""Forced aperture photometry on WISE/NEOWISE L1b frames, with honest errors.

Addresses the E7 adversarial review:
* pixels flagged by the L1b mask (fatal bits per the WISE Explanatory Supplement
  sec. IV.4.a, plus transient/outlier bits) are excluded; a frame with > 25% of its
  aperture masked is rejected;
* per-frame error = uncertainty image in the aperture (if given) + sky-level error,
  else the sky-annulus scatter;
* per-visit error = max(error of the weighted mean, robust scatter / sqrt(n)), plus a
  systematic floor sigma_sys^2 = s_abs^2 + (s_rel * F)^2 calibrated on control
  positions so that constant light curves have median reduced chi^2 = 1.
Fluxes are normalised to zeropoint 22.5 (m = 22.5 - 2.5 log10 f).
"""
from __future__ import annotations

from dataclasses import dataclass

import numpy as np

# WISE L1b mask: fatal bits 0-4, 9, 10-18 (Expl. Suppl. IV.4.a); we also drop 21 (transient bad
# pixel), 26 (non-linearity unreliable), 27-28 (cosmic ray / spike outlier).
BAD_BITS = sum(1 << b for b in (0, 1, 2, 3, 4, 9, *range(10, 19), 21, 26, 27, 28))
R_AP, R_IN, R_OUT = 2.0, 4.0, 7.0          # pixels (2.75"/px): aperture 5.5", annulus 11-19"


def frame_flux(img: np.ndarray, x: float, y: float, magzp: float, unc: np.ndarray | None = None,
               msk: np.ndarray | None = None) -> tuple[float, float] | None:
    """Sky-subtracted aperture flux and 1-sigma error at pixel (x, y), ZP-normalised; None if unusable."""
    img = np.asarray(img, float)
    good = np.isfinite(img)
    if msk is not None:
        good &= (np.asarray(msk).astype(np.int64) & BAD_BITS) == 0
    if unc is not None:
        good &= np.isfinite(unc)
    yy, xx = np.indices(img.shape)
    rr = np.hypot(xx - x, yy - y)
    ap_all = rr < R_AP
    ap, ann = ap_all & good, (rr >= R_IN) & (rr < R_OUT) & good
    if not (0 <= x < img.shape[1] and 0 <= y < img.shape[0]) or ap_all.sum() < 8 or ann.sum() < 20:
        return None
    if ap.sum() < 0.75 * ap_all.sum():
        return None
    sky_pix = img[ann]
    sky = np.median(sky_pix)
    sky_sd = 1.4826 * np.median(np.abs(sky_pix - sky))
    n_ap = ap_all.sum()                                   # masked aperture pixels filled with the mean
    flux = img[ap].mean() * n_ap - n_ap * sky
    if unc is not None:
        var = np.sum(np.asarray(unc, float)[ap] ** 2) * n_ap / ap.sum()
    else:
        var = n_ap * sky_sd**2
    var += (n_ap * 1.2533 * sky_sd / np.sqrt(ann.sum())) ** 2
    s = 10 ** (-0.4 * (magzp - 22.5))
    return float(flux * s), float(np.sqrt(var) * s)


def visit_flux(fluxes, errs) -> tuple[float, float] | None:
    """Combine the frames of one visit: weighted mean; error is the larger of the propagated
    error and the robust frame-to-frame scatter / sqrt(n)."""
    f, e = np.asarray(fluxes, float), np.asarray(errs, float)
    if f.size < 3:
        return None
    w = 1 / e**2
    mean = float(np.sum(w * f) / np.sum(w))
    stat = float(1 / np.sqrt(np.sum(w)))
    scat = float(1.4826 * np.median(np.abs(f - np.median(f))) / np.sqrt(f.size))
    return mean, max(stat, scat)


@dataclass(frozen=True)
class Floor:
    s_abs: float = 0.0
    s_rel: float = 0.0

    def apply(self, flux, err):
        f, e = np.asarray(flux, float), np.asarray(err, float)
        return np.sqrt(e**2 + self.s_abs**2 + (self.s_rel * f) ** 2)


def reduced_chi2_const(flux, err) -> float:
    f, e = np.asarray(flux, float), np.asarray(err, float)
    w = 1 / e**2
    m = np.sum(w * f) / np.sum(w)
    return float(np.sum(((f - m) / e) ** 2) / max(f.size - 1, 1))


def calibrate_floor(curves: list[tuple[np.ndarray, np.ndarray]]) -> Floor:
    """Fit (s_abs, s_rel) so constant control light curves have median reduced chi^2 = 1:
    s_abs on the faintest third (by median |flux|), then s_rel on the brightest third."""
    if len(curves) < 10:
        return Floor()                                   # too few controls to calibrate: no floor
    lvl = np.array([np.median(np.abs(f)) for f, _ in curves])
    lo, hi = np.percentile(lvl, [33, 67])
    faint = [c for c, l in zip(curves, lvl) if l <= lo]
    bright = [c for c, l in zip(curves, lvl) if l >= hi]

    def solve(group, make):
        a, b = 0.0, 1e6
        if np.median([reduced_chi2_const(f, e) for f, e in group]) <= 1:
            return 0.0
        for _ in range(60):
            m = (a + b) / 2
            fl = make(m)
            chi = np.median([reduced_chi2_const(f, fl.apply(f, e)) for f, e in group])
            a, b = (m, b) if chi > 1 else (a, m)
        return (a + b) / 2

    s_abs = solve(faint, lambda s: Floor(s, 0.0))
    s_rel = solve(bright, lambda s: Floor(s_abs, s / 1e6))  # search s_rel in [0, 1] via scaled variable
    return Floor(s_abs, s_rel / 1e6)
