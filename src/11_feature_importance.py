import pandas as pd
import joblib
import matplotlib.pyplot as plt

model = joblib.load("Outputs/tce_exoplanet_model.pkl")

features = ["period", "power", "depth"]

importance = model.feature_importances_

for f, i in zip(features, importance):
    print(f"{f}: {i:.4f}")

plt.bar(features, importance)
plt.title("Feature Importance")
plt.ylabel("Importance")
plt.show()