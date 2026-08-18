import numpy as np
from src.terrain import slope_degrees
def test_flat():
    assert np.allclose(slope_degrees(np.ones((4,4))),0)
