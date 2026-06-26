import streamlit as st
import lightkurve as lk
import matplotlib.pyplot as plt
import joblib
import pandas as pd
import numpy as np
import tempfile
import warnings
from pathlib import Path

warnings.filterwarnings("ignore")

st.set_page_config(
    page_title="AI Exoplanet Detector",
    page_icon="🌌",
    layout="wide"
)

MODEL_PATH = Path("Outputs/advanced_exoplanet_model.pkl")

st.sidebar.title("🌌 AI Exoplanet Detector")
st.sidebar.write("Detect possible exoplanet transit signals from TESS light curve data.")
st.sidebar.markdown("---")
st.sidebar.write("**Tech Used:** Python, Streamlit, Lightkurve, Scikit-learn")
st.sidebar.write("**Author:** Ritesh Rawat")

st.title("🌌 AI-Based Exoplanet Transit Detection System")
st.write("Upload a TESS `.fits` file to clean the light curve, detect transit-like signals, estimate parameters, and classify the result using AI.")

if not MODEL_PATH.exists():
    st.error("Model file not found: `Outputs/advanced_exoplanet_model.pkl`")
    st.info("Train the model first or place the trained model inside the `Outputs/` folder.")
    st.stop()

model = joblib.load(MODEL_PATH)

uploaded_file = st.file_uploader("📤 Upload a TESS `.fits` file", type=["fits"])

if uploaded_file is not None:
    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".fits") as tmp:
            tmp.write(uploaded_file.read())
            file_path = tmp.name

        st.success("✅ FITS file uploaded successfully!")

        with st.spinner("Processing light curve and detecting transit signal..."):
            lc = lk.read(file_path)
            lc_clean = lc.remove_nans().flatten()

            flux = lc_clean.flux.value
            time = lc_clean.time.value

            bls = lc_clean.to_periodogram(method="bls", period=(0.5, 10))

            period = bls.period_at_max_power.value
            power = bls.max_power
            duration = bls.duration_at_max_power.value
            depth = 1 - np.nanmin(flux)
            flux_mean = np.nanmean(flux)
            flux_std = np.nanstd(flux)
            snr = depth / flux_std if flux_std != 0 else 0
            time_span = np.nanmax(time) - np.nanmin(time)
            num_transits = time_span / period if period != 0 else 0

            features = pd.DataFrame({
                "period": [period],
                "power": [power],
                "depth": [depth],
                "duration": [duration],
                "snr": [snr],
                "num_transits": [num_transits],
                "flux_mean": [flux_mean],
                "flux_std": [flux_std]
            })

            prediction = model.predict(features)[0]
            probability = model.predict_proba(features)[0][1]

        st.subheader("📊 Estimated Transit Parameters")

        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Orbital Period", f"{period:.4f} days")
        col2.metric("Transit Depth", f"{depth:.6f}")
        col3.metric("Duration", f"{duration:.4f} days")
        col4.metric("SNR", f"{snr:.2f}")

        st.dataframe(features, use_container_width=True)

        st.subheader("🤖 AI Classification Result")

        if prediction == 1:
            st.success("✅ Possible Exoplanet Transit Candidate Detected")
        else:
            st.warning("⚠️ Likely Noise / Non-Transit Signal")

        st.metric("AI Confidence", f"{probability * 100:.2f}%")

        tab1, tab2, tab3 = st.tabs([
            "Cleaned Light Curve",
            "BLS Periodogram",
            "Folded Light Curve"
        ])

        with tab1:
            fig1, ax1 = plt.subplots(figsize=(12, 4))
            ax1.scatter(time, flux, s=1)
            ax1.set_xlabel("Time")
            ax1.set_ylabel("Normalized Flux")
            ax1.set_title("Cleaned TESS Light Curve")
            st.pyplot(fig1)

        with tab2:
            fig2, ax2 = plt.subplots(figsize=(12, 4))
            ax2.plot(bls.period.value, bls.power.value)
            ax2.set_xlabel("Period (days)")
            ax2.set_ylabel("BLS Power")
            ax2.set_title("Box Least Squares Periodogram")
            st.pyplot(fig2)

        with tab3:
            folded_lc = lc_clean.fold(period=period)
            fig3, ax3 = plt.subplots(figsize=(12, 4))
            ax3.scatter(folded_lc.time.value, folded_lc.flux.value, s=1)
            ax3.set_xlabel("Phase")
            ax3.set_ylabel("Normalized Flux")
            ax3.set_title("Phase-Folded Light Curve")
            st.pyplot(fig3)

        st.info(
            "The model uses BLS power, transit depth, duration, SNR, number of transits, "
            "and flux statistics to classify possible transit-like signals."
        )

    except Exception as error:
        st.error("Something went wrong while processing the FITS file.")
        st.exception(error)
else:
    st.info("Upload a `.fits` file to start the analysis.")