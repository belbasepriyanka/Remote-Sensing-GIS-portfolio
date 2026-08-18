from src.data_generation import generate_spatial
from src.benchmark import spatial_cv
def test_cv():
    m=spatial_cv(generate_spatial(n=500)); assert 0<=m['accuracy']<=1
