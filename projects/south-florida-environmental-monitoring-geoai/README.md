# South Florida Environmental Change & Flood Risk Monitoring with GeoAI

## Project Goal
Build an end-to-end geospatial workflow to monitor environmental change and flood susceptibility in South Florida using multi-sensor satellite data, vegetation indices, water indices, drought indicators, terrain information, time-series analysis, machine learning, and GIS automation.

This project is designed as a portfolio project for remote sensing, GIS, environmental monitoring, GeoAI, and geospatial data science roles.

## Core Questions
1. Where has land cover changed over time?
2. Which areas show persistent vegetation decline or recovery?
3. Where are temporary and permanent surface-water changes occurring?
4. Which areas experienced flood-like inundation signatures?
5. How do vegetation condition and drought indicators vary through time?
6. Can satellite, terrain, and environmental variables be combined to classify environmental condition or flood susceptibility?
7. Can the entire workflow be automated and exported as GIS-ready products?

## Study Area
South Florida, USA.

Suggested focus areas:
- Miami-Dade County
- Broward County
- Everglades / surrounding wetlands
- Lower Florida Keys

You can replace the study area with any U.S. county, watershed, or disaster-affected region.

## Data Sources
- Sentinel-1 SAR: flood / surface-water mapping
- Sentinel-2 MSI: vegetation, land cover, water, built-up areas
- Landsat 8/9: long-term environmental change
- SRTM or 3DEP DEM: elevation, slope, terrain
- CHIRPS or ERA5-Land: rainfall / climate indicators
- Optional LiDAR: USGS 3DEP point clouds or DEM products
- Optional NLCD: reference land-cover labels

## Main Technologies
- Google Earth Engine
- Python
- GeoPandas
- Rasterio
- Xarray
- Scikit-learn
- Matplotlib
- ArcGIS Pro or QGIS
- Git / GitHub

## Workflow

### 1. Satellite Preprocessing
- Filter Sentinel-2 by date and cloud cover
- Apply cloud masking
- Create seasonal or annual composites
- Process Sentinel-1 VV/VH backscatter
- Normalize data for temporal comparison

### 2. Environmental Indices
Calculate:
- NDVI: vegetation vigor
- NDMI: canopy moisture
- NDWI / MNDWI: surface water
- NBR: disturbance / vegetation stress
- NDBI: built-up areas

### 3. Land-Cover Classification
Train a Random Forest model using spectral bands + indices.

Suggested classes:
- Water
- Wetland
- Forest / woody vegetation
- Grass / agriculture
- Bare soil
- Urban / built-up

Metrics:
- Overall accuracy
- Precision
- Recall
- F1-score
- Confusion matrix

### 4. Vegetation Change
Compare NDVI and NDMI across years.

Outputs:
- Greening
- Stable vegetation
- Moderate decline
- Severe decline

### 5. Flood Mapping
Use Sentinel-1 pre-event and post-event imagery.

Example logic:
- Compare VV/VH backscatter before vs. after event
- Identify strong decreases in backscatter
- Remove permanent water
- Mask steep slopes
- Estimate potentially inundated area

### 6. Drought / Moisture Monitoring
Create monthly or seasonal NDVI and NDMI time series.

Optional:
- Add precipitation anomalies
- Add standardized drought indicators
- Identify periods of vegetation stress

### 7. GeoAI Analysis
Create a feature stack including:
- Sentinel-2 bands
- NDVI
- NDMI
- MNDWI
- NDBI
- Sentinel-1 VV/VH
- Elevation
- Slope
- Distance to water
- Rainfall anomaly

Train:
- Random Forest
- XGBoost (optional)

Potential targets:
- Land-cover class
- Flood susceptibility
- Vegetation stress category

### 8. Satellite Time-Series Analysis
Generate:
- Monthly NDVI trend
- Monthly NDMI trend
- Surface-water frequency
- Seasonal flood extent
- Annual land-cover change

### 9. GIS Automation
Automate:
- Raster clipping
- Projection
- Zonal statistics
- Area calculations
- Map export
- CSV summary generation
- GeoTIFF export

## Portfolio Outputs
Create the following final products:

1. Land-cover classification map
2. Vegetation-change map
3. Flood extent map
4. NDVI time-series figure
5. Surface-water frequency map
6. Environmental change summary table
7. GeoAI model metrics
8. GIS-ready GeoTIFF outputs
9. LinkedIn project summary
10. GitHub repository

## Suggested Repository Structure

```text
South_Florida_Environmental_Monitoring_GeoAI/
│
├── README.md
├── requirements.txt
├── data/
├── notebooks/
│   └── 01_environmental_monitoring_workflow.ipynb
├── scripts/
│   ├── indices.py
│   ├── change_detection.py
│   ├── flood_mapping.py
│   ├── landcover_rf.py
│   └── gis_automation.py
├── outputs/
└── linkedin_post.md
```

## Strong Resume Bullet
Developed an automated multi-sensor environmental monitoring workflow integrating Sentinel-1 SAR, Sentinel-2, Landsat, terrain, vegetation indices, time-series analysis, and Random Forest classification to map land-cover change, vegetation condition, surface-water dynamics, and flood susceptibility.

## Skills Demonstrated
Remote Sensing | GIS | Sentinel-1 | Sentinel-2 | Landsat | SAR | Flood Mapping | Land-Cover Classification | Vegetation Monitoring | Drought Monitoring | Time-Series Analysis | GeoAI | Machine Learning | Python | Google Earth Engine | ArcGIS Pro | QGIS | GIS Automation