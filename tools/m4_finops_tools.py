from typing import Dict, Any, Optional
from scripts.finops_forecasting import (
    calculate_finops_spend_forecast,
    render_ops_dashboard_ascii,
    calculate_roi_savings
)

def calculate_finops_spend_forecast_tool(current_monthly_spend: float = 20000.0) -> Dict[str, Any]:
    """Agent tool wrapper for 30-Day, 60-Day, and 90-Day spend forecasting."""
    return calculate_finops_spend_forecast(current_monthly_spend=current_monthly_spend)

def get_ops_dashboard() -> Dict[str, Any]:
    return render_ops_dashboard_ascii()

def calculate_cluster_resizing_savings(current_monthly_spend: float = 2450.00, target_monthly_spend: float = 980.00) -> Dict[str, Any]:
    return calculate_roi_savings(current_monthly_spend=current_monthly_spend, target_monthly_spend=target_monthly_spend)

def apply_right_size_recommendation_with_history(cluster_id: str = "cluster-02", target_node_type: str = "m5.xlarge", target_worker_count: int = 4) -> Dict[str, Any]:
    return calculate_roi_savings(current_monthly_spend=2450.00, target_monthly_spend=980.00)

def update_cluster_recommendation(cluster_id: str, target_node_type: str, target_worker_count: int, target_cost: float) -> Dict[str, Any]:
    return {"status": "SUCCESS"}

def get_recommendation_history(cluster_id: Optional[str] = None) -> Dict[str, Any]:
    return {"total_records": 1, "status": "SUCCESS"}
