// Import `aoi` and `training`: reference features with integer class and spatial group_id.
// Use non-overlapping geographic groups, not one ID per pixel.
var bands = ['B2','B3','B4','B8','B11','B12'];
function prepare(image) {
  var s = image.select('SCL');
  return image.select(bands).multiply(0.0001).updateMask(s.gte(4).and(s.lte(7)));
}
var source = ee.ImageCollection('COPERNICUS/S2_SR_HARMONIZED').filterBounds(aoi)
  .filterDate('2024-01-01','2025-01-01').filter(ee.Filter.lt('CLOUDY_PIXEL_PERCENTAGE',60));
var image = source.map(prepare).median().clip(aoi);
// One random split per spatial group, assigned before pixels are sampled.
var ids = training.aggregate_array('group_id').distinct();
var groups = ee.FeatureCollection(ids.map(function(id) {return ee.Feature(null,{group_id:id});}))
  .randomColumn('split',42,'uniform',['group_id']);
var joined = ee.Join.saveFirst('group_record').apply(training,groups,
  ee.Filter.equals({leftField:'group_id',rightField:'group_id'}));
var assigned = ee.FeatureCollection(joined).map(function(f) {
  return f.set('split',ee.Feature(f.get('group_record')).get('split'));
});
function sample(features) {
  return image.sampleRegions({collection:features,properties:['class','group_id'],scale:20,
    geometries:true,tileScale:4});
}
var train = sample(assigned.filter(ee.Filter.lt('split',0.75)));
var test = sample(assigned.filter(ee.Filter.gte('split',0.75)));
print('Scene count',source.size());
print('Training class counts',train.aggregate_histogram('class'));
print('Held-out class counts',test.aggregate_histogram('class'));
print('Training spatial groups',train.aggregate_array('group_id').distinct());
print('Held-out spatial groups',test.aggregate_array('group_id').distinct());
// Inspect counts: stop and revise references if any class is absent or a set is empty.
var model = ee.Classifier.smileRandomForest({numberOfTrees:200,seed:42})
  .train({features:train,classProperty:'class',inputProperties:bands});
var predicted = test.classify(model);
var order = training.aggregate_array('class').distinct().sort();
var cm = predicted.errorMatrix('class','classification',order);
print('Class order',order);print('Spatial holdout confusion matrix',cm);
print('Overall accuracy',cm.accuracy());print('Kappa',cm.kappa());
print('Producer accuracy / recall',cm.producersAccuracy());
print('Consumer accuracy / precision',cm.consumersAccuracy());
var classified = image.classify(model).toInt16();
Map.centerObject(aoi,10);Map.addLayer(classified.randomVisualizer(),{},'Land cover');
Export.table.toDrive({collection:predicted,description:'landcover_held_out_predictions',fileFormat:'CSV'});
Export.image.toDrive({image:classified,description:'landcover_spatial_holdout_model',region:aoi,
  scale:20,maxPixels:1e10,fileFormat:'GeoTIFF',formatOptions:{cloudOptimized:true}});
