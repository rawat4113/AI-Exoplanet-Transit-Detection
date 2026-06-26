from astropy.io import fits
import matplotlib.pyplot as plt
import os

fits_folder = "Data/Fits"

files = [f for f in os.listdir(fits_folder) if f.endswith(".fits")]

print("Total FITS files:", len(files))
print("First file:", files[0])

file_path = os.path.join(fits_folder, files[0])

hdul = fits.open(file_path)
data = hdul[1].data

time = data["TIME"]
flux = data["PDCSAP_FLUX"]

plt.figure(figsize=(12, 5))
plt.plot(time, flux, ".", markersize=1)
plt.xlabel("Time")
plt.ylabel("Brightness")
plt.title("First TESS Light Curve")
plt.show()

hdul.close()