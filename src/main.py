from fastapi import FastAPI
import uvicorn
from src.api.core.config import settings
from src.api.routers import predictions


app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION
)


app.include_router(predictions.router)

@app.get("/")
def read_root():
    return {"message": "Car Price Predictor API"}


if __name__ == "__main__":
    uvicorn.run("src.main:app", host="127.0.0.1", port=8000, reload=True)