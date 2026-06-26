import warnings
warnings.filterwarnings("ignore")

import lightkurve as lk
import pandas as pd
from pathlib import Path

# Find all FITS files
fits_files = list(Path("Data/Fits").glob("*.fits"))

print("Total FITS files found:", len(fits_files))

all_features = []

for file in fits_files:

    try:
        # Read light curve
        lc = lk.read(file)

        # Clean data
        lc = lc.remove_nans().flatten()

        # Transit search
        bls = lc.to_periodogram(
            method="bls",
            period=(0.5, 10)
        )

        # Extract features
        period = bls.period_at_max_power.value
        power = bls.max_power
        depth = 1 - lc.flux.value.min()

        all_features.append({
            "file": file.name,
            "period": period,
            "power": power,
            "depth": depth
        })

        print("Processed:", file.name)

    except Exception as e:
        print("Skipped:", file.name)
        print("Reason:", e)

# Create DataFrame
df = pd.DataFrame(all_features)

# Save dataset
df.to_csv("Outputs/all_features.csv", index=False)

print("\n================================")
print("Total processed:", len(df))
print("Saved: Outputs/all_features.csv")
print("================================")