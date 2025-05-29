import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from fastapi.testclient import TestClient
from naella_app.main import app
import pytest

client = TestClient(app)


def test_create_user():
    response = client.post(
        "/users",
        json={
            "name": "Ana",
            "last_name": "Silva",
            "gender": "Female",
            "age": 37,
            "height": 157,
            "current_weight": 64,
            "ideal_weight": 57,
            "fisical_activity_score": 1.3,
        },
    )
    assert response.status_code == 200
    assert "id" in response.json()["user"]


def test_create_user_invalid_data():
    response = client.post(
        "/users",
        json={
            "name": "Ana",
            "last_name": "Nosilva",
            "gender": "male",
            "age": -37,
            "height": 157,
            "current_weight": 64,
            "ideal_weight": 57,
            "fisical_activity_score": 1.3,
        },
    )
    assert response.status_code == 422


def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
