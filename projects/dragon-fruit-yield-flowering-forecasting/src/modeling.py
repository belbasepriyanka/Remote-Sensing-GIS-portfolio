from __future__ import annotations
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier,RandomForestRegressor
from sklearn.metrics import accuracy_score,f1_score,roc_auc_score,mean_absolute_error,r2_score
from sklearn.model_selection import GroupKFold,cross_val_predict
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder,StandardScaler

NUM=['month','temperature_c','rainfall_mm','gdd','growth_cm','ndvi','ndre','soil_k_mgkg','tissue_n_pct','treatment_t_acre']; CAT=['environment','species']; FEATURES=NUM+CAT

def _prep(num=NUM,cat=CAT): return ColumnTransformer([('num',StandardScaler(),num),('cat',OneHotEncoder(handle_unknown='ignore'),cat)])

def flowering_classifier(df):
    model=Pipeline([('prep',_prep()),('rf',RandomForestClassifier(n_estimators=350,max_depth=10,min_samples_leaf=2,class_weight='balanced',random_state=42,n_jobs=-1))]); cv=GroupKFold(5); X=df[FEATURES]; y=df.flowering; groups=df.plant_id
    pred=cross_val_predict(model,X,y,groups=groups,cv=cv,method='predict'); prob=cross_val_predict(model,X,y,groups=groups,cv=cv,method='predict_proba')[:,1]; metrics={'task':'flowering_probability','model':'RandomForestClassifier','accuracy':accuracy_score(y,pred),'f1':f1_score(y,pred,zero_division=0),'roc_auc':roc_auc_score(y,prob)}
    model.fit(X,y); names=model.named_steps['prep'].get_feature_names_out(); imp=pd.DataFrame({'feature':names,'importance':model.named_steps['rf'].feature_importances_}).sort_values('importance',ascending=False); out=df[['plant_id','month','flowering']].copy(); out['predicted_probability']=prob; out['predicted_class']=pred; return metrics,imp,out

def yield_regression(df):
    agg=df.groupby(['plant_id','environment','species','treatment_t_acre'],as_index=False).agg(temperature_c=('temperature_c','mean'),rainfall_mm=('rainfall_mm','sum'),gdd=('gdd','sum'),growth_cm=('growth_cm','max'),ndvi=('ndvi','mean'),ndre=('ndre','mean'),soil_k_mgkg=('soil_k_mgkg','mean'),tissue_n_pct=('tissue_n_pct','mean'),flower_count=('flower_count','sum'),fruit_count=('fruit_count','sum'),yield_g=('yield_g','sum'))
    num=['temperature_c','rainfall_mm','gdd','growth_cm','ndvi','ndre','soil_k_mgkg','tissue_n_pct','treatment_t_acre','flower_count','fruit_count']; cat=['environment','species']; model=Pipeline([('prep',_prep(num,cat)),('rf',RandomForestRegressor(n_estimators=400,max_depth=10,min_samples_leaf=2,random_state=42,n_jobs=-1))]); cv=GroupKFold(5); X=agg[num+cat]; y=agg.yield_g; groups=agg.plant_id; pred=cross_val_predict(model,X,y,groups=groups,cv=cv); metrics={'task':'season_yield_g','model':'RandomForestRegressor','mae':mean_absolute_error(y,pred),'r2':r2_score(y,pred)}; model.fit(X,y); names=model.named_steps['prep'].get_feature_names_out(); imp=pd.DataFrame({'feature':names,'importance':model.named_steps['rf'].feature_importances_}).sort_values('importance',ascending=False); out=agg[['plant_id','yield_g']].copy(); out['predicted_yield_g']=pred; return metrics,imp,out,agg
