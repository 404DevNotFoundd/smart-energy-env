from fastapi import FastAPI
from env import SmartEnergyEnv, Action

app = FastAPI()

env = SmartEnergyEnv()

# ✅ Root endpoint (prevents 404)
@app.get("/")
def home():
    return {"status": "running"}

# ✅ Health check
@app.get("/health")
def health():
    return {"status": "ok"}

# ✅ REQUIRED: Reset environment
@app.post("/reset")
def reset():
    obs = env.reset()
    return obs.dict()

# ✅ REQUIRED: Step function
@app.post("/step")
def step(action: Action):
    obs, reward, done, _ = env.step(action)
    return {
        "observation": obs.dict(),
        "reward": reward.dict(),
        "done": done
    }

# ✅ Entry point (VERY IMPORTANT)
def main():
    return app
