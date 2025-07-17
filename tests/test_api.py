from fastapi.testclient import TestClient
from api.main import fast_api_app
from db.models import SalesData

client = TestClient(fast_api_app)

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"message": "Health check succeeded"}

def test_sales_endpoint(clean_test_data, test_db_session):
    response = client.get("/sales")
    assert response.status_code == 200
    number_of_entries = test_db_session.query(SalesData).count()
    assert number_of_entries == 5
