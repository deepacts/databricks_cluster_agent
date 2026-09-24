import json
from typing import Dict, Any, List
from agent.registry import TOOL_REGISTRY, execute_tool

SYSTEM_PROMPT = """You are the Databricks Autonomous FinOps & Governance Specialist AI.
Your purpose is to monitor, analyze, secure, and right-size Databricks clusters, jobs, and SQL warehouses
across 8 functional modules: Telemetry & Live Discovery, Workload Intelligence Engine,
Governance & Guardrails, FinOps & Cost Forecasting, Cluster Modernization, Job Failure RCA & Reliability,
Cluster Drift & Upgrade Readiness, and Autonomous Remediation Engine.
Always provide high-confidence quantitative findings (e.g. 96-98% Confidence), actionable policy JSON remediations,
and exact dollar ROI cost savings calculations."""

class DatabricksFinOpsAgent:
    """Autonomous Databricks FinOps & Governance AI Agent supporting 8 functional modules."""

    def __init__(self, workspace_host: str = None, token: str = None):
        self.system_prompt = SYSTEM_PROMPT
        self.tools = TOOL_REGISTRY

    def run_full_estate_audit(self) -> Dict[str, Any]:
        """Runs an autonomous end-to-end audit across all 8 functional modules."""
        audit_results = {}

        # Module 1: Telemetry
        audit_results["module1_clusters"] = execute_tool("list_databricks_clusters")
        audit_results["module1_system_tables"] = execute_tool("query_databricks_system_tables", table_name="system.query.history")

        # Module 2: Workload Intelligence Engine
        audit_results["module2_workload_intel"] = execute_tool("analyze_workload_intelligence", cluster_id="cluster-01")

        # Module 3: Governance & Guardrails
        audit_results["module3_compliance"] = execute_tool("audit_cluster_policy_compliance_and_remediations", cluster_id="cluster-02")
        audit_results["module3_budget"] = execute_tool("audit_budget_guardrails_and_quotas", cost_center="CC-901")

        # Module 4: FinOps & Forecasting
        audit_results["module4_forecast"] = execute_tool("calculate_finops_spend_forecast", current_monthly_spend=20000.0)
        audit_results["module4_dashboard"] = execute_tool("get_ops_dashboard")

        # Module 5: Cluster Modernization
        audit_results["module5_photon"] = execute_tool("predict_photon_acceleration_and_speedup", cluster_id="cluster-01")
        audit_results["module5_serverless"] = execute_tool("evaluate_serverless_compute_migration", cluster_id="cluster-02")

        # Module 6: Job Failure RCA
        audit_results["module6_rca"] = execute_tool("analyze_job_failure_rca", job_id="job-etl-daily")

        # Module 7: Cluster Drift, Upgrade & Storage
        audit_results["module7_drift"] = execute_tool("detect_cluster_drift", cluster_id="cluster-02")
        audit_results["module7_upgrade"] = execute_tool("evaluate_dbr_upgrade_readiness", cluster_id="cluster-01", target_dbr="15.4 LTS")
        audit_results["module7_delta"] = execute_tool("audit_delta_lake_storage_optimization", table_name="catalog.gold.claims_fact")

        # Module 8: Auto-Healing Engine
        audit_results["module8_auto_healing"] = execute_tool("generate_auto_healing_remediation_spec", cluster_id="cluster-02")

        # Assemble Master Audit Markdown Report
        master_report = f"""# 🧠 Databricks Autonomous FinOps & Governance Estate Audit Report

{audit_results['module4_dashboard']['ascii_dashboard']}

---

{audit_results['module2_workload_intel']['markdown_report']}

---

{audit_results['module3_compliance']['markdown_report']}

---

{audit_results['module5_photon']['markdown_report']}

---

{audit_results['module5_serverless']['markdown_report']}

---

### 🚨 Job Failure Root Cause Analysis (RCA)
```text
{audit_results['module6_rca']['plain_text_report']}
```

---

### 📉 Cluster Drift & Change Intelligence
```text
{audit_results['module7_drift']['plain_text_report']}
```

---

### 🚀 Upgrade Readiness Advisor
```text
{audit_results['module7_upgrade']['plain_text_report']}
```

---

### 📈 FinOps Cost Forecast Engine
```text
{audit_results['module4_forecast']['plain_text_report']}
```

---

{audit_results['module8_auto_healing']['markdown_report']}
"""

        return {
            "status": "COMPLETED",
            "modules_executed": 8,
            "total_tools_evaluated": len(TOOL_REGISTRY),
            "master_markdown_report": master_report,
            "raw_audit_details": audit_results
        }
