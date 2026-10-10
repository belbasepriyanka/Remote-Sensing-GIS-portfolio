// Demonstration code, 2026. Import your labeled FeatureCollection as `training` and AOI as `aoi`.
var bands=['B2','B3','B4','B8','B11','B12'];
var im=ee.ImageCollection('COPERNICUS/S2_SR_HARMONIZED').filterBounds(aoi).filterDate('2024-01-01','2025-01-01').filter(ee.Filter.lt('CLOUDY_PIXEL_PERCENTAGE',20)).median().select(bands).divide(10000);
var samples=im.sampleRegions({collection:training,properties:['class'],scale:20,geometries:true}).randomColumn('split',42);
var train=samples.filter(ee.Filter.lt('split',0.7));var test=samples.filter(ee.Filter.gte('split',0.7));
var model=ee.Classifier.smileRandomForest(200).train({features:train,classProperty:'class',inputProperties:bands});
var predicted=test.classify(model);var cm=predicted.errorMatrix('class','classification');print('Held-out confusion matrix',cm);print('Overall accuracy',cm.accuracy());print('Kappa',cm.kappa());
Map.addLayer(im.classify(model).randomVisualizer(),{},'Land cover');
