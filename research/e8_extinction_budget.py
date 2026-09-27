"""E8: is the clump's own dust column enough to hide a newborn protostar at 4.6 um?

Hypothesis (from the literature synthesis): a newborn is dark at 3-5 um because of
dust. Test which dust: the beam-averaged clump column that Hi-GAL measures, or the
unresolved inner envelope (10^2-10^3 AU) that the collapse models describe.

Per prestellar clump (0 < d <= 4 kpc):
  N_H2 = Sigma / (mu_H2 m_H), mu_H2 = 2.8      (Kauffmann+2008)
  A_V  = 2 N_H2 / 1.87e21 cm^-2                 (Bohlin+1978, R_V = 3.1)
  A_K  = 0.112 A_V                              (Rieke & Lebofsky 1985)
  A_4.5 = 0.43 A_K                              (Indebetouw+2005)
A source at the clump centre sees half the column: A_4.5(centre) = A_4.5 / 2.
Anchor: the OBSERVED Spitzer [4.5] of HOPS Class 0 protostars (Furlan+2016, VizieR
J/ApJS/224/5), each scaled to 5.5 L_sun (m_norm = [4.5] + 2.5 log10(L_tot / 5.5)). This is a
model-dependent scenario, not a decomposition: the anchor already contains the Orion
envelopes, viewing geometry and foreground extinction of those sources, so 'distance' and
'clump column' below are shifts relative to an Orion-like Class 0, and the inner envelope
is not separable. Monte Carlo: each clump draws m_norm from the HOPS distribution
(two-level bootstrap: resample the anchor set, then the exact expectation per clump), giving
16-50-84% bands on the detectable fraction that reflect the anchor sample's own uncertainty:
  W2(L, d) = m_norm - 2.5 log10(L / 5.5) + 5 log10(d / 0.42 kpc) [+ A_4.5(centre)]
Detectable if W2 <= 14.3 (NEOWISE 90% completeness, single exposure).
Writes artifacts/e8/extinction_budget.json.
"""
from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "artifacts" / "e8"
M_H = 1.6735e-24            # g
MU_H2 = 2.8
NH_PER_AV = 1.87e21         # cm^-2 mag^-1
AK_PER_AV = 0.112
A45_PER_AK = 0.43
W2_LIMIT = 14.3
HOPS_W2, HOPS_L, HOPS_D = 12.16, 5.5, 0.42
LUMS = [1.0, 5.0, 25.0, 100.0]


def a45_from_sigma(sigma_g_cm2: np.ndarray) -> np.ndarray:
    n_h2 = sigma_g_cm2 / (MU_H2 * M_H)
    a_v = 2 * n_h2 / NH_PER_AV
    return A45_PER_AK * AK_PER_AV * a_v


def w2_unextincted(lum: float, d_kpc: np.ndarray, m_norm: float = HOPS_W2) -> np.ndarray:
    return m_norm - 2.5 * np.log10(lum / HOPS_L) + 5 * np.log10(d_kpc / HOPS_D)


def hops_class0_mnorm() -> np.ndarray:
    """Luminosity-normalised observed [4.5] (Vega) of HOPS Class 0 sources; cached; fallback = median + 0.8 mag scatter."""
    f = ROOT / "cache" / "hops_class0_mnorm.json"
    if f.exists():
        return np.array(json.loads(f.read_text()))
    try:
        from astroquery.vizier import Vizier
        v = Vizier(columns=["**"], row_limit=-1)
        a1, a2 = v.get_catalogs("J/ApJS/224/5/table1")[0], v.get_catalogs("J/ApJS/224/5/table2")[0]
        unit = str(a2["F4.5"].unit or "Jy").lower()
        to_jy = 1e-3 if "mjy" in unit else 1.0                              # read the unit, do not assume it
        t1, t2 = a1.to_pandas(), a2.to_pandas()
        m = t1.merge(t2, on="HOPS")
        m = m[(m["Class"].astype(str).str.strip() == "0") & (m["F4.5"] > 0) & (m["Ltot"] > 0)]
        mag = -2.5 * np.log10(m["F4.5"].astype(float) * to_jy / 179.7)      # -> Vega, IRAC 4.5 ZP 179.7 Jy
        print(f"HOPS F4.5 unit: {unit}; n Class 0 with F4.5 and Ltot: {len(m)}")
        mn = (mag + 2.5 * np.log10(m["Ltot"].astype(float) / HOPS_L)).values
        mn = mn[np.isfinite(mn)]
        assert mn.size >= 20
    except Exception as e:  # noqa: BLE001  network/format problems fall back to a documented scatter
        print("HOPS fetch failed, using median +/- 0.8 mag scatter:", str(e)[:120])
        mn = HOPS_W2 + 0.8 * np.random.default_rng(0).standard_normal(200)
    f.parent.mkdir(exist_ok=True)
    f.write_text(json.dumps([round(float(x), 4) for x in mn]))
    return mn


