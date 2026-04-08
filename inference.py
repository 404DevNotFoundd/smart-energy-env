from fastapi import FastAPI
from pydantic import BaseModel
from inference import main

app = FastAPI()

class InputData(BaseModel):
    text: str

@app.get("/")
def home():
    return {"status": "running"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/predict")
def predict(data: InputData):
    result = main(data.dict())
    return result
