import argparse
import json
import os
from nlp.claim_extractor import LiteratureClaimExtractor

def main():
    parser = argparse.ArgumentParser(description="Hypo Literature Synthesizer CLI")
    parser.add_argument("--demo", action="store_true", help="Synthesize sample academic papers")
    args = parser.parse_args()

    corpus_file = os.path.join(os.path.dirname(__file__), "corpus", "sample_abstracts.json")

    if args.demo:
        with open(corpus_file, "r") as f:
            papers = json.load(f)
        print("=== HYPO SCIENTIFIC LITERATURE SYNTHESIS REPORT ===\n")
        for p in papers:
            claims = LiteratureClaimExtractor.extract_empirical_claims(p["abstract"])
            bibtex = LiteratureClaimExtractor.format_bibtex(p)
            print(f"Title: {p['title']}")
            print(f"Venue: {p['venue']} ({p['year']}) | DOI: {p['doi']}")
            print(f"Empirical Claims Extracted:")
            for c in claims:
                print(f"  * [{c['claim_type']}]: {c['value']}")
            print("\nGenerated BibTeX:")
            print(bibtex)
            print("-" * 50)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
