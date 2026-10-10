// Demonstration implementation added in 2026; adapt AOI and dates.
var aoi = ee.Geometry.Rectangle([-80.6,25.3,-80.2,25.7]);
var mask = function(im) { var scl=im.select('SCL'); var good=scl.neq(3).and(scl.neq(8)).and(scl.neq(9)).and(scl.neq(10)).and(scl.neq(11)); return im.updateMask(good).divide(10000).copyProperties(im,['system:time_start']); };
var images=ee.ImageCollection('COPERNICUS/S2_SR_HARMONIZED').filterBounds(aoi).filterDate('2024-01-01','2025-01-01').filter(ee.Filter.lt('CLOUDY_PIXEL_PERCENTAGE',60)).map(mask);
var composite=images.median().clip(aoi); var ndvi=composite.normalizedDifference(['B8','B4']).rename('NDVI');
print('Scene count',images.size()); Map.centerObject(aoi,10); Map.addLayer(ndvi,{min:-0.2,max:0.9,palette:['brown','yellow','green']},'NDVI');
Export.image.toDrive({image:ndvi,description:'s2_ndvi_example',region:aoi,scale:10,maxPixels:1e10});
