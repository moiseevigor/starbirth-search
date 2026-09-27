"""E3-lite: archival history of a turn-on candidate position.

For each candidate position collects, server-side via IRSA TAP:
  * NEOWISE-R single exposures within 60" -> per-visit coverage (any field source
    detected = the position was imaged) and the candidate's W1/W2 light curve (<=3")
  * AllWISE source (2010-11) and AllWISE multi-epoch photometry within 6"
  * GLIMPSE I archive (IRAC 3.6-8.0 um, 2004-05) and MIPSGAL 24 um (2005-06) within 6"
  * SPICY YSO candidate within 6"
  * SIMBAD objects within 10" (CDS TAP)
Writes artifacts/e3_vet/<designation>/*.csv and prints a summary.
Usage: python research/e3_vet_candidate.py HIGALBM354.2348+0.5057 [...]
"""
from __future__ import annotations

import io
import sys
from pathlib import Path

import httpx
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
IRSA = "https://irsa.ipac.caltech.edu/TAP/sync"
SIMBAD = "https://simbad.cds.unistra.fr/simbad/sim-tap/sync"
NEO0 = 56640.0


def tap(url: str, q: str) -> pd.DataFrame:
    r = httpx.post(url, data={"QUERY": q, "FORMAT": "csv", "LANG": "ADQL", "REQUEST": "doQuery"}, timeout=600)
    r.raise_for_status()
    if r.text.lstrip().startswith("<"):
        raise RuntimeError(r.text[:600])
    return pd.read_csv(io.StringIO(r.text))


def cone(table: str, cols: str, ra: float, dec: float, r_arcsec: float, url: str = IRSA) -> pd.DataFrame:
    q = (f"SELECT {cols} FROM {table} WHERE 1=CONTAINS(POINT('ICRS', ra, dec), "
         f"CIRCLE('ICRS', {ra}, {dec}, {r_arcsec / 3600:.8f}))")
    return tap(url, q)


def sep(ra, dec, ra0, dec0):
    ra, dec = np.asarray(ra, dtype=float), np.asarray(dec, dtype=float)
    return 3600 * np.hypot(((ra - ra0 + 180) % 360 - 180) * np.cos(np.radians(dec0)), dec - dec0)


FILES = ("neowise_60arcsec", "lightcurve", "allwise", "allwise_mep", "glimpse", "mipsgal", "spicy", "simbad")


def with_sep(d: pd.DataFrame, ra: float, dec: float) -> pd.DataFrame:
    """Add the separation (arcsec) from the target to any table with ra/dec; error rows are left untouched."""
    if d is None or d.empty or "ra" not in d or "dec" not in d:
        return d
    d = d.copy()
    d["sep"] = sep(d.ra.astype(float), d.dec.astype(float), ra, dec)
    return d


