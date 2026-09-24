from agent.autonomous_agent import DatabricksFinOpsAgent
from agent.registry import TOOL_REGISTRY, execute_tool

def test_tool_registry_complete():
    assert len(TOOL_REGISTRY) >= 17, f"Expected at least 17 tools, found {len(TOOL_REGISTRY)}"

def test_autonomous_agent_full_audit():
    agent = DatabricksFinOpsAgent()
    res = agent.run_full_estate_audit()
    assert res["status"] == "COMPLETED"
    assert res["modules_executed"] == 8
    assert res["total_tools_evaluated"] >= 17
    assert "Databricks Autonomous FinOps & Governance Estate Audit Report" in res["master_markdown_report"]
