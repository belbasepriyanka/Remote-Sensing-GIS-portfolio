# Automated Sentinel-2 Time-Series Pipeline

## Overview

A Google Earth Engine workflow for processing multispectral Sentinel-2 observations, generating cloud-filtered surface reflectance composites, estimating vegetation conditions, and exporting geospatial products.

## Technologies

Google Earth Engine, Sentinel-2 Level-2A, JavaScript, GDAL, GeoTIFF, Linux.

## Workflow

1. Select the area of interest and observation period.
2. Retrieve the Sentinel-2 surface-reflectance image collection.
3. Filter scene-level cloudiness and mask cloudy, shadowed, and snow-covered pixels using scene classification (SCL).
4. Apply the surface-reflectance scaling factor and generate a median composite.
5. Calculate NDVI from red and near-infrared bands.
6. Export the NDVI raster and optionally convert it to Cloud Optimized GeoTIFF (COG).

## Run the code

Open [Google Earth Engine Code Editor](https://code.earthengine.google.com/), paste [sentinel2.js](sentinel2.js), adjust `aoi` and dates, and execute. Run the export task in Earth Engine's Tasks panel.

To convert an exported GeoTIFF to a COG using GDAL:

```bash
gdal_translate -of COG input.tif output_cog.tif
gdalinfo output_cog.tif
```

## QA/QC

Check scene selection, acquisition dates, remaining clouds and shadows, masked pixels, projection, pixel size, spectral ranges, and composite artifacts. Document all processing settings and inspect exported raster metadata.

## Scope

The included script covers the Sentinel-2 workflow. Planet and NAIP imagery, multi-sensor harmonization, batch mosaicking, and independently measured processing-performance statistics are outside this script's current scope. Replace the demonstration area with the intended project boundary.
