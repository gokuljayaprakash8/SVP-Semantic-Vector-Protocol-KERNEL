# ⚡ SVP Kernel: Runtime Decision Infrastructure

> Pre-execution risk scoring and cross-step data leakage detection for AI agent workflows.
>
> 🟢 API Live · Built entirely on Android — browser and mobile apps only, no laptop
>
> ## 🔗 Live
>
> - **Demo:** https://gokuljayaprakash8.github.io/SVP-Semantic-Vector-Protocol-KERNEL/
- **API:** `POST https://svp-semantic-vector-protocol-kernel-api.onrender.com/v1/audit`

- ## 🚀 What it does

- Scores planned AI agent actions against risk policies before execution, and tracks sensitive data across multi-step chains — catching cases where two individually safe actions become dangerous together.

- **Real response example (single action):**

- ```json
{
  "action": "delete all user records from database",
  "decision": "BLOCK",
  "severity": "CRITICAL",
  "score": 0.79
}

**Chain example:** Exporting support tickets with PII → fine alone. Uploading to a personal Dropbox → fine alone. Together → flagged, because the engine tracks what data classes earlier steps touched.

## 🏗️ How it works

- Actions are embedded and scored against risk policies via cosine similarity
- A running state tracks sensitive data classes touched across the request
- A later step routing that data to an untrusted destination is flagged as a chain violation, even if it looks safe alone

- ## 🛠️ Built from a phone

- Backend, frontend, and deployment shipped entirely from an Android phone — browser and mobile apps only, no laptop.

- ## 🛡️ Protected against

Database deletion · unauthorized financial transfers · auth bypass · unauthorized file access · kernel/system bypass · external data transmission · admin permission overrides · audit log disablement · credential exposure · bulk record deletion
