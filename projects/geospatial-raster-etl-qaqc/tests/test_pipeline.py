import pandas as pd
from src.qaqc import qa_report
def test_qaqc():
    df=pd.DataFrame({'crs':['EPSG:32617'],'resolution_m':[10],'nodata_pct':[1]}); assert qa_report(df).qa_status.iloc[0]=='PASS'
