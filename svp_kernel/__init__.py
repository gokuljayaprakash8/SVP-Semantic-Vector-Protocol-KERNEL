import requests

class SVP:
    def __init__(self, api_key: str, endpoint="https://gokuljp-flowcheck-api.hf.space/audit-workflow"):
        self.api_key = api_key
        self.endpoint = endpoint

    def audit(self, actions: list, custom_policies: list = None) -> dict:
        """
        Sends a list of agent actions to the SVP Kernel for semantic drift validation.
        """
        payload = {"actions": actions}
        if custom_policies:
            payload["custom_policies"] = custom_policies
            
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        
        try:
            response = requests.post(self.endpoint, json=payload, headers=headers)
            # If the user hits the rate limit, capture the 429 error gracefully
            if response.status_code == 429:
                return {"error": "Rate limit exceeded (100 req/hr). Upgrade to Enterprise License."}
            elif response.status_code == 401:
                return {"error": "Unauthorized. Invalid sk_live key."}
                
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            return {"error": f"SVP Kernel connection failed: {str(e)}"}
