// Configure matching event windows. A backscatter change is a candidate signal.
var aoi=ee.Geometry.Rectangle([-80.6,25.3,-80.2,25.7]);
var preStart='2024-07-01',preEnd='2024-08-01';
var postStart='2024-09-01',postEnd='2024-10-01';
var collection=ee.ImageCollection('COPERNICUS/S1_GRD').filterBounds(aoi)
  .filter(ee.Filter.eq('instrumentMode','IW'))
  .filter(ee.Filter.listContains('transmitterReceiverPolarisation','VV'))
  .filter(ee.Filter.eq('orbitProperties_pass','ASCENDING'));
var preSource=collection.filterDate(preStart,preEnd);
var postSource=collection.filterDate(postStart,postEnd);
var common=ee.List(preSource.aggregate_array('relativeOrbitNumber_start')).distinct()
  .filter(ee.Filter.inList('item',postSource.aggregate_array('relativeOrbitNumber_start').distinct()));
print('Common relative orbits (must be non-empty)',common);
// Auto-select one common orbit; verify this choice and incidence-angle coverage.
var orbit=common.sort().get(0);
preSource=preSource.filter(ee.Filter.eq('relativeOrbitNumber_start',orbit));
postSource=postSource.filter(ee.Filter.eq('relativeOrbitNumber_start',orbit));
print('Chosen orbit',orbit);print('Pre/post scene counts',preSource.size(),postSource.size());
var pre=preSource.select('VV').median().clip(aoi);
var post=postSource.select('VV').median().clip(aoi);
var delta=post.subtract(pre).rename('VV_change_dB');
var water=ee.Image('JRC/GSW1_4/GlobalSurfaceWater').select('occurrence').unmask(0).gte(90);
var slope=ee.Terrain.slope(ee.Image('USGS/SRTMGL1_003'));
var candidate=delta.lte(-3).and(water.not()).and(slope.lte(5)).rename('new_water_candidate');
var area=candidate.multiply(ee.Image.pixelArea()).reduceRegion({reducer:ee.Reducer.sum(),
  geometry:aoi,scale:20,maxPixels:1e9});
print('Candidate area m2, not confirmed flood extent',area);
Map.centerObject(aoi,10);Map.addLayer(delta,{min:-5,max:5,palette:['red','white','blue']},'VV difference dB');
Map.addLayer(candidate.selfMask(),{palette:['cyan']},'New-water candidates');
Export.image.toDrive({image:delta.addBands(candidate).float(),description:'sar_change_candidates',
  region:aoi,scale:20,crs:'EPSG:32617',maxPixels:1e10,fileFormat:'GeoTIFF',
  formatOptions:{cloudOptimized:true}});
