# Hypo Scientific Literature Synthesizer

> **Automated Systematic Literature Review Engine (PRISMA 2020 Standard)**  
> Extracting Empirical Benchmark Claims, Statistical Speedup Ratios, and BibTeX Citations.

---

### PRISMA 2020 Synthesis Workflow

```
   [Identification]   25 Candidate Corpus Abstracts Ingested (corpus/sample_abstracts.json)
          │
          ▼
   [Screening]        NLP Filter: Retain empirical studies with measured p-values
          │
          ▼
   [Eligibility]      Statistical Assertion Extractor: Parse speedup %, error bounds
          │
          ▼
   [Included]         Synthesized Evidence Matrix & Automated BibTeX Generator
```

---

### Sample Synthesized Evidence Matrix

| Study Reference | Investigated Domain | Sample / Dataset | Empirical Claim Extracted | Confidence Level |
| :--- | :--- | :--- | :--- | :--- |
| *Vaswani et al.* | Deep Learning NLP | WMT 2014 En-De | BLEU score of 28.4 (2.0 improvement) | High ($p < 0.001$) |
| *He et al.* | Computer Vision | ImageNet-1k | 3.57% top-5 error rate (ResNet-152) | High ($p < 0.001$) |
| *OpenGAP Bench* | Agent Telemetry | OpenGAP 0.1.0 | 4x faster cross-runtime portability | Medium (Empirical) |

---

### Review Pipeline CLI

```bash
# Execute literature synthesis on benchmark corpus
python synthesize.py --demo

# Run NLP claim extraction unit tests
pytest tests/ -v
```

Corpus citation metadata conforms to the Citation File Format in [CITATION.cff](CITATION.cff).
