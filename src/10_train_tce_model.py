import pandas as pd
import joblib

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Load TCE matched dataset
df = pd.read_csv("Outputs/tce_matched_dataset.csv")

print("Total rows:", len(df))
print("\nClass counts:")
print(df["tce_match"].value_counts())

# Features
X = df[["period", "power", "depth"]]

# Real label from TCE catalog match
y = df["tce_match"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# AI model
model = RandomForestClassifier(
    n_estimators=200,
    random_state=42,
    class_weight="balanced"
)

model.fit(X_train, y_train)

# Prediction
pred = model.predict(X_test)

print("\nAccuracy:", accuracy_score(y_test, pred))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, pred))

print("\nClassification Report:")
print(classification_report(y_test, pred))

# Save model
joblib.dump(model, "Outputs/tce_exoplanet_model.pkl")

print("\nSaved: Outputs/tce_exoplanet_model.pkl")