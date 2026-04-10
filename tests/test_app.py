"""
Basic tests for the Flask application.
"""
import pytest
from src.app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as c:
        yield c


def test_health(client):
    resp = client.get("/health")
    assert resp.status_code == 200
    assert resp.get_json()["status"] == "ok"


def test_data_requires_user_id(client):
    resp = client.get("/data")
    assert resp.status_code == 400


def test_data_returns_user(client):
    resp = client.get("/data?user_id=42")
    assert resp.status_code == 200
    assert resp.get_json()["user_id"] == "42"
