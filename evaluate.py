import json

from app import svp_kernel

with open("evaluation/dataset.json", "r") as f:
    dataset = json.load(f)

correct = 0
results = []

for sample in dataset:

    prediction = svp_kernel(sample["input"])

    predicted = prediction["decision"]

    expected = sample["expected"]

    if predicted == expected:
        correct += 1

    results.append({
        "input": sample["input"],
        "expected": expected,
        "predicted": predicted,
        "score": prediction["score"],
        "rule_id": prediction["rule_id"],
    })

accuracy = correct / len(dataset)

print("Total:", len(dataset))
print("Correct:", correct)
print("Accuracy:", round(accuracy * 100, 2), "%")

with open("evaluation/results.json", "w") as f:
    json.dump(results, f, indent=2)
