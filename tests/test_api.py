from fastapi.testclient import TestClient
from api.main import fast_api_app

client = TestClient(fast_api_app)

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"message": "Health check succeeded"}

def test_sales_endpoint(clean_test_data):
    response = client.get("/sales")
    assert response.status_code == 200
    assert len(response.json()) == 5
