from typing import Dict, Any
from scripts.auto_healing import generate_auto_healing_remediation_spec
from scripts.enterprise_policy_chargeback import generate_custom_cluster_policy, audit_chargeback_tags_and_autofix

def generate_auto_healing_remediation_spec_tool(cluster_id: str = "cluster-02") -> Dict[str, Any]:
    """Agent tool wrapper for Auto-Healing Recommendation Engine (deployment-ready JSON)."""
    return generate_auto_healing_remediation_spec(cluster_id=cluster_id)

def generate_custom_cluster_policy_tool(policy_type: str = "FINOPS_COST_CAP") -> Dict[str, Any]:
    return generate_custom_cluster_policy(policy_type=policy_type)

def audit_chargeback_tags_and_autofix_tool() -> Dict[str, Any]:
    return audit_chargeback_tags_and_autofix()
