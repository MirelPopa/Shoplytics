from fastapi.testclient import TestClient
from api.main import fast_api_app

client = TestClient(fast_api_app)

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"message": "Health check succeeded"}
