from fastapi import FastAPI
from pydantic import BaseModel

from env import SmartEnergyEnv

app = FastAPI()
env = SmartEnergyEnv()

# ---------- Root ----------
@app.get("/")
def home():
    return {"status": "Smart Energy Environment running"}

# ---------- Reset ----------
@app.post("/reset")
def reset():
    obs = env.reset()
    return {"observation": obs}

# ---------- Step ----------
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

# ---------- State ----------
@app.get("/state")
def state():
    return env.state(
