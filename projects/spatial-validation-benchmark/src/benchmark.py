from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GroupKFold, cross_val_predict
from sklearn.metrics import accuracy_score, f1_score
def spatial_cv(df):
    X=df[['f1','f2']]; y=df.label; blocks=(df.x//25).astype(int)*4+(df.y//25).astype(int)
    pred=cross_val_predict(RandomForestClassifier(n_estimators=250,random_state=42),X,y,cv=GroupKFold(5),groups=blocks)
    return {'accuracy':accuracy_score(y,pred),'f1':f1_score(y,pred)}
