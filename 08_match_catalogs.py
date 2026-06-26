import pandas as pd

# Load extracted features
features = pd.read_csv("Outputs/all_features.csv")

# Load TOI catalog
toi = pd.read_csv(
    "Data/Catalogs/tois.csv",
    comment="#",
    on_bad_lines="skip"
)

print("Features rows:", len(features))
print("TOI rows:", len(toi))

# Extract TIC ID from FITS filename
features["ticid"] = (
    features["file"]
    .str.extract(r"-(\d+)-0120")[0]
    .astype("int64")
)

# Keep only useful TOI columns
toi_small = toi[["TIC", "TOI Disposition"]].copy()

# Merge
merged = features.merge(
    toi_small,
    left_on="ticid",
    right_on="TIC",
    how="left"
)

# Create labels
def create_label(x):
    if pd.isna(x):
        return -1      # Unknown
    elif x == "FP":
        return 0       # False Positive
    else:
        return 1       # Planet Candidate / KP / CP

merged["label"] = merged["TOI Disposition"].apply(create_label)

# Save
merged.to_csv(
    "Outputs/labeled_dataset.csv",
    index=False
)

print("\nLabel counts:")
print(merged["label"].value_counts())

print("\nFirst rows:")
print(
    merged[
        ["ticid",
         "period",
         "power",
         "depth",
         "TOI Disposition",
         "label"]
    ].head()
)

print("\nSaved: Outputs/labeled_dataset.csv")