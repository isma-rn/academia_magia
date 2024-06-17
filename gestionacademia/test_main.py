from fastapi.testclient import TestClient

from .main import app

client = TestClient(app)

def test_read_solicitudes():
    response = client.get("/solicitud/")
    assert response.status_code == 200
    