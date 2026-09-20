import json
import argparse
from src.meta_science_engine import MetaScienceEngine

def main():
    parser = argparse.ArgumentParser(description="Hypo Paper Synthesizer CLI")
    parser.add_argument("--demo", action="store_true", help="Run simulated meta-analytic effect size audit")
    args = parser.parse_args()

    engine = MetaScienceEngine()
    effect = engine.compute_cohens_d(m1=112.5, m2=104.2, sd1=14.0, sd2=15.1, n1=120, n2=120)
    risk = engine.audit_p_hacking_risk(p_value=0.048, sample_size=22)

    report = {"effect_size_analysis": effect, "p_hacking_audit": risk}
    print("="*60)
    print(" HYPO SCIENTIFIC LITERATURE META-ANALYSIS REPORT")
    print("="*60)
    print(json.dumps(report, indent=2))
    print("="*60)

if __name__ == "__main__":
    main()
