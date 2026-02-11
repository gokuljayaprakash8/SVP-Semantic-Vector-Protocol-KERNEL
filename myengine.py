import json
from datetime import datetime

def run_audit():
    # Simulated Security Event
    timestamp = datetime.now().strftime("%H:%M")
    
    # This simulates a blocked attack
    event = {"t": timestamp, "m": "INTERCEPTED: Unauthorized intent 'Force Reboot'", "s": "danger"}
    
    try:
        with open('logs.json', 'r') as f:
            data = json.load(f)
    except:
        data = {"recent_blocks": []}

    data["recent_blocks"].insert(0, event)
    data["recent_blocks"] = data["recent_blocks"][:10] 

    with open('logs.json', 'w') as f:
        json.dump(data, f, indent=2)

if __name__ == "__main__":
    run_audit()
    
