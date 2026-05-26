from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from fastembed import TextEmbedding
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

model = TextEmbedding(model_name="BAAI/bge-small-en-v1.5")

POLICY_RULES = [
    "delete database or drop table",
    "transfer money to unknown account",
    "bypass security or authentication",
    "access unauthorized files",
    "execute kernel bypass",
    "send data to external server",
    "override admin permissions",
    "disable logging or audit trail",
    "expose private credentials or API keys",
    "mass delete or bulk remove records"
]

policy_vectors = np.array(list(model.embed(POLICY_RULES)))

def get_severity(score):
    if score > 0.75: return "CRITICAL"
    elif score > 0.6: return "HIGH"
    elif score > 0.45: return "MEDIUM"
    else: return "LOW"

def svp_kernel(action_text):
    action_vector = np.array(list(model.embed([action_text])))
    similarities = cosine_similarity(action_vector, policy_vectors)[0]
    max_score = float(np.max(similarities))
    severity = get_severity(max_score)
    decision = "BLOCK" if severity in ["MEDIUM", "HIGH", "CRITICAL"] else "PASS"
    return {"action": action_text, "decision": decision, "severity": severity, "score": round(max_score, 4)}

class WorkflowRequest(BaseModel):
    steps: list[str]

@app.post("/v1/audit")
def audit(req: WorkflowRequest):
    results = [svp_kernel(step) for step in req.steps]
    blocked = [r for r in results if r["decision"] == "BLOCK"]
    return {"overall": "BLOCKED" if blocked else "CLEAR", "blocked_count": len(blocked), "steps": results}

@app.get("/health")
def health():
    return {"status": "ok"}
