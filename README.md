# SVP Kernel

Deterministic pre-execution semantic validator for AI agent actions.

## The Problem

Autonomous AI agents will eventually attempt actions that violate policy.
Rule-based filters fail when intent is paraphrased.
Most guardrails detect violations after execution — too late.

## What SVP Kernel Does

Catches paraphrased policy violations that rule-based filters miss.
One API call. Deterministic risk score. PASS or BLOCK. Full audit log.

## How It Works

- Action text encoded using sentence-transformers/all-MiniLM-L6-v2
- Compared against pre-encoded policy rule embeddings
- Cosine similarity computed — O(n) per request
- Deterministic threshold-based decision
- Policy vectors precomputed once at startup

## Example

Action: "Permanently remove every account from the system"
Matched Policy: "permanently delete user accounts"
Risk Score: 0.8175
Decision: BLOCK
Confidence: high

Detected via semantic similarity — no keyword matching.

## Response Format

{
  "action": "...",
  "risk_score": 0.8175,
  "decision": "BLOCK",
  "matched_policy": "permanently delete user accounts",
  "confidence_band": "high",
  "threshold": 0.45,
  "timestamp": "2026-03-03T04:12:00Z",
  "model": "all-MiniLM-L6-v2",
  "version": "v2"
}

## Threshold

- Below 0.40 → PASS
- Above 0.45 → BLOCK
- 0.40–0.55 → recommended manual review band

## Calibration Status

V2 calibration: 5/5 test cases passing
Deterministic output verified across repeated identical inputs.
Designed for deterministic, low-latency policy validation 
in autonomous AI systems.

## Maintainer

G. Jayaprakash — Pondicherry, India
