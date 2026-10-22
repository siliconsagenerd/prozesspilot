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