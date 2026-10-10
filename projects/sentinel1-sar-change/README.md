# Sentinel-1 SAR Change Detection

## Overview

A radar-based Earth observation workflow for exploring surface changes between pre-event and post-event observation windows using Sentinel-1 VV backscatter.

## Technologies

Google Earth Engine, Sentinel-1 GRD, JavaScript, SAR backscatter analysis, geospatial change detection.

## Processing workflow

1. Configure the area of interest and observation windows.
2. Retrieve Sentinel-1 GRD imagery with IW acquisition mode and VV polarization.
3. Select a consistent orbit pass and build pre-event and post-event median backscatter composites.
4. Calculate the difference in decibels: `post - pre`.
5. Display spatial backscatter variation to identify areas for subsequent investigation.

## Run

Open [Google Earth Engine](https://code.earthengine.google.com/), paste [change.js](change.js), and configure `aoi`, event dates, and available orbit imagery. Run the script and inspect the VV difference layer.

## QA/QC and interpretation

Review incidence angle, image availability, acquisition geometry, seasonal surface moisture, speckle, layover, and radar shadow. For more reliable comparison, filter by relative orbit number where appropriate and use suitable independent reference data.

The Earth Engine Sentinel-1 GRD archive includes standardized preprocessing, including terrain correction. This workflow does not perform additional speckle filtering or separate ESA SNAP processing. A backscatter difference should not be interpreted as a confirmed flood or vegetation-loss classification without supporting validation.
