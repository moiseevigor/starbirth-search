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
