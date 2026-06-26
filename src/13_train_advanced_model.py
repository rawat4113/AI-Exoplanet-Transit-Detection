import pandas as pd
import joblib

from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Load advanced features
features = pd.read_csv("Outputs/advanced_features.csv")

# Load TCE matched labels
labels = pd.read_csv("Outputs/tce_matched_dataset.csv")

# Keep only ticid and label
labels = labels[["ticid", "tce_match"]]

# Merge features with labels
df = features.merge(labels, on="ticid", how="inner")

print("Total rows:", len(df))
print("\nClass counts:")
print(df["tce_match"].value_counts())

X = df[[
    "period",
    "power",
    "depth",
    "duration",
    "snr",
    "num_transits",
    "flux_mean",
    "flux_std"
]]

y = df["tce_match"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

models = {
    "Random Forest": RandomForestClassifier(
        n_estimators=300,
        random_state=42,
        class_weight="balanced"
    ),
    "Gradient Boosting": GradientBoostingClassifier(
        random_state=42
    ),
    "Logistic Regression": LogisticRegression(
        max_iter=1000,
        class_weight="balanced"
    )
}

best_model = None
best_score = 0
results = []

for name, model in models.items():
    print("\n==============================")
    print(name)
    print("==============================")

    model.fit(X_train, y_train)
    pred = model.predict(X_test)

    acc = accuracy_score(y_test, pred)
    results.append({
        "model": name,
        "accuracy": acc
    })

    print("Accuracy:", acc)
    print("\nConfusion Matrix:")
    print(confusion_matrix(y_test, pred))
    print("\nClassification Report:")
    print(classification_report(y_test, pred))

    if acc > best_score:
        best_score = acc
        best_model = model

results_df = pd.DataFrame(results)
results_df.to_csv("Outputs/model_comparison.csv", index=False)

joblib.dump(best_model, "Outputs/advanced_exoplanet_model.pkl")

print("\n================================")
print("Best accuracy:", best_score)
print("Saved: Outputs/advanced_exoplanet_model.pkl")
print("Saved: Outputs/model_comparison.csv")
print("================================")