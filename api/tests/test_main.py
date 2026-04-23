from fastapi.testclient import TestClient
from api.main import app


client = TestClient(app)


def test_healthcheck():
    response = client.get("/")
    assert response.status_code == 200


def test_redis_connection(monkeypatch):
    # mock redis client
    monkeypatch.setenv("REDIS_HOST", "fakehost")
    monkeypatch.setenv("REDIS_PORT", "1234")
    # your app should handle bad redis gracefully
    response = client.get("/redis-status")
    assert response.status_code in (200, 503)


def test_example_endpoint():
    response = client.get("/api/example")
    assert response.status_code == 200
    assert "result" in response.json()
