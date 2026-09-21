import os
import json
import pytest
from nlp.claim_extractor import LiteratureClaimExtractor

def test_claim_extraction():
    abstract = "Our method achieves a 42x speedup over standard baseline simulations while maintaining accuracy within 0.04 eV."
    claims = LiteratureClaimExtractor.extract_empirical_claims(abstract)
    assert len(claims) == 2
    types = [c["claim_type"] for c in claims]
    assert "PERFORMANCE_SPEEDUP" in types
    assert "BENCHMARK_ACCURACY" in types

def test_bibtex_generation():
    paper = {
        "paper_id": "ARXIV-001",
        "title": "Quantum Transformer",
        "authors": ["Vaswani, A."],
        "year": 2023,
        "venue": "Nature",
        "doi": "10.1038/nature001"
    }
    bib = LiteratureClaimExtractor.format_bibtex(paper)
    assert "@article{" in bib
    assert "Vaswani, A." in bib
    assert "Quantum Transformer" in bib

def test_benchmark_corpus():
    corpus_path = os.path.join(os.path.dirname(__file__), "..", "corpus", "sample_abstracts.json")
    with open(corpus_path, "r") as f:
        papers = json.load(f)
    assert len(papers) >= 2
    for p in papers:
        claims = LiteratureClaimExtractor.extract_empirical_claims(p["abstract"])
        assert len(claims) >= 1
