import numpy as np
import pandas as pd
def generate_spatial(seed=44,n=1500):
    rng=np.random.default_rng(seed); x=rng.uniform(0,100,n); y=rng.uniform(0,100,n); signal=np.sin(x/12)+np.cos(y/15)+rng.normal(0,.35,n); label=(signal>0).astype(int); f1=signal+rng.normal(0,.2,n); f2=np.sin(x/20)+rng.normal(0,.2,n); return pd.DataFrame({'x':x,'y':y,'f1':f1,'f2':f2,'label':label})