def main() -> None:
    cat = pd.read_csv(ROOT / "cache" / "higal360clump.csv")
    c = cat[(cat.evol_flag == 1) & (cat.dist > 0) & (cat.dist <= 4) & (cat.surf_dens > 0)].copy()
    c["a45_full"] = a45_from_sigma(c.surf_dens.values)
    c["a45_centre"] = c.a45_full / 2
    res = {"n": int(len(c)), "sigma_med_g_cm2": float(c.surf_dens.median()),
           "a45_centre_pct": {p: float(np.percentile(c.a45_centre, p)) for p in (10, 50, 90, 99)},
           "a_v_full_pct": {p: float(np.percentile(c.a45_full / (A45_PER_AK * AK_PER_AV), p)) for p in (10, 50, 90)},
           "per_lum": []}
    mn = hops_class0_mnorm()
    rng = np.random.default_rng(8)
    res["anchor"] = {"n_hops_class0": int(mn.size), "mnorm_median": float(np.median(mn)),
                     "mnorm_p16_p84": [float(np.percentile(mn, 16)), float(np.percentile(mn, 84))],
                     "note": "observed HOPS Class 0 [4.5] scaled to 5.5 Lsun: includes Orion envelope, geometry and foreground extinction"}
    for L in LUMS:
        w0 = w2_unextincted(L, c.dist.values)
        w = w0 + c.a45_centre.values
        need = np.clip(W2_LIMIT - w0, 0, None) / (A45_PER_AK * AK_PER_AV)
        f0, f1 = [], []
        base0 = w2_unextincted(L, c.dist.values, m_norm=0.0)           # W2 without the anchor term
        for _ in range(300):
            # two-level bootstrap: resample the 80-source anchor SET (its own sampling uncertainty), then
            # take the exact expectation over that set for every clump (no per-clump draw noise)
            anchor = rng.choice(mn, mn.size)
            thr0 = W2_LIMIT - base0                                    # per clump: max anchor value that still detects
            f0.append(float(np.mean([np.mean(anchor <= t) for t in thr0])))
            f1.append(float(np.mean([np.mean(anchor <= t) for t in thr0 - c.a45_centre.values])))
        band = lambda a: [float(np.percentile(a, 16)), float(np.percentile(a, 50)), float(np.percentile(a, 84))]  # noqa: E731
        res["per_lum"].append({"L": L, "frac_detectable_no_ext": float(np.mean(w0 <= W2_LIMIT)),
                               "frac_detectable_clump_ext": float(np.mean(w <= W2_LIMIT)),
                               "band_no_ext": band(f0), "band_clump_ext": band(f1),
                               "w2_med_no_ext": float(np.median(w0)), "w2_med_clump_ext": float(np.median(w)),
                               "a_v_centre_needed_med": float(np.median(need))})
    hist, edges = np.histogram(c.a45_centre, bins=np.linspace(0, 3, 31))
    res["a45_hist"] = {"edges": edges.round(2).tolist(), "counts": hist.tolist()}
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "extinction_budget.json").write_text(json.dumps(res))
    print(json.dumps({k: v for k, v in res.items() if k != "a45_hist"}, indent=1))


if __name__ == "__main__":
    main()
