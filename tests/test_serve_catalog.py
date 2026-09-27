import importlib.util
from pathlib import Path

import pytest

spec = importlib.util.spec_from_file_location("serve_catalog", Path(__file__).parents[1] / "scripts" / "serve_catalog.py")
sc = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sc)


def test_valid_review_normalised():
    r = sc.validate({"key": "c17643", "decision": "refute", "reasoning": "Spitzer YSO already present.",
                     "reviewer": "igor", "tags": ["pre-existing"], "extra": "dropped"})
    assert r["decision"] == "refute" and "time" in r and "extra" not in r


@pytest.mark.parametrize("bad", [
    {"key": "../etc", "decision": "approve", "reasoning": "long enough text", "reviewer": "x"},
    {"key": "c1", "decision": "maybe", "reasoning": "long enough text", "reviewer": "x"},
    {"key": "c1", "decision": "approve", "reasoning": "short", "reviewer": "x"},
    {"key": "c1", "decision": "approve", "reasoning": "long enough text", "reviewer": ""},
])
def test_invalid_reviews_rejected(bad):
    with pytest.raises(ValueError):
        sc.validate(bad)


def test_request_checks_reject_foreign_pages():
    ok = {"Content-Type": "application/json", "Origin": "http://127.0.0.1:8792", "Host": "127.0.0.1:8792", "X-CSRF-Token": "tok"}
    assert sc.check_request(ok, 8792, "tok") is None
    assert "content type" in sc.check_request({**ok, "Content-Type": "text/plain"}, 8792, "tok")
    assert "cross-origin" in sc.check_request({**ok, "Origin": "http://evil.example"}, 8792, "tok")
    assert "Host" in sc.check_request({**ok, "Host": "evil.example"}, 8792, "tok")
    assert "CSRF" in sc.check_request({**ok, "X-CSRF-Token": "wrong"}, 8792, "tok")


import json as _json  # noqa: E402
import threading  # noqa: E402
import urllib.request  # noqa: E402


def _post(port, body, token, ctype="application/json"):
    req = urllib.request.Request(f"http://127.0.0.1:{port}/api/reviews", data=_json.dumps(body).encode(), method="POST",
                                 headers={"Content-Type": ctype, "X-CSRF-Token": token, "Origin": f"http://127.0.0.1:{port}"})
    try:
        with urllib.request.urlopen(req) as r:
            return r.status, _json.loads(r.read())
    except urllib.error.HTTPError as e:
        return e.code, _json.loads(e.read())


def test_http_fails_closed_without_catalog(tmp_path, monkeypatch):
    web = tmp_path / "viewer"; (web / "catalog").mkdir(parents=True)
    monkeypatch.setattr(sc, "WEB", web); monkeypatch.setattr(sc, "STORE", tmp_path / "r.jsonl")
    srv = sc.make_server(0); port = srv.server_address[1]; monkeypatch.setattr(sc, "PORT", port)
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    good = {"key": "c1", "decision": "refute", "reasoning": "long enough reasoning text", "reviewer": "t"}
    try:
        assert _post(port, good, sc.CSRF)[0] == 503                                   # no catalog built
        (web / "catalog" / "index.js").write_text("window.CAT={not json")
        assert _post(port, good, sc.CSRF)[0] == 503                                   # corrupt catalog
        (web / "catalog" / "index.js").write_text('window.CAT={"gallery":[{"key":"c1"}]};')
        assert _post(port, good, "wrong")[0] == 403                                   # bad token
        assert _post(port, good, sc.CSRF, ctype="text/plain")[0] == 403               # wrong content type
        assert _post(port, {**good, "key": "c2"}, sc.CSRF)[0] == 400                  # unknown key
        code, rec = _post(port, good, sc.CSRF)
        assert code == 201 and rec["decision"] == "refute"
        assert (tmp_path / "r.jsonl").read_text().count("\n") == 1
    finally:
        srv.shutdown()
