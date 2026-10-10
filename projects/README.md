# Geospatial Remote Sensing Projects

Python, GIS, and Google Earth Engine workflows for Earth observation data processing, vegetation monitoring, land-use analysis, supervised classification, and SAR change detection.

## Project collection

| Project | Focus | Technologies |
| --- | --- | --- |
| [Automated Sentinel-2 Time-Series Pipeline](sentinel2-timeseries/) | Cloud masking, surface reflectance, NDVI composites, image exports | Sentinel-2, Google Earth Engine, GDAL |
| [National Land-Use Classification, Nepal](nepal-landuse/) | Land-use mapping and vector data quality checks | ArcGIS, QGIS, GeoPandas, geodatabases |
| [Vegetation Change Detection](vegetation-change/) | Seasonal NDVI, SAVI and EVI comparisons | Sentinel-2, Google Earth Engine |
| [Random Forest Land-Cover Classification](random-forest-landcover/) | Supervised classification and accuracy assessment | Sentinel-2, Google Earth Engine, Random Forest |
| [Sentinel-1 SAR Change Detection](sentinel1-sar-change/) | Pre/post-event radar backscatter analysis | Sentinel-1, Google Earth Engine |

## Reproducibility

Each folder includes a technical README with the workflow, input requirements, execution instructions, QA considerations, and limitations. Earth Engine scripts use configurable geographic areas and observation dates. Projects requiring labeled samples or reference datasets must be supplied with those inputs before evaluation.

## Getting started

1. Select a project and read its README.
2. Configure the study area, acquisition dates, and reference inputs.
3. Run the script using the specified software.
4. Review the output and validation checks before interpreting results.

The available code demonstrates processing methods; original restricted datasets and unverified numerical results are not included. The [data and validation checklist](VALIDATION_CHECKLIST.md) provides the metadata needed for further reproducibility.
