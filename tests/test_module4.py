from modules.module4_compute.tools import (
    predict_photon_acceleration_and_speedup,
    evaluate_serverless_compute_migration
)

def test_predict_photon_acceleration_and_speedup():
    res = predict_photon_acceleration_and_speedup("cluster-01")
    assert res["status"] == "SUCCESS"
    assert res["confidence_score"] == "98%"
    assert res["speedup_multiplier"] == "3.4x"
    assert res["latency_reduction_pct"] == 71.0

def test_evaluate_serverless_compute_migration():
    res = evaluate_serverless_compute_migration("cluster-02")
    assert res["status"] == "SUCCESS"
    assert res["confidence_score"] == "96%"
    assert res["serverless_eligibility"] == "PRIME_CANDIDATE"
    assert res["monthly_idle_savings_usd"] == 980.00
