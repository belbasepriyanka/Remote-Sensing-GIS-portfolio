# Geospatial Raster ETL and QA/QC

Inspect raster inputs before analysis, then build a consistent mosaic and clipped analysis product. The local demo writes actual GeoTIFFs and reads their metadata with Rasterio.

## Quick start

```bash
python -m pip install -r requirements.txt
python scripts/run_demo.py
python -m pytest -q
```

The demonstration generates two adjacent synthetic raster tiles with declared CRS, resolution and NoData. It inventories their metadata, checks CRS/resolution/type consistency, mosaics the tiles, clips an AOI and writes a QA report and quicklook.

## Inspect your own rasters

```bash
python scripts/inspect_rasters.py /path/to/rasters --output outputs/raster_inventory.csv
```

The inspector scans `.tif` files using raster windows and reports dimensions, band count, CRS, resolution, data type, first-band masked/non-finite coverage and valid-value range. It does not alter inputs or infer a missing CRS.

## Outputs

| File | Purpose |
|---|---|
| `outputs/input_qaqc.csv` | Input metadata and value coverage |
| `outputs/mosaic.tif` | Merged raster |
| `outputs/analysis_ready_clip.tif` | Clipped analysis raster |
| `outputs/qa_report.json` | Checks and output statistics |
| `outputs/quicklook.png` | Computed preview |

![Computed synthetic raster preview](outputs/quicklook.png)

## Scope

Synthetic tile values demonstrate processing, not a measured satellite product. CRS/resolution/dtype checks are necessary but do not replace pixel-grid alignment, band definitions, calibration and acquisition-date review. The real-file inspector summarizes band 1; additional bands need their own value checks.
