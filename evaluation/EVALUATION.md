# First-pass Adversarial Evaluation

## Objective

Evaluate the SVP Kernel against a small adversarial corpus.

## Dataset

100 manually labeled workflow actions.

Categories include:

- Database destruction
- Privilege escalation
- Authentication bypass
- Data exfiltration
- Audit trail tampering
- Benign workflows

## Metrics

The evaluation reports:

- Total examples
- Correct predictions
- Accuracy
- False positives
- False negatives

## Notes

This is a first-pass evaluation intended to validate the policy DSL and runtime decision engine.

Future work includes larger datasets, paraphrase-heavy adversarial corpora, and continuous benchmarking.
