# 🌌 AI-Exoplanet-Transit-Detection

> **An AI-powered end-to-end pipeline for detecting exoplanet transit signals from noisy TESS light curve data using feature engineering, Box Least Squares (BLS), and Machine Learning.**

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Scikit--Learn-orange)
![Astronomy](https://img.shields.io/badge/Astronomy-TESS-purple)
![License](https://img.shields.io/badge/License-MIT-green)

---

# 🚀 Overview

Detecting exoplanets from stellar light curves is challenging because transit signals are extremely small and often hidden by instrumental noise and stellar variability.

This project implements a complete AI-powered pipeline that:

* Reads NASA TESS `.fits` files
* Cleans noisy light curve data
* Detects possible transit signals using Box Least Squares (BLS)
* Estimates orbital parameters
* Extracts astrophysical features
* Uses Machine Learning to classify potential exoplanet candidates
* Visualizes every stage of the detection pipeline

---

# ✨ Features

* 📂 Upload TESS FITS files
* 🧹 Automatic light curve cleaning
* 📈 Transit detection using Box Least Squares (BLS)
* 🌍 Estimate orbital period, transit depth and duration
* 📊 Phase-folded light curve visualization
* 🤖 AI-based transit classification
* 📉 Interactive plots and statistical summaries
* 🌐 Streamlit web interface

---

# 🛰️ Pipeline Workflow

## 🛰️ Pipeline Workflow

```mermaid
flowchart TD
    A[Upload TESS FITS File] --> B[Read Light Curve]
    B --> C[Clean & Normalize Data]
    C --> D[Transit Detection using BLS]
    D --> E[Estimate Transit Parameters]
    E --> F[Extract Features]
    F --> G[AI Classification]
    G --> H[Visualization & Results]

    D --> I[Orbital Period]
    D --> J[Transit Depth]
    D --> K[Duration]
    D --> L[SNR]

(the three backticks immediately after `D --> L[SNR]`)

Without those three backticks, GitHub thinks everything below (like `# 📸 Application Preview`) is still part of the Mermaid diagram, which causes the error.

---

If it **still gives an error**, send me a screenshot of the **README edit page** showing the Mermaid section. I'll point out the exact line to fix.

# 📸 Application Preview

## 📤 Upload FITS File

<p align="center">
  <img src="images/upload.png" width="900">
</p>

## 📤 Upload FITS File

<p align="center">
  <img src="images/upload.png" width="900">
</p>

---

## 🧹 Cleaned Light Curve

<p align="center">
  <img src="images/cleaned_lightcurve.png" width="900">
</p>

---

## 📈 Transit Detection (BLS)

<p align="center">
  <img src="images/bls_periodogram.png" width="900">
</p>

---

## 📊 Estimated Transit Parameters

<p align="center">
  <img src="images/parameters.png" width="900">
</p>

---

## 🌌 Phase Folded Light Curve

<p align="center">
  <img src="images/folded_curve.png" width="900">
</p>

---

## 🤖 AI Classification Result

<p align="center">
  <img src="images/classification.png" width="900">
</p>

# 📂 Project Structure

```text
AI-Exoplanet-Transit-Detection/
│
├── Data/
│   └── Catalogs/
│
├── Outputs/
├── Plots/
│
├── app.py
├── 01_read_lightcurve.py
├── 02_clean_lightcurve.py
├── 03_detect_transit.py
├── 04_extract_features.py
├── 05_train_model.py
├── 06_predict.py
├── 07_catalog_analysis.py
├── 08_match_catalogs.py
├── 09_match_tce_catalog.py
├── 10_train_tce_model.py
├── 11_feature_importance.py
├── 12_advanced_features.py
├── 13_train_advanced_model.py
│
├── requirements.txt
├── README.md
└── LICENSE
```

---

# 🛠 Technologies Used

| Category         | Tools               |
| ---------------- | ------------------- |
| Language         | Python              |
| Astronomy        | Astropy, Lightkurve |
| Data Analysis    | NumPy, Pandas       |
| Machine Learning | Scikit-learn        |
| Visualization    | Matplotlib          |
| Web App          | Streamlit           |

---

# 📊 AI Model

The model uses engineered features including:

* Transit Period
* Transit Depth
* Transit Duration
* Signal-to-Noise Ratio (SNR)
* Number of Detected Transits
* Flux Mean
* Flux Standard Deviation

These features are used to classify whether the detected signal is likely to be a genuine exoplanet transit or noise.

---

# ⚙️ Installation

```bash
git clone https://github.com/rawat4113/AI-Exoplanet-Transit-Detection.git

cd AI-Exoplanet-Transit-Detection

pip install -r requirements.txt
```

---

# ▶️ Run

```bash
streamlit run app.py
```

Open:

```
http://localhost:8501
```

---

# 📈 Current Capabilities

* Read TESS FITS observations
* Detect periodic transit signals
* Estimate orbital parameters
* AI classification
* Interactive visualizations

---

# 🚀 Future Improvements

* Deep Learning (CNN/LSTM) based classifier
* Multi-sector TESS support
* NASA Exoplanet Archive integration
* Confidence calibration
* Explainable AI (SHAP)
* Cloud deployment

---

# 👨‍💻 Author

**Ritesh Rawat**

B.Tech Information Technology

Aspiring Data Scientist & AI/ML Engineer

---

# 📜 License

This project is licensed under the MIT License.

