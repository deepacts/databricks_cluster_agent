import sys
import argparse
import json
from agent.autonomous_agent import DatabricksFinOpsAgent
from agent.registry import execute_tool, TOOL_REGISTRY

def main():
    parser = argparse.ArgumentParser(description="Databricks Autonomous FinOps & Governance CLI")
    parser.add_argument("--audit", action="store_true", help="Run full estate autonomous audit across all 5 modules")
    parser.add_argument("--dashboard", action="store_true", help="Display real-time visual ops ASCII dashboard")
    parser.add_argument("--tool", type=str, help="Execute a specific tool by name")
    parser.add_argument("--args", type=str, help="JSON string arguments for tool execution")

    args = parser.parse_args()

    agent = DatabricksFinOpsAgent()

    if args.audit:
        print("🚀 Running full autonomous estate audit...")
        result = agent.run_full_estate_audit()
        print(result["master_markdown_report"])
    elif args.dashboard:
        res = execute_tool("get_ops_dashboard")
        print(res["ascii_dashboard"])
    elif args.tool:
        tool_args = json.loads(args.args) if args.args else {}
        res = execute_tool(args.tool, **tool_args)
        if isinstance(res, dict) and "markdown_report" in res:
            print(res["markdown_report"])
        else:
            print(json.dumps(res, indent=2))
    else:
        print("Databricks Autonomous FinOps & Governance CLI")
        print(f"Available tools ({len(TOOL_REGISTRY)}):")
        for tool_name in TOOL_REGISTRY:
            print(f"  - {tool_name}")
        print("\nUsage:")
        print("  python3 cli.py --audit")
        print("  python3 cli.py --dashboard")
        print("  python3 cli.py --tool query_databricks_system_tables --args '{\"table_name\": \"system.billing.list_prices\"}'")

if __name__ == "__main__":
    main()
