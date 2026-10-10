# Sentinel-1 SAR Change Detection

**Proposed historical research window:** 2025 (requires verification). **Reference implementation:** 2026.

## Goal
Demonstrate pre/post-event Sentinel-1 SAR VV backscatter comparison in Google Earth Engine. This can support flood or vegetation-change exploration, but **difference values alone do not prove flooding, forest loss or any physical cause**.

## Input and caveats
- `COPERNICUS/S1_GRD`: calibrated, terrain-corrected GRD backscatter in dB in Earth Engine.
- Same polarization (VV), instrument mode (IW) and orbit pass (ascending) are selected.
- Sample AOI and 2024 windows in the code are placeholders, not a verified study/event.
- Different relative orbit numbers can cause geometric/backscatter differences; filter them when validating a real event.

## Run
1. Open https://code.earthengine.google.com/, paste `change.js`, and change AOI/date windows.
2. Confirm both collections have observations and comparable acquisition geometry.
3. Inspect VV before/after layers and the difference `post - pre` (dB).
4. Use independent optical/high-resolution imagery, flood footprints or field data to validate detected change.

## Interpretation and QA
- Inspect no-data, layover/shadow, speckle, seasonal moisture and angle-of-incidence differences.
- Use suitable smoothing and threshold selection only after specifying a physical change-detection method.
- Earth Engine's `COPERNICUS/S1_GRD` already includes terrain correction; this script does not separately run SNAP nor add custom speckle filtering.
- A demonstrated RGB/polarimetric flood map would require a separate, properly evaluated method.

## Outstanding information
Original study region, flood/change event date, relative-orbit selection, reference imagery and independent test labels, thresholds, confusion matrix and accuracy. No validated detection result is claimed.
