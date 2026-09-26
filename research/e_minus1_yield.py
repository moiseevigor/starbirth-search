"""E-1: expected observable turn-ons (signal Y) vs accretion-burst background (B).

Signal (steady-state flux through the prestellar->protostellar boundary):
    N_T = N_proto(d<dmax) * dt / tau_proto
    Y   = N_T * df_W2 * (1 - f_prehost)
Background (bursts of protostars hidden in "prestellar" clumps and invisible
in AllWISE, lifted above the W2 limit by a >=2 mag burst):
    B   = N_pre(d<dmax) * f_hidden * dt / burst_interval * p_lift

df_W2, f_prehost measured by e_minus1_detectability; tau_proto, burst_interval,
f_hidden from docs/LITERATURE.md; p_lift is an explicit guess (0.1-0.5).
Writes artifacts/e_minus1/yield_grid.csv.
"""
from __future__ import annotations

from itertools import product
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "artifacts" / "e_minus1"
DT_YR = 12.0

TAU_PROTO_MYR = (0.1, 0.25, 0.7)      # Battersby+2017 star-forming phase; Elia+2021 ~1-4e5 yr
BURST_INTERVAL_YR = (1000.0, 438.0)   # Fischer+2019; Zakri+2022 (Class 0)
F_HIDDEN = (0.05, 0.2)                # hidden-protostar fraction; lit 18-38% for low-mass cores
P_LIFT = (0.1, 0.5)                   # P(burst lifts an AllWISE-invisible source above W2 limit)


def w2_rates(m: pd.DataFrame) -> dict[str, float]:
    det = lambda p="": m[p + "sep"].notna() & (m[p + "w2snr"] >= 5)  # noqa: E731
    m = m.assign(on=det(), off=det("off_"), lm=m.l_bol / m.mass)
    pro = m[(m.evol_flag == 2) & (m.mass > 0) & np.isfinite(m.lm)]
    young = pro[pro.lm <= pro.lm.quantile(0.25)]
    pre = m[m.evol_flag == 1]
    return {
        "df_w2_young": young.on.mean() - young.off.mean(),
        "df_w2_all": pro.on.mean() - pro.off.mean(),
        "f_prehost": pre.on.mean() - pre.off.mean(),
        "f_off": m.off.mean(),
        "n_young": len(young),
    }


def grid(cat: pd.DataFrame, r: dict[str, float]) -> pd.DataFrame:
    rows = []
    for dmax in (2.0, 4.0, np.inf):
        sel = (cat.dist > 0) & (cat.dist <= dmax) if np.isfinite(dmax) else np.ones(len(cat), bool)
        n_pre = int(((cat.evol_flag == 1) & sel).sum())
        n_proto = int(((cat.evol_flag == 2) & sel).sum())
        for tau in TAU_PROTO_MYR:
            n_t = n_proto * DT_YR / (tau * 1e6)
            y = n_t * r["df_w2_young"] * (1 - r["f_prehost"])
            bs = [n_pre * fh * DT_YR / bi * pl for bi, fh, pl in product(BURST_INTERVAL_YR, F_HIDDEN, P_LIFT)]
            rows.append(dict(dmax_kpc=dmax, n_pre=n_pre, n_proto=n_proto, tau_proto_myr=tau,
                             N_T=n_t, Y=y, B_min=min(bs), B_max=max(bs),
                             SB_best=y / min(bs), SB_worst=y / max(bs)))
    return pd.DataFrame(rows)


def main() -> None:
    cat = pd.read_csv(ROOT / "cache" / "higal360clump.csv")
    r = w2_rates(pd.read_csv(OUT / "allwise_match.csv"))
    g = grid(cat, r)
    OUT.mkdir(parents=True, exist_ok=True)
    g.to_csv(OUT / "yield_grid.csv", index=False)
    pd.Series(r).to_csv(OUT / "w2_rates.csv", header=["value"])
    print({k: round(float(v), 4) for k, v in r.items()})
    print(g.round(3).to_string(index=False))


if __name__ == "__main__":
    main()
