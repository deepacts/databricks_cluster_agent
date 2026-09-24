from typing import Dict, Any, Optional
from scripts.governance_audit import (
    audit_hipaa_compliance,
    audit_spot_risk_and_health,
    audit_budget_and_quotas
)

def audit_cluster_policy_compliance_and_remediations(cluster_id: Optional[str] = "cluster-02") -> Dict[str, Any]:
    """Agent tool wrapper for HIPAA security policy auditing and drop-in JSON remediation specs."""
    return audit_hipaa_compliance(cluster_id=cluster_id)

def audit_cluster_health_and_spot_risk(cluster_id: Optional[str] = "cluster-01") -> Dict[str, Any]:
    """Agent tool wrapper for Spot ratio risk and driver memory health auditing."""
    return audit_spot_risk_and_health(cluster_id=cluster_id)

def audit_budget_guardrails_and_quotas(cost_center: Optional[str] = "CC-901") -> Dict[str, Any]:
    """Agent tool wrapper for budget quota auto-quarantine bounds enforcement."""
    return audit_budget_and_quotas(cost_center=cost_center)
