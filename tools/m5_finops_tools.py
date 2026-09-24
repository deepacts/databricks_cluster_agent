from typing import Dict, Any, Optional
from scripts.finops_roi import (
    render_ops_dashboard_ascii,
    calculate_roi_savings,
    apply_right_size_action,
    update_db_recommendation,
    fetch_audit_history
)

def get_ops_dashboard() -> Dict[str, Any]:
    """Agent tool wrapper rendering ASCII dashboard."""
    return render_ops_dashboard_ascii()

def calculate_cluster_resizing_savings(current_monthly_spend: float = 2450.00, target_monthly_spend: float = 980.00) -> Dict[str, Any]:
    """Agent tool wrapper for ROI monthly and annual savings calculations."""
    return calculate_roi_savings(current_monthly_spend=current_monthly_spend, target_monthly_spend=target_monthly_spend)

def apply_right_size_recommendation_with_history(cluster_id: str = "cluster-02", target_node_type: str = "m5.xlarge", target_worker_count: int = 4) -> Dict[str, Any]:
    """Agent tool wrapper executing right-sizing and persistent audit logging."""
    return apply_right_size_action(cluster_id=cluster_id, target_node_type=target_node_type, target_worker_count=target_worker_count)

def update_cluster_recommendation(cluster_id: str, target_node_type: str, target_worker_count: int, target_cost: float) -> Dict[str, Any]:
    """Agent tool wrapper updating DB sizing specs."""
    return update_db_recommendation(cluster_id=cluster_id, target_node_type=target_node_type, target_worker_count=target_worker_count, target_cost=target_cost)

def get_recommendation_history(cluster_id: Optional[str] = None) -> Dict[str, Any]:
    """Agent tool wrapper fetching audit trail logs."""
    return fetch_audit_history(cluster_id=cluster_id)
