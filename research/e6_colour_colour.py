"""E6: extinction or envelope? Colour-colour test of SPICY hosts.

Extinction law 4.5-8 um is flat (Indebetouw+2005: A_3.6/A_K = 0.56, A_4.5 = A_5.8 =
A_8.0 = 0.43), so [4.5]-[5.8] is ~extinction-free while [3.6]-[4.5] gains
0.13 A_K.
  H_ext: clump Class II hosts are redder than the field in [3.6]-[4.5] but NOT in
         [4.5]-[5.8]  (|delta median| < 0.1 mag).
  H_env: both colours shift (intrinsically embedded / misclassified).
Also reports the implied A_K from the [3.6]-[4.5] shift and the fraction meeting
the full Gutermuth+2009 Class I colour cut ([3.6]-[4.5] > 0.7 and [4.5]-[5.8] > 0.7).
Writes artifacts/e6/colour_colour.json.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "research"))
from e5_host_classes import COLS, by_ids, tap  # noqa: E402

OUT = ROOT / "artifacts" / "e6"
E_AK = 0.56 - 0.43          # E([3.6]-[4.5]) per unit A_K


def boot_median_diff(a: np.ndarray, b: np.ndarray, rng, n: int = 2000) -> list[float]:
    d = [np.median(rng.choice(a, a.size)) - np.median(rng.choice(b, b.size)) for _ in range(n)]
    return [float(np.percentile(d, 2.5)), float(np.percentile(d, 97.5))]


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    rng = np.random.default_rng(6)
    groups = {
        "prestellar clumps": by_ids(pd.read_csv(ROOT / "artifacts" / "e4" / "spicy_on.csv").spicy),
        "protostellar clumps": by_ids(pd.read_csv(ROOT / "artifacts" / "e5" / "spicy_protostellar.csv").spicy),
        "field (|b| < 1 deg)": tap(f"SELECT {COLS} FROM spicy WHERE MOD(spicy, 20) = 0 AND b BETWEEN -1 AND 1"),
    }
    pts, res = {}, {"E_per_AK": E_AK, "groups": {}}
    for k, d in groups.items():
        c = d[d["class"] == "ClassII"].assign(c1=lambda x: x.mag3_6 - x.mag4_5, c2=lambda x: x.mag4_5 - x.mag5_8,
                                              c3=lambda x: x.mag4_5 - x.mag8_0)
        c = c.dropna(subset=["c1", "c2"])
        pts[k] = c
        res["groups"][k] = {"n": len(c), "med_c1": float(c.c1.median()), "med_c2": float(c.c2.median()),
                            "med_c3": float(c.c3.median()),
                            "frac_gutermuth_classI": float(((c.c1 > 0.7) & (c.c2 > 0.7)).mean()),
                            "x": [round(v, 3) for v in c.c2], "y": [round(v, 3) for v in c.c1]}
    fld = pts["field (|b| < 1 deg)"]
    for k in ("prestellar clumps", "protostellar clumps"):
        g = pts[k]
        r = res["groups"][k]
        r["d_c1"] = r["med_c1"] - res["groups"]["field (|b| < 1 deg)"]["med_c1"]
        r["d_c2"] = r["med_c2"] - res["groups"]["field (|b| < 1 deg)"]["med_c2"]
        r["d_c3"] = r["med_c3"] - res["groups"]["field (|b| < 1 deg)"]["med_c3"]
        r["d_c1_ci95"] = boot_median_diff(g.c1.values, fld.c1.values, rng)
        r["d_c2_ci95"] = boot_median_diff(g.c2.values, fld.c2.values, rng)
        r["d_c3_ci95"] = boot_median_diff(g.c3.dropna().values, fld.c3.dropna().values, rng)
        r["A_K_implied"] = r["d_c1"] / E_AK
        r["verdict"] = "extinction" if abs(r["d_c2"]) < 0.1 else "envelope/intrinsic"
    (OUT / "colour_colour.json").write_text(json.dumps(res))
    for k, r in res["groups"].items():
        print(f"{k:22s} n={r['n']:5d} med[3.6-4.5]={r['med_c1']:.2f} med[4.5-5.8]={r['med_c2']:.2f} "
              f"med[4.5-8.0]={r['med_c3']:.2f} GutermuthI={r['frac_gutermuth_classI']:.2f}"
              + (f"  d_c1={r['d_c1']:+.2f}{[round(x, 2) for x in r['d_c1_ci95']]} d_c2={r['d_c2']:+.2f}"
                 f"{[round(x, 2) for x in r['d_c2_ci95']]} d_c3={r['d_c3']:+.2f} A_K~{r['A_K_implied']:.1f} "
                 f"-> {r['verdict']}" if "d_c1" in r else ""))


if __name__ == "__main__":
    main()
