# Workflow Verification

Local checks completed using Python 3.12. Public Earth Engine scripts were reviewed and checked for JavaScript syntax; satellite execution/export requires an authorized Earth Engine run and is outside these local checks.

| Project | Command | Result |
|---|---|---|
| geospatial-raster-etl-qaqc | `python -m pytest -q` | 1 passed in 0.36s |
| terrain-hydrology-modeling | `python -m pytest -q` | 3 passed in 0.06s |
| south-florida-environmental-monitoring-geoai | `python -m pytest -q` | 3 passed in 0.06s |
| nepal-landuse | `python -m pytest -q` | 3 passed in 0.42s |
| dragon-fruit-yield-flowering-forecasting | `python -m pytest -q` | 2 passed in 9.77s |
| spatial-validation-benchmark | `python -m pytest -q` | 1 passed in 2.49s |

The documented demo entry points were run and generated their output files. Synthetic metrics check the controlled examples and do not establish real-site accuracy. DeepWeeds checks cover dataset loading and model shape, not full dataset training.

## Checked dependencies

- numpy: 2.3.5
- pandas: 2.2.3
- matplotlib: 3.10.8
- scikit-learn: 1.8.0
- geopandas: 1.2.0
- rasterio: 1.5.2
- shapely: 2.2.0
- pytest: 9.1.1
- laspy: 2.7.0
- lazrs: 0.8.2
- fastapi: 0.143.0
- torch: 2.14.1+cpu
- torchvision: 0.29.1+cpu

Generated plots are computed from the documented demo inputs. GitHub Actions results may differ until the remote workflow has run.
