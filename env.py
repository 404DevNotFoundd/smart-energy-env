from pydantic import BaseModel
import random

class Observation(BaseModel):
    region_demands: list
    available_power: int
    time_step: int

class Action(BaseModel):
    allocation: list

class Reward(BaseModel):
    score: float

class SmartEnergyEnv:
    def __init__(self, regions=3):
        self.regions = regions
        self.max_power = 200
        self.time = 0

    def reset(self):
        self.time = 0
        self.state_data = {
            "region_demands": [random.randint(20, 80) for _ in range(self.regions)],
            "available_power": self.max_power,
            "time_step": 0
        }
        return Observation(**self.state_data)

    def state(self):
        return Observation(**self.state_data)

    def step(self, action: Action):
        allocation = action.allocation
        demands = self.state_data["region_demands"]

        error = sum(abs(a - d) for a, d in zip(allocation, demands))
        max_error = sum(demands)
        score = max(0.0, 1.0 - (error / (max_error + 1)))

        reward = Reward(score=round(score, 3))

        self.time += 1
        self.state_data["time_step"] = self.time
        self.state_data["region_demands"] = [
            random.randint(20, 100) for _ in range(self.regions)
        ]

        done = self.time >= 10

        return Observation(**self.state_data), reward, done, {}
