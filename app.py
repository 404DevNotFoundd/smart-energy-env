from fastapi import FastAPI
from pydantic import BaseModel
from env import SmartEnergyEnv

app = FastAPI()
env = SmartEnergyEnv()

# ---------------- ROOT (FIX FOR 404) ----------------
@app.get("/")
def root():
    return {
        "status": "ok",
        "message": "Smart Energy OpenEnv is running"
    }

# ---------------- RESET ----------------
@app.post("/reset")
def reset():
    obs = env.reset()
    return {
        "observation": obs,
        "message": "Environment reset successful"
    }

# ---------------- STEP ----------------
class ActionRequest(BaseModel):
    action: dict

@app.post("/step")
def step(req: ActionRequest):
    obs, reward, done, info = env.step(req.action)
    return {
        "observation": obs,
        "reward": float(reward),
        "done": done,
        "info": info
    }

# ---------------- STATE ----------------
@app.get("/state")
def state():
    return env.state()
