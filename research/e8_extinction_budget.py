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
Unextincted W2 of a Class 0 source, scaled from the HOPS median (Furlan+2016, vault
note: [4.5] = 12.16 Vega at 420 pc for L_tot = 5.5 L_sun), assuming F_4.5 ~ L:
  W2_0(L, d) = 12.16 - 2.5 log10(L / 5.5) + 5 log10(d / 0.42 kpc)
Detectable if W2_0 + A_4.5(centre) <= 14.3 (NEOWISE 90% completeness, single exposure).
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


def w2_unextincted(lum: float, d_kpc: np.ndarray) -> np.ndarray:
    return HOPS_W2 - 2.5 * np.log10(lum / HOPS_L) + 5 * np.log10(d_kpc / HOPS_D)


def main() -> None:
    cat = pd.read_csv(ROOT / "cache" / "higal360clump.csv")
    c = cat[(cat.evol_flag == 1) & (cat.dist > 0) & (cat.dist <= 4) & (cat.surf_dens > 0)].copy()
    c["a45_full"] = a45_from_sigma(c.surf_dens.values)
    c["a45_centre"] = c.a45_full / 2
    res = {"n": int(len(c)), "sigma_med_g_cm2": float(c.surf_dens.median()),
           "a45_centre_pct": {p: float(np.percentile(c.a45_centre, p)) for p in (10, 50, 90, 99)},
           "a_v_full_pct": {p: float(np.percentile(c.a45_full / (A45_PER_AK * AK_PER_AV), p)) for p in (10, 50, 90)},
           "per_lum": []}
    for L in LUMS:
        w0 = w2_unextincted(L, c.dist.values)
        w = w0 + c.a45_centre.values
        # column needed to hide it: A_4.5 >= W2_LIMIT - w0  -> A_V,centre needed
        need = np.clip(W2_LIMIT - w0, 0, None) / (A45_PER_AK * AK_PER_AV)
        res["per_lum"].append({"L": L, "frac_detectable_no_ext": float(np.mean(w0 <= W2_LIMIT)),
                               "frac_detectable_clump_ext": float(np.mean(w <= W2_LIMIT)),
                               "w2_med_no_ext": float(np.median(w0)), "w2_med_clump_ext": float(np.median(w)),
                               "a_v_centre_needed_med": float(np.median(need))})
    hist, edges = np.histogram(c.a45_centre, bins=np.linspace(0, 3, 31))
    res["a45_hist"] = {"edges": edges.round(2).tolist(), "counts": hist.tolist()}
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "extinction_budget.json").write_text(json.dumps(res))
    print(json.dumps({k: v for k, v in res.items() if k != "a45_hist"}, indent=1))


if __name__ == "__main__":
    main()
