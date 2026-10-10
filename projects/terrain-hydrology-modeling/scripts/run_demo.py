from pathlib import Path
import sys,json
import numpy as np
import matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT))
from src.data_generation import generate_dem
from src.terrain import slope_degrees,d8_accumulation
(ROOT/'outputs').mkdir(exist_ok=True);(ROOT/'figures').mkdir(exist_ok=True)
dem=generate_dem();slope=slope_degrees(dem,10);acc,receiver=d8_accumulation(dem,10)
np.savez_compressed(ROOT/'outputs/terrain_arrays.npz',dem=dem,slope=slope,accumulation=acc,receiver=receiver)
summary={'data_type':'synthetic','cell_size_m':10,'mean_slope_deg':float(slope.mean()),
 'maximum_contributing_cells':int(acc.max()),'sink_cells':int((receiver<0).sum()),
 'method':'D8 steepest downslope; no pit filling or flat routing'}
(ROOT/'outputs/summary.json').write_text(json.dumps(summary,indent=2))
fig,axes=plt.subplots(1,3,figsize=(11,4))
for ax,values,title in zip(axes,[dem,slope,np.log1p(acc)],['Synthetic DEM (m)','Slope (degrees)','log(1 + D8 contributing cells)']):
 im=ax.imshow(values);ax.set_title(title);ax.axis('off');fig.colorbar(im,ax=ax,shrink=.7)
fig.tight_layout();fig.savefig(ROOT/'figures/terrain_quicklook.svg');plt.close(fig)
print(json.dumps(summary,indent=2))
