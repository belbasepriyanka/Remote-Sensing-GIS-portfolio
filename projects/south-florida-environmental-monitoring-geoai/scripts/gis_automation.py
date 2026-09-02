"""GIS automation utilities."""

from pathlib import Path
import geopandas as gpd

def reproject_vector(input_path, output_path, epsg=32617):
    gdf = gpd.read_file(input_path)
    gdf = gdf.to_crs(epsg=epsg)
    gdf.to_file(output_path)
    return output_path

def list_geotiffs(folder):
    return sorted(Path(folder).glob("*.tif"))