def archive(name: str, ra: float, dec: float) -> dict[str, pd.DataFrame]:
    """Archival history of any position (cached in artifacts/e3_vet/<name>/)."""
    out = ROOT / "artifacts" / "e3_vet" / name
    # cache format v2: all four GLIMPSE-family archives + separations; older caches are recomputed
    if (out / "VERSION").exists() and (out / "VERSION").read_text().strip() == "v2" and \
            all((out / f"{f}.csv").exists() for f in FILES):
        def rd(f):
            try:
                d = pd.read_csv(out / f"{f}.csv", index_col=0 if f == "lightcurve" else None)
            except pd.errors.EmptyDataError:
                return pd.DataFrame()
            return with_sep(d, ra, dec) if f == "simbad" else d
        return {f: rd(f) for f in FILES}
    out.mkdir(parents=True, exist_ok=True)
    neo = cone("neowiser_p1bs_psd", "ra, dec, mjd, w1mpro, w1sigmpro, w1snr, w2mpro, w2sigmpro, w2snr, cc_flags",
               ra, dec, 60)
    neo["sep"] = sep(neo.ra, neo.dec, ra, dec)
    neo["visit"] = ((neo.mjd - NEO0) // 182.625).astype(int)
    cover = neo.groupby("visit").size()                      # field detections per visit
    src = neo[neo.sep <= 3]
    lc = src.groupby("visit").agg(n=("mjd", "size"), w1=("w1mpro", "median"), w2=("w2mpro", "median"),
                                  w2snr=("w2snr", "median"), mjd=("mjd", "median"))
    lc["w1_w2"] = lc.w1 - lc.w2
    lc = lc.reindex(range(22))
    lc["field_dets_60"] = cover.reindex(range(22)).fillna(0).astype(int)
    aw = cone("allwise_p3as_psd", "designation, ra, dec, w1mpro, w2mpro, w3mpro, w4mpro, w2snr, cc_flags",
              ra, dec, 6)
    aw["sep"] = sep(aw.ra, aw.dec, ra, dec)
    mep = cone("allwise_p3as_mep", "ra, dec, mjd, w1mpro_ep, w2mpro_ep, w2sigmpro_ep", ra, dec, 6)
    mep["sep"] = sep(mep.ra, mep.dec, ra, dec)
    # GLIMPSE I 10<|l|<65, II |l|<10, 3D higher |b|, Vela-Carina l=255-295: query all four archives
    gl = pd.concat([cone(t, "ra, dec, mag3_6, mag4_5, mag5_8, mag8_0", ra, dec, 6).assign(survey=t)
                    for t in ("glimpse_s07_ar", "glimpse2_v2arc", "glimpse3d_v2arc", "velcara")], ignore_index=True)
    gl["sep"] = sep(gl.ra, gl.dec, ra, dec)
    mg = cone("mipsgalc", "ra, dec, mag_24, fnu_24", ra, dec, 6)
    mg["sep"] = sep(mg.ra, mg.dec, ra, dec)
    sp = cone("spicy", "spicy, ra, dec, class, alpha, mag3_6, mag4_5, mag8_0, var", ra, dec, 10)
    sp["sep"] = sep(sp.ra, sp.dec, ra, dec)
    try:
        sb = tap(SIMBAD, f"SELECT main_id, otype, ra, dec FROM basic WHERE 1=CONTAINS(POINT('ICRS', ra, dec), "
                         f"CIRCLE('ICRS', {ra}, {dec}, {10 / 3600:.8f}))")
        sb = with_sep(sb, ra, dec)
    except Exception as e:  # noqa: BLE001  an outage is recorded as an error row (consumers treat it as unavailable)
        sb = pd.DataFrame({"error": [str(e)[:200]]})
    res = {"neowise_60arcsec": neo, "lightcurve": lc, "allwise": aw, "allwise_mep": mep, "glimpse": gl,
           "mipsgal": mg, "spicy": sp, "simbad": sb}
    for f, d in res.items():
        d.to_csv(out / f"{f}.csv", index=(f == "lightcurve"))
    (out / "VERSION").write_text("v2")
    return res


def vet(designation: str) -> dict:
    cat = pd.read_csv(ROOT / "cache" / "higal360clump.csv")
    h = cat[cat.designation == designation].iloc[0]
    ra, dec = float(h.ra), float(h.dec)
    A = archive(designation, ra, dec)
    lc, aw, mep, gl, mg, sp, sb = (A[k] for k in ("lightcurve", "allwise", "allwise_mep", "glimpse", "mipsgal",
                                                   "spicy", "simbad"))
    res = {"designation": designation, "ra": ra, "dec": dec, "dist_kpc": h.dist, "mass": h.mass,
           "temp": h.temp, "l_bol": h.l_bol, "f24_higal": h.f24, "ulim_70": h.ulim_70}
    print(f"\n=== {designation}  ra={ra:.5f} dec={dec:.5f}  d={h.dist} kpc  M={h.mass} Msun  T={h.temp} K  "
          f"Lbol={h.l_bol}  f24(HiGAL)={h.f24}  ulim70={h.ulim_70}")
    print("NEOWISE per visit (n=cand dets <=3\", field_dets_60 = coverage proxy):")
    print(lc[["n", "w1", "w2", "w1_w2", "w2snr", "field_dets_60"]].round(2).T.to_string())
    print("AllWISE <=6\":", aw[["w1mpro", "w2mpro", "w3mpro", "w4mpro", "sep"]].round(2).to_dict("records"))
    print("AllWISE MEP <=3\" (2010) n=", int((mep.sep <= 3).sum()),
          "W2 median", round(float(mep[mep.sep <= 3].w2mpro_ep.median()), 2) if (mep.sep <= 3).any() else None)
    print("GLIMPSE <=6\":", gl[["survey", "mag3_6", "mag4_5", "mag5_8", "mag8_0", "sep"]].round(2).to_dict("records"))
    print("MIPSGAL <=6\":", mg[["mag_24", "fnu_24", "sep"]].round(3).to_dict("records"))
    print("SPICY <=10\":", sp.to_dict("records"))
    print("SIMBAD <=10\":", sb.to_dict("records"))
    return res


if __name__ == "__main__":
    for d in sys.argv[1:]:
        vet(d)
