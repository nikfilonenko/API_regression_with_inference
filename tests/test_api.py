# test_api.py
from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_predict_item():
    payload = {
        "year": 2015,
        "km_driven": 30000,
        "fuel": "Petrol",
        "seller_type": "Individual",
        "transmission": "Manual",
        "owner": "First Owner",
        "mileage": 21.5,
        "engine": 1197,
        "max_power": 82.0,
        "seats": 5
    }
    response = client.post("/predict_item", json=payload)
    assert response.status_code == 200
    assert "predicted_price" in response.json()

def test_predict_items():
    test_data = """year,km_driven,fuel,seller_type,transmission,owner,mileage,engine,max_power,seats
2015,30000,Petrol,Individual,Manual,First Owner,21.5,1197,82.0,5
2017,25000,Diesel,Dealer,Automatic,Second Owner,18.0,1396,105.0,5
"""

    with open('test_data.csv', 'w') as f:
        f.write(test_data)

    with open('test_data.csv', 'rb') as file:
        response = client.post("/predict_items", files={"file": ("test_data.csv", file)})
        assert response.status_code == 200
        assert "message" in response.json()