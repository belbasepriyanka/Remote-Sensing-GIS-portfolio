# GIS and Remote Sensing Portfolio Projects

This directory includes **five reference implementations**, added in 2026 to document methods relevant to the ResourceWise GIS Analyst role:

| Folder | Main method | Historical period status |
| --- | --- | --- |
| [sentinel2-timeseries](sentinel2-timeseries) | Sentinel-2 surface reflectance, cloud masking, NDVI, GDAL COG export | 2023–2025 research period: verify |
| [nepal-landuse](nepal-landuse) | Land-use geodata QA example | National project 2018–2022 per resume |
| [vegetation-change](vegetation-change) | Sentinel-2 NDVI/SAVI/EVI change mapping | 2024: verify |
| [random-forest-landcover](random-forest-landcover) | GEE Random Forest with held-out accuracy | 2024: verify |
| [sentinel1-sar-change](sentinel1-sar-change) | Sentinel-1 VV pre/post backscatter difference | 2025: verify |

**Transparency:** The original research projects and these GitHub example implementations are not necessarily identical. These code examples are published in 2026 and have not been executed against original datasets in this repository. They should not be described as historical commits or proven processing outcomes.

## How to run
- For `.js` scripts, use the [Google Earth Engine Code Editor](https://code.earthengine.google.com/), with Earth Engine access, and edit the AOI/inputs/dates.
- For the Nepal GeoPandas Python example, see its README and requirements.
- Do not publish private field points or licensed commercial imagery without permission.

## Verification needed before putting outcomes on a resume
- Actual area/boundary and location, temporal period, source imagery inventory
- Data sources and independent reference dataset
- Number/names of land-cover classes
- Validation design, confusion matrix, accuracy, kappa, and uncertainty
- Original processing logs, dates, supporting maps and authorization to share

See [VALIDATION_CHECKLIST.md](VALIDATION_CHECKLIST.md) for a fill-in template.
