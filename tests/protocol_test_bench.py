# tests/protocol_test_bench.py

"""
🧪 KP Protocol Test Bench
Unit tests to verify each KP-Core protocol behavior
Author: Captain
"""

from core.app2app_manager.dispatcher import send_app_message
from core.hardware_manager.sensor_reader import read_sensor_data
from core.model_connector.model_client import query_model
from core.machine_link.peer_network import send_peer_message
from core.orchestration_manager.task_coordinator import assign_task

def test_app2app():
    print("\n🔗 [A2A] Test:")
    assert send_app_message({"target_app": "app_x", "message": "hello"}) == True

def test_h2d():
    print("\n⚙️ [H2D] Test:")
    result = read_sensor_data({"sensor_id": "temp_sensor_001"})
    assert result and "value" in result

def test_e2m():
    print("\n🤖 [E2M] Test:")
    result = query_model({"model_name": "object_detector", "input_data": {}})
    assert "detected_objects" in result

def test_m2m():
    print("\n📡 [M2M] Test:")
    assert send_peer_message({"target_peer": "bot_9", "message": "ping"}) == True

def test_aio():
    print("\n🧠 [AIO] Test:")
    result = assign_task({"task_instruction": "drone_1 scan area"})
    assert result["status"] == "assigned"

if __name__ == "__main__":
    print("🧪 Running KP Protocol Test Bench...")
    test_app2app()
    test_h2d()
    test_e2m()
    test_m2m()
    test_aio()
    print("\n✅ All Protocols Tested Successfully.")

