# Sentinel-2 Vegetation Change Detection

**Proposed historical research window:** 2024 (unverified); **demonstration implementation:** 2026.

## Goal
Compare growing-season vegetation condition using Sentinel-2 surface reflectance and three commonly used indices: NDVI, SAVI and EVI. The `change.js` script is a reproducible **example**, not a verified result from an original field trial.

## Input
- `COPERNICUS/S2_SR_HARMONIZED` surface-reflectance imagery, with SCL cloud/shadow masking.
- A demonstration polygon in south Florida, not a verified study boundary.
- Two annual intervals, 2023 and 2024, used as placeholders.

## Run
1. Copy `change.js` into https://code.earthengine.google.com/.
2. Replace the AOI and both dates with actual study location and matched growing-season windows.
3. Run to produce a displayed map of later NDVI minus earlier NDVI.
4. Check the distribution and map sign: negative values indicate a decrease in estimated greenness; changes can also result from seasonality, cloud or soil.
5. Export layers via `Export.image.toDrive` if needed.

## Methods
- NDVI: `(NIR - RED)/(NIR + RED)`.
- SAVI: `1.5 * (NIR - RED)/(NIR + RED + 0.5)`.
- EVI: `2.5 * (NIR - RED)/(NIR + 6*RED - 7.5*BLUE + 1)`.
- The script creates median composites and a difference image, not a causal attribution model.

## QA and validation
Use acquisition-date consistency, cloud/no-data diagnostics, CRS/scale checks, selected high-resolution reference imagery and independent field sample plots. Avoid confusing spectral change with verified land-use transitions.

## Information required to validate resume claims
Study-area polygon, observation dates, cloud coverage acceptance threshold, field plot locations and dates, validation methodology, sample count, effect/accuracy values. No numerical results are claimed in this repository.
