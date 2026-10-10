# Random Forest Land-Cover Classification

## Overview

A supervised land-cover mapping workflow that uses Sentinel-2 multispectral predictor bands and labeled reference data to train and assess a Random Forest classifier.

## Technologies

Google Earth Engine, Sentinel-2 Level-2A, JavaScript, Random Forest, classification accuracy assessment.

## Inputs

- `aoi`: a geographic region supplied as an Earth Engine geometry.
- `training`: an Earth Engine FeatureCollection of labeled reference features with integer `class` values.
- A documented land-cover legend corresponding to the class labels.
- Image dates selected for the relevant region and land-cover conditions.

## Workflow

1. Load multispectral bands B2, B3, B4, B8, B11, and B12.
2. Generate an image composite from the selected dates.
3. Extract spectral predictors at labeled training features.
4. Separate samples into training and held-out testing groups using a reproducible random seed.
5. Train a Random Forest classifier with 200 trees.
6. Classify the composite and calculate a held-out confusion matrix, overall accuracy, and Cohen's kappa.

## Run

Open [Google Earth Engine](https://code.earthengine.google.com/). Import `aoi` and labeled `training` features, then run [classify.js](classify.js). The script prints accuracy outputs after the inputs are provided.

## Accuracy and limitations

Random samples drawn from neighboring geographic areas may not provide spatially independent evaluation. For mapping assessments, use independent reference samples or spatially grouped validation. The current script does not apply an SCL cloud mask, implement SVM comparison, or conduct pixel/object segmentation.

No fixed number of land-cover classes or measured accuracy is provided because these depend on the training data and study design.
