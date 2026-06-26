import pandas as pd

toi_path = "Data/Catalogs/tois.csv"
tce_path = "Data/Catalogs/tess2018206190142-s0001-s0001_dvr-tcestats.csv"

# skip bad/comment lines safely
toi = pd.read_csv(toi_path, comment="#", on_bad_lines="skip")
tce = pd.read_csv(tce_path, comment="#", on_bad_lines="skip")

print("\n===== TOI CATALOG =====")
print("Rows, Columns:", toi.shape)
print("\nColumns:")
print(toi.columns.tolist())
print("\nFirst 5 rows:")
print(toi.head())

print("\n===== TCE STATS =====")
print("Rows, Columns:", tce.shape)
print("\nColumns:")
print(tce.columns.tolist())
print("\nFirst 5 rows:")
print(tce.head())