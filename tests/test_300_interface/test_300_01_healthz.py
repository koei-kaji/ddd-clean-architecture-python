from fastapi import status
from fastapi.testclient import TestClient

from rest_api.main import Path


class TestGet:
    def test_200(self, fixt_client: TestClient) -> None:
        response = fixt_client.get(Path.healthz.value)
        assert response.status_code == status.HTTP_200_OK
