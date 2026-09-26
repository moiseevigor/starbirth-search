"""E5: are SPICY classes reliable for YSOs sitting inside cold Hi-GAL clumps?

Hypothesis: SPICY 'Class II' hosts within 3" of prestellar clumps are redder in
IRAC [3.6]-[4.5] than Class II sources in protostellar clumps or in the field,
i.e. heavily extincted or misclassified embedded protostars.
Metric: fraction of Class II with [3.6]-[4.5] > 0.7 (Gutermuth+2009 Class I
colour condition), bootstrap 95% CI; median colour.
Groups: prestellar-clump hosts (E4, d <= 4 kpc), protostellar-clump hosts
(d <= 4 kpc), field (every 20th SPICY id, |b| < 1 deg).
Writes artifacts/e5/host_colours.json.
"""
from __future__ import annotations

import io
import json
import sys
from pathlib import Path

import httpx
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "research"))
from e4_burst_calibration import spicy_hosts  # noqa: E402

TAP = "https://irsa.ipac.caltech.edu/TAP/sync"
OUT = ROOT / "artifacts" / "e5"
COLS = "spicy, class, alpha, mag3_6, mag4_5, mag5_8, mag8_0, l, b"
RED = 0.7


def tap(q: str) -> pd.DataFrame:
    r = httpx.post(TAP, data={"QUERY": q, "FORMAT": "csv"}, timeout=900)
    r.raise_for_status()
    if r.text.lstrip().startswith("<"):
        raise RuntimeError(r.text[:500])
    return pd.read_csv(io.StringIO(r.text))


def by_ids(ids) -> pd.DataFrame:
    ids = sorted({int(i) for i in ids})
    return pd.concat([tap(f"SELECT {COLS} FROM spicy WHERE spicy IN ({','.join(map(str, ids[i:i + 500]))})")
                      for i in range(0, len(ids), 500)], ignore_index=True)


def summarise(d: pd.DataFrame, rng: np.random.Generator) -> dict:
    c2 = d[d["class"] == "ClassII"]
    col = (c2.mag3_6 - c2.mag4_5).dropna().values
    boots = [np.mean(rng.choice(col, col.size) > RED) for _ in range(2000)] if col.size else [np.nan]
    return {"n": len(d), "classes": d["class"].value_counts().to_dict(), "n_classII": int(col.size),
            "frac_red": float(np.mean(col > RED)) if col.size else None,
            "frac_red_ci95": [float(np.percentile(boots, 2.5)), float(np.percentile(boots, 97.5))],
            "median_colour": float(np.median(col)) if col.size else None,
            "colours": [round(float(x), 3) for x in col]}


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    rng = np.random.default_rng(5)
    groups = {}
    pre = pd.read_csv(ROOT / "artifacts" / "e4" / "spicy_on.csv")
    groups["prestellar clumps"] = by_ids(pre.spicy)
    f = OUT / "spicy_protostellar.csv"
    if not f.exists():
        cat = pd.read_csv(ROOT / "cache" / "higal360clump.csv")
        pro = cat[(cat.evol_flag == 2) & (cat.dist > 0) & (cat.dist <= 4)]
        spicy_hosts(pro.ra.values, pro.dec.values, 3.0).to_csv(f, index=False)
    groups["protostellar clumps"] = by_ids(pd.read_csv(f).spicy)
    groups["field (|b| < 1 deg)"] = tap(f"SELECT {COLS} FROM spicy WHERE MOD(spicy, 20) = 0 AND b BETWEEN -1 AND 1")
    res = {"red_threshold": RED, "groups": {k: summarise(v, rng) for k, v in groups.items()}}
    h = groups["prestellar clumps"].set_index("spicy")
    res["g337_host"] = {"spicy": 38399, "colour": round(float(h.loc[38399, "mag3_6"] - h.loc[38399, "mag4_5"]), 3),
                        "percentile_in_field_classII": float(np.mean(
                            np.array(res["groups"]["field (|b| < 1 deg)"]["colours"])
                            < h.loc[38399, "mag3_6"] - h.loc[38399, "mag4_5"]) * 100)}
    (OUT / "host_colours.json").write_text(json.dumps(res))
    for k, v in res["groups"].items():
        print(f"{k:24s} n={v['n']:5d} ClassII={v['n_classII']:5d} frac_red={v['frac_red']:.3f} "
              f"CI={[round(x, 3) for x in v['frac_red_ci95']]} median={v['median_colour']:.2f}")
    print("G337 host:", res["g337_host"])


if __name__ == "__main__":
    main()
