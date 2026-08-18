from __future__ import annotations
import numpy as np
import pandas as pd

SPECIES=['Red','White','Yellow']; ENVIRONMENTS=['High tunnel','Open field']; TREATMENTS=[0,5,10,20]; OBS_MONTHS=[1,2,3,4,5,6,7,8]

def generate_demo(seed:int=42)->pd.DataFrame:
    """Generate synthetic repeated-measures dragon-fruit phenology/yield data."""
    rng=np.random.default_rng(seed); rows=[]; plant_num=0
    for env in ENVIRONMENTS:
      for species in SPECIES:
       for treatment in TREATMENTS:
        for rep in range(1,4):
         plant_num+=1; plant_id=f'DF{plant_num:03d}'; species_eff={'Red':.65,'White':.35,'Yellow':-.25}[species]; env_eff=.18 if env=='High tunnel' else 0; treatment_eff={0:-.15,5:.20,10:.35,20:.10}[treatment]; vigor=1+species_eff+env_eff+treatment_eff+rng.normal(0,.12)
         for month in OBS_MONTHS:
          temp=22.5+.9*month+(.7 if env=='High tunnel' else 0)+rng.normal(0,.8); rain=max(0,105+35*np.sin(month/1.7)+rng.normal(0,18)); gdd=max(0,(temp-10)*30); growth=35+11*month+18*vigor+rng.normal(0,6)
          ndvi=np.clip(.42+.035*month+.06*vigor-.00035*max(rain-150,0)+rng.normal(0,.025),.2,.92); ndre=np.clip(.18+.024*month+.05*vigor+rng.normal(0,.018),.08,.60); soil_k=max(25,105+5*treatment-.045*month*rain+rng.normal(0,12)); tissue_n=np.clip(1.4+.05*month+.12*vigor+rng.normal(0,.08),.8,3)
          logit=-5.2+.9*month+.9*species_eff+.55*treatment_eff+.5*env_eff+1.6*(ndre-.25); flower_prob=1/(1+np.exp(-logit)); flowers=int(rng.poisson(max(.02,flower_prob*3.2))); set_prob=np.clip(.16+.08*species_eff+.045*treatment_eff+.08*ndvi-.0006*max(rain-155,0),.03,.55); fruits=int(rng.binomial(flowers,set_prob)) if flowers else 0; yield_g=max(0,fruits*(285+30*species_eff+18*treatment_eff+rng.normal(0,28)))
          rows.append({'plant_id':plant_id,'replicate':rep,'environment':env,'species':species,'treatment_t_acre':treatment,'month':month,'temperature_c':round(temp,3),'rainfall_mm':round(rain,3),'gdd':round(gdd,3),'growth_cm':round(growth,3),'ndvi':round(float(ndvi),4),'ndre':round(float(ndre),4),'soil_k_mgkg':round(soil_k,3),'tissue_n_pct':round(float(tissue_n),3),'flower_count':flowers,'flowering':int(flowers>0),'fruit_count':fruits,'fruit_set':int(fruits>0),'yield_g':round(yield_g,2)})
    return pd.DataFrame(rows)
