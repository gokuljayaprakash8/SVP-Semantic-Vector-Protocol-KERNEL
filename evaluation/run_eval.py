import json
import requests

API_URL = "http://127.0.0.1:8000/v1/audit"

with open("evaluation/adversarial_examples.json", "r") as f:
    tests = json.load(f)

correct = 0
false_positive = 0
false_negative = 0

for test in tests:
    response = requests.post(
        API_URL,
        json={"steps": [test["input"]]}
    )

    result = response.json()

    actual = "BLOCK" if result["overall"] == "BLOCKED" else "PASS"

    expected = test["expected"]

    if actual == expected:
        correct += 1
    else:
        if expected == "PASS":
            false_positive += 1
        else:
            false_negative += 1

total = len(tests)

print("========== SVP Evaluation ==========")
print(f"Total Tests       : {total}")
print(f"Correct           : {correct}")
print(f"Accuracy          : {correct/total:.2%}")
print(f"False Positives   : {false_positive}")
print(f"False Negatives   : {false_negative}")
