// Configure AOI, dates and output CRS before running in Earth Engine.
var config = {
  aoi: ee.Geometry.Rectangle([-80.6, 25.3, -80.2, 25.7]),
  start: '2024-01-01', end: '2025-01-01', crs: 'EPSG:32617', scale: 20
};
var names = ['B2', 'B3', 'B4', 'B5', 'B8', 'B11'];
function prepare(image) {
  var scl = image.select('SCL');
  var valid = scl.gte(4).and(scl.lte(7));
  var sr = image.select(names).multiply(0.0001).updateMask(valid);
  function nd(a, b, name) {
    return sr.expression('(a-b)/(a+b)', {a: sr.select(a), b: sr.select(b)}).rename(name);
  }
  return sr.addBands([nd('B8','B4','NDVI'), nd('B8','B5','NDRE'), nd('B8','B11','NDMI')])
    .copyProperties(image, ['system:time_start']);
}
var images = ee.ImageCollection('COPERNICUS/S2_SR_HARMONIZED')
  .filterBounds(config.aoi).filterDate(config.start, config.end)
  .filter(ee.Filter.lt('CLOUDY_PIXEL_PERCENTAGE', 60)).map(prepare);
var start = ee.Date(config.start);
var months = ee.List.sequence(0, ee.Date(config.end).difference(start, 'month').ceil().subtract(1));
var indexNames = ['NDVI','NDRE','NDMI'];
// Typed, fully masked fallback preserves bands for empty months.
var empty = ee.Image.constant([0,0,0]).rename(indexNames).updateMask(ee.Image(0));
var monthly = ee.ImageCollection.fromImages(months.map(function(m) {
  var date = start.advance(m, 'month');
  var stop = ee.Date(ee.Number(date.advance(1, 'month').millis()).min(ee.Date(config.end).millis()));
  var subset = images.filterDate(date, stop).select(indexNames);
  var median = ee.Image(ee.Algorithms.If(subset.size().gt(0), subset.median(), empty));
  var count = ee.Image(ee.Algorithms.If(subset.size().gt(0), subset.select('NDVI').count(),
    ee.Image(0).rename('NDVI'))).rename('valid_observations');
  return median.addBands(count).clip(config.aoi).set({
    'system:time_start':date.millis(), 'month':date.format('YYYY-MM'), 'scene_count':subset.size()
  });
}));
var rows = ee.FeatureCollection(monthly.toList(monthly.size()).map(function(obj) {
  var image = ee.Image(obj);
  var means = image.select(indexNames).reduceRegion({reducer:ee.Reducer.mean(),
    geometry:config.aoi,scale:config.scale,crs:config.crs,maxPixels:1e9});
  var coverage = image.select('valid_observations').unmask(0).gt(0).reduceRegion({
    reducer:ee.Reducer.mean(),geometry:config.aoi,scale:config.scale,crs:config.crs,maxPixels:1e9});
  return ee.Feature(null, means).set({month:image.get('month'),scene_count:image.get('scene_count'),
    valid_coverage_fraction:coverage.get('valid_observations')});
}));
print('Scenes', images.size()); print('Monthly QA and index means', rows);
print(ui.Chart.feature.byFeature(rows,'month',indexNames));
Map.centerObject(config.aoi,10);
Map.addLayer(monthly.select('NDVI').median(),{min:-0.2,max:0.9,palette:['brown','yellow','green']},'NDVI');
Export.table.toDrive({collection:rows,description:'sentinel2_monthly_indices',fileFormat:'CSV'});
Export.image.toDrive({image:monthly.toBands().float(),description:'sentinel2_monthly_stack',
  region:config.aoi,scale:config.scale,crs:config.crs,maxPixels:1e10,fileFormat:'GeoTIFF',
  formatOptions:{cloudOptimized:true}});
