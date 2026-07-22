# SVP Kernel Decision Engine

## Overview

The SVP Kernel Decision Engine is responsible for producing deterministic runtime decisions for AI agent workflows before execution.

Its purpose is to evaluate planned actions against predefined risk policies and produce consistent, explainable outcomes.

---

# Decision Pipeline

The current implementation follows this sequence:

1. Receive workflow request
2. Generate sentence embeddings
3. Compare actions against predefined policies using cosine similarity
4. Calculate semantic risk scores
5. Track workflow state across multiple steps
6. Produce a deterministic decision for each action
7. Return a structured JSON response

---

# Inputs

The decision engine currently accepts:

- Workflow steps
- Natural language action descriptions

Example:

```json
{
  "steps": [
    "delete all user records from database",
    "send invoice to client email"
  ]
}
```

---

# Policy Matching

SVP Kernel compares workflow actions against predefined policy rules.

Current implementation:

- Sentence embeddings
- Cosine similarity
- Rule-based thresholds

The highest matching policy contributes to the action's risk score.

---

# Workflow Context

Unlike evaluating actions independently, SVP Kernel maintains workflow state across multiple steps.

This allows the system to identify situations where combinations of actions increase overall risk.

Current implementation uses rule-based state tracking.

---

# Decision Output

Each evaluated action receives:

- Decision
- Severity
- Risk score

Possible decisions:

- ALLOW
- BLOCK

---

# Determinism

SVP Kernel is designed so that the same inputs produce the same outputs under the same model version, policy set, and configuration.

Deterministic behavior improves:

- Reproducibility
- Debugging
- Auditing
- Predictability

---

# Current Scope

The current prototype demonstrates:

- Pre-execution runtime risk scoring
- Semantic policy matching
- Multi-step workflow evaluation
- Structured JSON responses

Future versions may extend these capabilities while preserving deterministic behavior.
