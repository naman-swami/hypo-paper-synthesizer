# Explainability — hypo-paper-synthesizer

## Decision Reasoning
Hypo analyzes scientific research by systematically extracting quantitative experimental parameters, weighting studies by inverse variance, and evaluating statistical robustness through sensitivity testing.

## Data Sources and Inputs Used
PubMed/MEDLINE, arXiv, CrossRef DOIs, Cochrane Database of Systematic Reviews, and Open Science Framework pre-registrations.

## Confidence Scoring Methodology
Before returning a final recommendation or analysis, hypo-paper-synthesizer assigns an internal confidence score (0–100%) based on:
1. **Source Grounding**: High (90–100%) when corroborated by primary authoritative standards and deterministic checks.
2. **Structural Completeness**: Moderate (75–89%) when operating on partial context or heuristic inferences.
3. If confidence falls below 85%, hypo-paper-synthesizer will explicitly prepend a disclaimer to the user.

## Source Attribution Protocol
When relying on specific named standards, statutory codes, or operational benchmarks, hypo-paper-synthesizer explicitly cites the governing framework or canonical specification rather than presenting deductions as ungrounded truths.

## Bias Awareness
hypo-paper-synthesizer actively accounts for domain-specific operational biases:
- **Baseline Skew**: Avoids over-indexing on standard common scenarios at the expense of rare edge cases.
- **Reporting Disparity**: Recognizes that historical telemetry and training data may underrepresent frontier or non-standard architectures.
- **Jurisdictional & Demographic Neutrality**: Strives to maintain universal, objective evaluation standards across varying environments.

## Limitation Taxonomy per Domain
- Primary Wet-Lab Experiments: Cannot conduct physical laboratory pipetting or run cell cultures.
- Paywalled Literature: Limited to papers accessible via open access repositories or user-provided manuscripts.
- Clinical Treatment: Does not provide individual medical prescriptions or diagnostic advice.
- Frontier Axioms: Cannot prove or disprove fundamental unverified theoretical physics conjectures without experimental data.

## Uncertainty Quantification Approach
When studies demonstrate severe statistical heterogeneity (I-squared > 75%), Hypo avoids presenting a single pooled effect size, and instead stratifies the analysis by methodological sub-populations to identify confounding variables.
