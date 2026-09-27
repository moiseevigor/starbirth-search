import numpy as np

from starbirth.features.forced_phot import BAD_BITS, Floor, calibrate_floor, frame_flux, reduced_chi2_const, visit_flux


def _star(flux=1000.0, sky=50.0, noise=2.0, seed=0, n=15):
    rng = np.random.default_rng(seed)
    yy, xx = np.indices((n, n))
    psf = np.exp(-((xx - 7) ** 2 + (yy - 7) ** 2) / (2 * 1.0**2))
    return sky + flux * psf / psf.sum() + rng.normal(0, noise, (n, n))


def test_flux_recovered_and_zero_without_source():
    yy, xx = np.indices((15, 15))
    psf = np.exp(-((xx - 7) ** 2 + (yy - 7) ** 2) / 2.0)
    frac = psf[np.hypot(xx - 7, yy - 7) < 2].sum() / psf.sum()   # exact discrete aperture fraction (~0.77)
    f, e = frame_flux(_star(), 7, 7, magzp=22.5)
    assert abs(f - 1000 * frac) < 5 * e and e > 0
    f0, e0 = frame_flux(_star(flux=0), 7, 7, magzp=22.5)
    assert abs(f0) < 5 * e0


def test_masked_aperture_rejects_frame():
    msk = np.zeros((15, 15), int)
    msk[5:10, 5:10] = 1 << 2                   # dead pixels over the aperture
    assert frame_flux(_star(), 7, 7, 22.5, msk=msk) is None
    msk[:] = 1 << 8                            # bit 8 is not in BAD_BITS
    assert (1 << 8) & BAD_BITS == 0 and frame_flux(_star(), 7, 7, 22.5, msk=msk) is not None


def test_visit_error_takes_scatter_when_errors_underestimated():
    m, e = visit_flux([100, 140, 60, 120, 80], [1, 1, 1, 1, 1])
    assert e > 5                               # propagated error (0.45) would be far too small


def test_floor_calibration_brings_chi2_to_one():
    rng = np.random.default_rng(3)
    curves = []
    for lvl in rng.uniform(0, 5000, 300):
        err = np.full(20, 10.0)
        flux = lvl + rng.normal(0, np.sqrt(10**2 + 30**2 + (0.02 * lvl) ** 2), 20)
        curves.append((flux, err))
    fl = calibrate_floor(curves)
    chi = np.median([reduced_chi2_const(f, fl.apply(f, e)) for f, e in curves])
    assert 0.8 < chi < 1.25 and fl.s_abs > 10
    assert Floor().apply([1.0], [2.0])[0] == 2.0


def test_floor_needs_controls():
    assert calibrate_floor([]) == Floor() and calibrate_floor([(np.ones(5), np.ones(5))]) == Floor()
