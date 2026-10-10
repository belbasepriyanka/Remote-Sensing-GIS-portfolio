// Compare matched observation seasons; configure dates and AOI.
var aoi=ee.Geometry.Rectangle([-80.6,25.3,-80.2,25.7]);
function clean(im){var s=im.select('SCL');return im.updateMask(s.gte(4).and(s.lte(7))).divide(10000);}
function composite(start,end){return ee.ImageCollection('COPERNICUS/S2_SR_HARMONIZED').filterBounds(aoi).filterDate(start,end).filter(ee.Filter.lt('CLOUDY_PIXEL_PERCENTAGE',60)).map(clean).median().clip(aoi);}
function indices(im){var ndvi=im.normalizedDifference(['B8','B4']).rename('NDVI');var savi=im.expression('1.5*(n-r)/(n+r+0.5)',{n:im.select('B8'),r:im.select('B4')}).rename('SAVI');var evi=im.expression('2.5*(n-r)/(n+6*r-7.5*b+1)',{n:im.select('B8'),r:im.select('B4'),b:im.select('B2')}).rename('EVI');return ee.Image.cat([ndvi,savi,evi]);}
var earlier=indices(composite('2023-01-01','2024-01-01'));var later=indices(composite('2024-01-01','2025-01-01'));var diff=later.select('NDVI').subtract(earlier.select('NDVI')).rename('NDVI_change');
Map.centerObject(aoi,10);Map.addLayer(diff,{min:-0.4,max:0.4,palette:['red','white','green']},'NDVI change');

var changes=later.subtract(earlier).rename(['delta_NDVI','delta_SAVI','delta_EVI']);
Export.image.toDrive({image:changes.float(),description:'vegetation_index_change',region:aoi,
  scale:10,crs:'EPSG:32617',maxPixels:1e10,fileFormat:'GeoTIFF',formatOptions:{cloudOptimized:true}});
print('Mean index changes',changes.reduceRegion({reducer:ee.Reducer.mean(),geometry:aoi,
  scale:20,maxPixels:1e9}));
