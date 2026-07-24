import yaml

REQUIRED = [
    "id",
    "description",
    "patterns",
    "threshold",
    "severity",
    "action",
]

def load_policy_file(path):
    with open(path, "r") as f:
        config = yaml.safe_load(f)

    if "policies" not in config:
        raise ValueError("Missing 'policies' section")

    for policy in config["policies"]:
        for field in REQUIRED:
            if field not in policy:
                raise ValueError(
                    f"Policy {policy.get('id','UNKNOWN')} missing '{field}'"
                )

    return config
