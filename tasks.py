from env import SmartEnergyEnv, Action

# ---------- GRADER ----------
def compute_score(env, action):
    obs, reward, done, _ = env.step(action)
    return reward.score


# ---------- TASKS ----------
def easy_task():
    env = SmartEnergyEnv(regions=2)
    env.reset()
    action = Action(allocation=[50, 50])
    return compute_score(env, action)


def medium_task():
    env = SmartEnergyEnv(regions=3)
    env.reset()
    action = Action(allocation=[60, 40, 50])
    return compute_score(env, action)


def hard_task():
    env = SmartEnergyEnv(regions=5)
    env.reset()
    action = Action(allocation=[30, 40, 50, 60, 20])
    return compute_score(env, action)


def run_all_tasks():
    return {
        "easy": easy_task(),
        "medium": medium_task(),
        "hard": hard_task()
    }