import logging
import json
import socket
from datetime import datetime
from typing import Dict, Any

class SVPThermometer:
    """
    Structured JSON telemetry logger for Enterprise SIEM integration.
    """
    def __init__(self, app_name: str = "svp-agent-runtime"):
        self.logger = logging.getLogger(app_name)
        self.logger.setLevel(logging.INFO)
        
        if not self.logger.handlers:
            handler = logging.StreamHandler()
            self.logger.addHandler(handler)
            
        self.hostname = socket.gethostname()

    def _build_payload(self, event_type: str, severity: str, metadata: Dict[str, Any]) -> str:
        payload = {
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "hostname": self.hostname,
            "event_type": event_type,
            "severity": severity,
            "kernel_version": "1.0.0",
            "metadata": metadata
        }
        return json.dumps(payload)

    def log_threat_intercept(self, action: str, score: float, policy_triggered: str):
        metadata = {
            "intercepted_action": action,
            "confidence_score": score,
            "violated_policy": policy_triggered,
            "action_status": "KILLED_AT_RUNTIME"
        }
        msg = self._build_payload("SEMANTIC_DRIFT_DETECTED", "CRITICAL", metadata)
        self.logger.critical(msg)

    def log_system_health(self, status: str, latency_ms: int):
        metadata = {"api_status": status, "latency_ms": latency_ms}
        msg = self._build_payload("KERNEL_HEALTH_CHECK", "INFO", metadata)
        self.logger.info(msg)
      
