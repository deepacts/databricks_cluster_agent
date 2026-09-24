from modules.module1_telemetry.tools import (
    query_databricks_system_tables,
    fetch_live_databricks_clusters,
    list_databricks_clusters
)

def test_query_databricks_system_tables():
    res = query_databricks_system_tables("system.billing.list_prices")
    assert res["status"] == "SUCCESS"
    assert res["row_count"] > 0
    assert any("sku_name" in r for r in res["results"])

def test_fetch_live_databricks_clusters():
    clusters = fetch_live_databricks_clusters()
    assert isinstance(clusters, list)
    assert len(clusters) > 0
    assert "cluster_id" in clusters[0]

def test_list_databricks_clusters():
    res = list_databricks_clusters()
    assert res["status"] == "SUCCESS"
    assert res["total_clusters"] > 0
    assert res["total_monthly_cost_usd"] > 0
