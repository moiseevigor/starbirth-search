"""E7 analysis: calibrate the delta-BIC threshold on offset positions, count faint turn-ons.

Rise candidate: delta-BIC >= T (T = 99th percentile of offset positions with a
positive step and onset in visits 3-19, i.e. FPR <= 1%), positive step, onset in
visits 3-19. 'from nothing' if the pre-onset flux is < 3 sigma of the pre-onset
standard error of the mean above zero (no source before), else 'brightening'.
Writes artifacts/e7/summary.json (counts, threshold, top candidates with light curves).
"""
from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
CACHE = ROOT / "cache" / "e7"
OUT = ROOT / "artifacts" / "e7"


def main() -> None:
    rows = [json.loads(f.read_text()) for f in CACHE.glob("*.json")]
    df = pd.DataFrame(rows)
    df = df[df.dbic.notna()] if "dbic" in df else df.iloc[:0]
    tg = pd.read_csv(OUT / "targets.csv").set_index("tid")
    df["e1_class"] = tg.e1_class.reindex(df.tid).values
    ok = (df.step > 0) & df.onset_visit.between(3, 19)
    off = df[(df.label == "off") & ok]
    thr = float(np.percentile(off.dbic, 99)) if len(off) else np.inf
    df["rise"] = ok & (df.dbic >= thr)

    def pre_sigma(r) -> float:
        """Pre-onset mean flux in units of its standard error (from the per-visit errors)."""
        f, e, v = np.array(r["flux"]), np.array(r["err"]), np.array(r["visit"])
        m = v < r["onset_visit"]
        return float(f[m].mean() / (np.sqrt(np.sum(e[m] ** 2)) / m.sum())) if m.sum() >= 3 else np.nan

    df["pre_sigma"] = [pre_sigma(r) if r.rise else np.nan for _, r in df.iterrows()]
    # a rise is only 'from nothing' if forced photometry AND the catalog agree: no W2 SNR >= 5 detection
    # within 3" before the onset (E1 rows), otherwise the forced pre-flux was just noisy (E7 vetting, tid 16087)
    rows = {lab: pd.read_csv(ROOT / "artifacts" / "e1_full" / f"neowise_rows_{lab}.csv") for lab in ("on", "off")}

    def cat_pre(r) -> bool:
        g = rows[r.label]
        g = g[g.tid == r.tid]
        dra = ((g.ra - g.t_ra + 180) % 360 - 180) * np.cos(np.radians(g.t_dec))
        sep = 3600 * np.hypot(dra, g.dec - g.t_dec)
        pre = (g.mjd - 56640.0) // 182.625 < r.onset_visit
        return bool(((sep <= 3) & (g.w2snr >= 5) & pre).any())

    df["cat_pre"] = [cat_pre(r) if r.rise else False for _, r in df.iterrows()]
    df["kind"] = np.where(~df.rise, "", np.where((df.pre_sigma < 3) & ~df.cat_pre, "from nothing", "brightening"))
    res = {"threshold_dbic": thr, "n": df.groupby("label").size().to_dict()}
    for lab in ("on", "off"):
        d = df[df.label == lab]
        res[lab] = {"n": len(d), "rises": int(d.rise.sum()),
                    "by_e1_class": d[d.rise].e1_class.value_counts().to_dict(),
                    "from_nothing": int((d.kind == "from nothing").sum()),
                    "dbic": [round(float(x), 1) for x in d.dbic.clip(-50, 1e5)]}
    cand = df[(df.label == "on") & df.rise].sort_values("dbic", ascending=False)
    res["candidates"] = [{"tid": int(r.tid), "e1_class": r.e1_class, "kind": r.kind, "dbic": round(float(r.dbic), 1),
                          "onset_year": round(2013.95 + (r.onset_visit + 0.5) * 0.5, 1), "ra": r.ra, "dec": r.dec,
                          "mag_pre": round(22.5 - 2.5 * np.log10(r.pre), 2) if r.pre > 0 else None,
                          "mag_post": round(22.5 - 2.5 * np.log10(r.post), 2) if r.post > 0 else None,
                          "year": [round(2013.95 + (v + 0.5) * 0.5, 2) for v in r.visit],
                          "flux": [round(x, 1) for x in r.flux], "err": [round(x, 1) for x in r.err]}
                         for _, r in cand.head(40).iterrows()]
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "summary.json").write_text(json.dumps(res))
    print(json.dumps({k: v for k, v in res.items() if k != "candidates"} | {
        "on": {k: v for k, v in res["on"].items() if k != "dbic"}, "off": {k: v for k, v in res["off"].items() if k != "dbic"}},
        indent=1))
    print(pd.DataFrame(res["candidates"]).drop(columns=["year", "flux", "err"]).head(25).to_string())


if __name__ == "__main__":
    main()
