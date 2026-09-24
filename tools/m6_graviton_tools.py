from typing import Dict, Any
from scripts.graviton_architecture import (
    evaluate_graviton_arm64_migration,
    evaluate_single_node_cluster_conversion
)

def evaluate_graviton_arm64_migration_tool(cluster_id: str = "cluster-02") -> Dict[str, Any]:
    """Agent tool wrapper for AWS Graviton (ARM64) architecture migration evaluation."""
    return evaluate_graviton_arm64_migration(cluster_id=cluster_id)

def evaluate_single_node_cluster_conversion_tool(cluster_id: str = "cluster-02") -> Dict[str, Any]:
    """Agent tool wrapper for Single-Node mode conversion evaluation."""
    return evaluate_single_node_cluster_conversion(cluster_id=cluster_id)
