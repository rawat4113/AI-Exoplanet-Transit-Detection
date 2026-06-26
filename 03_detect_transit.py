import warnings
warnings.filterwarnings("ignore")

import lightkurve as lk
import matplotlib.pyplot as plt

file = "Data/Fits/tess2018206045859-s0001-0000000025245855-0120-s_lc.fits"

# Load and clean
lc = lk.read(file)
lc = lc.remove_nans().flatten()

print("Searching for transit signals...")

# Box Least Squares period search
bls = lc.to_periodogram(method='bls',
                        period=(0.5, 10))

print("Best Period:", bls.period_at_max_power)

plt.figure(figsize=(10,5))
plt.plot(bls.period.value,
         bls.power.value)

plt.xlabel("Period (days)")
plt.ylabel("BLS Power")
plt.title("Transit Search")
plt.show()