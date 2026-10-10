# Vegetation Change Detection with Sentinel-2

Compare surface-reflectance composites from two observation periods using NDVI, SAVI and EVI. Outputs support screening for lower or higher vegetation greenness.

## Processing

[change.js](change.js) queries harmonized Sentinel-2 imagery, retains SCL classes 4–7, scales reflectance, computes three indices, and exports `delta_NDVI`, `delta_SAVI` and `delta_EVI` in a GeoTIFF. It also prints regional mean changes and displays the NDVI difference.

| Index | Formula |
|---|---|
| NDVI | `(NIR - red) / (NIR + red)` |
| SAVI | `1.5 * (NIR - red) / (NIR + red + 0.5)` |
| EVI | `2.5 * (NIR - red) / (NIR + 6*red - 7.5*blue + 1)` |

## Run and review

Paste the script into [Earth Engine](https://code.earthengine.google.com/). Configure the AOI, dates and output CRS. Use comparable growing seasons and inspect coverage in both composites. Start the export from Tasks.

Negative differences indicate lower index values, not a confirmed cause of vegetation loss. Weather, seasonality, background soil and cloud contamination can change the signal. Independently labeled reference observations are needed to validate a disturbance interpretation.

The script uses configurable example dates and coordinates. Local array-based tests and a computed change quicklook are available in the [environmental monitoring workflow](../south-florida-environmental-monitoring-geoai/). Multi-class land-cover transitions are implemented in [the raster change module](https://github.com/belbasepriyanka/geospatial-land-cover-ml/tree/main/multitemporal_change_detection).
