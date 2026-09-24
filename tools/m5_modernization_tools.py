from typing import Dict, Any, Optional
from scripts.compute_modernization import predict_photon_speedup, evaluate_serverless_migration
from scripts.graviton_architecture import evaluate_graviton_arm64_migration, evaluate_single_node_cluster_conversion

def predict_photon_acceleration_and_speedup(cluster_id: str = "cluster-01") -> Dict[str, Any]:
    return predict_photon_speedup(cluster_id=cluster_id)

def evaluate_serverless_compute_migration(cluster_id: Optional[str] = "cluster-02") -> Dict[str, Any]:
    return evaluate_serverless_migration(cluster_id=cluster_id)

def evaluate_graviton_arm64_migration_tool(cluster_id: str = "cluster-02") -> Dict[str, Any]:
    return evaluate_graviton_arm64_migration(cluster_id=cluster_id)

def evaluate_single_node_cluster_conversion_tool(cluster_id: str = "cluster-02") -> Dict[str, Any]:
    return evaluate_single_node_cluster_conversion(cluster_id=cluster_id)
