# core/machine_link/peer_network.py

"""
KP-M2M: Peer-to-Peer Machine Messaging (Mock v0.1)
Author: Captain
Version: 0.1
Date: 2025-04-27
"""

import time

# Simulated peer registry (can be extended to use UDP broadcast or WebSocket)
PEER_REGISTRY = {
    "drone_1": "192.168.1.101",
    "bot_9": "192.168.1.102",
    "sensor_3": "192.168.1.103"
}

def send_peer_message(payload):
    """
    Simulates sending a message from one KP machine to another.
    :param payload: Dict with keys 'target_peer' and 'message'
    """
    target = payload.get("target_peer", "unknown_peer").lower()
    message = payload.get("message", "ping")

    if target not in PEER_REGISTRY:
        print(f"❌ [M2M] Peer '{target}' not found in network.")
        return False

    ip = PEER_REGISTRY[target]
    print(f"📡 [M2M] Sending message to peer '{target}' @ {ip}: {message}")
    time.sleep(0.2)

    # Simulated successful delivery
    print(f"✅ [M2M] '{target}' acknowledged: \"{message}\"")
    return True

