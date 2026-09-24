from modules.module2_workload.tools import (
    analyze_unified_workload_and_scaling_efficiency,
    analyze_advanced_cluster_telemetry_and_anomalies,
    analyze_job_workloads_and_recommend_scaling,
    analyze_workload_vs_cluster_efficiency
)

def test_analyze_unified_workload_and_scaling_efficiency():
    res = analyze_unified_workload_and_scaling_efficiency("cluster-01")
    assert res["status"] == "SUCCESS"
    assert res["confidence_score"] == "96%"
    assert "CODE_INEFFICIENCY" in res["workload_diagnosis"]
    assert "Unified Workload Analysis & Sizing Efficiency Engine" in res["markdown_report"]

def test_analyze_advanced_cluster_telemetry_and_anomalies():
    res = analyze_advanced_cluster_telemetry_and_anomalies()
    assert res["status"] == "SUCCESS"
    assert res["confidence_score"] == "95%"
    assert res["anomalies_detected_count"] > 0

def test_analyze_job_workloads_and_recommend_scaling():
    res = analyze_job_workloads_and_recommend_scaling("job-etl-daily")
    assert res["status"] == "SUCCESS"
    assert res["confidence_score"] == "94%"
    assert res["recommended_worker_count"] == 6

def test_analyze_workload_vs_cluster_efficiency():
    res = analyze_workload_vs_cluster_efficiency("cluster-01")
    assert res["status"] == "SUCCESS"
    assert res["root_cause_classification"] == "CODE_INEFFICIENCY"
