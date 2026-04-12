from env import SmartEnergyEnv, Action
import random

def run_task(name, regions, noise):
    env = SmartEnergyEnv(regions=regions)
    obs = env.reset()

    print(f"[START] task={name}", flush=True)

    step_count = 0
    total_reward = 0

    done = False
    while not done:
        action = Action(
            allocation=[d + random.randint(-noise, noise) for d in obs.region_demands]
        )

        obs, reward, done, _ = env.step(action)

        step_count += 1
        total_reward += reward.score

        print(f"[STEP] step={step_count} reward={reward.score}", flush=True)

    avg_score = total_reward / step_count

    print(f"[END] task={name} score={round(avg_score,3)} steps={step_count}", flush=True)


def main():
    # Run all tasks
    run_task("easy", regions=2, noise=5)
    run_task("medium", regions=3, noise=10)
    run_task("hard", regions=5, noise=20)


if __name__ == "__main__":
    main()
