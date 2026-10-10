# Geospatial Remote Sensing Projects

A collection of geospatial workflows covering satellite time-series processing, land-use classification, vegetation monitoring, supervised machine learning, and SAR-based change analysis.

Each project folder contains implementation notes, executable example scripts, input requirements, processing methods, and quality-control guidance. The workflows are intended to be adapted to documented study areas and datasets.

## Projects

| Project | Workflow |
| --- | --- |
| [Automated Sentinel-2 Time-Series Pipeline](sentinel2-timeseries/) | Sentinel-2 surface reflectance, cloud and shadow masking, spectral indices, GeoTIFF export, and GDAL COG conversion |
| [National Land-Use Classification, Nepal](nepal-landuse/) | Land-use mapping project context, spatial data quality checks, and geodatabase validation methods |
| [Vegetation Change Detection](vegetation-change/) | NDVI, SAVI, EVI and seasonal comparison using Sentinel-2 imagery |
| [Random Forest Land-Cover Classification](random-forest-landcover/) | Sentinel-2 predictor bands, supervised classification, holdout testing, and accuracy assessment |
| [Sentinel-1 SAR Change Detection](sentinel1-sar-change/) | Pre/post-event VV backscatter comparison and SAR interpretation checks |

## Getting started

1. Open a project folder and read its README for required data, software, parameters, and limitations.
2. Google Earth Engine examples can be run in the [Earth Engine Code Editor](https://code.earthengine.google.com/), after configuring an appropriate region and dates.
3. The Python geometry-validation example uses GeoPandas and includes its own dependency file.
4. Use independent reference data when reporting classification, vegetation-change, or SAR change results.

## Data and reproducibility

These folders contain documented example implementations of methods used in geospatial analysis. Original project datasets, exact regions, acquisition inventories, and independent reference observations are not distributed with the code. Scripts and examples were uploaded to this repository in 2026; this does not establish when individual research activities originally took place.

Quantitative results are reported only after the relevant data, evaluation protocol, and measurements are available. See the [validation checklist](VALIDATION_CHECKLIST.md) for information required to reproduce and assess outputs.

## Usage notes

Project-specific study-area boundaries, observation dates, class definitions, and dataset permissions should be checked before running or publishing analyses. No unverified accuracy or processing-performance values are asserted here.
