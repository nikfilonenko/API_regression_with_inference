from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_predict_item():
    payload = {
        "name": "bmw",
        "year": 2024,
        "km_driven": 5000,
        "fuel": "Diesel",
        "seller_type": "Individual",
        "transmission": "Manual",
        "owner": "First Owner",
        "mileage": 23.00,
        "engine": 1396,
        "max_power": 103.52,
        "torque": 250.00,
        "seats": 5,
        "max_torque_rpm": 4500
    }
    response = client.post("/predict_item", json=payload)
    assert response.status_code == 200
    assert "predicted_price" in response.json()

def test_predict_items():
    with open('tests/data/test.csv', 'rb') as file:
        response = client.post("/predict_items", files={"file": ("test_data.csv", file)})
        assert response.status_code == 200
        assert "message" in response.json()