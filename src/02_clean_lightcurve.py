import warnings
warnings.filterwarnings("ignore")

import lightkurve as lk
import matplotlib.pyplot as plt

file = "Data/Fits/tess2018206045859-s0001-0000000025245855-0120-s_lc.fits"

lc = lk.read(file)

# Remove bad points
lc_clean = lc.remove_nans()

# Flatten stellar variability
lc_flat = lc_clean.flatten(window_length=101)

plt.figure(figsize=(12,5))
plt.scatter(lc_flat.time.value,
            lc_flat.flux.value,
            s=1)

plt.title("Cleaned Light Curve")
plt.xlabel("Time")
plt.ylabel("Normalized Flux")
plt.show()