"""Local server for the candidate review catalog.

Serves viewer/ (catalog.html, data, imagery) and stores human reviews in
reviews/reviews.jsonl inside the repo (append-only; the latest entry per candidate
is its current decision, earlier ones are the audit trail).

    .venv/bin/python scripts/serve_catalog.py            # http://127.0.0.1:8792/catalog.html
Binds to 127.0.0.1 only.
"""
from __future__ import annotations

import argparse
import json
import re
import threading
from datetime import datetime, timezone
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WEB = ROOT / "viewer"
STORE = ROOT / "reviews" / "reviews.jsonl"
DECISIONS = {"approve", "refute", "unsure"}
KEY = re.compile(r"^[a-z0-9_-]{1,40}$")
LOCK = threading.Lock()


def read_reviews() -> list[dict]:
    if not STORE.exists():
        return []
    return [json.loads(line) for line in STORE.read_text().splitlines() if line.strip()]


def validate(r: dict) -> dict:
    """Trust boundary: only well-formed reviews reach the repo file."""
    key, dec = str(r.get("key", "")), str(r.get("decision", ""))
    why, who = str(r.get("reasoning", "")).strip(), str(r.get("reviewer", "")).strip()
    if not KEY.match(key):
        raise ValueError("invalid candidate key")
    if dec not in DECISIONS:
        raise ValueError("decision must be approve, refute or unsure")
    if not (10 <= len(why) <= 5000):
        raise ValueError("reasoning must be 10-5000 characters")
    if not (1 <= len(who) <= 60):
        raise ValueError("reviewer name is required (max 60 characters)")
    tags = [str(t)[:40] for t in r.get("tags", [])][:10] if isinstance(r.get("tags"), list) else []
    return {"key": key, "decision": dec, "reasoning": why, "reviewer": who, "tags": tags,
            "machine_verdict": str(r.get("machine_verdict", ""))[:80],
            "time": datetime.now(timezone.utc).isoformat(timespec="seconds")}


class Handler(SimpleHTTPRequestHandler):
    def _json(self, code: int, obj) -> None:
        body = json.dumps(obj).encode()
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):  # noqa: N802
        if self.path.split("?")[0] == "/api/reviews":
            return self._json(200, read_reviews())
        return super().do_GET()

    def do_POST(self):  # noqa: N802
        if self.path != "/api/reviews":
            return self._json(404, {"error": "not found"})
        n = int(self.headers.get("Content-Length", 0))
        if n > 20000:
            return self._json(413, {"error": "review too large"})
        try:
            rec = validate(json.loads(self.rfile.read(n) or b"{}"))
        except (ValueError, json.JSONDecodeError) as e:
            return self._json(400, {"error": str(e)})
        with LOCK:
            STORE.parent.mkdir(parents=True, exist_ok=True)
            with STORE.open("a") as f:
                f.write(json.dumps(rec) + "\n")
        return self._json(201, rec)

    def end_headers(self):
        if self.path.endswith((".js", ".json", ".html")):
            self.send_header("Cache-Control", "no-store")   # always show freshly built data
        super().end_headers()


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--port", type=int, default=8792)
    a = p.parse_args()
    srv = ThreadingHTTPServer(("127.0.0.1", a.port), partial(Handler, directory=str(WEB)))
    print(f"review catalog: http://127.0.0.1:{a.port}/catalog.html  (reviews -> {STORE.relative_to(ROOT)})")
    srv.serve_forever()


if __name__ == "__main__":
    main()
