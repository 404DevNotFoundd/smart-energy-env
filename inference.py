import os
from tasks import run_all_tasks

print("[START] Running Smart Energy Environment")

results = run_all_tasks()

for task, score in results.items():
    print(f"[STEP] Task: {task}, Score: {score}")

print("[END] Completed Execution")