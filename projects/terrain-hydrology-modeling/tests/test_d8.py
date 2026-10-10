import numpy as np
from src.terrain import d8_accumulation,slope_degrees

def test_plane_routes_to_low_edge_and_conserves_contributing_area():
 z=np.array([[4,3,2],[3,2,1],[2,1,0]],float)
 acc,rec=d8_accumulation(z)
 assert acc[-1,-1]==9
 assert acc[rec<0].sum()==z.size

def test_slope_uses_physical_cell_spacing():
 z=np.tile(np.arange(4,dtype=float),(4,1))*10
 assert np.allclose(slope_degrees(z,10),45)
