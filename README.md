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

This feature helps researchers better evaluate model performance in scenarios where the relative ordering of predictions is more important than absolute values.
Documentation and Usage
Documentation can be found here.
There are tutorial notebooks in the examples/ directory.
Chemprop recently underwent a ground-up rewrite and new major release (v2.0.0). A helpful transition guide from Chemprop v1 to v2 can be found here. This includes a side-by-side comparison of CLI argument options, a list of which arguments will be implemented in later versions of v2, and a list of changes to default hyperparameters.
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
A more extensive list of successful Chemprop applications is given in our 2023 paper

Version 1.x
For users who have not yet made the switch to Chemprop v2.0, please reference the following resources.
v1 Documentation

Documentation of Chemprop v1 is available here. Note that the content of this site is several versions behind the final v1 release (v1.7.1) and does not cover the full scope of features available in chemprop v1.
The v1 README is the best source for documentation on more recently-added features.
Please also see descriptions of all the possible command line arguments in the v1 args.py file.

v1 Tutorials and Examples

Benchmark scripts - scripts from our 2023 paper, providing examples of many features using Chemprop v1.6.1
ACS Fall 2023 Workshop - presentation, interactive demo, exercises on Google Colab with solution key
Google Colab notebook - several examples, intended to be run in Google Colab rather than as a Jupyter notebook on your local machine
nanoHUB tool - a notebook of examples similar to the Colab notebook above, doesn't require any installation

YouTube video - lecture accompanying nanoHUB tool


These slides provide a Chemprop tutorial and highlight additions as of April 28th, 2020

v1 Known Issues
We have discontinued support for v1 since v2 has been released, but we still appreciate v1 bug reports and will tag them as v1-wontfix so the community can find them easily.
