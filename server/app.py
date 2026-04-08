from fastapi import FastAPI
from env import SmartEnergyEnv, Action

app = FastAPI()

env = SmartEnergyEnv()

# Root endpoint
@app.get("/")
def home():
    return {"status": "running"}

# Health check
@app.get("/health")
def health():
    return {"status": "ok"}

# Reset environment
@app.post("/reset")
def reset():
    obs = env.reset()
    return obs.dict()

# Step function
@app.post("/step")
def step(action: Action):
    obs, reward, done, _ = env.step(action)
    return {
        "observation": obs.dict(),
        "reward": reward.dict(),
        "done": done
    }

# Entry point
def main():
    return app

# REQUIRED for validator
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("server.app:app", host="0.0.0.0", port=7860)
