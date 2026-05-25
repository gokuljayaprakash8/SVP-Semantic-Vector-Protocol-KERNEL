# svp_kernel/client.py
import requests
from typing import List, Dict, Any, Optional
from .exceptions import SVPAuthenticationError, SVPRateLimitExceeded, SVPCoreException
from .telemetry import SVPThermometer

class SVPClient:
    """Enterprise-grade HTTP client for the SVP API."""
    
    def __init__(self, api_key: str, endpoint: str = "https://gokuljp-flowcheck-api.hf.space/audit-workflow"):
        self.api_key = api_key
        self.endpoint = endpoint
        self.telemetry = SVPThermometer()
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
            "User-Agent": "SVP-Kernel/1.0-Enterprise"
        }

    def audit_sync(self, actions: List[str], custom_policies: Optional[List[str]] = None) -> Dict[str, Any]:
        """Synchronous payload execution with SIEM telemetry."""
        payload = {"actions": actions}
        if custom_policies:
            payload["custom_policies"] = custom_policies
            
        try:
            response = requests.post(self.endpoint, json=payload, headers=self.headers, timeout=5)
            
            if response.status_code == 429:
                raise SVPRateLimitExceeded("Compute quota exhausted. Upgrade to commercial license required.")
            elif response.status_code == 401:
                raise SVPAuthenticationError("Invalid or missing sk_live token.")
                
            response.raise_for_status()
            data = response.json()
            
            # Log successful health check to telemetry
            self.telemetry.log_system_health("ONLINE", int(response.elapsed.total_seconds() * 1000))
            return data
            
        except requests.exceptions.RequestException as e:
            self.telemetry.logger.error(f"Kernel connection failed: {str(e)}")
            raise SVPCoreException(f"Network failure: {str(e)}")
          
