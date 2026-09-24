from modules.module3_governance.tools import (
    audit_cluster_policy_compliance_and_remediations,
    audit_cluster_health_and_spot_risk,
    audit_budget_guardrails_and_quotas
)

def test_audit_cluster_policy_compliance_and_remediations():
    res = audit_cluster_policy_compliance_and_remediations("cluster-02")
    assert res["status"] == "SUCCESS"
    assert res["compliance_status"] == "NON_COMPLIANT"
    assert res["confidence_score"] == "98%"
    assert res["compliant_config_json"]["data_security_mode"] == "SINGLE_USER"
    assert res["compliant_config_json"]["no_public_ip"] is True

def test_audit_cluster_health_and_spot_risk():
    res = audit_cluster_health_and_spot_risk("cluster-01")
    assert res["status"] == "SUCCESS"
    assert res["confidence_score"] == "93%"
    assert res["spot_worker_ratio_pct"] == 75.0

def test_audit_budget_guardrails_and_quotas():
    res = audit_budget_guardrails_and_quotas("CC-901")
    assert res["status"] == "SUCCESS"
    assert res["confidence_score"] == "97%"
    assert res["quota_consumed_pct"] == 85.0
