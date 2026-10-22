
from prozesspilot.agents.runtime import _route


def test_route_complaint_requires_approval():
    r = _route("complaint", 0.95, None)
    assert r["requires_approval"] is True
    assert "complaint" in r["reasons"]


def test_route_low_confidence():
    r = _route("product_question", 0.5, None)
    assert r["requires_approval"] is True
    assert "low_confidence" in r["reasons"]


def test_route_high_conf_simple_ready():
    r = _route("product_question", 0.9, None)
    assert r["requires_approval"] is False
    assert r["decision"] == "ready_for_review"


def test_route_high_value_customer():
    r = _route("product_question", 0.95, {"tier": "vip", "has_open_complaint": False})
    assert r["requires_approval"] is True
    assert "high_value_customer" in r["reasons"]


def test_route_open_complaint():
    r = _route("product_question", 0.95, {"tier": "standard", "has_open_complaint": True})
    assert r["requires_approval"] is True