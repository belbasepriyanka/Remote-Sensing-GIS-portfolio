from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[1]; sys.path.insert(0,str(ROOT))
from src.data_generation import generate_dem
from src.terrain import slope_degrees, flow_accumulation_proxy
dem=generate_dem(); print('Mean slope',slope_degrees(dem).mean()); print('Max flow proxy',flow_accumulation_proxy(dem).max())
