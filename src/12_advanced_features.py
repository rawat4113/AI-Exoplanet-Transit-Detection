import warnings
warnings.filterwarnings("ignore")

import lightkurve as lk
import pandas as pd
import numpy as np
from pathlib import Path

fits_files = list(Path("Data/Fits").glob("*.fits"))

print("Total FITS files found:", len(fits_files))

rows = []

for file in fits_files:
    try:
        lc = lk.read(file)
        lc_clean = lc.remove_nans().flatten()

        bls = lc_clean.to_periodogram(
            method="bls",
            period=(0.5, 10)
        )

        period = bls.period_at_max_power.value
        power = bls.max_power
        duration = bls.duration_at_max_power.value

        flux = lc_clean.flux.value
        time = lc_clean.time.value

        depth = 1 - np.nanmin(flux)
        flux_mean = np.nanmean(flux)
        flux_std = np.nanstd(flux)

        snr = depth / flux_std if flux_std != 0 else 0

        time_span = np.nanmax(time) - np.nanmin(time)
        num_transits = time_span / period if period != 0 else 0

        ticid = file.name.split("-")[2]

        rows.append({
            "file": file.name,
            "ticid": int(ticid),
            "period": period,
            "power": power,
            "depth": depth,
            "duration": duration,
            "snr": snr,
            "num_transits": num_transits,
            "flux_mean": flux_mean,
            "flux_std": flux_std
        })

        print("Processed:", file.name)

    except Exception as e:
        print("Skipped:", file.name)
        print("Reason:", e)

df = pd.DataFrame(rows)

df.to_csv("Outputs/advanced_features.csv", index=False)

print("\n================================")
print("Total processed:", len(df))
print("Saved: Outputs/advanced_features.csv")
print("================================")