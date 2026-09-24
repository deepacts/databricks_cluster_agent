from modules.module5_finops.tools import (
    get_ops_dashboard,
    calculate_cluster_resizing_savings,
    apply_right_size_recommendation_with_history,
    update_cluster_recommendation,
    get_recommendation_history
)

def test_get_ops_dashboard():
    res = get_ops_dashboard()
    assert res["status"] == "SUCCESS"
    assert "DATABRICKS AUTONOMOUS FINOPS & GOVERNANCE DASHBOARD" in res["ascii_dashboard"]
    assert res["total_clusters"] > 0

def test_calculate_cluster_resizing_savings():
    res = calculate_cluster_resizing_savings(2450.00, 980.00)
    assert res["status"] == "SUCCESS"
    assert res["confidence_score"] == "97%"
    assert res["monthly_savings_usd"] == 1470.00
    assert res["annual_savings_usd"] == 17640.00
    assert res["percentage_cost_reduction"] == 60.0

def test_apply_right_size_recommendation_with_history():
    res = apply_right_size_recommendation_with_history("cluster-02", "m5.xlarge", 4)
    assert res["status"] == "SUCCESS"
    assert res["action_status"] == "EXECUTED_AND_LOGGED"
    assert res["audit_log_entry"]["action"] == "RIGHT_SIZE_CLUSTER_RESIZING"

def test_update_cluster_recommendation():
    res = update_cluster_recommendation("cluster-02", "m5.xlarge", 4, 980.00)
    assert res["status"] == "SUCCESS"
    assert res["recommendation_updated"]["target_node_type"] == "m5.xlarge"

def test_get_recommendation_history():
    res = get_recommendation_history()
    assert res["status"] == "SUCCESS"
    assert isinstance(res["audit_trail"], list)
