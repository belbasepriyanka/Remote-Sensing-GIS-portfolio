import sys
from pathlib import Path
import numpy as np
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from indices import normalized_difference
from change_detection import classify_ndvi_change
from flood_mapping import candidate_flood_mask,apply_terrain_mask

def test_invalid_pixels_remain_unclassified():
 before=np.array([[.5,np.nan]]);after=np.array([[.2,.8]])
 assert classify_ndvi_change(before,after).tolist()==[[1,0]]

def test_water_candidate_terrain_filter():
 pre=np.array([-8.,-8.]);post=np.array([-12.,-9.])
 assert apply_terrain_mask(candidate_flood_mask(pre,post),np.array([8.,1.])).tolist()==[False,False]

def test_safe_ratio_zero_denominator():
 assert np.isnan(normalized_difference(np.array([0.]),np.array([0.]))[0])
