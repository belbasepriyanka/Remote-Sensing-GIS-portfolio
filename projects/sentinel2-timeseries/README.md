# Automated Sentinel-2 Time-Series Pipeline

**Historical work:** 2023–2025 (verify exact dates). **Code publication:** 2026.

Reproducible example for Sentinel-2 cloud masking, seasonal NDVI composites and export in Google Earth Engine. The previously described 500+ scenes across Sentinel-2, Planet and NAIP are a resume claim, not a benchmark reproduced by this example. Planet and NAIP require separate ingestion workflows.

## Run
Paste `sentinel2.js` into the Earth Engine Code Editor. Change the AOI and dates. Export GeoTIFF to Drive. For Linux/GDAL conversion to COG, use `gdal_translate -of COG input.tif output_cog.tif`.

## Validation
Inspect image count, cloud coverage, projection, nodata and reflectance scaling. No production QA results are claimed here.
