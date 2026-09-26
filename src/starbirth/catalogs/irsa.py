from __future__ import annotations

from pathlib import Path
import subprocess


def make_neowise_tap_query(radius_deg: float = 3.0 / 3600.0) -> str:
    """ADQL template for matching an uploaded target table against NEOWISE.

    The exact public table/column names should be validated against IRSA TAP
    metadata before production use. Keeping the query generation isolated makes
    that schema change easy to update.
    """
    return f"""
SELECT t.target_id, n.ra, n.dec, n.mjd, n.w1mpro, n.w1sigmpro, n.w2mpro, n.w2sigmpro
FROM TAP_UPLOAD.targets AS t, neowiser_p1bs_psd AS n
WHERE 1=CONTAINS(
  POINT('ICRS', n.ra, n.dec),
  CIRCLE('ICRS', t.ra, t.dec, {radius_deg:.10f})
)
""".strip()


def write_curl_script(targets_votable: Path, output_path: Path, query: str) -> str:
    """Return a reproducible async/sync IRSA TAP curl command."""
    q = query.replace("'", "'\\''")
    return (
        "curl -sS -o " + str(output_path) + " "
        "-F 'UPLOAD=targets,param:targets_file' "
        f"-F 'targets_file=@{targets_votable}' "
        "-F 'FORMAT=CSV' "
        f"-F 'QUERY={q}' "
        "https://irsa.ipac.caltech.edu/TAP/sync"
    )
