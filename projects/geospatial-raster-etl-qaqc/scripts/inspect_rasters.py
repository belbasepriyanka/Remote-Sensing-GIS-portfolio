"""Inventory real GeoTIFF metadata and masked-data coverage, without changing inputs."""
from pathlib import Path
import argparse
import numpy as np
import pandas as pd
import rasterio

def inspect(path):
    with rasterio.open(path) as src:
        valid=0;total=0;minimum=np.inf;maximum=-np.inf
        for _,window in src.block_windows(1):
            data=src.read(1,window=window,masked=True)
            values=data.compressed();values=values[np.isfinite(values)]
            total+=data.size;valid+=len(values)
            if len(values):minimum=min(minimum,float(values.min()));maximum=max(maximum,float(values.max()))
        return {'file':str(path),'crs':str(src.crs) if src.crs else None,
          'bands':src.count,'width':src.width,'height':src.height,'dtype':src.dtypes[0],
          'resolution_x':src.res[0],'resolution_y':src.res[1],
          'nodata_pct_band1':100*(1-valid/total),'valid_min_band1':minimum if valid else None,
          'valid_max_band1':maximum if valid else None,'status':'PASS' if src.crs and valid else 'REVIEW'}
if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('folder',type=Path)
    p.add_argument('--output',type=Path,default=Path('outputs/raster_inventory.csv'));args=p.parse_args()
    paths=sorted(args.folder.rglob('*.tif'))
    if not paths:raise SystemExit('No .tif files found')
    args.output.parent.mkdir(parents=True,exist_ok=True)
    pd.DataFrame([inspect(path) for path in paths]).to_csv(args.output,index=False)
    print(args.output)
