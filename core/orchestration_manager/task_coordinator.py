# core/orchestration_manager/task_coordinator.py

"""
KP-AIO: Multi-Agent Task Orchestration (Mock v0.1)
Author: Captain
Version: 0.1
Date: 2025-04-27
"""

import time
import random

# Simulated agent registry
AGENT_REGISTRY = {
    "drone_1": "ready",
    "bot_2": "idle",
    "scanner_3": "busy"
}

def assign_task(payload):
    """
    Assign a task to a known KP agent.
    :param payload: Dict with 'task_instruction' (raw task text)
    :return: Task assignment result
    """
    task = payload.get("task_instruction", "").strip().lower()

    if not task:
        print("⚠️ [AIO] No task provided.")
        return {"status": "error", "reason": "empty task"}

    # Naive agent assignment (pick idle one)
    target_agent = select_available_agent()
    if not target_agent:
        print("❌ [AIO] No available agent to assign task.")
        return {"status": "error", "reason": "no agents available"}

    print(f"🧠 [AIO] Assigning task '{task}' to agent '{target_agent}'...")
    time.sleep(0.3)

    # Simulate task execution
    AGENT_REGISTRY[target_agent] = "busy"

    print(f"✅ [AIO] Agent '{target_agent}' acknowledged task: '{task}'")
    return {"status": "assigned", "agent": target_agent, "task": task}

def select_available_agent():
    """
    Return the first idle agent from the registry.
    """
    for agent, status in AGENT_REGISTRY.items():
        if status in ["ready", "idle"]:
            return agent
    return None

