"""Simple vegetation change classification."""

import numpy as np

def classify_ndvi_change(ndvi_old, ndvi_new):
    delta = ndvi_new - ndvi_old
    out = np.full(delta.shape, 0, dtype=np.uint8)
    out[delta <= -0.20] = 1
    out[(delta > -0.20) & (delta <= -0.08)] = 2
    out[(delta > -0.08) & (delta < 0.08)] = 3
    out[(delta >= 0.08) & (delta < 0.20)] = 4
    out[delta >= 0.20] = 5
    return out
