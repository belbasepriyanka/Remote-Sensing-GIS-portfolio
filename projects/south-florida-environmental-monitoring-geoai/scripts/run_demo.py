"""Exercise environmental monitoring utilities on fictional, aligned raster arrays."""
from pathlib import Path
import json
import numpy as np
import matplotlib.pyplot as plt
import rasterio
from rasterio.transform import from_origin
from indices import ndvi,ndmi,mndwi
from change_detection import classify_ndvi_change
from flood_mapping import candidate_flood_mask,apply_terrain_mask
ROOT=Path(__file__).resolve().parents[1];out=ROOT/'outputs';out.mkdir(exist_ok=True)
rng=np.random.default_rng(42);n=80
red=rng.uniform(.08,.22,(n,n));nir=rng.uniform(.3,.6,(n,n));swir=rng.uniform(.15,.35,(n,n));green=rng.uniform(.08,.2,(n,n))
old=ndvi(nir,red);new=old.copy();new[20:45,25:55]-=.25;new=np.clip(new,-1,1)
change=classify_ndvi_change(old,new)
pre=rng.normal(-9,1,(n,n));post=pre+rng.normal(0,.6,(n,n));post[45:65,10:40]-=5
slope=rng.uniform(0,8,(n,n));candidate=apply_terrain_mask(candidate_flood_mask(pre,post),slope)
profile=dict(driver='GTiff',height=n,width=n,count=4,dtype='float32',crs='EPSG:32617',transform=from_origin(500000,2800000,20,20),nodata=-9999)
with rasterio.open(out/'synthetic_environmental_layers.tif','w',**profile) as dst:
 dst.write(np.stack([new,ndmi(nir,swir),mndwi(green,swir),candidate.astype(float)]).astype('float32'))
 for i,name in enumerate(['NDVI','NDMI','MNDWI','SAR_candidate'],1):dst.set_band_description(i,name)
summary={'data_type':'synthetic','seed':42,'coordinates':'fictional UTM grid',
 'decline_pixels':int(((change==1)|(change==2)).sum()),'sar_candidate_pixels':int(candidate.sum()),
 'sar_candidate_area_m2':int(candidate.sum())*400,'scope':'methods demonstration, not South Florida event results'}
(out/'summary.json').write_text(json.dumps(summary,indent=2))
fig,axes=plt.subplots(1,3,figsize=(11,4))
for ax,arr,title in zip(axes,[new,new-old,candidate],['Synthetic NDVI','NDVI change','SAR water candidate']):
 im=ax.imshow(arr);ax.set_title(title);ax.axis('off');fig.colorbar(im,ax=ax,shrink=.7)
fig.tight_layout();fig.savefig(out/'quicklook.svg');plt.close(fig)
print(json.dumps(summary,indent=2))
