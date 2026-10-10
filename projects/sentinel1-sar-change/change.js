// Example only; adjust event, orbit, polarization, AOI and validation data.
var aoi=ee.Geometry.Rectangle([-80.6,25.3,-80.2,25.7]);
function window(start,end){return ee.ImageCollection('COPERNICUS/S1_GRD').filterBounds(aoi).filterDate(start,end).filter(ee.Filter.eq('instrumentMode','IW')).filter(ee.Filter.listContains('transmitterReceiverPolarisation','VV')).filter(ee.Filter.eq('orbitProperties_pass','ASCENDING')).select('VV').median().clip(aoi);}
var pre=window('2024-07-01','2024-08-01');var post=window('2024-09-01','2024-10-01');var delta=post.subtract(pre).rename('VV_change_dB');
Map.centerObject(aoi,10);Map.addLayer(delta,{min:-5,max:5,palette:['red','white','blue']},'VV difference (dB)');
