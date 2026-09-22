# Systematic Literature Review Methodology (PRISMA 2020 Standard)

## 1. Compliance with PRISMA 2020 Statement
Hypo executes automated academic literature synthesis conforming to the **Preferred Reporting Items for Systematic Reviews and Meta-Analyses (PRISMA 2020 Statement)** guidelines (Page et al., 2021).

---

## 2. The 4-Stage Systematic Review Workflow

```
┌────────────────────────────────────────────────────────┐
│ 1. IDENTIFICATION                                      │
│ - Ingest candidate abstracts from corpus/              │
│ - Query academic APIs (arXiv, PubMed, Semantic Scholar)│
└──────────────────────────┬─────────────────────────────┘
                           │
                           ▼
┌────────────────────────────────────────────────────────┐
│ 2. SCREENING                                           │
│ - Remove duplicate DOI entries and preprints           │
│ - Filter by keyword relevance and study design         │
└──────────────────────────┬─────────────────────────────┘
                           │
                           ▼
┌────────────────────────────────────────────────────────┐
│ 3. ELIGIBILITY                                         │
│ - Verify presence of quantitative empirical benchmarks │
│ - Reject qualitative position papers without data      │
└──────────────────────────┬─────────────────────────────┘
                           │
                           ▼
┌────────────────────────────────────────────────────────┐
│ 4. INCLUDED & SYNTHESIS                                │
│ - Extract statistical effect sizes and speedup claims  │
│ - Generate Evidence Matrix and standard BibTeX records │
└────────────────────────────────────────────────────────┘
```

---

## 3. Empirical Assertion Extraction Algorithms
The natural language extraction engine (`nlp/claim_extractor.py`) parses academic abstracts for concrete empirical assertions:

### A. Statistical Significance & Benchmark Metrics
- **$p$-value Extraction**: Regex pattern matching for $p < 0.05$, $p < 0.01$, and $p < 0.001$.
- **Speedup Claims**: Normalizes reported compute gains ($4\times$, $25\%$, $10\text{x}$) against baseline models.
- **Accuracy Benchmarks**: Parses standardized evaluation metrics (BLEU, ROUGE, Top-1 / Top-5 Error Rate, F1-Score).

### B. Confidence Scoring Formulation
Each extracted claim receives an evidence confidence rating ($C \in [0.0, 1.0]$):

$$C = w_{\text{stat}} \cdot S_{\text{stat}} + w_{\text{peer}} \cdot S_{\text{peer}} + w_{\text{rep}} \cdot S_{\text{rep}}$$

Where:
- $S_{\text{stat}}$: Rigor of statistical reporting (presence of error bounds and confidence intervals).
- $S_{\text{peer}}$: Publication venue tier (top-tier conferences: NeurIPS, ICML, Nature, Science vs. non-peer-reviewed arXiv).
- $S_{\text{rep}}$: Public availability of open-source artifacts, benchmarks, and code repositories.

---

## 4. Citation File Format & BibTeX Standards
All synthesized outputs include validated BibTeX records and conform to the Citation File Format declared in [CITATION.cff](CITATION.cff).
