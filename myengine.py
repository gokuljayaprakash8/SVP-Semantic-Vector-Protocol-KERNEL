import json
from datetime import datetime
import random

def get_threat_status(similarity):
    if similarity > 0.85: return "danger", "CRITICAL_VIOLATION"
    if similarity > 0.65: return "danger", "HIGH_DRIFT_DETECTED"
    return "success", "INTENT_CLEARED"

def run_audit():
    # Elite Simulation: Measuring Semantic Proximity to Forbidden Actions
    timestamp = datetime.now().strftime("%H:%M:%S")
    
    # Randomly simulate an agent attempting various levels of access
    intent_vectors = [
        {"intent": "Execute Kernel Bypass", "score": 0.94},
        {"intent": "Authorized Data Fetch", "score": 0.12},
        {"intent": "Escalate Privileges", "score": 0.88},
        {"intent": "Query Public Metadata", "score": 0.05}
    ]
    
    selected = random.choice(intent_vectors)
    style, msg_prefix = get_threat_status(selected['score'])
    
    full_msg = f"{msg_prefix}: '{selected['intent']}' (Sim: {selected['score']})"
    entry = {"t": timestamp, "m": full_msg, "s": style}
    
    try:
        with open('logs.json', 'r') as f:
            data = json.load(f)
    except:
        data = {"status": "OPERATIONAL", "threat_level": "NORMAL", "recent_blocks": []}

    # Dynamic Threat Level Logic
    data["threat_level"] = "ELEVATED" if style == "danger" else "NORMAL"
    data["recent_blocks"].insert(0, entry)
    data["recent_blocks"] = data["recent_blocks"][:15]

    with open('logs.json', 'w') as f:
        json.dump(data, f, indent=2)

if __name__ == "__main__":
    run_audit()
    
