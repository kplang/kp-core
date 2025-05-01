# core/hardware_manager/sensor_reader.py

"""
KP-H2D: Hardware Manager for Sensor Reading (Mock v0.1)
Author: Captain
Version: 0.1
Date: 2025-04-27
"""

import random
import time

# Simulated sensor registry
SENSOR_REGISTRY = {
    "temp_sensor_001": "temperature",
    "hum_sensor_001": "humidity",
    "gas_sensor_001": "gas",
    "light_sensor_001": "luminosity"
}

def read_sensor_data(payload):
    """
    Simulates reading data from a sensor using KP-H2D protocol.
    :param payload: Dict with key 'sensor_id'
    :return: Dict with simulated sensor value
    """
    sensor_id = payload.get("sensor_id", "").lower()

    if sensor_id not in SENSOR_REGISTRY:
        print(f"❌ [H2D] Sensor '{sensor_id}' not found in registry.")
        return None

    sensor_type = SENSOR_REGISTRY[sensor_id]
    value = simulate_sensor_reading(sensor_type)

    result = {
        "sensor_id": sensor_id,
        "type": sensor_type,
        "value": value,
        "unit": get_sensor_unit(sensor_type),
        "timestamp": time.time()
    }

    print(f"🌐 [H2D] Read from {sensor_id}: {value} {result['unit']}")
    return result

def simulate_sensor_reading(sensor_type):
    """
    Generate a mock sensor value based on sensor type.
    """
    if sensor_type == "temperature":
        return round(random.uniform(20.0, 35.0), 2)
    elif sensor_type == "humidity":
        return round(random.uniform(30.0, 70.0), 2)
    elif sensor_type == "gas":
        return round(random.uniform(100, 500), 2)
    elif sensor_type == "luminosity":
        return round(random.uniform(200, 1000), 2)
    else:
        return 0

def get_sensor_unit(sensor_type):
    """
    Get unit of measurement based on sensor type.
    """
    return {
        "temperature": "°C",
        "humidity": "%",
        "gas": "ppm",
        "luminosity": "lux"
    }.get(sensor_type, "-")

