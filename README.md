<h1 align="center">Remote Sensing & GIS Portfolio</h1>
<p align="center"><strong>Priyanka Belbase</strong> · Geospatial Data Science · GeoAI · Environmental Modeling</p>
<p align="center">Documented projects, reproducible code, and applied research across satellite, UAV, LiDAR, and field data</p>
<p align="center">
  <a href="https://github.com/belbasepriyanka">GitHub profile</a> ·
  <a href="https://scholar.google.com/citations?user=bkSmlQ8AAAAJ">Google Scholar</a> ·
  <a href="https://www.linkedin.com/in/priyanka-belbase/">LinkedIn</a> ·
  <a href="mailto:belbase.priyanka@gmail.com">Email</a>
</p>

---

I am an Earth System Science Ph.D. candidate at Florida International University. I successfully defended my dissertation in June 2026, with my degree expected in Fall 2026. This **GitHub-native portfolio** connects my remote-sensing research with applied projects in environmental monitoring, precision agriculture, spatial data engineering, and machine learning.

**Explore:** [Featured projects](#featured-projects) · [GIS workflows](#gis--data-engineering) · [Research](#research--publications) · [Methods](#tools--methods) · [Reproducibility](#data--reproducibility)

## Featured projects

### Spotlight: GeoAI Multi-Sensor Crop Stress Intelligence

[![GeoAI crop-stress project](https://raw.githubusercontent.com/belbasepriyanka/sentinel2-vegetation-health-monitoring/main/assets/preview.svg)](https://github.com/belbasepriyanka/sentinel2-vegetation-health-monitoring)

**[Explore the multi-sensor workflow and source code →](https://github.com/belbasepriyanka/sentinel2-vegetation-health-monitoring)** · [Spatially grouped ML demonstration](https://github.com/belbasepriyanka/sentinel2-vegetation-health-monitoring/tree/main/multisensor)

Satellite vegetation indices, simulated UAV canopy information, hyperspectral features, soil moisture, and weather indicators are combined in a reproducible crop-stress demonstration. The standalone Python extension includes spatial cross-validation, held-out stress probabilities, an uncertainty proxy, feature-importance analysis, and GIS-ready scouting priorities. Public data is simulated; a separate Earth Engine workflow handles real Sentinel-2 imagery.

Each project links to an actual repository. Preview images lead to the underlying code and documentation.

| Project | Scope and methods |
|:--|:--|
| [![Dragon fruit project](https://raw.githubusercontent.com/belbasepriyanka/dragon-fruit-remote-sensing-precision-agriculture/main/assets/preview.svg)](https://github.com/belbasepriyanka/dragon-fruit-remote-sensing-precision-agriculture) | **[Dragon Fruit: Remote Sensing & Precision Agriculture](https://github.com/belbasepriyanka/dragon-fruit-remote-sensing-precision-agriculture)**<br>Experimental design, soil and tissue nutrients, spectral indicators, crop phenology, and grouped model validation.<br><sub>Python · Hyperspectral · Sentinel-2 · Random Forest</sub> |
| [![Hyperspectral plant stress](https://raw.githubusercontent.com/belbasepriyanka/hyperspectral-plant-stress-ml/main/assets/preview.svg)](https://github.com/belbasepriyanka/hyperspectral-plant-stress-ml) | **[Hyperspectral Plant Stress ML](https://github.com/belbasepriyanka/hyperspectral-plant-stress-ml)**<br>Preprocessing, spectral feature analysis, PCA, SVM and Random Forest, grouped validation, and stress-screening outputs.<br><sub>Python · PCA · scikit-learn · Spectral analysis</sub> |
| [![Sentinel-2 crop monitoring](https://raw.githubusercontent.com/belbasepriyanka/sentinel2-vegetation-health-monitoring/main/assets/preview.svg)](https://github.com/belbasepriyanka/sentinel2-vegetation-health-monitoring) | **[GeoAI Multi-Sensor Crop Stress Intelligence](https://github.com/belbasepriyanka/sentinel2-vegetation-health-monitoring)**<br>Sentinel-2 processing, simulated multi-sensor fusion, spatially grouped validation, stress probabilities and GIS-ready scouting priorities.<br><sub>Sentinel-2 · Google Earth Engine · Python · GeoAI</sub> |
| [![SAR flood mapping](https://raw.githubusercontent.com/belbasepriyanka/sar-flood-mapping-change-detection/main/assets/preview.svg)](https://github.com/belbasepriyanka/sar-flood-mapping-change-detection) | **[Sentinel-1 SAR Flood Intelligence](https://github.com/belbasepriyanka/sar-flood-mapping-change-detection)**<br>Historical Pakistan 2022 public-data case study, pre/post change detection, flood-screening uncertainty, exposure assessment, and a demo API/dashboard.<br><sub>Sentinel-1 · Earth Engine · FastAPI · Streamlit</sub> |
| [![LiDAR canopy mapping](https://raw.githubusercontent.com/belbasepriyanka/lidar-canopy-terrain-analysis/main/assets/preview.svg)](https://github.com/belbasepriyanka/lidar-canopy-terrain-analysis) | **[LiDAR & NAIP Urban Tree-Canopy Mapping](https://github.com/belbasepriyanka/lidar-canopy-terrain-analysis)**<br>USGS 3DEP point-cloud ingestion, DSM/DTM/CHM, multispectral features, Random Forest, and spatial quality review.<br><sub>LiDAR · NAIP · ArcGIS Pro · Python</sub> |
| [![Land-cover machine learning](https://raw.githubusercontent.com/belbasepriyanka/geospatial-land-cover-ml/main/assets/preview.svg)](https://github.com/belbasepriyanka/geospatial-land-cover-ml) | **[Land-Cover ML, Change Detection & DeepWeeds](https://github.com/belbasepriyanka/geospatial-land-cover-ml)**<br>Random vs spatial holdout assessment, multitemporal raster transitions, and a separate PyTorch weed-image classification extension.<br><sub>scikit-learn · Raster processing · PyTorch</sub> |

## GIS & data engineering

The projects below live **inside this portfolio repository**. They illustrate how I organize spatial workflows from input checks to repeatable deliverables.

| Workflow | What it demonstrates |
|:--|:--|
| **[South Florida Environmental Monitoring with GeoAI](projects/south-florida-environmental-monitoring-geoai/)** | Multi-sensor environmental monitoring, vegetation change, flood-risk screening, satellite time series, and GIS automation. |
| **[Geospatial Raster ETL & QA/QC](projects/geospatial-raster-etl-qaqc/)** | Raster inventory, CRS and resolution checks, NoData screening, metadata validation, and automated quality reports. |
| **[Spatial Validation Benchmark](projects/spatial-validation-benchmark/)** | Random versus spatial-block evaluation, leakage awareness, and documented machine-learning metrics. |
| **[Terrain & Hydrology Modeling](projects/terrain-hydrology-modeling/)** | DEM derivatives, slope, drainage and flow analysis, hydrologic screening, and validation. |
| **[Dragon Fruit Yield & Flowering Forecasting](projects/dragon-fruit-yield-flowering-forecasting/)** | Agricultural forecasting workflow and supporting project documentation. |

## Research & publications

My doctoral work investigates white-, red-, and yellow-fleshed dragon fruit under high-tunnel and open-field conditions in South Florida. Research topics include morphology and phenology, plant and soil nutrition, spectral reflectance across 350–2500 nm, plant disease detection, and long-term production economics.

Selected peer-reviewed publications:

- **2026 · Applied Sciences:** Dragon fruit disease detection using spectral reflectance.
- **2025 · Soil Systems:** Soil/plant nutrient status and spectral reflectance in high-tunnel systems.
- **2025 · Agronomy:** A review of dragon fruit nutrient and pest management.

[View publications and citation records on Google Scholar →](https://scholar.google.com/citations?user=bkSmlQ8AAAAJ)

## Tools & methods

| Focus | Stack |
|:--|:--|
| **GIS** | ArcGIS Pro, ArcGIS Online/Enterprise, ArcPy, QGIS, Google Earth Engine, PostGIS |
| **Data handling** | Python, R, SQL, NumPy, Pandas, GeoPandas, Rasterio, geodatabases |
| **Remote sensing** | Sentinel-1/2, Landsat, NAIP, PlanetScope, UAV, hyperspectral, LiDAR |
| **Modeling** | Random Forest, SVM, PCA, PyTorch, regression, classification, change detection |
| **Validation** | Spatial and grouped holdouts, confusion matrices, F1, IoU, MAE, R², QA/QC |
| **Products** | Technical maps, raster/vector outputs, dashboards, APIs, and written methods |

## Data & reproducibility

**Different projects use different data sources.** Some include real public Earth-observation workflows, while others include synthetic datasets to demonstrate methods without exposing unpublished or restricted research data. Please check each project's README for its specific data provenance, run instructions, limitations, and interpretation of any reported metrics.

GitHub commits indicate when files were published or maintained, not necessarily when the underlying fieldwork took place. Project examples are not claims of operational model performance unless independently validated.

---

<p align="center"><strong>Priyanka Belbase</strong><br />
<a href="https://github.com/belbasepriyanka">GitHub</a> ·
<a href="https://www.linkedin.com/in/priyanka-belbase/">LinkedIn</a> ·
<a href="https://scholar.google.com/citations?user=bkSmlQ8AAAAJ">Google Scholar</a></p>
