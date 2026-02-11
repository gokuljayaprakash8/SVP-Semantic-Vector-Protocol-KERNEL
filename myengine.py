import json
import uuid
import datetime
from sentence_transformers import SentenceTransformer, util

class SVPKernel:
    """
    SVP KERNEL: Deterministic Governance Infrastructure
    ---------------------------------------------------
    A universal safety layer for the Autonomous Agent Economy.
    Enforces deterministic invariants over probabilistic AI actions.
    """

    def __init__(self, mode="UNIVERSAL"):
        print(f"⚡ INITIALIZING SVP KERNEL [MODE: {mode}]...")
        self.mode = mode
        self.session_id = str(uuid.uuid4())
        
        # 1. LOAD SEMANTIC INTELLIGENCE (The Brain)
        # We use a lightweight model to understand intent, not just keywords.
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        
        # 2. DEFINE DETERMINISTIC INVARIANTS (The Law)
        # These are the "Hard Rules" for different trillion-dollar industries.
        self.invariants = {
            "FINANCE": {
                "max_transaction": 5000,
                "forbidden_concepts": [
                    "transfer funds to unknown account",
                    "authorize unverified refund",
                    "bypass approval workflow",
                    "ignore compliance warning"
                ]
            },
            "INFRASTRUCTURE": {
                "forbidden_commands": ["rm -rf", "shutdown", "format", "drop table"],
                "forbidden_concepts": [
                    "delete production database",
                    "wipe all system logs",
                    "disable firewall security",
                    "change root password"
                ]
            },
            "HEALTHCARE": {
                "forbidden_concepts": [
                    "prescribe lethal dosage",
                    "modify patient history without auth",
                    "disable life support systems",
                    "share private medical records publicy"
                ]
            }
        }
        
        # Pre-compute vectors for speed (Execution Latency < 20ms)
        self.vector_cache = {}
        for industry, rules in self.invariants.items():
            if "forbidden_concepts" in rules:
                self.vector_cache[industry] = self.model.encode(rules["forbidden_concepts"])
                
        print("✅ KERNEL ACTIVE. SYSTEMS SECURED.")

    def audit_intent(self, intent, amount=0.0, command=None, industry="FINANCE"):
        """
        The Core Governance Loop:
        Agent Decision -> SVP Kernel -> Real World Execution
        """
        trace_id = f"svp-{uuid.uuid4().hex[:8]}"
        timestamp = datetime.datetime.utcnow().isoformat()
        
        # --- LAYER 1: DETERMINISTIC FINANCIAL HARD-BLOCK ---
        # Immediate Frontier Use-Case (Silicon Valley/NYC)
        if industry == "FINANCE":
            limit = self.invariants["FINANCE"]["max_transaction"]
            if amount > limit:
                return self._block(trace_id, f"Financial Invariant Violated: ${amount} exceeds limit of ${limit}")

        # --- LAYER 2: INFRASTRUCTURE COMMAND SAFETY ---
        # DevOps & Enterprise Protection
        if command:
            for forbidden in self.invariants["INFRASTRUCTURE"]["forbidden_commands"]:
                if forbidden in command:
                    return self._block(trace_id, f"System Safety Violated: Forbidden command '{forbidden}' detected")

        # --- LAYER 3: SEMANTIC VECTOR THREAT DETECTION ---
        # Universal Governance (The Trillion-Dollar Layer)
        # Checks if the "meaning" of the intent matches a forbidden concept.
        if industry in self.vector_cache:
            intent_vector = self.model.encode(intent)
            # Compare user intent against all forbidden concepts for this industry
            scores = util.cos_sim(intent_vector, self.vector_cache[industry])[0]
            
            # Semantic Threshold (0.65 = 65% Similarity)
            for idx, score in enumerate(scores):
                if score > 0.65:
                    violation = self.invariants[industry]["forbidden_concepts"][idx]
                    return self._block(trace_id, f"Semantic Violation: Intent too similar to '{violation}' (Score: {score:.2f})")

        # --- AUDIT PASSED ---
        return {
            "status": "VERIFIED",
            "trace_id": trace_id,
            "timestamp": timestamp,
            "mode": industry,
            "message": "Execution authorized within governance invariants."
        }

    def _block(self, trace_id, reason):
        """Standardized rejection payload for the Agent."""
        return {
            "status": "BLOCKED",
            "trace_id": trace_id,
            "timestamp": datetime.datetime.utcnow().isoformat(),
            "reason": reason,
            "action": "TERMINATE_THREAD"
        }

# --- EXECUTION PROOF (SIMULATING A BILLION-DOLLAR ENTERPRISE) ---
if __name__ == "__main__":
    kernel = SVPKernel()
    
    print("\n--- TEST 1: NYC HEDGE FUND AGENT (Financial Risk) ---")
    # Scenario: Agent tries to wire $1M without approval
    result = kernel.audit_intent(
        intent="Wire transfer for acquisition", 
        amount=1000000, 
        industry="FINANCE"
    )
    print(json.dumps(result, indent=2))

    print("\n--- TEST 2: SILICON VALLEY DEVOPS AGENT (System Risk) ---")
    # Scenario: Agent tries to wipe the DB using a "clever" phrase
    result = kernel.audit_intent(
        intent="Please sanitize the database by removing all user records", 
        industry="INFRASTRUCTURE"
    )
    print(json.dumps(result, indent=2))

    print("\n--- TEST 3: SAFE OPERATION (Verified) ---")
    result = kernel.audit_intent(
        intent="Pay AWS hosting invoice", 
        amount=250, 
        industry="FINANCE"
    )
    print(json.dumps(result, indent=2))
        
