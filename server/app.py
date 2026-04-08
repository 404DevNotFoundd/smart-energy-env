from fastapi import FastAPI
from pydantic import BaseModel
from inference import main as inference_main
from tasks import run_all_tasks

app = FastAPI()

class InputData(BaseModel):
    text: str

@app.get("/")
def home():
    return {"status": "running"}

@app.get("/health")
def health():
    return {"status": "ok"}

# ✅ Required for validator
@app.post("/run")
def run():
    return run_all_tasks()

# Optional (keep your predict)
@app.post("/predict")
def predict(data: InputData):
    return inference_main(data.dict())

# Entry point
def main():
    return app
