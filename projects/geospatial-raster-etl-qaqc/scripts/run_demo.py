from pathlib import Path
import sys, pandas as pd
ROOT=Path(__file__).resolve().parents[1]; sys.path.insert(0,str(ROOT))
from src.qaqc import qa_report
df=pd.read_csv(ROOT/'data/sample_raster_inventory.csv'); report=qa_report(df); print(report[['tile','qa_status']].to_string(index=False))
