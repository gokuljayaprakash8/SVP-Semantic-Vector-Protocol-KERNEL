import requests

class SVP:
    def __init__(self, endpoint="https://gokuljp-flowcheck-api.hf.space/audit-workflow"):
        self.endpoint = endpoint

    def audit(self, actions: list) -> dict:
        """
        Sends a list of agent actions to the SVP Kernel for semantic drift validation.
        """
        payload = {"actions": actions}
        try:
            response = requests.post(self.endpoint, json=payload)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            return {"error": f"SVP Kernel connection failed: {str(e)}"}
          
