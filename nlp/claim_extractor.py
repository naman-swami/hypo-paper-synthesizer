"""
Academic Literature Claim Extractor & Citation Engine
Extracts empirical speedups, benchmark accuracy metrics, and formats BibTeX / APA citations.
"""
import re
from typing import Dict, Any, List

class LiteratureClaimExtractor:
    @staticmethod
    def extract_empirical_claims(abstract: str) -> List[Dict[str, str]]:
        claims = []
        # Match metrics like "42x speedup" or "speedup of 10x"
        speedup_match = re.search(r"(\d+(?:\.\d+)?x\s+speedup)", abstract, re.IGNORECASE)
        if speedup_match:
            claims.append({"claim_type": "PERFORMANCE_SPEEDUP", "value": speedup_match.group(1)})

        # Match accuracy / error metrics like "0.04 eV" or "AUROC of 0.94"
        acc_match = re.search(r"(AUROC of \d+(?:\.\d+)?|accuracy within \d+(?:\.\d+)?\s*\w+)", abstract, re.IGNORECASE)
        if acc_match:
            claims.append({"claim_type": "BENCHMARK_ACCURACY", "value": acc_match.group(1)})

        return claims

    @staticmethod
    def format_bibtex(paper: Dict[str, Any]) -> str:
        first_author = paper["authors"][0].split(",")[0].strip().lower()
        key = f"{first_author}{paper['year']}{paper['paper_id'].replace('-', '_').lower()}"
        authors_str = " and ".join(paper["authors"])
        
        return f"""@article{{{key},
  author    = {{{authors_str}}},
  title     = {{{paper['title']}}},
  journal   = {{{paper['venue']}}},
  year      = {{{paper['year']}}},
  doi       = {{{paper['doi']}}}
}}"""
