from __future__ import annotations

from dataclasses import dataclass
import numpy as np


@dataclass(frozen=True)
class ChangePointResult:
    index: int | None
    delta_bic: float
    pre_mean: float
    post_mean: float
    amplitude: float


def best_persistent_step(
    flux: np.ndarray,
    sigma: np.ndarray,
    min_points_each_side: int = 4,
) -> ChangePointResult:
    """Find the best single persistent step in O(n) time.

    Uses prefix sums for weighted Gaussian least squares. Positive delta_BIC
    means the two-level model is preferred over a constant model.
    """
    y = np.asarray(flux, dtype=float)
    s = np.asarray(sigma, dtype=float)
    good = np.isfinite(y) & np.isfinite(s) & (s > 0)
    y, s = y[good], s[good]
    n = len(y)
    if n < 2 * min_points_each_side:
        return ChangePointResult(None, float("-inf"), np.nan, np.nan, np.nan)

    w = 1.0 / (s * s)
    wy = w * y
    wy2 = w * y * y

    cw = np.r_[0.0, np.cumsum(w)]
    cwy = np.r_[0.0, np.cumsum(wy)]
    cwy2 = np.r_[0.0, np.cumsum(wy2)]

    total_w, total_wy, total_wy2 = cw[-1], cwy[-1], cwy2[-1]
    mu0 = total_wy / total_w
    chi0 = total_wy2 - (total_wy * total_wy) / total_w
    bic0 = chi0 + np.log(n)

    k = np.arange(min_points_each_side, n - min_points_each_side + 1)
    w1 = cw[k]
    wy1 = cwy[k]
    wy21 = cwy2[k]
    w2 = total_w - w1
    wy2s = total_wy - wy1
    wy22 = total_wy2 - wy21

    mu1 = wy1 / w1
    mu2 = wy2s / w2
    chi1 = wy21 - (wy1 * wy1) / w1
    chi2 = wy22 - (wy2s * wy2s) / w2
    bic = chi1 + chi2 + 3.0 * np.log(n)
    delta = bic0 - bic

    j = int(np.argmax(delta))
    return ChangePointResult(
        int(k[j]),
        float(delta[j]),
        float(mu1[j]),
        float(mu2[j]),
        float(mu2[j] - mu1[j]),
    )
