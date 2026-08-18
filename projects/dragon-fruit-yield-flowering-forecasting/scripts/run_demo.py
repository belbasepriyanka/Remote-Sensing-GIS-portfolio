from pathlib import Path
import sys,pandas as pd,matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parents[1]; sys.path.insert(0,str(ROOT))
from src.data_generation import generate_demo
from src.modeling import flowering_classifier,yield_regression
for d in [ROOT/'data',ROOT/'figures',ROOT/'results']: d.mkdir(exist_ok=True)
df=generate_demo(); df.to_csv(ROOT/'data'/'sample_dragon_fruit_yield_demo.csv',index=False)
fm,fi,fp=flowering_classifier(df); ym,yi,yp,agg=yield_regression(df); pd.DataFrame([fm,ym]).to_csv(ROOT/'results'/'model_metrics.csv',index=False); fi.to_csv(ROOT/'results'/'flowering_feature_importance.csv',index=False); yi.to_csv(ROOT/'results'/'yield_feature_importance.csv',index=False); fp.to_csv(ROOT/'results'/'flowering_predictions.csv',index=False); yp.to_csv(ROOT/'results'/'yield_predictions.csv',index=False)
p=df.groupby(['month','species'],as_index=False)[['flower_count']].mean(); fig,ax=plt.subplots(figsize=(8,5));
for sp,g in p.groupby('species'): ax.plot(g.month,g.flower_count,marker='o',label=sp)
ax.set(xlabel='Month',ylabel='Mean flower count',title='Synthetic flowering dynamics by species'); ax.legend(); fig.tight_layout(); fig.savefig(ROOT/'figures'/'flowering_time_series.svg'); plt.close(fig)
print(pd.DataFrame([fm,ym]).to_string(index=False))
