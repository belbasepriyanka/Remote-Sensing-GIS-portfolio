import numpy as np
def slope_degrees(dem):
    gy,gx=np.gradient(dem); return np.degrees(np.arctan(np.hypot(gx,gy)))
def flow_accumulation_proxy(dem):
    s=slope_degrees(dem); return np.maximum(0,(dem.max()-dem))*np.exp(-s/25)
