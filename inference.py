from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Root endpoint (FIXES YOUR 404 ISSUE)
@app.get("/")
def home():
    return {
        "status": "running",
        "message": "API is live and working"
    }

# Health check endpoint (often required in hackathons)
@app.get("/health")
def health():
    return {"status": "ok"}

# Example request model
class InputData(BaseModel):
    text: str

# Example inference endpoint (you can modify logic later)
@app.post("/predict")
def predict(data: InputData):
    text = data.text.lower()

    # dummy logic (replace with your model later)
    if "win" in text:
        result = "positive"
    else:
        result = "neutral"

    return {
        "input": data.text,
        "prediction": result
    }
