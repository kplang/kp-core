# core/app2app_manager/dispatcher.py

"""
KP-A2A: Application-to-Application Messaging Dispatcher
Author: Captain
Version: 0.1
Date: 2025-04-27
"""

import time

# Simulate a basic registry of other apps (In real-world: service discovery or socket endpoints)
APP_REGISTRY = {
    "app_x": "local endpoint",
    "app_y": "mock endpoint",
    "logger": "internal service"
}

def send_app_message(payload):
    """
    Simulates sending a message from one KP app to another.
    :param payload: Dict with keys 'target_app' and 'message'
    """
    target = payload.get("target_app", "unknown_app").lower()
    message = payload.get("message", "ping")

    if target not in APP_REGISTRY:
        print(f"❌ [A2A] Target app '{target}' not found in registry.")
        return False

    print(f"📡 [A2A] Sending message to '{target}': {message}")
    
    # Simulated processing delay
    time.sleep(0.2)

    # Simulated app response
    print(f"✅ [A2A] '{target}' successfully received: \"{message}\"")
    return True

