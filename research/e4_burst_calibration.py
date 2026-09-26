"""E4: calibrate the E1 turn-on rate against published protostellar burst intervals.

Hypothesis: E1 turn-ons hosted by Spitzer-catalogued YSOs (SPICY) occur at the
rate expected from published burst recurrence (Zakri+2022, Park+2021,
Contreras Pena+2024).  Falsified if the implied interval lies outside the
published confidence intervals.

  N_host  = SPICY YSOs within R of searched clumps (offset positions = chance)
  N_eff   = hosts NOT steadily detected by NEOWISE from 2014 (only these can
            register as a turn-on)
  k       = E1 turn-ons whose host is a SPICY YSO
  tau     = N_eff * dt_eff * completeness / k,  exact Poisson CI on k
Writes artifacts/e4/burst_calibration.json.
"""
from __future__ import annotations

import io
import json
import math
import sys
from pathlib import Path

import httpx
import numpy as np
import pandas as pd
from astropy.table import Table

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from starbirth.features.turn_on import classify  # noqa: E402

TAP = "https://irsa.ipac.caltech.edu/TAP/sync"
OUT = ROOT / "artifacts" / "e4"
DT_EFF = (19 - 3) * 0.5      # yr: onsets recognisable from visit 3 to visit 19 (needs >= 3 later visits)
COMPLETENESS = 0.87          # mean E1 injection completeness (SNR >= 10), docs/FEASIBILITY.md
LIT = [("Zakri+2022 Class I + flat", 1741, 527, 12011, "95%"), ("Zakri+2022 all protostars", 879, 400, 2515, "95%"),
       ("Park+2021 protostars (NEOWISE)", 683, 356, 1579, "90%"),
       ("Contreras Pena+2024 Class I FUor", 1750, 880, 2870, "68%")]


def poisson_ci(k: int, cl: float = 0.95) -> tuple[float, float]:
    """Exact (Garwood) two-sided CI on a Poisson mean, by bisection on the CDF."""
    a = (1 - cl) / 2

    def cdf(lam: float, kk: int) -> float:
        return sum(math.exp(-lam) * lam**i / math.factorial(i) for i in range(kk + 1)) if kk >= 0 else 0.0

    def solve(f):
        lo, hi = 0.0, 100.0 + 10 * k
        for _ in range(80):
            mid = (lo + hi) / 2
            lo, hi = (mid, hi) if f(mid) > 0 else (lo, mid)
        return (lo + hi) / 2

    lower = 0.0 if k == 0 else solve(lambda lam: a - (1 - cdf(lam, k - 1)))
    upper = solve(lambda lam: cdf(lam, k) - a)
    return lower, upper


def spicy_hosts(ra: np.ndarray, dec: np.ndarray, radius: float, chunk: int = 2000) -> pd.DataFrame:
    parts = []
    for i in range(0, len(ra), chunk):
        t = Table({"tid": np.arange(i, min(i + chunk, len(ra))), "ra": ra[i:i + chunk], "dec": dec[i:i + chunk]})
        buf = io.BytesIO()
        t.write(buf, format="votable")
        q = (f"SELECT t.tid, s.spicy, s.class, s.mag4_5 FROM TAP_UPLOAD.t AS t, spicy AS s WHERE "
             f"1=CONTAINS(POINT('ICRS', s.ra, s.dec), CIRCLE('ICRS', t.ra, t.dec, {radius / 3600:.8f}))")
        r = httpx.post(TAP, data={"QUERY": q, "FORMAT": "csv", "UPLOAD": "t,param:tbl"},
                       files={"tbl": ("t.xml", buf.getvalue())}, timeout=900)
        r.raise_for_status()
        if r.text.lstrip().startswith("<"):
            raise RuntimeError(r.text[:500])
        parts.append(pd.read_csv(io.StringIO(r.text)))
    return pd.concat(parts, ignore_index=True).drop_duplicates("tid")


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    s = pd.read_csv(ROOT / "artifacts" / "e1_full" / "pilot_targets.csv")
    n = len(s)
    res = {"n_searched": n, "radius_arcsec": 3.0, "dt_eff_yr": DT_EFF, "completeness": COMPLETENESS}
    for lab, dd in (("on", 0.0), ("off", 60.0)):
        f = OUT / f"spicy_{lab}.csv"
        h = pd.read_csv(f) if f.exists() else spicy_hosts(s.ra.values, s.dec.values + dd / 3600, 3.0)
        h.to_csv(f, index=False)
        cls = classify(pd.read_csv(ROOT / "artifacts" / "e1_full" / f"neowise_rows_{lab}.csv"), n)
        h = h.assign(e1_class=cls.reindex(h.tid).values)
        res[lab] = {"n_host": len(h), "by_spicy_class": h["class"].value_counts().to_dict(),
                    "by_e1_class": h.e1_class.value_counts().to_dict(),
                    "n_eff": int((h.e1_class != "steady").sum()),
                    "turn_on_hosts": h.loc[h.e1_class == "turn_on", ["tid", "spicy", "class", "mag4_5"]].to_dict("records")}
    k = len(res["on"]["turn_on_hosts"])
    n_eff = res["on"]["n_eff"]   # a chance-aligned SPICY source is still a YSO that can burst: keep all on-source hosts
    lo, hi = poisson_ci(k)
    exposure = n_eff * DT_EFF * COMPLETENESS            # host-years in which a turn-on would be caught
    res["k"] = k
    res["exposure_host_yr"] = exposure
    res["tau_yr"] = exposure / k if k else None
    res["tau_ci95_yr"] = [exposure / hi, exposure / lo if lo > 0 else None]
    res["literature"] = [dict(zip(("who", "tau", "lo", "hi", "ci"), x)) for x in LIT]
    res["consistent_with"] = [x[0] for x in LIT if not (res["tau_ci95_yr"][0] > x[3]
                                                         or (res["tau_ci95_yr"][1] or 1e99) < x[2])]
    # class split: bursts are much rarer in Class II (Contreras Pena+2019: ~1e5 yr) than Class I / flat
    h = pd.read_csv(OUT / "spicy_on.csv")
    h["e1"] = classify(pd.read_csv(ROOT / "artifacts" / "e1_full" / "neowise_rows_on.csv"), n).reindex(h.tid).values
    res["by_class"] = []
    for label, classes in (("Class I + flat", ["ClassI", "FS"]), ("Class II", ["ClassII"])):
        y = h[h["class"].isin(classes)]
        ne, kk = int((y.e1 != "steady").sum()), int((y.e1 == "turn_on").sum())
        l2, h2 = poisson_ci(kk)
        ex = ne * DT_EFF * COMPLETENESS
        res["by_class"].append({"label": label, "n_eff": ne, "k": kk, "tau_yr": ex / kk if kk else None,
                                "ci95": [ex / h2, ex / l2 if l2 > 0 else None]})
    (OUT / "burst_calibration.json").write_text(json.dumps(res, indent=1, default=str))
    print(json.dumps({k2: v for k2, v in res.items() if k2 not in ("literature",)}, indent=1, default=str))


if __name__ == "__main__":
    main()
