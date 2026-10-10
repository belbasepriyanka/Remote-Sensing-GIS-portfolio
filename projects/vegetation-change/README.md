# Vegetation Change Detection with Sentinel-2

## Overview

A multispectral remote sensing workflow for comparing vegetation condition between observation periods through NDVI, SAVI, and EVI.

## Technologies

Google Earth Engine, Sentinel-2 Level-2A, JavaScript, multispectral vegetation indices.

## Processing steps

1. Define the study area and two comparable observation periods.
2. Query Sentinel-2 surface-reflectance scenes.
3. Apply scene classification cloud and shadow masking.
4. Generate a median surface-reflectance composite for each period.
5. Calculate NDVI, SAVI, and EVI.
6. Generate a vegetation change image using the difference between the two NDVI composites.

## Vegetation indices

- **NDVI**: `(NIR - RED) / (NIR + RED)`
- **SAVI**: `1.5 × (NIR - RED) / (NIR + RED + 0.5)`
- **EVI**: `2.5 × (NIR - RED) / (NIR + 6 × RED - 7.5 × BLUE + 1)`

## Run

Open [Google Earth Engine](https://code.earthengine.google.com/) and run [change.js](change.js). Update `aoi`, dates, and visualization parameters to match the region and growing seasons being studied.

## Interpretation and QA/QC

Negative NDVI differences can indicate lower greenness during the later period; positive differences can indicate increased greenness. These patterns can also reflect seasonality, soil background, atmospheric contamination, or differences in acquisition conditions. Inspect cloud and no-data coverage, ensure comparable seasons, and validate interpretations with field or reference imagery.

## Data inputs

The source script contains example coordinates and dates. Project-specific boundary files and matched field measurements can be connected to extend this workflow.
