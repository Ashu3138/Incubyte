from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_register_and_login():
    res = client.post("/api/auth/register", json={
        "username": "testuser",
        "email": "test@test.com",
        "password": "pass123"
    })
    assert res.status_code in (200, 400)

    res = client.post("/api/auth/login", json={
        "username": "testuser",
        "password": "pass123"
    })
    assert res.status_code == 200
    assert "access_token" in res.json()
