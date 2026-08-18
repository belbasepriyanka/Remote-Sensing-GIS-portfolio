def qa_report(df, expected_crs='EPSG:32617', expected_resolution=10, max_nodata=5):
    out=df.copy(); out['crs_ok']=out.crs.eq(expected_crs); out['resolution_ok']=out.resolution_m.eq(expected_resolution); out['qa_status']=((out.crs_ok)&(out.resolution_ok)&(out.nodata_pct<max_nodata)).map({True:'PASS',False:'REVIEW'}); return out
