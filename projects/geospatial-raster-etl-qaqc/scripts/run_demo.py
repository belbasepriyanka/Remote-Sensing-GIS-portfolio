"""Generate, inspect, mosaic and clip two synthetic raster tiles."""
from pathlib import Path
import runpy
runpy.run_path(str(Path(__file__).resolve().parents[1]/'src/demo.py'),run_name='__main__')
