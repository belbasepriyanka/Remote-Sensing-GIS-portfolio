# Data and Validation Checklist

This checklist records the supporting information needed to reproduce geospatial analyses and assess their reliability.

| Project | Study boundary | Observation dates | Image inventory | Reference data | Classification legend | Accuracy outputs |
| --- | --- | --- | --- | --- | --- | --- |
| Sentinel-2 time series | Supply AOI | Supply intervals | Sentinel-2 image IDs | Optional field observations | Not applicable | Cloud coverage, valid pixels |
| Nepal land-use | Supply approved district boundaries | Supply image dates | Approved satellite imagery | Reference land-use observations | Supply original legend | Independent accuracy assessment |
| Vegetation change | Supply AOI | Match comparable seasons | Sentinel-2 image IDs | Field measurements or high-resolution imagery | Not applicable | Index-change diagnostics |
| Random Forest classification | Supply AOI | Supply image dates | Sentinel-2 image IDs | Labeled training and validation polygons | Supply classes | Confusion matrix, overall accuracy, kappa |
| Sentinel-1 change | Supply AOI | Identify event windows | Sentinel-1 image IDs and orbit metadata | Independent event or optical reference | Not applicable | Validation against reference changes |

## Processing metadata

- Data source, collection identifier and acquisition filters
- Coordinate reference system and spatial resolution
- Cloud, shadow, and no-data handling
- Preprocessing and feature-generation settings
- Training, test, and independent validation design, where relevant
- Software environment and script version
- Output format and interpretation limitations

Record measured metrics from executed workflows and retain relevant input references for reproducibility.
