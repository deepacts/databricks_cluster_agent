from typing import Dict, Any
from scripts.job_rca_reliability import analyze_job_failure_rca

def analyze_job_failure_rca_tool(job_id: str = "job-etl-daily") -> Dict[str, Any]:
    """Agent tool wrapper for automated Job Failure Root Cause Analysis."""
    return analyze_job_failure_rca(job_id=job_id)
