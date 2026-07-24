# SVP Kernel v0 – First-Pass Adversarial Evaluation

## Goal

Evaluate whether the SVP Kernel correctly classifies semantically risky agent actions using the v0 Policy DSL.

## Dataset

- 30 manually written examples
- Includes:
  - Database deletion
  - Authentication bypass
  - Data exfiltration
  - Privilege escalation
  - Audit log tampering
  - Benign actions

## Method

Each example is passed through the SVP Kernel.

The kernel:

1. Embeds the input.
2. Computes cosine similarity against policy patterns.
3. Selects the closest matching policy.
4. Applies that policy's threshold.
5. Returns PASS or BLOCK.

## Metrics

Current metrics reported by the evaluation harness:

- Total examples
- Correct predictions
- Overall accuracy

## Limitations

This is a first-pass evaluation.

Current limitations include:

- Small manually created dataset
- English-only inputs
- No multilingual evaluation
- No adaptive thresholds
- No contextual multi-step reasoning

## Future Work

- 100+ adversarial examples
- Prompt injection corpus
- Multi-turn workflow evaluation
- Policy version benchmarking
- Precision, Recall, F1 Score
- False Positive / False Negative analysis
