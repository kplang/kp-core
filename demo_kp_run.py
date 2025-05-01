# demo_kp_run.py

"""
🧪 KP-Core Demo Script
Runs a predefined voice → code → action test using KP-Core modules.
Author: Captain
"""

from core.voice_engine.listener import listen_for_voice_command
from core.code_parser.interpreter import execute_kp_code
from core.app2app_manager.dispatcher import send_app_message
from core.hardware_manager.sensor_reader import read_sensor_data
from core.model_connector.model_client import query_model
from core.machine_link.peer_network import send_peer_message
from core.orchestration_manager.task_coordinator import assign_task

def simulate_voice_command(raw_voice):
    print(f"\n🎤 Voice Command: {raw_voice}")
    voice_input = {
        "raw_voice": raw_voice,
        "intent": "process_command",
        "parameters": {},
        "kp_code": raw_voice
    }

    instruction = execute_kp_code(voice_input, {})
    action = instruction.get("action_type")
    payload = instruction.get("payload")

    if action == "app_message":
        send_app_message(payload)
    elif action == "hardware_read":
        read_sensor_data(payload)
    elif action == "model_query":
        query_model(payload)
    elif action == "peer_message":
        send_peer_message(payload)
    elif action == "assign_task":
        assign_task(payload)
    else:
        print(f"⚠️ Unrecognized action: {action}")

if __name__ == "__main__":
    print("🚀 KP Demo Starting...")
    simulate_voice_command("send message to app_x: system ready")
    simulate_voice_command("read sensor temp_sensor_001")
    simulate_voice_command("ask model object_detector")
    simulate_voice_command("send peer bot_9: ping")
    simulate_voice_command("assign task bot_2 patrol perimeter")
    print("\n✅ KP Demo Completed.")

