from typing import Dict, Any, Optional
from scripts.telemetry_discovery import (
    get_system_table_telemetry,
    fetch_active_workspace_clusters,
    summarize_cluster_estate
)

def query_databricks_system_tables(table_name: str = "system.query.history", query: Optional[str] = None, time_range_days: int = 30) -> Dict[str, Any]:
    """Agent tool wrapper for System Tables SQL queries."""
    return get_system_table_telemetry(table_name=table_name, query=query, time_range_days=time_range_days)

def fetch_live_databricks_clusters() -> list:
    """Agent tool wrapper for active cluster REST synchronization."""
    return fetch_active_workspace_clusters()

def list_databricks_clusters() -> Dict[str, Any]:
    """Agent tool wrapper for cluster estate summary."""
    return summarize_cluster_estate()
