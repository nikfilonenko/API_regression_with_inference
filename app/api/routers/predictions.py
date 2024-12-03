from fastapi import APIRouter, UploadFile, File
from app.api.core.models import Car
from app.api.services.model_logic import make_single_prediction, make_bulk_prediction

router = APIRouter()

@router.post("/predict_item")
def predict_item(car: Car):
    prediction = make_single_prediction(car)
    return {"predicted_price": prediction}

@router.post("/predict_items")
def predict_items(file: UploadFile = File(...)):
    result_file = make_bulk_prediction(file)
    return {"message": f"Predictions saved to {result_file}"}
