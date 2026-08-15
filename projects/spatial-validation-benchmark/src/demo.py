from pathlib import Path
import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_recall_fscore_support, ConfusionMatrixDisplay
from sklearn.model_selection import train_test_split, GroupShuffleSplit

ROOT = Path(__file__).resolve().parents[1]
OUTPUTS = ROOT / "outputs"
OUTPUTS.mkdir(exist_ok=True)

rng = np.random.default_rng(7)
n = 2200
x = rng.uniform(0, 100, n)
y = rng.uniform(0, 100, n)
spatial_signal = np.sin(x / 9) + np.cos(y / 11)
noise = rng.normal(0, 0.55, n)
label = np.where(spatial_signal + noise > 0.8, "class_A", np.where(spatial_signal + noise < -0.8, "class_C", "class_B"))

f1 = spatial_signal + rng.normal(0, 0.22, n)
f2 = np.sin(x / 12) + rng.normal(0, 0.25, n)
f3 = np.cos(y / 13) + rng.normal(0, 0.25, n)
f4 = rng.normal(0, 1, n)

df = pd.DataFrame({"x": x, "y": y, "f1": f1, "f2": f2, "f3": f3, "f4": f4, "label": label})
features = ["f1", "f2", "f3", "f4"]

def score_split(train_idx, test_idx):
    model = RandomForestClassifier(n_estimators=300, random_state=42, class_weight="balanced")
    model.fit(df.loc[train_idx, features], df.loc[train_idx, "label"])
    pred = model.predict(df.loc[test_idx, features])
    y_true = df.loc[test_idx, "label"]
    p, r, f1s, _ = precision_recall_fscore_support(y_true, pred, average="macro", zero_division=0)
    return model, pred, {
        "accuracy": float(accuracy_score(y_true, pred)),
        "precision_macro": float(p),
        "recall_macro": float(r),
        "f1_macro": float(f1s),
    }

idx = np.arange(n)
tr_random, te_random = train_test_split(idx, test_size=0.25, random_state=42, stratify=df["label"])
model_random, pred_random, metrics_random = score_split(tr_random, te_random)

block_x = (x // 20).astype(int)
block_y = (y // 20).astype(int)
groups = block_y * 10 + block_x
splitter = GroupShuffleSplit(n_splits=1, test_size=0.25, random_state=42)
tr_spatial, te_spatial = next(splitter.split(df[features], df["label"], groups=groups))
model_spatial, pred_spatial, metrics_spatial = score_split(tr_spatial, te_spatial)

summary = {"random_split": metrics_random, "spatial_block_split": metrics_spatial}
(OUTPUTS / "metrics.json").write_text(json.dumps(summary, indent=2))

fig, ax = plt.subplots(figsize=(7, 5))
for name, metrics in summary.items():
    ax.bar(name, metrics["f1_macro"], label=name)
ax.set_ylim(0, 1)
ax.set_ylabel("Macro F1")
ax.set_title("Random vs spatial validation")
fig.tight_layout()
fig.savefig(OUTPUTS / "validation_comparison.png", dpi=180)
plt.close(fig)

ConfusionMatrixDisplay.from_predictions(df.loc[te_random, "label"], pred_random)
plt.title("Random split confusion matrix")
plt.tight_layout()
plt.savefig(OUTPUTS / "confusion_random.png", dpi=180)
plt.close()

ConfusionMatrixDisplay.from_predictions(df.loc[te_spatial, "label"], pred_spatial)
plt.title("Spatial holdout confusion matrix")
plt.tight_layout()
plt.savefig(OUTPUTS / "confusion_spatial.png", dpi=180)
plt.close()

print(json.dumps(summary, indent=2))
