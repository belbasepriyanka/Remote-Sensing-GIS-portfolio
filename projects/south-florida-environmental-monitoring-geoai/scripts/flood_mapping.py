"""Starter logic for Sentinel-1 flood-change mapping."""

import numpy as np

def db_difference(pre_db, post_db):
    """Negative values indicate lower post-event backscatter."""
    return post_db - pre_db

def candidate_flood_mask(pre_db, post_db, threshold_db=-3.0):
    diff = db_difference(pre_db, post_db)
    return diff <= threshold_db

def apply_terrain_mask(mask, slope_deg, max_slope=5.0):
    return mask & (slope_deg <= max_slope)
