"""Random Forest land-cover classification starter."""

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

def train_random_forest(X_train, y_train, n_estimators=300, random_state=42):
    model = RandomForestClassifier(
        n_estimators=n_estimators,
        max_features="sqrt",
        class_weight="balanced",
        random_state=random_state,
        n_jobs=-1,
    )
    model.fit(X_train, y_train)
    return model

def evaluate_model(model, X_test, y_test):
    pred = model.predict(X_test)
    return {
        "accuracy": accuracy_score(y_test, pred),
        "confusion_matrix": confusion_matrix(y_test, pred),
        "classification_report": classification_report(y_test, pred),
    }
