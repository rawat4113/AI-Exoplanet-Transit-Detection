import pandas as pd

features = pd.read_csv("Outputs/all_features.csv")
tce = pd.read_csv(
    "Data/Catalogs/tess2018206190142-s0001-s0001_dvr-tcestats.csv",
    comment="#",
    on_bad_lines="skip"
)

features["ticid"] = (
    features["file"]
    .str.extract(r"-(\d+)-0120")[0]
    .astype("int64")
)

tce_small = tce[[
    "ticid",
    "tce_period",
    "tce_depth",
    "tce_duration",
    "tce_model_snr"
]].copy()

merged = features.merge(
    tce_small,
    on="ticid",
    how="left"
)

merged["tce_match"] = merged["tce_period"].notna().astype(int)

merged.to_csv("Outputs/tce_matched_dataset.csv", index=False)

print("Total rows:", len(merged))
print("\nTCE match counts:")
print(merged["tce_match"].value_counts())

print("\nFirst rows:")
print(merged[[
    "ticid",
    "period",
    "power",
    "depth",
    "tce_period",
    "tce_depth",
    "tce_duration",
    "tce_model_snr",
    "tce_match"
]].head(10))

print("\nSaved: Outputs/tce_matched_dataset.csv")