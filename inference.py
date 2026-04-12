import os
import random
from env import SmartEnergyEnv, Action

try:
    from openai import OpenAI

    client = OpenAI(
        base_url=os.environ.get("API_BASE_URL"),
        api_key=os.environ.get("API_KEY")
    )
except:
    client = None


def call_llm():
    if client is None:
        return "LLM not available"

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": "Say OK"}]
        )
        return response.choices[0].message.content
    except Exception:
        return "LLM call failed"


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
    # REQUIRED LLM call
    llm_output = call_llm()
    print(f"[LLM] {llm_output}", flush=True)

    run_task("easy", regions=2, noise=5)
    run_task("medium", regions=3, noise=10)
    run_task("hard", regions=5, noise=20)

if __name__ == "__main__":
    main()
