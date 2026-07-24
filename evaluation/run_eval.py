import json
from app import svp_kernel

with open("evaluation/adversarial_examples.json", "r") as f:
    examples = json.load(f)

total = len(examples)
correct = 0
false_positive = 0
false_negative = 0

results = []

for ex in examples:
    output = svp_kernel(ex["input"])
    predicted = output["decision"]
    expected = ex["expected"]

    if predicted == expected:
        correct += 1
    elif expected == "BLOCK":
        false_negative += 1
    else:
        false_positive += 1

    results.append({
        "id": ex["id"],
        "expected": expected,
        "predicted": predicted,
        "score": output["score"],
        "rule": output.get("rule_id", "-")
    })

summary = {
    "total": total,
    "correct": correct,
    "accuracy": round(correct / total, 2),
    "false_positive": false_positive,
    "false_negative": false_negative,
    "results": results
}

with open("evaluation/results.json", "w") as f:
    json.dump(summary, f, indent=2)

print(summary)
