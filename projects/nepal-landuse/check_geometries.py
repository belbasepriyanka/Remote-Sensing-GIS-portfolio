"""Example vector QA; not original Nepal project code."""
import sys
import geopandas as gpd

def main(path):
    gdf=gpd.read_file(path)
    print('Features:',len(gdf),'CRS:',gdf.crs)
    print('Null geometries:',int(gdf.geometry.isna().sum()))
    print('Invalid geometries:',int((~gdf.geometry.is_valid).sum()))
    print('Duplicate geometries:',int(gdf.geometry.to_wkb().duplicated().sum()))

if __name__=='__main__':
    if len(sys.argv)!=2: raise SystemExit('Usage: python check_geometries.py INPUT')
    main(sys.argv[1])
