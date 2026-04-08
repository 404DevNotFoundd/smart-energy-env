from fastapi import FastAPI
from pydantic import BaseModel
from inference import main

app = FastAPI()

# Request format
class InputData(BaseModel):
    text: str

# Root endpoint
@app.get("/")
def home():
    return {
        "status": "running",
        "message": "API is live"
    }

# Health check
@app.get("/health")
def health():
    return {
        "status": "ok"
    }

# Prediction endpoint
@app.post("/predict")
def predict(data: InputData):
    result = main(data.dict())
    return result
