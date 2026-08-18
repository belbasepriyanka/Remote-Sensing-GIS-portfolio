import numpy as np
def generate_dem(seed=55,n=120):
    rng=np.random.default_rng(seed); x=np.linspace(0,1,n); X,Y=np.meshgrid(x,x); return 120-50*Y+18*np.sin(4*X)*np.cos(3*Y)+rng.normal(0,.4,(n,n))
