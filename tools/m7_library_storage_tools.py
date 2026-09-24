from typing import Dict, Any
from scripts.library_storage_audit import (
    audit_cluster_libraries_and_init_scripts,
    audit_delta_lake_storage_optimization
)

def audit_cluster_libraries_and_init_scripts_tool(cluster_id: str = "cluster-01") -> Dict[str, Any]:
    """Agent tool wrapper for auditing cluster init scripts and library dependencies."""
    return audit_cluster_libraries_and_init_scripts(cluster_id=cluster_id)

def audit_delta_lake_storage_optimization_tool(table_name: str = "catalog.gold.claims_fact") -> Dict[str, Any]:
    """Agent tool wrapper for Delta Lake storage layout optimization (OPTIMIZE/ZORDER/VACUUM)."""
    return audit_delta_lake_storage_optimization(table_name=table_name)
