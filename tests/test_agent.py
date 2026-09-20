import pytest
from src.meta_science_engine import MetaScienceEngine

def test_cohens_d():
    engine = MetaScienceEngine()
    res = engine.compute_cohens_d(100.0, 90.0, 10.0, 10.0, 50, 50)
    assert res["cohens_d"] == 1.0
    assert res["effect_size_magnitude"] == "LARGE"

def test_p_hacking_detection():
    engine = MetaScienceEngine()
    audit = engine.audit_p_hacking_risk(0.048, sample_size=20)
    assert audit["replication_risk_tier"] == "HIGH_REPLICATION_RISK"
