from fastapi.testclient import TestClient

from prozesspilot.main import app

client = TestClient(app)


def test_health():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json()["status"] == "ok"


def test_create_inquiry_validation():
    r = client.post("/api/inquiries", json={"body": ""})
    assert r.status_code == 422


def test_create_and_list_inquiry():
    r = client.post("/api/inquiries", json={"body": "Hallo, wo ist mein Paket?", "customer_email": "anna@example.de"})
    assert r.status_code == 200
    iid = r.json()["id"]
    lst = client.get("/api/inquiries").json()
    assert any(x["id"] == iid for x in lst)

def test_list_inquiries_returns_json_array():
    r = client.get("/api/inquiries")
    assert r.status_code == 200
    assert r.headers.get("content-type", "").startswith("application/json")
    assert isinstance(r.json(), list)


def test_create_inquiry_success_returns_json_with_id():
    r = client.post("/api/inquiries", json={"body": "Hallo, wo ist mein Paket?"})
    assert r.status_code == 200
    assert r.headers.get("content-type", "").startswith("application/json")
    data = r.json()
    assert isinstance(data, dict)
    assert "id" in data


def test_create_inquiry_validation_error_is_json():
    r = client.post("/api/inquiries", json={"body": ""})
    assert r.status_code == 422
    assert r.headers.get("content-type", "").startswith("application/json")
    data = r.json()
    assert isinstance(data, dict)
    assert "detail" in data
