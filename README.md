# MatInfo_EBSD: Materials Informatics for EBSD and Nanoindentation

This repository contains code, analysis notebooks, and machine learning pipelines for correlating **Electron Backscatter Diffraction (EBSD)** microstructure features with **Nanoindentation** mechanical response curves.

---

## 📌 Project Overview

- **Microstructure-Property Linkage**: Spatially mapping and correlating nanoindentation curves with local crystallographic orientation, grain boundary proximity, Kernel Average Misorientation (KAM), and phase maps.
- **Pop-in Phenomenon Analysis**: Detection, classification, and statistical modeling of pop-in events during indentation loading curves.
- **Machine Learning**: Predicting local mechanical behaviors and pop-in loads from localized crystallographic features.

---

## 📂 Repository Structure

```
├── dataset/
│   ├── eth.ipynb                 # Analysis and modeling notebooks
│   └── test.ipynb
├── images/                       # Presentation & visualization figures
│   ├── grain_boundary_map.png
│   ├── indent_cluster_plot.png
│   └── ...
├── Plots/                        # Microstructural maps & feature engineering
│   ├── EDA.ipynb
│   ├── feature_engineering.ipynb
│   ├── ebsd_orientation_map.png
│   ├── kam_map.png
│   ├── phase_map.png
│   └── sem_image.png
├── format_data.py                # Data structuring and preprocessing utility
├── grid.ipynb                    # Grid coordinate mapping
├── mapping.ipynb                 # EBSD-to-nanoindentation spatial mapping
├── ml.ipynb                      # Machine learning workflows
├── plots.ipynb                   # Visualization and plotting routines
├── popin.ipynb                   # Pop-in detection and analysis (v1)
├── popinV2.ipynb                 # Advanced pop-in analysis (v2)
├── requirements.txt              # Python dependencies
└── .gitignore                    # Excludes raw data dumps and heavy files
```

> **Note on Data**: Raw nanoindentation text dumps, large JSON/CSV datasets, and batch-generated curve plots are excluded from this repository via `.gitignore` to maintain a clean codebase.

---

## 🚀 Getting Started

### 1. Installation
Clone the repository and install the dependencies:
```bash
git clone https://github.com/harshu0117/MatInfo_EBSD.git
cd MatInfo_EBSD
pip install -r requirements.txt
```

### 2. Dependencies
- Python 3.9+
- `numpy`
- `pandas`
- `scipy`
- `matplotlib`
- `seaborn`
- `ipywidgets`
- `ipykernel`
