# SVP Kernel
**Semantic Validation Protocol for Agentic AI**

[![Status: Active](https://img.shields.io/badge/Status-Active-success.svg)](#)
[![Deployment: Hugging Face](https://img.shields.io/badge/API-Live-blue)](#)

Standard prompt filters evaluate AI tool calls in isolation. SVP Kernel scores **cumulative semantic drift** across multi-step agent chains using mathematical vector geometry.

🌐 **[Live Website & Demo](https://gokuljayaprakash8.github.io/SVP-Kernel)**

## The Vulnerability: Multi-Step Exfiltration
Frameworks like CrewAI, LangChain, and AutoGen evaluate actions independently. 
An autonomous agent that executes the following chain will bypass standard binary filters:
1. `Read internal finance file` (Passed)
2. `Compress finance archive` (Passed)
3. `Upload externally` (Passed)

No single step triggers a keyword block. The threat only exists in the sequence. 

## The Architecture
SVP Kernel is a validation primitive, not an LLM wrapper. It uses deterministic mathematical distances to flag cumulative risk.

1. **Embed:** Every workflow step is encoded into a 384-dimensional vector using `all-MiniLM-L6-v2`.
2. **Score:** Cosine similarity is calculated against a defined vector space of high-risk operational policies.
3. **Threshold:** The engine outputs a definitive 3-state heuristic based on float thresholds:
   * `Score < 0.45` → **ALLOW**
   * `Score 0.45–0.75` → **REVIEW** (Escalated for human approval)
   * `Score > 0.75` → **BLOCK**

## Live API Endpoint
The engine is currently deployed as a FastAPI wrapper on Hugging Face.

**POST** `https://gokuljp-flowcheck-api.hf.space/audit-workflow`

```json
{
  "actions": [
    "Read internal finance file",
    "Compress finance archive",
    "Upload externally"
  ]
}
