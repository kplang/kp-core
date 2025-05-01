# kp_core.py

"""
KP Language Core Bootstrapper
Author: Captain
Version: 0.1
Date: 2025-04-27
"""

import sys
import time

# Core KP Modules (To be implemented in core/)
from core.voice_engine.listener import listen_for_voice_command
from core.code_parser.interpreter import execute_kp_code
from core.app2app_manager.dispatcher import send_app_message
from core.hardware_manager.sensor_reader import read_sensor_data
from core.model_connector.model_client import query_model
from core.machine_link.peer_network import send_peer_message
from core.orchestration_manager.task_coordinator import assign_task

# Supporting System Modules (To be implemented in system/)
from system.security_manager.authenticator import authenticate_device
from system.context_memory.context_store import ContextStore
from system.logger_monitor.logger import log_event
from system.event_loop.repl_listener import start_repl_loop

# Settings
from settings import KP_SETTINGS

# Initialize KP System Context
context = ContextStore()

def startup_kp_core():
    print("🚀 Starting KP-Core...")
    log_event("KP-Core starting up...")

    # Security Check
    if not authenticate_device(KP_SETTINGS['device_id']):
        print("❌ Authentication Failed. Shutting down KP-Core.")
        sys.exit(1)

    print("✅ Device Authenticated. KP-Core Initialized.")
    log_event("Device authenticated successfully.")

def run_kp_event_loop():
    """
    Main KP Event Loop: Listen -> Understand -> Dispatch -> Execute -> Respond
    """
    print("🎙️ Listening for Voice Commands or KP Scripts...")
    log_event("Entering KP Main Event Loop.")

    while True:
        try:
            # 1. Listen for Voice Command or Input
            user_input = listen_for_voice_command()

            # 2. Parse and Understand
            kp_instruction = execute_kp_code(user_input, context)

            # 3. Dispatch based on Action Type
            action_type = kp_instruction.get('action_type')
            payload = kp_instruction.get('payload')

            if action_type == "app_message":
                send_app_message(payload)
            elif action_type == "hardware_read":
                sensor_data = read_sensor_data(payload)
                print(f"🌡️ Sensor Data: {sensor_data}")
            elif action_type == "model_query":
                model_response = query_model(payload)
                print(f"🤖 Model Response: {model_response}")
            elif action_type == "peer_message":
                send_peer_message(payload)
            elif action_type == "assign_task":
                assign_task(payload)
            else:
                print(f"⚠️ Unknown Action Type: {action_type}")
                log_event(f"Unknown action_type received: {action_type}")

            time.sleep(0.1)  # Prevent CPU 100% busy loop

        except KeyboardInterrupt:
            print("\n🛑 KP-Core Shutting Down. Goodbye Captain!")
            log_event("KP-Core terminated by user.")
            break
        except Exception as e:
            print(f"❗ Error in KP-Core Loop: {e}")
            log_event(f"Error in event loop: {e}")
            time.sleep(1)

if __name__ == "__main__":
    startup_kp_core()
    run_kp_event_loop()

