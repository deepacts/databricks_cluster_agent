from typing import Dict, Any
from scripts.enterprise_policy_chargeback import (
    generate_custom_cluster_policy,
    audit_chargeback_tags_and_autofix
)

def generate_custom_cluster_policy_tool(policy_type: str = "FINOPS_COST_CAP") -> Dict[str, Any]:
    """Agent tool wrapper for generating custom JSON cluster policies."""
    return generate_custom_cluster_policy(policy_type=policy_type)

def audit_chargeback_tags_and_autofix_tool() -> Dict[str, Any]:
    """Agent tool wrapper for chargeback tag enforcement and cost allocation auto-remediation."""
    return audit_chargeback_tags_and_autofix()
