# Coastal Tidal Zones Analysis

### GIS · Python · Spatial Analysis · Temporal Data Analytics

An end-to-end GIS and data analytics portfolio project exploring the spatial and temporal characteristics of coastal tidal zones using Python, geospatial processing, statistical analysis, and scientific visualization.

## 🚀 Live Demo

**Explore the interactive Streamlit dashboard:**

👉 **[Open Coastal Tidal Zones Analysis — Live Dashboard](https://gis-tidal-zones-analysis-project-przzqtfiashxbxzzab227f.streamlit.app/)**

The dashboard provides an interactive environment for exploring spatial patterns, temporal trends, statistical distributions, and data quality.

**Source code:** [View the project on GitHub](https://github.com/AramMehraban/GIS-Tidal-Zones-Analysis-Project)

> **Data transparency:** This project uses a synthetic dataset created for portfolio and analytical workflow demonstration. The results do not represent measurements from a real coastal monitoring program.

---

## Project Overview

Coastal environments are shaped by tidal processes and changing environmental conditions. This project demonstrates how tabular data can be transformed into geospatial datasets, analyzed over time, and presented through reproducible analytical workflows.

The analysis focuses on three coastal tidal zones:

- 🟡 **Intertidal Zone** — the area between high and low tide, alternately exposed and submerged.
- 🔵 **Subtidal Zone** — the area that normally remains underwater.
- 🔴 **Supratidal Zone** — the area above normal tidal influence that may be affected by exceptional tides or wave action.

The project covers a synthetic time series from **1982 to 2018**.

## Project Objectives

- Explore temporal patterns across coastal tidal zones.
- Compare statistical distributions and variations in the dataset.
- Process and manage spatial data using Python GIS libraries.
- Create and work with geospatial data in GeoPackage format.
- Integrate analytical workflows with SQLite.
- Generate statistical plots and geospatial visualizations.
- Present analytical results through an interactive web dashboard.
- Document data limitations and ensure transparent interpretation.

## Technologies

| Area | Tools |
|---|---|
| Programming | Python |
| Data analysis | Pandas, NumPy |
| GIS and spatial processing | GeoPandas, Shapely |
| Geospatial data format | GeoPackage (`.gpkg`) |
| Database | SQLite |
| Visualization | Matplotlib, Seaborn, Plotly |
| Interactive dashboard | Streamlit |
| Development | Jupyter Notebook, VS Code, Git, GitHub |

## Analytical Workflow

1. **Data preparation** — prepare and inspect the synthetic tidal dataset.
2. **Temporal analysis** — explore changes across the 1982–2018 period.
3. **Statistical analysis** — compare distributions and patterns across tidal zones.
4. **Geospatial processing** — transform tabular records into spatial data structures.
5. **Data storage** — work with geospatial data and SQLite-based analytical workflows.
6. **Visualization** — create plots and maps to communicate analytical results.
7. **Interactive reporting** — present selected results through a Streamlit web application.
8. **Interpretation** — summarize patterns and limitations without presenting synthetic results as real-world observations.

## Interactive Dashboard

The Streamlit application is the online presentation layer of this portfolio project.

👉 **[Launch the live dashboard](https://gis-tidal-zones-analysis-project-przzqtfiashxbxzzab227f.streamlit.app/)**

The application is designed to support exploration of the following topics:

- **Executive Overview** — a summary of the dataset and principal indicators.
- **GIS & Spatial Analysis** — exploration of spatial data and geospatial outputs.
- **Temporal Analysis** — investigation of patterns over time.
- **Statistical Analysis** — comparison of distributions and numerical characteristics.
- **Data Quality** — inspection of missing values and data completeness.
- **Data Explorer** — interactive inspection of available records.
- **Project Information** — methodology, technologies, and project documentation.

*The exact content available in each dashboard section depends on the current application implementation and the data files included in the repository.*

## Visual Results

The repository contains the following visual outputs.

### GIS Visualization

![Tidal Zone GIS Visualization](figures/Tidal-Zone-GIS-Visualization.png)

### Height Comparison Across Basins

![Height Comparison Across Basins](figures/Height-Comparison-Across-Basins.png)

### Height Distribution Across Tidal Zones

![Height Distribution Across Tidal Zones](figures/Height-Distribution-Across-Tidal-Zones.png)

### Temporal Change in Tidal Zones

![Temporal Change of Height in Tidal Zone](figures/Temporal-Change-of-Height-in-Tidal-Zone.png)

### Coastal Zone Area Change Over Time

![Coastal Zone Area Change Over Time](figures/Coastal-Zone-Area-change-Over-time.png)

Additional plots are available in the `figures/` directory.

## Key Observations

The analysis of the synthetic dataset illustrates patterns such as:

- Differences in temporal variability between tidal zones.
- Differences in height distributions across zones and basins.
- Changes in simulated coastal-zone area over time.
- Opportunities to combine statistical summaries with geospatial visualization.

> **Interpretation note:** These observations are derived from synthetic data and should not be interpreted as evidence of actual environmental change. Real-world conclusions would require validated observational data and appropriate scientific context.

## Repository Structure

```text
GIS-Tidal-Zones-Analysis-Project/
│
├── app.py
├── data/
│   ├── tidal_data.csv
│   └── tidal_data.gpkg
│
├── figures/
│   ├── Coastal-Zone-Area-change-Over-time.png
│   ├── Dataset.png
│   ├── Height-Comparison-Across-Basins.png
│   ├── Height-Distribution-Across-Tidal-Zones.png
│   ├── Height-Distribution-Shape-per-Zone.png
│   ├── Temporal-Change-of-Height-in-Tidal-Zone.png
│   └── Tidal-Zone-GIS-Visualization.png
│
├── src/
│   ├── analysis.py
│   ├── gis_processing.py
│   ├── main.py
│   └── visualization.py
│
├── notebook.ipynb
├── requirements.txt
├── .gitignore
└── README.md
```

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/AramMehraban/GIS-Tidal-Zones-Analysis-Project.git
cd GIS-Tidal-Zones-Analysis-Project
```

### 2. Create a virtual environment

**Windows PowerShell:**

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

If PowerShell blocks script activation, use the following command in the current terminal session and try again:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### 4. Run the Streamlit dashboard

```bash
python -m streamlit run app.py
```

The application should open in your browser at the local address displayed in the terminal, usually `http://localhost:8501`.

### 5. Run the analytical workflow

```bash
python src/main.py
```

You can also open `notebook.ipynb` in Jupyter Notebook or VS Code to explore the analysis interactively.

> **Execution note:** The commands above describe the intended workflow. Successful execution depends on the installed dependencies, the availability of the required data files, and the current implementation of the scripts.

## Skills Demonstrated

- GIS and geospatial data processing.
- Spatial data handling with GeoPandas and Shapely.
- Python-based data analysis.
- Temporal and statistical analysis.
- Working with CSV and GeoPackage datasets.
- Database integration concepts using SQLite.
- Statistical and scientific visualization.
- Interactive dashboard development with Streamlit.
- Data quality assessment and transparent documentation.
- Reproducible project organization and version control with Git.

## Project Purpose

This project demonstrates a practical combination of GIS concepts and Python-based data analytics. It is intended as a portfolio example for roles such as:

- GIS Analyst
- Geospatial Data Analyst
- Junior Data Analyst
- GIS and Environmental Data Analytics Specialist

The project emphasizes structured data processing, transparent documentation, geospatial analysis, and clear visualization of analytical results.

## Author

**Aram Mehraban**

GIS & Data Analytics Portfolio

- **Live Dashboard:** [Coastal Tidal Zones Analysis](https://gis-tidal-zones-analysis-project-przzqtfiashxbxzzab227f.streamlit.app/)
- **GitHub Repository:** [GIS-Tidal-Zones-Analysis-Project](https://github.com/AramMehraban/GIS-Tidal-Zones-Analysis-Project)