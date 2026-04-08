from fastapi import FastAPI
from pydantic import BaseModel
from env import SmartEnergyEnv

app = FastAPI()
env = SmartEnergyEnv()

@app.get("/")
def root():
    return {"status": "ok"}

@app.post("/reset")
def reset():
    return {"observation": env.reset()}

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

@app.get("/state")
def state():
    return env.state()