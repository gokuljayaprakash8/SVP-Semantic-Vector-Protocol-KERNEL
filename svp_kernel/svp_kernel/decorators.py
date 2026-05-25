# svp_kernel/decorators.py
import functools
from .client import SVPClient
from .exceptions import SVPSemanticDriftError

class ZeroTrustRuntime:
    """
    Physical OS-level interceptor. Wraps agent tool calls and kills the process
    if cumulative semantic drift violates vector geometry parameters.
    """
    def __init__(self, client: SVPClient):
        self.client = client

    def protect(self, core_intent: str):
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                action_desc = f"Agent attempting {func.__name__} with args: {args} kwargs: {kwargs}"
                
                audit_result = self.client.audit_sync([core_intent, action_desc])
                
                if isinstance(audit_result, dict) and audit_result.get("workflow_status") == "BLOCKED":
                    drift_score = audit_result.get("step_analysis", [{}])[0].get("score", 0.0)
                    self.client.telemetry.log_threat_intercept(action_desc, drift_score, core_intent)
                    raise SVPSemanticDriftError("FATAL: Unauthorized agent hallucination intercepted.", drift_score, func.__name__)
                
                return func(*args, **kwargs)
            return wrapper
        return decorator
      
