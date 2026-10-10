"""Terrain derivatives and downslope D8 routing. Flats and pits remain sinks."""
import numpy as np

def slope_degrees(dem, cell_size_m=1.0):
    if cell_size_m <= 0: raise ValueError('Cell size must be positive')
    gy,gx=np.gradient(np.asarray(dem,dtype=float),cell_size_m)
    return np.degrees(np.arctan(np.hypot(gx,gy)))

def d8_accumulation(dem, cell_size_m=1.0):
    z=np.asarray(dem,dtype=float)
    if z.ndim!=2 or not np.isfinite(z).all():raise ValueError('Provide a finite 2D DEM')
    if cell_size_m<=0:raise ValueError('Cell size must be positive')
    nr,nc=z.shape
    receiver=np.full(z.shape,-1,dtype=int)
    for r in range(nr):
      for c in range(nc):
        best=0.0
        for dr,dc in [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]:
          rr,cc=r+dr,c+dc
          if 0<=rr<nr and 0<=cc<nc:
            drop=(z[r,c]-z[rr,cc])/(cell_size_m*np.hypot(dr,dc))
            if drop>best:best=drop;receiver[r,c]=rr*nc+cc
    acc=np.ones(z.size,dtype=float)
    for i in np.argsort(z.ravel())[::-1]:
      target=receiver.ravel()[i]
      if target>=0:acc[target]+=acc[i]
    return acc.reshape(z.shape),receiver

def flow_accumulation_proxy(dem):
    s=slope_degrees(dem)
    return np.maximum(0,(dem.max()-dem))*np.exp(-s/25)
