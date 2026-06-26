import pandas as pd
import joblib

# Load trained model
model = joblib.load("Outputs/exoplanet_model.pkl")

# Load features
df = pd.read_csv("Outputs/all_features.csv")

# Select input features
X = df[["period", "power", "depth"]]

# Predict
predictions = model.predict(X)

# Add predictions to dataframe
df["prediction"] = predictions

# Convert 0/1 into readable labels
df["prediction_label"] = df["prediction"].map({
    0: "Low chance",
    1: "High chance"
})

# Save result
df.to_csv("Outputs/predictions.csv", index=False)

print(df[["file", "period", "power", "depth", "prediction_label"]].head(10))
print("\nSaved: Outputs/predictions.csv")