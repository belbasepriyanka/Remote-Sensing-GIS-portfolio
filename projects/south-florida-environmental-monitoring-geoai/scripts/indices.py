"""Common remote-sensing indices for raster / numpy workflows."""

import numpy as np

def normalized_difference(a, b):
    denom = a + b
    out = np.full(np.broadcast(a,b).shape, np.nan, dtype=float)
    return np.divide(a-b, denom, out=out, where=np.abs(denom)>=1e-10)

def ndvi(nir, red):
    return normalized_difference(nir, red)

def ndmi(nir, swir1):
    return normalized_difference(nir, swir1)

def ndwi(green, nir):
    return normalized_difference(green, nir)

def mndwi(green, swir1):
    return normalized_difference(green, swir1)

def nbr(nir, swir2):
    return normalized_difference(nir, swir2)

def ndbi(swir1, nir):
    return normalized_difference(swir1, nir)
