# National Land-Use Classification, Nepal

**Historical employment/project window:** 2018–2022 according to the uploaded resume. **Code example published:** 2026. This project should **not** be labeled "2023" unless continued work during 2023 can be substantiated.

## Project context
The resume describes national land-use classification and suitability mapping across 15+ municipal districts in Nepal, and building geodatabases with domains, subtypes and topology constraints. The original data, authoritative class definitions and ArcGIS geodatabase are not shared here.

## Included code
`check_geometries.py` provides an **independent example** of automated vector validation with GeoPandas. It counts null/invalid/duplicate geometry and reports CRS.

## Run
Install Python 3.10+, create an environment, then:
```bash
python -m pip install -r requirements.txt
python check_geometries.py your_boundaries.geojson
```
Use public or authorized vector features. The script reads any format supported by GeoPandas/Fiona/Pyogrio.

## Recommended real-project methodology
1. Collect approved satellite imagery, administrative boundaries and training/reference polygons.
2. Document the original CRS and reproject into an explicitly selected project CRS.
3. Classify according to a documented land-use legend.
4. Build attribute constraints (coded value domains, subtypes) and topological rules in an ESRI geodatabase.
5. Validate overlaps, gaps, self-intersections, geometry validity and attribute completeness.
6. Compare mapped classes against independent validation samples; produce a confusion matrix and area summaries per district.
7. Archive metadata and processing versions.

## Caveats and evidence still needed
The script does not reproduce enterprise geodatabase subtypes/domains, run land-cover classification or establish any accuracy score. To publish actual historical results, obtain authorized datasets, class legend, dates, study-area boundaries and original maps.
