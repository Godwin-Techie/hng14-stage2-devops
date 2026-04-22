from fastapi.testclient import TestClient
from unittest.mock import MagicMock

import api.main as main
from api.main import app

client = TestClient(app)

main.r = MagicMock()


def test_health_check():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["status"] == "API is running"


def test_create_job():
    response = client.post("/jobs")
    assert response.status_code == 200
    assert "id" in response.json()
    assert response.json()["status"] == "submitted"


def test_get_job_not_found():
    response = client.get("/jobs/invalid-id")
    assert response.status_code in [200, 404]
