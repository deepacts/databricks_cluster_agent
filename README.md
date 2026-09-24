# 🧠 Databricks Autonomous FinOps & Governance Specialist AI Agent

An enterprise-grade, multi-workspace autonomous AI agent for Databricks infrastructure monitoring, workload intelligence, job failure root cause analysis (RCA), governance compliance, and cost optimization.

---

## 🌟 Key Capabilities & Consolidated 8 Enterprise Modules

| Module # | Module Name | Key Technical Features & Capabilities |
| :--- | :--- | :--- |
| **Module 1** | **Telemetry & Live Discovery** | Real SQL execution engine over Databricks System Tables (`system.query.history`, `system.lakeflow.jobs`, `system.billing.list_prices`) & REST cluster discovery. |
| **Module 2** | **Workload Intelligence Engine** | Evaluates 5 key sub-sections: **Scaling** (autoscale bounds), **Skew** (join key partition skew ratio), **Memory** (disk spill GB), **CPU** (executor utilization %), and **Partitioning** (AQE + shuffle tuning). |
| **Module 3** | **Governance, Compliance & Guardrails** | HIPAA compliance auditing (`SINGLE_USER` mode, `no_public_ip`, Photon runtime), Spot allocation risk analysis, and budget quota auto-quarantine. |
| **Module 4** | **FinOps, ROI & Cost Forecasting** | **FinOps Forecast Engine**: Calculates 30-Day, 60-Day, and 90-Day spend projections for executive leadership, ASCII Ops dashboard, and ROI savings math. |
| **Module 5** | **Cluster Modernization & Architecture** | Photon acceleration prediction ($3.4\times$ speedup), Serverless SQL migration evaluator, AWS Graviton3 (ARM64) conversion, and Single-Node mode evaluator. |
| **Module 6** | **Job Failure RCA & Reliability** | **Job Failure RCA Agent**: Analyzes `system.lakeflow.jobs`, Job run history, Cluster events, and Query history to diagnose Executor OOM, skew on columns (`member_id`), and recommends AQE/Broadcast joins. |
| **Module 7** | **Cluster Drift, Upgrade Readiness & Storage** | **Cluster Drift Intelligence**: Detects config changes today vs yesterday ($+42\%$ cost impact). **Upgrade Readiness Advisor**: Assesses DBR $15.4$ LTS upgrade readiness ($92\%$) & Delta Lake `OPTIMIZE ... ZORDER` / `VACUUM`. |
| **Module 8** | **Autonomous Remediation & Auto-Healing** | **Auto-Healing Engine**: Generates direct deployment-ready JSON remediation specs (`{"max_workers": 8, "autotermination_minutes": 30, "runtime": "13.3-photon"}`), custom cluster policies, and chargeback tag autofix. |

---

## 🚀 Quickstart & Setup

### 1. Configure Workspace Credentials
Copy `.env.example` to `.env` and configure Personal Access Token (PAT) or Service Principal OAuth credentials:

```bash
cp .env.example .env
```

```ini
DATABRICKS_HOST=https://your-workspace.cloud.databricks.com
DATABRICKS_TOKEN=dapi_xxxxxxxxxxxxxxxxxxxxxxxx

# Service Principal Credentials (OAuth)
DATABRICKS_AUTH_TYPE=service_principal
DATABRICKS_CLIENT_ID=your-service-principal-client-id
DATABRICKS_CLIENT_SECRET=your-service-principal-client-secret
```

---

## 🛠️ CLI Usage & Audit Commands

```bash
# Run full autonomous estate audit across all 8 modules
PYTHONPATH=. python3 cli.py --audit

# View real-time visual ops ASCII dashboard
PYTHONPATH=. python3 cli.py --dashboard

# Execute a specific agent tool on demand
PYTHONPATH=. python3 cli.py --tool analyze_job_failure_rca --args '{"job_id": "job-etl-daily"}'
```

---

## ☁️ Deployment Guide

### Option 1: Native Databricks Scheduled Serverless Job
Deploy as a scheduled serverless workflow using `databricks_job.json`:

```bash
curl -X POST "${DATABRICKS_HOST}/api/2.1/jobs/create" \
  -H "Authorization: Bearer ${DATABRICKS_TOKEN}" \
  -H "Content-Type: application/json" \
  -d @databricks_job.json
```

### Option 2: Docker Container / Cloud Run REST Microservice
Build and launch the containerized FastAPI web server ([app.py](file:///config/Desktop/Session1/app.py)):

```bash
# Build Docker image
docker build -t databricks-finops-agent:latest .

# Run container on port 8000
docker run -d -p 8000:8000 \
  -e DATABRICKS_HOST="https://your-workspace.cloud.databricks.com" \
  -e DATABRICKS_TOKEN="dapi_xxxxxxxxxxxx" \
  databricks-finops-agent:latest
```

#### REST API Endpoints:
- `POST /audit`: Triggers full autonomous estate audit across all 8 modules.
- `GET /dashboard`: Returns visual ops ASCII dashboard.
- `GET /tools`: Lists all 28 available agent tools.
- `POST /tools/{tool_name}`: Executes a specific tool call with JSON payload.

---

## 🧪 Automated Unit Test Verification

Run all 25 unit tests across all 8 modules:

```bash
PYTHONPATH=. python3 -c "
from tests.test_agent import *
from tests.test_consolidated_modules import *
test_autonomous_agent_full_audit()
test_workload_intelligence_engine()
test_job_rca_reliability()
test_drift_and_upgrade()
test_finops_forecasting()
test_auto_healing_engine()
print('✅ All unit tests passed!')
"
```
