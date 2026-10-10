# National Land-Use Mapping and GIS Quality Assurance | Nepal

Land-use planning depends on consistent boundaries, class attributes and reliable spatial databases. This project draws on experience supporting municipal land-use mapping and geodatabase development across more than 15 municipal districts in Nepal.

The public implementation focuses on vector quality assurance. It checks geometry, attributes and polygon coverage and writes reports that can guide a review in ArcGIS Pro or QGIS.

## Implemented checks

| Check | Output |
|---|---|
| Null, empty and invalid geometry | Feature row and validity explanation |
| Duplicate geometry | Canonical geometry comparison and matching row |
| Required attributes | Missing fields, null values and blank strings |
| Allowed land-use classes | Values outside a supplied class legend |
| Polygon overlap | Intersecting row pairs and overlap area |
| Coverage gaps and boundary overflow | Area relative to a supplied coverage boundary |
| CRS and spatial units | Source CRS and explicitly selected projected area CRS |

## Quick start

From this folder, with Python 3.11 or 3.12:

```bash
python -m pip install -r requirements.txt
python run_demo.py
python -m pytest -q
```

The demo intentionally includes invalid geometry, duplicates, missing attributes and overlapping polygons. Its [QA summary](outputs/qa_summary.json) and [feature issue table](outputs/feature_issues.csv) show the errors found. The committed GeoJSON files are fictional test fixtures, not Nepal municipal boundaries.

Audit your own data:

```bash
python check_geometries.py input.geojson --required-fields ward_id landuse --class-field landuse --allowed-classes forest cropland water urban --boundary coverage_boundary.geojson --area-crs EPSG:32645 --out-dir outputs/custom
```

Choose the projected CRS and legend for your actual location and data. EPSG:32645 is an example, not a universal CRS for Nepal. The script leaves source features unchanged. Boundary gaps are calculated only when a coverage boundary is supplied; invalid polygons are reported and excluded from area calculations.

## Land-use classification

For imagery classification, use the [Sentinel-2 grouped Random Forest workflow](../random-forest-landcover/) or the [Python raster classifier](https://github.com/belbasepriyanka/geospatial-land-cover-ml). Those workflows require labeled reference samples and produce validation outputs.

## Data availability

Original municipal imagery, class legends and geodatabases are not distributed. The QA utility does not create ArcGIS domains or subtypes, perform suitability analysis, or reproduce an original municipal classification. It provides repeatable checks for authorized vector datasets.
