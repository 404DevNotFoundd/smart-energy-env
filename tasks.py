from env import SmartEnergyEnv, Action
import random

def run_all_tasks():
    results = {}

    env = SmartEnergyEnv(regions=2)
    obs = env.reset()
    action = Action(allocation=[d + random.randint(-5, 5) for d in obs.region_demands])
    _, reward, _, _ = env.step(action)
    results["easy"] = round(reward.score, 3)

    env = SmartEnergyEnv(regions=3)
    obs = env.reset()
    action = Action(allocation=[d + random.randint(-10, 10) for d in obs.region_demands])
    _, reward, _, _ = env.step(action)
    results["medium"] = round(reward.score * 0.9, 3)

    env = SmartEnergyEnv(regions=5)
    obs = env.reset()
    action = Action(allocation=[d + random.randint(-20, 20) for d in obs.region_demands])
    _, reward, _, _ = env.step(action)
    results["hard"] = round(reward.score * 0.8, 3)

    return results
