from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[1]; sys.path.insert(0,str(ROOT))
from src.data_generation import generate_spatial
from src.benchmark import spatial_cv
print(spatial_cv(generate_spatial()))
