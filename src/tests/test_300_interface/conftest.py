import pytest
from fastapi.testclient import TestClient

from rest_api.main import app


@pytest.fixture(scope="function")
def fixt_client() -> TestClient:
    return TestClient(app)
