from fastapi.testclient import TestClient
from unittest.mock import MagicMock
import api.main as main

client = TestClient(main.app)

# Mock redis so we don’t need real server
main.r = MagicMock()


def test_root_endpoint():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"status": "API is running"}


def test_create_job():
    main.r.lpush.return_value = 1
    main.r.hset.return_value = 1

    response = client.post("/jobs")

    assert response.status_code == 200
    assert "id" in response.json()
    assert response.json()["status"] == "submitted"


def test_get_job_not_found():
    main.r.hget.return_value = None

    response = client.get("/jobs/123")

    assert response.status_code == 200
    assert "error" in response.json()
    