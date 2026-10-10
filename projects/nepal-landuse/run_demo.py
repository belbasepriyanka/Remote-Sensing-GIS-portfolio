"""Generate a small fictional geometry QA fixture, then audit it."""
from pathlib import Path
import json
import geopandas as gpd
from shapely.geometry import box, Polygon
from check_geometries import validate
ROOT = Path(__file__).resolve().parent
for d in ['data','outputs']: (ROOT/d).mkdir(exist_ok=True)
a=box(500000,3000000,500100,3000100)
frame=gpd.GeoDataFrame({'ward_id':['1','2','3','4',None,'6'],
 'landuse':['forest','cropland','forest','unknown','water','urban']},
 geometry=[a,box(500080,3000000,500180,3000100),a,
 Polygon([(500200,3000000),(500300,3000100),(500200,3000100),(500300,3000000),(500200,3000000)]),
 None,box(500300,3000000,500350,3000050)],crs='EPSG:32645')
boundary=gpd.GeoDataFrame(geometry=[box(500000,3000000,500400,3000200)],crs=frame.crs)
frame.to_crs(4326).to_file(ROOT/'data/synthetic_landuse.geojson',driver='GeoJSON')
boundary.to_crs(4326).to_file(ROOT/'data/synthetic_boundary.geojson',driver='GeoJSON')
summary,issues=validate(frame,['ward_id','landuse'],'landuse',['forest','cropland','water','urban'],boundary,'EPSG:32645')
(ROOT/'outputs/qa_summary.json').write_text(json.dumps(summary,indent=2))
issues.to_csv(ROOT/'outputs/feature_issues.csv',index=False)
print(json.dumps(summary,indent=2))
