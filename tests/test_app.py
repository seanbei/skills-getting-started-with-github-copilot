import pytest
from fastapi.testclient import TestClient
from src.app import app

def test_get_activities():
    # Arrange: Set up test client
    client = TestClient(app)
    # Act: Make the request
    response = client.get("/activities")
    # Assert: Check the response
    assert response.status_code == 200
    assert isinstance(response.json(), dict)
