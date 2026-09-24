from typing import Dict, Any
from scripts.drift_upgrade_storage import (
    detect_cluster_drift,
    evaluate_dbr_upgrade_readiness,
    audit_delta_lake_storage_optimization
)

def detect_cluster_drift_tool(cluster_id: str = "cluster-02") -> Dict[str, Any]:
    """Agent tool wrapper for Cluster Drift & Change Intelligence."""
    return detect_cluster_drift(cluster_id=cluster_id)

def evaluate_dbr_upgrade_readiness_tool(cluster_id: str = "cluster-01", target_dbr: str = "15.4 LTS") -> Dict[str, Any]:
    """Agent tool wrapper for Upgrade Readiness Advisor."""
    return evaluate_dbr_upgrade_readiness(cluster_id=cluster_id, target_dbr=target_dbr)

def audit_delta_lake_storage_optimization_tool(table_name: str = "catalog.gold.claims_fact") -> Dict[str, Any]:
    """Agent tool wrapper for Delta Lake Storage & Layout Optimization."""
    return audit_delta_lake_storage_optimization(table_name=table_name)
