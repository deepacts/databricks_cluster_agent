from typing import Dict, Any, Optional
from scripts.workload_intelligence import analyze_workload_intelligence
from scripts.workload_analysis import (
    diagnose_workload_and_scaling,
    detect_cluster_anomalies,
    optimize_batch_job_workers,
    calculate_workload_efficiency_index
)

def analyze_workload_intelligence_tool(cluster_id: str = "cluster-01") -> Dict[str, Any]:
    """Agent tool wrapper for Workload Intelligence Engine (Scaling, Skew, Memory, CPU, Partitioning)."""
    return analyze_workload_intelligence(cluster_id=cluster_id)

def analyze_unified_workload_and_scaling_efficiency(cluster_id: str = "cluster-01") -> Dict[str, Any]:
    return diagnose_workload_and_scaling(cluster_id=cluster_id)

def analyze_advanced_cluster_telemetry_and_anomalies(cluster_id: Optional[str] = None) -> Dict[str, Any]:
    return detect_cluster_anomalies(cluster_id=cluster_id)

def analyze_job_workloads_and_recommend_scaling(job_id: Optional[str] = "job-etl-daily") -> Dict[str, Any]:
    return optimize_batch_job_workers(job_id=job_id)

def analyze_workload_vs_cluster_efficiency(cluster_id: str = "cluster-01") -> Dict[str, Any]:
    return calculate_workload_efficiency_index(cluster_id=cluster_id)
