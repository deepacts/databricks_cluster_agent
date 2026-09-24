from scripts.graviton_architecture import evaluate_graviton_arm64_migration, evaluate_single_node_cluster_conversion
from scripts.library_storage_audit import audit_cluster_libraries_and_init_scripts, audit_delta_lake_storage_optimization
from scripts.enterprise_policy_chargeback import generate_custom_cluster_policy, audit_chargeback_tags_and_autofix
from agent.registry import execute_tool, TOOL_REGISTRY

def test_graviton_architecture_module():
    res = evaluate_graviton_arm64_migration("cluster-02")
    assert res["status"] == "SUCCESS"
    assert res["cost_reduction_pct"] == 20.0
    assert "m6g" in res["recommended_graviton_node_type"]

    sn_res = evaluate_single_node_cluster_conversion("cluster-02")
    assert sn_res["status"] == "SUCCESS"
    assert sn_res["recommended_workers"] == 0

def test_library_storage_audit_module():
    lib_res = audit_cluster_libraries_and_init_scripts("cluster-01")
    assert lib_res["status"] == "SUCCESS"
    assert lib_res["init_script_delay_mins"] > 0

    delta_res = audit_delta_lake_storage_optimization("catalog.gold.claims_fact")
    assert delta_res["status"] == "SUCCESS"
    assert "OPTIMIZE" in delta_res["markdown_report"]

def test_enterprise_policy_chargeback_module():
    pol_res = generate_custom_cluster_policy("FINOPS_COST_CAP")
    assert pol_res["status"] == "SUCCESS"
    assert "autotermination_minutes" in pol_res["policy_json_spec"]

    cb_res = audit_chargeback_tags_and_autofix()
    assert cb_res["status"] == "SUCCESS"
    assert cb_res["audited_clusters_count"] > 0

def test_new_tool_registry():
    assert "evaluate_graviton_arm64_migration" in TOOL_REGISTRY
    assert "audit_delta_lake_storage_optimization" in TOOL_REGISTRY
    assert "generate_custom_cluster_policy" in TOOL_REGISTRY

    exec_res = execute_tool("evaluate_graviton_arm64_migration", cluster_id="cluster-02")
    assert exec_res["status"] == "SUCCESS"

if __name__ == "__main__":
    test_graviton_architecture_module()
    test_library_storage_audit_module()
    test_enterprise_policy_chargeback_module()
    test_new_tool_registry()
    print("✅ All new module tests passed successfully!")
