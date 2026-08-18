from src.data_generation import generate_demo
from src.modeling import flowering_classifier,yield_regression

def test_demo_shape():
    df=generate_demo(); assert df['plant_id'].nunique()==72; assert len(df)==576

def test_models_run():
    df=generate_demo(); fm,_,_=flowering_classifier(df); ym,_,_,_=yield_regression(df); assert 0<=fm['accuracy']<=1; assert ym['mae']>=0
