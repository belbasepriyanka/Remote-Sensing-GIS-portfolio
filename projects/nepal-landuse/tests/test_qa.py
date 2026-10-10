import geopandas as gpd
from shapely.geometry import box, Polygon
from check_geometries import validate
import pytest

def test_distinguishes_null_invalid_duplicate_and_attribute():
 p=box(0,0,10,10)
 bad=Polygon([(0,0),(2,2),(0,2),(2,0),(0,0)])
 df=gpd.GeoDataFrame({'class':['forest','forest',None,'bad']},geometry=[p,p,None,bad],crs=32645)
 summary,issues=validate(df,['class'],'class',['forest'])
 counts=summary['issue_counts']
 assert counts['NULL_GEOMETRY']==1 and counts['INVALID_GEOMETRY']==1
 assert counts['DUPLICATE_GEOMETRY']==1 and counts['MISSING_ATTRIBUTE']==1

def test_overlap_gap_and_edge_touch():
 df=gpd.GeoDataFrame(geometry=[box(0,0,10,10),box(10,0,20,10)],crs=32645)
 boundary=gpd.GeoDataFrame(geometry=[box(0,0,30,10)],crs=32645)
 summary,_=validate(df,boundary=boundary,area_crs='EPSG:32645')
 assert summary['topology']['overlaps']==[]
 assert summary['topology']['gap_area_m2']==100
 assert summary['status']=='REVIEW'

def test_rejects_angular_area_crs():
 df=gpd.GeoDataFrame(geometry=[box(85,27,85.1,27.1)],crs=4326)
 with pytest.raises(ValueError,match='projected'):validate(df,area_crs='EPSG:4326')
