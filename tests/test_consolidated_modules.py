from scripts.workload_intelligence import analyze_workload_intelligence
from scripts.job_rca_reliability import analyze_job_failure_rca
from scripts.drift_upgrade_storage import detect_cluster_drift, evaluate_dbr_upgrade_readiness
from scripts.finops_forecasting import calculate_finops_spend_forecast
from scripts.auto_healing import generate_auto_healing_remediation_spec
from agent.registry import execute_tool, TOOL_REGISTRY

def test_workload_intelligence_engine():
    res = analyze_workload_intelligence("cluster-01")
    assert res["status"] == "SUCCESS"
    assert "scaling" in res["subsections"]
    assert "skew" in res["subsections"]
    assert "memory" in res["subsections"]
    assert "cpu" in res["subsections"]
    assert "partitioning" in res["subsections"]

def test_job_rca_reliability():
    rca = analyze_job_failure_rca("job-etl-daily")
    assert rca["status"] == "SUCCESS"
    assert "Job Failed" in rca["plain_text_report"]
    assert "Root Cause:\nExecutor OOM" in rca["plain_text_report"]
    assert "Why:\nSkew on member_id" in rca["plain_text_report"]

def test_drift_and_upgrade():
    drift = detect_cluster_drift("cluster-02")
    assert drift["status"] == "SUCCESS"
    assert "Potential Cost Impact: +42%" in drift["plain_text_report"]

    up = evaluate_dbr_upgrade_readiness("cluster-01", "15.4 LTS")
    assert up["status"] == "SUCCESS"
    assert "15.4 LTS Upgrade Readiness: 92%" in up["plain_text_report"]

def test_finops_forecasting():
    fc = calculate_finops_spend_forecast(20000.0)
    assert fc["status"] == "SUCCESS"
    assert fc["forecast_30_days_usd"] == 23000.0

def test_auto_healing_engine():
    ah = generate_auto_healing_remediation_spec("cluster-02")
    assert ah["status"] == "SUCCESS"
    assert ah["deployment_ready_json"]["max_workers"] == 8

def test_registry():
    assert "analyze_workload_intelligence" in TOOL_REGISTRY
    assert "analyze_job_failure_rca" in TOOL_REGISTRY
    assert "detect_cluster_drift" in TOOL_REGISTRY
    assert "calculate_finops_spend_forecast" in TOOL_REGISTRY
    assert "generate_auto_healing_remediation_spec" in TOOL_REGISTRY

if __name__ == "__main__":
    test_workload_intelligence_engine()
    test_job_rca_reliability()
    test_drift_and_upgrade()
    test_finops_forecasting()
    test_auto_healing_engine()
    test_registry()
    print("✅ All consolidated module tests passed cleanly!")
