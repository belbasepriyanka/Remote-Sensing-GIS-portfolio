# Sentinel-2 Random Forest Land-Cover Classification

Supervised land-cover mapping with a cloud-masked Sentinel-2 composite, spatial group holdout evaluation and GIS-ready exports.

## Inputs

Import `aoi` and `training` into Earth Engine. Reference features require:

| Field | Meaning |
|---|---|
| `class` | Integer class code from a documented legend |
| `group_id` | Spatially disjoint site or block identifier |

Use multiple groups containing representative examples of each class. Adjacent samples, repeated polygons and duplicated pixels should not be treated as independent observations. Holdout groups should represent the geographic transfer you want to evaluate.

## Implemented workflow

The script masks cloud/shadow/snow and scales B2, B3, B4, B8, B11 and B12 reflectance. It assigns a reproducible split to spatial groups before sampling pixels, trains a 200-tree Random Forest, and reports the held-out confusion matrix, overall accuracy, kappa, producer accuracy and consumer accuracy.

It exports held-out predictions as CSV and a classified GeoTIFF. The exported map uses the evaluated training model; held-out reference groups are not used to train that map.

## Run

Open [classify.js](classify.js) in the [Earth Engine Code Editor](https://code.earthengine.google.com/). Import the two inputs, set dates and run. Review scene count, group lists and class counts first. Revise references if either set is empty or a class is absent. Start exports in the Tasks panel.

For an offline runnable example with generated rasters, [the Python raster classification project](https://github.com/belbasepriyanka/geospatial-land-cover-ml#raster-classification-and-change-detection) includes inputs, maps, confusion matrices and automated tests.

## Validation

No fixed accuracy or class count is claimed without supplied references. A spatial group split reduces shared-location leakage but does not ensure independence across seasons or sensors. Area estimation and independent accuracy assessment need their own sampling design.

## References

[Sentinel-2](https://developers.google.com/earth-engine/datasets/catalog/COPERNICUS_S2_SR_HARMONIZED) · [Reproducible group randomization](https://developers.google.com/earth-engine/apidocs/ee-featurecollection-randomcolumn)
