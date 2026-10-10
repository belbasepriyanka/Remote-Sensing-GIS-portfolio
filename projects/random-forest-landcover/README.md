# Random Forest Land-Cover Classification

**Proposed historical window:** 2024 (not yet verified). **Demonstration code published:** 2026.

## Purpose
Train a Sentinel-2 Random Forest land-cover classifier in Google Earth Engine and calculate an **illustrative** holdout confusion matrix. This folder does not state a class count or result until real labels have been provided.

## Inputs you must supply
- A study-area polygon called `aoi`.
- A labeled `ee.FeatureCollection` called `training`, with numeric integer `class` values.
- A documented land-cover class legend and independent or held-out reference samples.
- Permission to publish input data, if sensitive or project-owned.

## Run
1. Open https://code.earthengine.google.com/ and import your AOI and labeled reference features into the Imports panel.
2. Paste `classify.js`. Match the variable names and study dates.
3. Inspect sample counts and verify each class has enough representation in both training and test partitions.
4. Run; see held-out confusion matrix, overall accuracy and Cohen's kappa in the console.
5. Do **not** copy values into the resume until labels and methodology have been reviewed and results rerun.

## Methods
- Predictor bands: B2, B3, B4, B8, B11 and B12 (10–20 m resolution).
- Sentinel-2 L2A median composite, Random Forest with 200 trees and reproducible random split.
- Note: simple random train/test split can leak spatial information. For job applications and research, prefer spatially grouped cross-validation and a truly independent dataset.
- The provided example does not implement SVM comparison, formal cloud masking or segmentation. Add these only when implemented and verified.

## Accuracy reporting
Provide class-count, confusion matrix, per-class precision/recall, overall accuracy, kappa and number of independent validation points, plus a summary of spatial sampling methodology. Do not insert placeholder accuracy as an achievement.

## Pending evidence
Original study-area location, class definitions, sampling files, actual model configuration, reproducible independent accuracy measurements.
