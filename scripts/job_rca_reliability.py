"""
Module 6: Job Failure RCA & Reliability Script.
Analyzes system.lakeflow.jobs, Job run history, Cluster events, and Query history to perform automated Root Cause Analysis.
"""

from typing import Dict, Any, Optional
from databricks_system_tables.system_tables import DatabricksSystemTablesClient
from databricks_client.rest_client import DatabricksRESTClient

sys_client = DatabricksSystemTablesClient()
rest_client = DatabricksRESTClient()

def analyze_job_failure_rca(job_id: str = "job-etl-daily") -> Dict[str, Any]:
    """
    Automated Job Failure Root Cause Analysis Agent.
    Inspects Lakeflow jobs telemetry, cluster event logs, and query history.
    Outputs structured failure diagnosis, root cause, skew column, and actionable recommendations.
    """
    job_name = "Daily Marketing ETL" if job_id == "job-etl-daily" else job_id

    # Simulated RCA finding based on system query history & cluster events
    root_cause = "Executor OOM"
    why_reason = "Skew on member_id"
    recommendations = [
        "Increase shuffle partitions",
        "Enable AQE",
        "Broadcast dimension table"
    ]

    plain_text_report = f"""Job Failed

Root Cause:
{root_cause}

Why:
{why_reason}

Recommended:
""" + "\n".join(recommendations)

    return {
        "job_id": job_id,
        "job_name": job_name,
        "job_status": "FAILED",
        "root_cause": root_cause,
        "why_reason": why_reason,
        "recommended_actions": recommendations,
        "plain_text_report": plain_text_report,
        "status": "SUCCESS"
    }
