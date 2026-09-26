"""Real telescope imagery for the viewer.

1. Multi-survey cutouts (CDS hips2fits): optical -> far-IR, one epoch each.
2. NEOWISE W2 per-visit stacks: individual L1b frames from IRSA IBE, reprojected
   onto one TAN grid centred on the target, median-stacked per ~6-month visit,
   and scaled with ONE stretch per target so brightness changes are real.
Outputs PNG/JPG under viewer/img/<key>/ and returns metadata dicts.
"""
from __future__ import annotations

import io
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from urllib.parse import quote

import httpx
import numpy as np
from astropy.io import ascii, fits
from astropy.wcs import WCS
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
CACHE = ROOT / "cache" / "viewer"
NEO0, VISIT = 56640.0, 182.625

# (key, HiPS id, label, epoch, wavelength)
SURVEYS = [
    ("dss2", "CDS/P/DSS2/color", "DSS2 optical", "1980s-90s", "0.4-0.9 um"),
    ("2mass", "CDS/P/2MASS/color", "2MASS JHKs", "1997-2001", "1.2-2.2 um"),
    ("vvv", "CDS/P/VISTA/VVV/DR4/ColorJYZ", "VISTA VVV", "2010-2015", "0.9-1.2 um"),
    ("glimpse", "IPAC/P/GLIMPSE360", "Spitzer GLIMPSE", "2004-2013", "3.6-8.0 um"),
    ("allwise", "CDS/P/allWISE/color", "AllWISE", "2010-2011", "3.4-22 um"),
    ("unwise", "CDS/P/unWISE/color-W2-W1W2-W1", "unWISE", "2010-2020 coadd", "3.4-4.6 um"),
    ("pacs70", "ESAVO/P/HERSCHEL/PACS70", "Herschel PACS 70", "2009-2012", "70 um"),
    ("pacs160", "ESAVO/P/HERSCHEL/PACS160", "Herschel PACS 160", "2009-2012", "160 um"),
    ("spire250", "ESAVO/P/HERSCHEL/SPIRE-250", "Herschel SPIRE 250", "2009-2012", "250 um"),
]


def _get(url: str, timeout: float = 120) -> bytes | None:
    for _ in range(3):
        try:
            r = httpx.get(url, timeout=timeout, follow_redirects=True)
            if r.status_code == 200:
                return r.content
        except httpx.HTTPError:
            pass
    return None


def hips_cutouts(key: str, ra: float, dec: float, fov_deg: float = 0.05, px: int = 300) -> list[dict]:
    out_dir = ROOT / "viewer" / "img" / key
    out_dir.mkdir(parents=True, exist_ok=True)
    res = []
    for sk, hips, label, epoch, wl in SURVEYS:
        f = out_dir / f"{sk}.jpg"
        if not f.exists():
            url = (f"https://alasky.cds.unistra.fr/hips-image-services/hips2fits?hips={quote(hips, safe='')}"
                   f"&width={px}&height={px}&fov={fov_deg}&projection=TAN&coordsys=icrs&ra={ra}&dec={dec}&format=jpg")
            b = _get(url)
            if b is None:
                continue
            f.write_bytes(b)
        a = np.asarray(Image.open(f).convert("L"), dtype=float)
        if a.std() < 2.0:  # blank = survey does not cover this position
            f.unlink()
            continue
        res.append({"survey": sk, "label": label, "epoch": epoch, "wl": wl, "src": f"img/{key}/{sk}.jpg"})
    return res


def _frames(ra: float, dec: float) -> list[dict]:
    f = CACHE / f"frames_{ra:.5f}_{dec:.5f}.tbl"
    if not f.exists():
        b = _get(f"https://irsa.ipac.caltech.edu/ibe/search/wise/neowiser/p1bm_frm?POS={ra},{dec}"
                 "&columns=scan_id,frame_num,mjd_obs,band,scangrp&where=band%3D2")
        f.write_bytes(b or b"")
    t = ascii.read(f, format="ipac")
    return [dict(scan_id=str(r["scan_id"]), frame_num=int(r["frame_num"]), mjd=float(r["mjd_obs"]),
                 scangrp=str(r["scangrp"])) for r in t]


def _cutout(fr: dict, ra: float, dec: float, size_arcsec: int) -> bytes | None:
    f = CACHE / "frames" / f"{fr['scan_id']}{fr['frame_num']:03d}_{ra:.5f}_{dec:.5f}.fits"
    if f.exists():
        return f.read_bytes()
    url = (f"https://irsa.ipac.caltech.edu/ibe/data/wise/neowiser/p1bm_frm/{fr['scangrp']}/{fr['scan_id']}/"
           f"{fr['frame_num']:03d}/{fr['scan_id']}{fr['frame_num']:03d}-w2-int-1b.fits"
           f"?center={ra},{dec}&size={size_arcsec}arcsec&gzip=false")
    b = _get(url, timeout=60)
    if b:
        f.parent.mkdir(parents=True, exist_ok=True)
        f.write_bytes(b)
    return b


