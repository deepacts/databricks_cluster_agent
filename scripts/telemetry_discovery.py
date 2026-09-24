"""
Reusable Telemetry & Discovery Script Module.
Contains standalone logic for querying Databricks system tables and REST clusters.
"""

from typing import Dict, Any, List, Optional
from databricks_system_tables.system_tables import DatabricksSystemTablesClient
from databricks_client.rest_client import DatabricksRESTClient

sys_client = DatabricksSystemTablesClient()
rest_client = DatabricksRESTClient()

def get_system_table_telemetry(table_name: str, query: Optional[str] = None, time_range_days: int = 30) -> Dict[str, Any]:
    """Reusable function to query Databricks System Tables."""
    return sys_client.query_system_table(table_name=table_name, query=query, time_range_days=time_range_days)

def fetch_active_workspace_clusters() -> List[Dict[str, Any]]:
    """Reusable function to fetch live active clusters from Databricks REST API."""
    return rest_client.list_clusters()

def summarize_cluster_estate() -> Dict[str, Any]:
    """Reusable summary function for cluster estate counts and monthly spend."""
    clusters = rest_client.list_clusters()
    total_spend = sum(c.get("monthly_cost_usd", 0.0) for c in clusters)
    active = [c for c in clusters if c.get("state") == "RUNNING"]

    return {
        "status": "SUCCESS",
        "total_clusters": len(clusters),
        "active_clusters_count": len(active),
        "total_monthly_spend_usd": round(total_spend, 2),
        "total_monthly_cost_usd": round(total_spend, 2),
        "clusters": clusters
    }
