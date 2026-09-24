from typing import Callable, Dict, Any

from tools.m1_telemetry_tools import (
    query_databricks_system_tables,
    fetch_live_databricks_clusters,
    list_databricks_clusters
)
from tools.m2_workload_tools import (
    analyze_workload_intelligence_tool,
    analyze_unified_workload_and_scaling_efficiency,
    analyze_advanced_cluster_telemetry_and_anomalies,
    analyze_job_workloads_and_recommend_scaling,
    analyze_workload_vs_cluster_efficiency
)
from tools.m3_governance_tools import (
    audit_cluster_policy_compliance_and_remediations,
    audit_cluster_health_and_spot_risk,
    audit_budget_guardrails_and_quotas
)
from tools.m4_finops_tools import (
    calculate_finops_spend_forecast_tool,
    get_ops_dashboard,
    calculate_cluster_resizing_savings,
    apply_right_size_recommendation_with_history,
    update_cluster_recommendation,
    get_recommendation_history
)
from tools.m5_modernization_tools import (
    predict_photon_acceleration_and_speedup,
    evaluate_serverless_compute_migration,
    evaluate_graviton_arm64_migration_tool,
    evaluate_single_node_cluster_conversion_tool
)
from tools.m6_job_rca_tools import (
    analyze_job_failure_rca_tool
)
from tools.m7_drift_upgrade_tools import (
    detect_cluster_drift_tool,
    evaluate_dbr_upgrade_readiness_tool,
    audit_delta_lake_storage_optimization_tool
)
from tools.m8_auto_healing_tools import (
    generate_auto_healing_remediation_spec_tool,
    generate_custom_cluster_policy_tool,
    audit_chargeback_tags_and_autofix_tool
)

TOOL_REGISTRY: Dict[str, Callable] = {
    # Module 1: Telemetry & Live Discovery
    "query_databricks_system_tables": query_databricks_system_tables,
    "fetch_live_databricks_clusters": fetch_live_databricks_clusters,
    "list_databricks_clusters": list_databricks_clusters,

    # Module 2: Workload Intelligence Engine
    "analyze_workload_intelligence": analyze_workload_intelligence_tool,
    "analyze_unified_workload_and_scaling_efficiency": analyze_unified_workload_and_scaling_efficiency,
    "analyze_advanced_cluster_telemetry_and_anomalies": analyze_advanced_cluster_telemetry_and_anomalies,
    "analyze_job_workloads_and_recommend_scaling": analyze_job_workloads_and_recommend_scaling,
    "analyze_workload_vs_cluster_efficiency": analyze_workload_vs_cluster_efficiency,

    # Module 3: Governance, Compliance & Policy Guardrails
    "audit_cluster_policy_compliance_and_remediations": audit_cluster_policy_compliance_and_remediations,
    "audit_cluster_health_and_spot_risk": audit_cluster_health_and_spot_risk,
    "audit_budget_guardrails_and_quotas": audit_budget_guardrails_and_quotas,

    # Module 4: FinOps, ROI & Cost Forecasting
    "calculate_finops_spend_forecast": calculate_finops_spend_forecast_tool,
    "get_ops_dashboard": get_ops_dashboard,
    "calculate_cluster_resizing_savings": calculate_cluster_resizing_savings,
    "apply_right_size_recommendation_with_history": apply_right_size_recommendation_with_history,
    "update_cluster_recommendation": update_cluster_recommendation,
    "get_recommendation_history": get_recommendation_history,

    # Module 5: Cluster Modernization & Architecture
    "predict_photon_acceleration_and_speedup": predict_photon_acceleration_and_speedup,
    "evaluate_serverless_compute_migration": evaluate_serverless_compute_migration,
    "evaluate_graviton_arm64_migration": evaluate_graviton_arm64_migration_tool,
    "evaluate_single_node_cluster_conversion": evaluate_single_node_cluster_conversion_tool,

    # Module 6: Job Failure RCA & Reliability
    "analyze_job_failure_rca": analyze_job_failure_rca_tool,

    # Module 7: Cluster Drift, Upgrade Readiness & Storage
    "detect_cluster_drift": detect_cluster_drift_tool,
    "evaluate_dbr_upgrade_readiness": evaluate_dbr_upgrade_readiness_tool,
    "audit_delta_lake_storage_optimization": audit_delta_lake_storage_optimization_tool,

    # Module 8: Autonomous Remediation & Auto-Healing Engine
    "generate_auto_healing_remediation_spec": generate_auto_healing_remediation_spec_tool,
    "generate_custom_cluster_policy": generate_custom_cluster_policy_tool,
    "audit_chargeback_tags_and_autofix": audit_chargeback_tags_and_autofix_tool,
}

def get_all_tools() -> list[Callable]:
    return list(TOOL_REGISTRY.values())

def execute_tool(tool_name: str, **kwargs) -> Any:
    if tool_name not in TOOL_REGISTRY:
        raise ValueError(f"Unknown tool '{tool_name}'. Available tools: {list(TOOL_REGISTRY.keys())}")
    return TOOL_REGISTRY[tool_name](**kwargs)
