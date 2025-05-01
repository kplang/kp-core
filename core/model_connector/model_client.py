# core/model_connector/model_client.py

"""
KP-E2M: Model Connector (Edge-to-Model) Mock v0.1
Author: Captain
Version: 0.1
Date: 2025-04-27
"""

import time
import random

# Simulated model registry
MODEL_REGISTRY = {
    "object_detector": "mock_model_v1",
    "chat_helper": "mock_llm_v2",
    "fault_predictor": "mock_predictor"
}

def query_model(payload):
    """
    Simulates querying a remote AI/LLM model.
    :param payload: Dict with model name and input_data
    :return: Dict with simulated model output
    """
    model_name = payload.get("model_name", "").lower()
    input_data = payload.get("input_data", {})

    if model_name not in MODEL_REGISTRY:
        print(f"❌ [E2M] Model '{model_name}' not found in registry.")
        return {"error": "model not available"}

    print(f"📡 [E2M] Querying model '{model_name}' with input: {input_data}")
    time.sleep(0.5)  # Simulated delay

    # Simulated responses
    if model_name == "object_detector":
        return {
            "detected_objects": ["tree", "person", "car"],
            "confidence": [0.91, 0.88, 0.79]
        }

    elif model_name == "chat_helper":
        prompt = input_data.get("prompt", "Hello")
        return {
            "response": f"Simulated LLM says: '{prompt[::-1]}'"
        }

    elif model_name == "fault_predictor":
        return {
            "prediction": "Failure in 3 days",
            "confidence": f"{random.randint(85, 99)}%"
        }

    return {"response": "Unknown model behavior."}

