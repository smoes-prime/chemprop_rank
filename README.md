<picture>
  <source media="(prefers-color-scheme: dark)" srcset="docs/source/_static/images/logo/chemprop_logo_dark_mode.svg">
  <img alt="ChemProp Logo" src="docs/source/_static/images/logo/chemprop_logo.svg">
</picture>

# Chemprop

[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/chemprop)](https://badge.fury.io/py/chemprop)
[![PyPI version](https://badge.fury.io/py/chemprop.svg)](https://badge.fury.io/py/chemprop)
[![Anaconda-Server Badge](https://anaconda.org/conda-forge/chemprop/badges/version.svg)](https://anaconda.org/conda-forge/chemprop)
[![Build Status](https://github.com/chemprop/chemprop/workflows/tests/badge.svg)](https://github.com/chemprop/chemprop/actions/workflows/tests.yml)
[![Documentation Status](https://readthedocs.org/projects/chemprop/badge/?version=main)](https://chemprop.readthedocs.io/en/main/?badge=main)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Downloads](https://static.pepy.tech/badge/chemprop)](https://pepy.tech/project/chemprop)
[![Downloads](https://static.pepy.tech/badge/chemprop/month)](https://pepy.tech/project/chemprop)
[![Downloads](https://static.pepy.tech/badge/chemprop/week)](https://pepy.tech/project/chemprop)

Chemprop is a repository containing message passing neural networks for molecular property prediction.
🆕 New Feature: Ranking Metrics in Model Evaluation
We've enhanced Chemprop to include ranking metrics during model evaluation. This addition allows for better assessment of how well models rank compounds, which is particularly useful for:

Virtual screening applications
Hit identification workflows
Prioritization of compounds for synthesis or testing
Lead optimization campaigns

The ranking metrics include:

Spearman's rank correlation coefficient
Kendall's tau
Normalized Discounted Cumulative Gain (NDCG)
Enrichment factors at different percentiles

### New RBO Loss Function

In addition to the existing ranking metrics, Chemprop now supports Rank-Biased Overlap (RBO) as a differentiable loss function during training and as an evaluation metric:

- **Implementation**: `RBOLoss` class in `chemprop/nn/metrics.py` computing `1 - RBO`
- **CLI Options**:
  - `--loss_function rbo` to select RBO loss
  - `--rbo_p FLOAT` to set the persistence parameter _p_ (default 0.9)
- **Usage**:
  ```bash
  chemprop_train --data_path data.csv --task_type regression \
                 --loss_function rbo --rbo_p 0.95
  ```
- **Testing**: Unit tests added in `tests/unit/test_rbo_loss.py` for toy ranking examples
- **Testing (RBO)**: Unit tests added in `tests/unit/test_rbo_loss.py` for toy ranking examples

### NDCG@10% Evaluation Metric

Chemprop now provides a Normalized Discounted Cumulative Gain metric focusing on the top 10% of predictions:

- **Implementation**: `NDCGTopFraction` class in `chemprop/nn/metrics.py`
- **CLI Options**:
  - `--metrics ndcg` to compute NDCG@10% during evaluation
- **Behavior**: Calculates DCG and IDCG over the top 10% of ranked compounds and reports the normalized score.

**Usage (as evaluation metric)**:
```bash
chemprop_train --data_path data.csv --task_type regression \
                --metrics ndcg --loss_function mse
```

**Running Tests**:
To execute the new ranking-loss and ranking-metric unit tests:
```bash
# Run RBO loss tests
pytest tests/unit/test_rbo_loss.py

# Run NDCG@10% metric tests
pytest tests/unit/test_ndcg_metric.py
```

This metric helps assess model ranking performance when only the top fraction of predictions are critical (e.g., virtual screening).

### Differentiable Ranking Loss Functions

Chemprop now supports several differentiable surrogate ranking losses that can be used to *optimize* ranking metrics directly:

- **SoftRank** (`softrank`): Matches predicted soft-ranks to true ranks via MSE of soft rank estimates.
- **ListNet** (`listnet`): Cross-entropy between ground-truth and predicted softmax distributions over scores.
- **ListMLE** (`listmle`): Maximum likelihood over permutations following the ground-truth ordering.
- **LambdaRank** (`lambdarank`): Pairwise logistic loss weighted by changes in NDCG.

**CLI Options**:
```bash
# Common tau (temperature) parameter for all surrogate losses:
--rank_tau FLOAT      # default 1.0

# To train with SoftRank loss:
--loss_function softrank --rank_tau 0.5

# To train with ListNet loss:
--loss_function listnet --rank_tau 1.0

# To train with ListMLE loss:
--loss_function listmle --rank_tau 1.0

# To train with LambdaRank loss:
--loss_function lambdarank --rank_tau 1.0
```

**Usage Example**:
```bash
chemprop_train --data_path data.csv --task_type regression \
               --loss_function listnet --rank_tau 0.7
```

These losses are fully implemented in PyTorch and backpropagate gradients during training to directly improve ranking performance.

### Running Tests for Ranking Losses and Metrics

To run unit tests for all ranking losses and RBO/NDCG implementations:
```bash
pytest tests/unit/test_rbo_loss.py
pytest tests/unit/test_ndcg_loss.py
pytest tests/unit/test_ranking_losses.py
```

License: Chemprop is free to use under the MIT License. The Chemprop logo is free to use under CC0 1.0.
References: Please cite the appropriate papers if Chemprop is helpful to your research.

Chemprop was initially described in the papers Analyzing Learned Molecular Representations for Property Prediction for molecules and Machine Learning of Reaction Properties via Learned Representations of the Condensed Graph of Reaction for reactions.
The interpretation functionality (available in v1, but not yet implemented in v2) is based on the paper Multi-Objective Molecule Generation using Interpretable Substructures.
Chemprop now has its own dedicated manuscript that describes and benchmarks it in more detail: Chemprop: A Machine Learning Package for Chemical Property Prediction.
A paper describing and benchmarking the changes in v2.0.0 is forthcoming.

Selected Applications: Chemprop has been successfully used in the following works.

A Deep Learning Approach to Antibiotic Discovery - Cell (2020): Chemprop was used to predict antibiotic activity against E. coli, leading to the discovery of Halicin, a novel antibiotic candidate. Model checkpoints are availabile on Zenodo.
Discovery of a structural class of antibiotics with explainable deep learning - Nature (2023): Identified a structural class of antibiotics selective against methicillin-resistant S. aureus (MRSA) and vancomycin-resistant enterococci using ensembles of Chemprop models, and explained results using Chemprop's interpret method.
ADMET-AI: A machine learning ADMET platform for evaluation of large-scale chemical libraries: Chemprop was trained on 41 absorption, distribution, metabolism, excretion, and toxicity (ADMET) datasets from the Therapeutics Data Commons. The Chemprop models in ADMET-AI are available both as a web server at admet.ai.greenstonebio.com and as a Python package at github.com/swansonk14/admet_ai.
A more extensive list of successful Chemprop applications is given in the 2023 paper
