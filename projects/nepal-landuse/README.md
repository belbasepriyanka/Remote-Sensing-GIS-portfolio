# National Land-Use Classification, Nepal

## Project overview

Geospatial land-use mapping and suitability analysis supporting district-level planning in Nepal. Project activities encompassed satellite image interpretation, standardizing spatial data, classification, and geodatabase quality management across more than 15 municipal districts.

## Technical focus

- Land-use and land-cover mapping from satellite imagery
- Spatial data standardization and coordinate reference systems
- Geodatabase design with field domains, subtypes, and topology rules
- Feature geometry validation and spatial data quality checks
- Land suitability and planning applications

## Included utility

[check_geometries.py](check_geometries.py) is a GeoPandas-based vector QA utility. It reports feature count, dataset CRS, and counts of null, invalid, and duplicate geometries. It can be used with supported vector formats such as GeoJSON and GeoPackage.

## Run

Install Python 3.10 or later, then:

```bash
python -m pip install -r requirements.txt
python check_geometries.py input.geojson
```

## Quality control

For an end-to-end land-use mapping workflow, review polygon validity, overlapping features, data completeness, boundary alignment, class attributes, and consistency across districts. Independently labeled samples are required to quantify classification accuracy.

## Project materials

Original administrative datasets, satellite scenes, mapped outputs, and enterprise geodatabase files are not distributed in this folder. The Python utility illustrates vector QA and does not implement the complete historical land-use classification process.
