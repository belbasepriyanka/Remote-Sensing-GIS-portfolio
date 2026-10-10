# Automated Sentinel-2 Time-Series Pipeline

**Portfolio implementation published:** 2026. **Historical research window:** 2023–2025 (dates require confirmation from records).

## Purpose
Reproducible Google Earth Engine (GEE) example for Sentinel-2 surface reflectance time series, cloud/shadow masking, annual composites and vegetation-index export. The workflow reflects the types of tasks described in the resume, but is newly published reference code, **not a copy of the original historical processing code**.

## Input and study area
- Source: `COPERNICUS/S2_SR_HARMONIZED` (Sentinel-2 L2A surface reflectance).
- Demo area: bounding rectangle near southern Florida in `sentinel2.js`. This is an **example**, not a verified project boundary.
- Dates: example year 2024; replace with documented acquisition windows.
- The claimed 500+ scenes spans Sentinel-2, Planet and NAIP; this script processes Sentinel-2 **only**. Do not use it as evidence of reproducing the 500+ scene total.

## Steps
1. Open https://code.earthengine.google.com/ with Earth Engine access and paste `sentinel2.js`.
2. Edit `aoi`, start and end dates, and cloud filtering threshold.
3. Run the script and check the printed scene count.
4. View the NDVI layer and inspect masked pixels.
5. Start the export task in the Tasks tab, retrieve the GeoTIFF from Google Drive.
6. On a Linux machine with GDAL, use `gdal_translate -of COG input.tif output_cog.tif`, then `gdalinfo output_cog.tif` to inspect output metadata.

## Processing details
- Masks SCL classes: 3 (cloud shadow), 8/9/10 (cloud/cirrus), 11 (snow/ice).
- Applies the Sentinel-2 reflectance scale factor of 0.0001.
- Uses per-band median composite and `(B8-B4)/(B8+B4)` NDVI; exports at 10 m.
- Median mosaics across a year are not equivalent to single-date scenes: phenology and seasonal sampling should be considered.

## Quality assurance checklist
- Verify scene-count/date range and acquired tile IDs.
- Review cloud and shadow remnants, edge artifacts, nodata coverage, outliers and visible seams.
- Record CRS/resolution and AOI boundaries; check coregistration against reference basemaps.
- Inspect reflectance range and NDVI histogram; compare with field plots if available.
- Record GDAL version, export scale and processing settings.

## Not yet verified
Exact historical study region, 500+ scene inventory and per-sensor breakdown, original dates, ground reference observations, performance timing and cloud-free pixel coverage. Planet and NAIP ingestion/reprojection are not implemented here.
