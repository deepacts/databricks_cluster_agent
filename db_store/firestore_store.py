import json
import os
from datetime import datetime
from typing import Dict, Any, List, Optional
from config.settings import config

class DatabricksFirestoreStore:
    """Persistent storage layer utilizing Firestore or local JSON fallback for audit trails & recommendations."""
    
    def __init__(self, db_path: str = None):
        self.db_path = db_path or config.local_db_path
        self._ensure_local_store()

    def _ensure_local_store(self):
        if not os.path.exists(self.db_path):
            initial_data = {
                "clusters": {
                    "cluster-01": {
                        "cluster_id": "cluster-01",
                        "cluster_name": "analytics-bi-warehouse",
                        "monthly_cost_usd": 1800.00,
                        "state": "RUNNING",
                        "node_type": "c5.2xlarge",
                        "num_workers": 6,
                        "updated_at": datetime.utcnow().isoformat()
                    },
                    "cluster-02": {
                        "cluster_id": "cluster-02",
                        "cluster_name": "data-science-dev",
                        "monthly_cost_usd": 2450.00,
                        "state": "RUNNING",
                        "node_type": "m5.4xlarge",
                        "num_workers": 8,
                        "updated_at": datetime.utcnow().isoformat()
                    }
                },
                "recommendations": {},
                "audit_logs": [
                    {
                        "timestamp": datetime.utcnow().isoformat(),
                        "action": "SYSTEM_INITIALIZED",
                        "cluster_id": "cluster-01",
                        "details": "Databricks FinOps Engine monitoring active."
                    }
                ]
            }
            with open(self.db_path, "w") as f:
                json.dump(initial_data, f, indent=2)

    def _read_store(self) -> Dict[str, Any]:
        try:
            with open(self.db_path, "r") as f:
                return json.load(f)
        except Exception:
            return {"clusters": {}, "recommendations": {}, "audit_logs": []}

    def _write_store(self, data: Dict[str, Any]):
        with open(self.db_path, "w") as f:
            json.dump(data, f, indent=2)

    def list_clusters(self) -> List[Dict[str, Any]]:
        """Fetch high-level summary listing from persistent storage."""
        data = self._read_store()
        return list(data.get("clusters", {}).values())

    def update_cluster_recommendation(self, cluster_id: str, target_node_type: str, target_worker_count: int, target_cost: float) -> Dict[str, Any]:
        """Update sizing specs in persistent database."""
        data = self._read_store()
        rec = {
            "cluster_id": cluster_id,
            "target_node_type": target_node_type,
            "target_worker_count": target_worker_count,
            "target_cost_usd": target_cost,
            "updated_at": datetime.utcnow().isoformat()
        }
        data.setdefault("recommendations", {})[cluster_id] = rec
        self._write_store(data)
        return rec

    def add_audit_log(self, cluster_id: str, action: str, before_config: Dict[str, Any], after_config: Dict[str, Any]) -> Dict[str, Any]:
        """Record immutable Before vs After audit log entry."""
        data = self._read_store()
        log_entry = {
            "log_id": f"audit-{len(data.get('audit_logs', [])) + 1:04d}",
            "timestamp": datetime.utcnow().isoformat(),
            "cluster_id": cluster_id,
            "action": action,
            "before_config": before_config,
            "after_config": after_config
        }
        data.setdefault("audit_logs", []).append(log_entry)
        
        # Update cluster in store
        if cluster_id in data.get("clusters", {}):
            data["clusters"][cluster_id]["node_type"] = after_config.get("node_type_id", data["clusters"][cluster_id].get("node_type"))
            data["clusters"][cluster_id]["num_workers"] = after_config.get("num_workers", data["clusters"][cluster_id].get("num_workers"))
            data["clusters"][cluster_id]["monthly_cost_usd"] = after_config.get("monthly_cost_usd", data["clusters"][cluster_id].get("monthly_cost_usd"))
            data["clusters"][cluster_id]["updated_at"] = datetime.utcnow().isoformat()

        self._write_store(data)
        return log_entry

    def get_audit_history(self, cluster_id: Optional[str] = None) -> List[Dict[str, Any]]:
        """Fetch historical optimization logs."""
        data = self._read_store()
        logs = data.get("audit_logs", [])
        if cluster_id:
            return [l for l in logs if l.get("cluster_id") == cluster_id]
        return logs
