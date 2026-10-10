# Automated Sentinel-2 Time-Series Pipeline

Monthly vegetation and moisture monitoring from Sentinel-2 surface reflectance. The workflow combines pixel-level quality masking, monthly compositing, observation counts, vegetation indices and cloud-optimized raster exports.

## Workflow

1. Configure the area, start/end dates, scale and output CRS.
2. Query harmonized Sentinel-2 Level-2A imagery and filter scene cloudiness.
3. Retain SCL classes 4–7 and scale spectral bands to reflectance.
4. Calculate NDVI, NDRE and NDMI for each observation.
5. Produce monthly median indices and valid-observation counts.
6. Summarize index means, scene counts and valid coverage by month.
7. Export a CSV time series and a multiband cloud-optimized GeoTIFF.

Empty months retain masked index bands and zero observation counts rather than inventing observations. Output is at 20 m to match red-edge and SWIR predictors; this does not make every input band natively 20 m.

## Run

Paste [sentinel2.js](sentinel2.js) into the [Earth Engine Code Editor](https://code.earthengine.google.com/). Set the intended AOI, dates and CRS, then run. Inspect printed scene counts and monthly coverage. Start exports from the Tasks panel.

The default rectangle and dates are configurable example inputs. No completed imagery export or processing-speed result is claimed here. Earth Engine execution requires an authorized project and an interactive run.

## Outputs and review

- `sentinel2_monthly_indices.csv`: NDVI, NDRE, NDMI, scene count and coverage fraction.
- `sentinel2_monthly_stack.tif`: monthly index bands and observation counts.
- An interactive time-series chart and NDVI map.

Check coverage, seasonal comparability and remaining cloud/shadow artifacts before interpreting trends. Regional means can change when the valid-pixel footprint changes.

## References

[Sentinel-2 dataset and scaling](https://developers.google.com/earth-engine/datasets/catalog/COPERNICUS_S2_SR_HARMONIZED). For local raster QA and handoff, see [Raster ETL and QA/QC](../geospatial-raster-etl-qaqc/).
