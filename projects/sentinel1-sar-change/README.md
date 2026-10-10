# Sentinel-1 SAR Change Detection

Compare pre-event and post-event VV backscatter while controlling acquisition geometry. This workflow produces a radar-change layer and screened new-water candidates for further review.

## Method

[change.js](change.js) filters Sentinel-1 GRD to IW mode, VV polarization and an ascending pass. It identifies relative orbits present in both date windows and selects one common orbit. Median VV composites are differenced in decibels: `post - pre`.

New-water screening uses a configurable negative-change threshold, excludes high-occurrence JRC permanent water and removes steep SRTM terrain. The script reports candidate area and exports the change and candidate layers.

## Run

Open the script in [Earth Engine](https://code.earthengine.google.com/). Set the AOI and event windows. Inspect common relative orbits and scene counts before interpreting the map. If no common orbit exists, revise the dates or pass. Set the output CRS for your location and start the export in Tasks.

## Interpretation

Radar change is sensitive to surface moisture, vegetation, acquisition geometry, layover, shadow and speckle. The threshold is illustrative and the candidate mask is not a validated flood product. No event accuracy is reported without independent reference labels.

The [full flood-analysis repository](https://github.com/belbasepriyanka/sar-flood-mapping-change-detection) adds Python validation, threshold sensitivity, exposure screening, a dashboard and a demo API. Its Pakistan public-data script is an Earth Engine pathway, separate from locally generated demo outputs.
