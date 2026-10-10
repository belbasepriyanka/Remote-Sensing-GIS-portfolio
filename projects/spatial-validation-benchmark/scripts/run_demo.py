from pathlib import Path
import sys,json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split,GroupShuffleSplit
from sklearn.metrics import accuracy_score,f1_score
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT))
from src.data_generation import generate_spatial
for d in ['data','results','figures']:(ROOT/d).mkdir(exist_ok=True)
df=generate_spatial();df.to_csv(ROOT/'data/sample_spatial_classification.csv',index=False)
X=df[['f1','f2']];y=df.label;groups=(df.x//25).astype(int)*4+(df.y//25).astype(int)
idx=np.arange(len(df));random=train_test_split(idx,test_size=.25,stratify=y,random_state=42)
spatial=next(GroupShuffleSplit(n_splits=1,test_size=.25,random_state=42).split(X,y,groups))
rows=[]
for name,(train,test) in [('random',random),('spatial',spatial)]:
 model=RandomForestClassifier(n_estimators=250,random_state=42).fit(X.iloc[train],y.iloc[train]);pred=model.predict(X.iloc[test])
 rows.append({'validation':name,'accuracy':accuracy_score(y.iloc[test],pred),'f1':f1_score(y.iloc[test],pred)})
 result=df.iloc[test].copy();result['prediction']=pred;result.to_csv(ROOT/f'results/{name}_predictions.csv',index=False)
 if name=='spatial':
  assert not(set(groups.iloc[train])&set(groups.iloc[test]))
  (ROOT/'results/spatial_groups.json').write_text(json.dumps({'train':sorted(map(int,set(groups.iloc[train]))),'test':sorted(map(int,set(groups.iloc[test])))},indent=2))
metrics=pd.DataFrame(rows);metrics.to_csv(ROOT/'results/benchmark_metrics.csv',index=False)
fig,ax=plt.subplots();ax.bar(metrics.validation,metrics.accuracy);ax.set(ylim=(0,1),ylabel='Accuracy',title='Synthetic random vs spatial holdout');fig.tight_layout();fig.savefig(ROOT/'figures/accuracy_comparison.svg');plt.close(fig)
fig,ax=plt.subplots();ax.scatter(df.x,df.y,c=groups,s=8,cmap='tab20');ax.set(title='Synthetic spatial blocks',xlabel='Fictional x',ylabel='Fictional y');fig.tight_layout();fig.savefig(ROOT/'figures/spatial_blocks.svg');plt.close(fig)
print(metrics.to_string(index=False))
