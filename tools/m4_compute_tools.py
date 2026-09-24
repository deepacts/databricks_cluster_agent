from typing import Dict, Any, Optional
from scripts.compute_modernization import (
    predict_photon_speedup,
    evaluate_serverless_migration
)

def predict_photon_acceleration_and_speedup(cluster_id: str = "cluster-01") -> Dict[str, Any]:
    """Agent tool wrapper for Photon speedup prediction and net DBU savings math."""
    return predict_photon_speedup(cluster_id=cluster_id)

def evaluate_serverless_compute_migration(cluster_id: Optional[str] = "cluster-02") -> Dict[str, Any]:
    """Agent tool wrapper for Serverless Compute migration evaluation."""
    return evaluate_serverless_migration(cluster_id=cluster_id)
