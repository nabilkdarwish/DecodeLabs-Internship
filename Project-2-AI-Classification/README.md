# AI Model Comparison Dashboard

A Python command-line project that trains and compares four classifiers on the Iris dataset. It was developed as Project 2 during the DecodeLabs Industrial Training Program.

## What it does

- Trains K-Nearest Neighbors, Logistic Regression, Decision Tree, and Random Forest classifiers.
- Presents holdout accuracy in a Rich terminal dashboard.
- Displays the highest-scoring model and a terminal accuracy chart.

## Evaluation approach

The project uses scikit-learn's built-in Iris dataset (150 samples, four numeric features, and three species classes). All models use the same stratified 75/25 train/test split with a fixed random seed, so repeated runs produce the same comparison. Standard scaling is fitted inside a pipeline for KNN and Logistic Regression; the tree-based models use the original feature values.

The dashboard reports accuracy on one holdout split. This is a small educational comparison, not a production benchmark; cross-validation and a larger, representative dataset would be needed for stronger conclusions.

## Requirements

- Python 3.9 or newer
- Packages listed in requirements.txt

## Run locally

~~~bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python main.py
~~~

## Project files

- main.py — command-line entry point
- model.py — reproducible split, model pipelines, and accuracy evaluation
- ui.py — Rich comparison table and best-model panel
- charts.py — terminal accuracy visualization

## Author

Nabil Khaled Darwish
