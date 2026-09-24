from fastapi import FastAPI, HTTPException, Body
from typing import Dict, Any, Optional
import uvicorn

from agent.autonomous_agent import DatabricksFinOpsAgent
from agent.registry import TOOL_REGISTRY, execute_tool

app = FastAPI(
    title="Databricks Autonomous FinOps & Governance Specialist API",
    description="REST API for autonomous estate auditing, workload intelligence, job RCA, and remediation.",
    version="1.0.0"
)

agent = DatabricksFinOpsAgent()

@app.get("/health")
def health_check():
    return {"status": "HEALTHY", "agent": "Databricks Autonomous FinOps & Governance Specialist", "tools_count": len(TOOL_REGISTRY)}

@app.post("/audit")
def run_full_audit():
    """Runs full end-to-end estate audit across all 8 modules."""
    return agent.run_full_estate_audit()

@app.get("/dashboard")
def get_dashboard():
    """Returns real-time visual ops dashboard."""
    return execute_tool("get_ops_dashboard")

@app.get("/tools")
def list_available_tools():
    """Lists all available agent tools."""
    return {"total_tools": len(TOOL_REGISTRY), "tools": list(TOOL_REGISTRY.keys())}

@app.post("/tools/{tool_name}")
def execute_agent_tool(tool_name: str, payload: Optional[Dict[str, Any]] = Body(default={})):
    """Executes a specific tool by name with arguments."""
    try:
        return execute_tool(tool_name, **payload)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 8080))
    uvicorn.run(app, host="0.0.0.0", port=port)