def neowise_stacks(key: str, ra: float, dec: float, per_visit: int = 8, npix: int = 64,
                   pix_arcsec: float = 1.5) -> list[dict]:
    """Median W2 stack per NEOWISE visit on a common grid (npix*pix_arcsec field)."""
    from reproject import reproject_interp

    frames = _frames(ra, dec)
    by_visit: dict[int, list[dict]] = {}
    for fr in frames:
        by_visit.setdefault(int((fr["mjd"] - NEO0) // VISIT), []).append(fr)
    todo = [fr for v in sorted(by_visit) for fr in sorted(by_visit[v], key=lambda x: x["mjd"])[:per_visit]]
    size = int(npix * pix_arcsec * 1.6)
    with ThreadPoolExecutor(8) as ex:
        blobs = list(ex.map(lambda fr: _cutout(fr, ra, dec, size), todo))

    w = WCS(naxis=2)
    w.wcs.ctype = ["RA---TAN", "DEC--TAN"]
    w.wcs.crval = [ra, dec]
    w.wcs.crpix = [npix / 2 + 0.5, npix / 2 + 0.5]
    w.wcs.cdelt = [-pix_arcsec / 3600, pix_arcsec / 3600]
    stacks: dict[int, list[np.ndarray]] = {}
    for fr, b in zip(todo, blobs):
        if not b:
            continue
        try:
            with fits.open(io.BytesIO(b)) as h:
                data, hdr = h[0].data.astype(float), h[0].header
            img, fp = reproject_interp((data, WCS(hdr)), w, shape_out=(npix, npix))
        except Exception:  # noqa: BLE001  one bad frame must not kill the stack
            continue
        img[fp < 0.5] = np.nan
        img -= np.nanmedian(img)                   # local sky
        stacks.setdefault(int((fr["mjd"] - NEO0) // VISIT), []).append(img)

    visits = sorted(stacks)
    meds = {v: np.nanmedian(np.stack(stacks[v]), axis=0) for v in visits}
    if not meds:
        return []
    allpix = np.concatenate([m[np.isfinite(m)] for m in meds.values()])
    c = slice(npix // 2 - 8, npix // 2 + 8)                      # central 24" box around the target
    core = np.concatenate([m[c, c][np.isfinite(m[c, c])] for m in meds.values()])
    lo, hi = np.percentile(allpix, 5), max(np.percentile(core, 99.5), np.percentile(allpix, 99))
    # ONE stretch for all epochs, set by the target's neighbourhood so its change is visible
    ref = np.nanmedian(np.stack([meds[v] for v in visits[:3]]), axis=0)   # pre-onset reference: first 3 visits
    dmax = np.nanpercentile(np.abs(np.stack([meds[v] - ref for v in visits])[:, c, c]), 99.5) or 1.0
    out_dir = ROOT / "viewer" / "img" / key / "neowise"
    out_dir.mkdir(parents=True, exist_ok=True)
    res = []
    for v in visits:
        m = np.nan_to_num(meds[v], nan=lo)
        x = np.clip((m - lo) / (hi - lo), 0, 1)
        x = np.arcsinh(10 * x) / np.arcsinh(10)
        im = Image.fromarray((255 * x).astype(np.uint8)[::-1]).resize((256, 256), Image.NEAREST)
        im.save(out_dir / f"v{v:02d}.png", optimize=True)
        d = np.clip(np.nan_to_num(meds[v] - ref) / dmax, -1, 1)[::-1]     # difference vs reference
        rgb = np.stack([np.where(d > 0, 1, 1 + d), 1 - np.abs(d), np.where(d < 0, 1, 1 - d)], -1)
        rgb = 0.08 + 0.92 * (1 - np.abs(d))[..., None] * 0 + rgb * 0.92   # white = no change
        Image.fromarray((255 * np.clip(rgb, 0, 1)).astype(np.uint8)).resize((256, 256), Image.NEAREST).save(
            out_dir / f"d{v:02d}.png", optimize=True)
        mjd = float(np.median([fr["mjd"] for fr in by_visit[v]]))
        res.append({"visit": v, "mjd": round(mjd, 2), "year": round(2013.95 + (mjd - NEO0) / 365.25, 2),
                    "n": len(stacks[v]), "src": f"img/{key}/neowise/v{v:02d}.png",
                    "diff": f"img/{key}/neowise/d{v:02d}.png"})
    for kind, pre in (("stack", "v"), ("diff", "d")):
        ims = [Image.open(out_dir / f"{pre}{r['visit']:02d}.png").convert("RGB") for r in res]
        sheet = Image.new("RGB", (256 * len(ims), 256))
        for i, im in enumerate(ims):
            sheet.paste(im, (256 * i, 0))
        sheet.save(ROOT / "viewer" / "img" / key / f"neowise_{kind}.png", optimize=True)
    for f in out_dir.glob("*.png"):
        f.unlink()
    out_dir.rmdir()
    return [{k: v for k, v in r.items() if k not in ("src", "diff")} for r in res]


if __name__ == "__main__":
    import json
    import sys
    key, ra, dec = sys.argv[1], float(sys.argv[2]), float(sys.argv[3])
    print(json.dumps({"hips": hips_cutouts(key, ra, dec), "neowise": neowise_stacks(key, ra, dec)})[:600])
