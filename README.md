# Hypo Scientific Literature Synthesizer

[![OpenGAP](https://img.shields.io/badge/OpenGAP-0.1.0-blue.svg)](agent.yaml)
[![Academic](https://img.shields.io/badge/Domain-Scientific_Literature_NLP-darkblue.svg)](docs/scientific_methodology.md)
[![Standard](https://img.shields.io/badge/Protocol-PRISMA_2020-purple.svg)](docs/scientific_methodology.md)
[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](requirements.txt)
[![CI](https://img.shields.io/badge/CI-Passing-brightgreen.svg)](.github/workflows/ci.yml)

An academic literature synthesis engine automating empirical claim extraction from research abstracts, PRISMA-compliant evidence summarization, and BibTeX citation formatting.

```
                    ┌─────────────────────────┐
                    │ Research Abstract Text  │
                    │   (arXiv / PubMed)      │
                    └────────────┬────────────┘
                                 │
                                 ▼
                    ┌─────────────────────────┐
                    │   nlp/claim_extractor   │
                    └────────────┬────────────┘
                                 │
                 ┌───────────────┴───────────────┐
                 ▼                               ▼
      ┌─────────────────────┐         ┌─────────────────────┐
      │  Empirical Claims   │         │  BibTeX & Citation  │
      │ (Speedups & AUROC)  │         │  (Standard Journal) │
      └──────────┬──────────┘         └──────────┬──────────┘
                 │                               │
                 └───────────────┬───────────────┘
                                 ▼
                    ┌─────────────────────────┐
                    │ Systematic Synthesis    │
                    │ (PRISMA Review Summary) │
                    └─────────────────────────┘
```

## Features

- **Empirical Claim Mining**: Identifies benchmark speedups ($42\times$) and quantitative statistical bounds (AUROC, eV).
- **Automated BibTeX Generation**: Outputs cleanly formatted, publication-ready BibTeX citation keys.
- **Academic Benchmark Corpus**: Bundles multi-disciplinary abstracts across molecular dynamics and genomics.

## Directory Structure

```
hypo-paper-synthesizer/
├── agent.yaml                       # OpenGAP 0.1.0 Manifest
├── EXPLAINABILITY.md                # 7-checkpoint research provenance
├── nlp/
│   └── claim_extractor.py           # Claim extraction & BibTeX formatter
├── corpus/
│   └── sample_abstracts.json        # Academic abstract corpus
├── docs/
│   └── scientific_methodology.md    # PRISMA review guidelines
├── tests/
│   └── test_agent.py                # Scientific NLP test suite
├── main.py                          # Synthesis CLI
└── requirements.txt
```

## Quick Start

```bash
# Run scientific claim extraction tests
pytest tests/ -v

# Synthesize benchmark research corpus
python main.py --demo
```
