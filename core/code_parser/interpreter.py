# core/code_parser/interpreter.py

"""
KP Code Parser and Interpreter
Author: Captain
Version: 0.1
Date: 2025-04-27
"""

def execute_kp_code(voice_or_text_input, context):
    """
    Parses the incoming KP code (or voice-translated text)
    and returns a structured instruction for the dispatcher.

    :param voice_or_text_input: dict from Voice Engine or direct KP script
    :param context: KP runtime context (variables, memory)
    :return: dict with action_type and payload
    """
    if not voice_or_text_input:
        return {"action_type": "noop", "payload": {}}

    raw_command = voice_or_text_input.get("kp_code", "").strip().lower()

    if not raw_command:
        return {"action_type": "noop", "payload": {}}

    # Very Simple Early Commands Mapping (Can be expanded later)
    if "send message" in raw_command:
        # Example: send message to app_x: hello world
        parts = raw_command.split(":")
        target = parts[0].replace("send message to", "").strip() if len(parts) > 1 else "unknown_app"
        message = parts[1].strip() if len(parts) > 1 else "hello"

        return {
            "action_type": "app_message",
            "payload": {
                "target_app": target,
                "message": message
            }
        }
    
    elif "read sensor" in raw_command:
        # Example: read sensor temp_sensor_001
        sensor_id = raw_command.replace("read sensor", "").strip()
        return {
            "action_type": "hardware_read",
            "payload": {
                "sensor_id": sensor_id
            }
        }

    elif "ask model" in raw_command:
        # Example: ask model object_detector
        model_name = raw_command.replace("ask model", "").strip()
        return {
            "action_type": "model_query",
            "payload": {
                "model_name": model_name,
                "input_data": {}
            }
        }

    elif "send peer" in raw_command:
        # Example: send peer drone_2: start
        parts = raw_command.split(":")
        target_peer = parts[0].replace("send peer", "").strip() if len(parts) > 1 else "unknown_peer"
        message = parts[1].strip() if len(parts) > 1 else "ping"

        return {
            "action_type": "peer_message",
            "payload": {
                "target_peer": target_peer,
                "message": message
            }
        }

    elif "assign task" in raw_command:
        # Example: assign task drone_1 clean area 2
        task_instruction = raw_command.replace("assign task", "").strip()
        return {
            "action_type": "assign_task",
            "payload": {
                "task_instruction": task_instruction
            }
        }

    else:
        # Default: treat as direct KP code execution (future)
        return {
            "action_type": "direct_execute",
            "payload": {
                "kp_code": raw_command
            }
        }

