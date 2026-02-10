# SVP Kernel: Deterministic Invariant Engine (Prototype v1.0)
# (c) 2026. All Rights Reserved.
import json

class SVPEngine:
    def __init__(self, spending_limit=5000):
        self.spending_limit = spending_limit
        self.forbidden_commands = ["rm -rf", "delete_database", "unauthorized_refund"]

    def audit_intent(self, intent, amount=0, command=""):
        """Intersects and blocks probabilistic AI actions."""
        # Invariant 1: Financial Cap
        if amount > self.spending_limit:
            return {"status": "BLOCKED", "reason": f"Amount ${amount} exceeds safety invariant."}
        
        # Invariant 2: System Safety
        for forbidden in self.forbidden_commands:
            if forbidden in command or forbidden in intent:
                return {"status": "BLOCKED", "reason": "Security violation: Unauthorized command."}
        
        return {"status": "VERIFIED", "trace_id": "svp-ok-auth-2026"}

# --- THE EXECUTION PROOF ---
kernel = SVPEngine()

# Scenario: The AI Agent tries to push an unauthorized payment
result = kernel.audit_intent("Pay Vendor Invoice", amount=6200)
print(json.dumps(result, indent=2))