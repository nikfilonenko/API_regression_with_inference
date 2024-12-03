from fastapi import APIRouter, UploadFile, File, HTTPException
from src.api.core.models import Car
from src.api.core.utils import is_csv
from src.api.services.model_logic import make_single_prediction, make_bulk_prediction


router = APIRouter()


@router.post("/predict_item")
def predict_item(car: Car):
    if car is None:
        raise HTTPException(status_code=404, detail="Uploaded features is not a valid.")
    try:
        prediction = make_single_prediction(car)
        return {"predicted_price": prediction}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/predict_items")
def predict_items(file: UploadFile = File(...)):
    if not is_csv(file):
        raise HTTPException(status_code=400, detail="Uploaded file is not a valid CSV file.")
    try:
        result_file = make_bulk_prediction(file)
        return {"message": f"Predictions saved to {result_file}"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error during prediction: {str(e)}")