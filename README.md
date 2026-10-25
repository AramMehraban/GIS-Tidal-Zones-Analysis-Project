# Coastal Tidal Zones Analysis

### GIS · Python · Spatial Analysis · Temporal Data Analytics

[🚀 Live Dashboard](https://gis-tidal-zones-analysis-project.streamlit.app/) | [📂 GitHub Repository](https://github.com/AramMehraban/GIS-Tidal-Zones-Analysis-Project)

An end-to-end GIS and data analytics portfolio project exploring the spatial and temporal characteristics of coastal tidal zones using Python, geospatial processing, statistical analysis, and scientific visualization.

> **Data Transparency:** This project uses a synthetic dataset created for portfolio and analytical workflow demonstration. The results do not represent measurements from a real coastal monitoring program.

---

## Table of Contents

- [Live Demo](#-live-demo)
- [Project Overview](#project-overview)
- [Tidal Zones](#tidal-zones)
- [Project Objectives](#project-objectives)
- [Technologies](#technologies)
- [Analytical Workflow](#analytical-workflow)
- [Interactive Dashboard](#interactive-dashboard)
- [Visual Results](#visual-results)
- [Key Observations](#key-observations)
- [Repository Structure](#repository-structure)
- [Getting Started](#getting-started)
- [Running the Dashboard](#running-the-dashboard)
- [Running the Analytical Workflow](#running-the-analytical-workflow)
- [Skills Demonstrated](#skills-demonstrated)
- [Limitations](#limitations)
- [Future Improvements](#future-improvements)
- [Author](#author)

---

## 🚀 Live Demo

Explore the interactive Streamlit dashboard:

### [Open Coastal Tidal Zones Analysis — Live Dashboard](https://gis-tidal-zones-analysis-project.streamlit.app/)

The application provides an interactive environment for exploring the available spatial data, temporal patterns, statistical distributions, and data-quality indicators.

**Source code:** [GIS-Tidal-Zones-Analysis-Project on GitHub](https://github.com/AramMehraban/GIS-Tidal-Zones-Analysis-Project)

---

## Project Overview

Coastal environments are shaped by tidal processes and changing environmental conditions. Geographic Information Systems (GIS) and data analytics provide useful methods for organizing spatial datasets, examining temporal patterns, and communicating analytical findings.

This project demonstrates an end-to-end workflow for processing and exploring coastal tidal-zone data using Python and geospatial tools.

The project combines:

- Python-based data processing and analysis
- Geospatial data handling
- Temporal and statistical analysis
- Scientific visualization
- CSV and GeoPackage data formats
- SQLite-based analytical workflows
- An interactive Streamlit dashboard

The dataset covers a synthetic time series from **1982 to 2018**. All results should be interpreted as demonstrations of analytical methods rather than evidence of actual coastal or environmental change.

## Tidal Zones

The project explores three conceptual coastal tidal zones.

### 1. Intertidal Zone

The area between the typical high-tide and low-tide boundaries. It is periodically exposed to the atmosphere and submerged by seawater.

### 2. Subtidal Zone

The area that normally remains underwater, even during low tide.

### 3. Supratidal Zone

The area above the normal high-tide boundary that may be influenced by exceptional tides, waves, or storm conditions.

These definitions provide the conceptual background for organizing and comparing the project's synthetic data.

## Project Objectives

The main objectives are to:

- Explore temporal patterns across coastal tidal zones.
- Compare statistical distributions and variations in the dataset.
- Process spatial data using Python GIS libraries.
- Create and work with geospatial data in GeoPackage format.
- Integrate analytical workflows with SQLite.
- Generate statistical plots and geospatial visualizations.
- Present selected results through an interactive web dashboard.
- Assess data quality and document analytical limitations.
- Demonstrate a reproducible GIS and data analytics workflow.

## Technologies

| Area | Technologies |
|---|---|
| Programming | Python |
| Data analysis | Pandas, NumPy |
| GIS and spatial processing | GeoPandas, Shapely |
| Geospatial data format | GeoPackage (`.gpkg`) |
| Database | SQLite |
| Statistical visualization | Matplotlib, Seaborn |
| Interactive visualization | Plotly |
| Web dashboard | Streamlit |
| Notebooks | Jupyter Notebook |
| Development tools | VS Code, Git, GitHub |

## Analytical Workflow

The project follows a structured analytical workflow.

### 1. Data Preparation

Inspect the synthetic dataset, review data types, and prepare the records for analysis.

### 2. Temporal Analysis

Explore patterns across the 1982–2018 time period and compare temporal variation among tidal-zone categories.

### 3. Statistical Analysis

Examine numerical distributions, summary statistics, and differences across zones and basins.

### 4. Geospatial Processing

Transform tabular records into spatial data structures and work with geospatial geometries using Python GIS libraries.

### 5. Data Storage

Work with CSV and GeoPackage files and demonstrate SQLite-based data workflows.

### 6. Visualization

Create statistical charts and geospatial visualizations to communicate patterns in the data.

### 7. Interactive Reporting

Present selected analytical outputs through the Streamlit dashboard.

### 8. Interpretation and Documentation

Summarize observations, describe limitations, and distinguish simulated patterns from real-world environmental evidence.

## Interactive Dashboard

### [Launch the Live Dashboard](https://gis-tidal-zones-analysis-project.streamlit.app/)

The Streamlit application is the interactive presentation layer of the project.

The dashboard is designed to support exploration of topics such as:

- **Executive Overview** — a summary of the dataset and selected indicators.
- **GIS & Spatial Analysis** — exploration of available geospatial data and outputs.
- **Temporal Analysis** — investigation of patterns over time.
- **Statistical Analysis** — comparison of distributions and numerical characteristics.
- **Data Quality** — inspection of missing values and data completeness.
- **Data Explorer** — interactive inspection of available records.
- **Project Information** — methodology, technologies, and documentation.

The exact features available in each section depend on the current implementation of the deployed application.

## Visual Results

The repository includes visual outputs illustrating different parts of the analytical workflow.

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

Additional visualizations may be available in the `figures/` directory.

> **Note:** GitHub displays these images only if the referenced files exist at the specified paths and filenames. Verify capitalization and spelling if any image does not render.

## Key Observations

The synthetic dataset can be used to demonstrate analytical patterns such as:

- Differences in temporal variability among tidal zones.
- Differences in height distributions across zones and basins.
- Changes in simulated coastal-zone area over time.
- The combination of statistical summaries and geospatial visualization.
- The importance of assessing data quality before interpreting results.

These are analytical themes rather than claims about measured environmental conditions.

> **Scientific interpretation:** Patterns derived from synthetic data must not be presented as evidence of real sea-level change, coastal erosion, or observed tidal behavior. Real-world conclusions require validated observational data, suitable spatial references, and appropriate scientific methods.

## Repository Structure

The following structure describes the expected organization of the project. The actual GitHub repository determines which files are available.

```text
GIS-Tidal-Zones-Analysis-Project/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
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
└── notebook.ipynb
```

## Getting Started

### Prerequisites

Install the following tools:

- Python
- Git
- A code editor such as Visual Studio Code
- A web browser

### 1. Clone the Repository

```bash
git clone https://github.com/AramMehraban/GIS-Tidal-Zones-Analysis-Project.git
cd GIS-Tidal-Zones-Analysis-Project
```

### 2. Create a Virtual Environment

On Windows PowerShell:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

If PowerShell blocks script activation, you can allow it for the current terminal session:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

Upgrade pip and install the project dependencies:

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### 4. Verify the Data Files

Check that the required CSV and GeoPackage files are present in the `data/` directory.

The analytical scripts and dashboard must reference the correct local file paths.

## Running the Dashboard

From the repository root, execute:

```bash
python -m streamlit run app.py
```

Streamlit will display a local URL in the terminal, usually:

`http://localhost:8501`

Open that URL in your browser to explore the dashboard locally.

## Running the Analytical Workflow

To run the main analytical workflow:

```bash
python src/main.py
```

You can also open `notebook.ipynb` in Jupyter Notebook or Visual Studio Code to explore the analysis interactively.

**Execution note:** These commands represent the intended workflow. Successful execution depends on the actual script implementation, installed dependencies, and availability of the required input files.

## Skills Demonstrated

This portfolio project demonstrates:

- GIS and geospatial data processing
- Spatial data handling with GeoPandas and Shapely
- Python-based data analysis
- Temporal and statistical analysis
- CSV and GeoPackage data management
- SQLite-based analytical workflows
- Statistical and scientific visualization
- Interactive dashboard development with Streamlit
- Data-quality assessment
- Reproducible project organization
- Technical documentation and version control

## Limitations

- **Synthetic data:** The dataset was created for portfolio and workflow demonstration.
- **No direct environmental evidence:** The results do not establish actual coastal changes or real tidal behavior.
- **Data dependency:** Analytical outputs depend on the assumptions and structure of the synthetic dataset.
- **Spatial validity:** Real-world GIS applications require appropriate coordinate reference systems, verified geometries, and reliable source data.
- **Generalizability:** Findings from simulated data cannot be generalized to actual coastal environments.

## Future Improvements

Potential future enhancements include:

- Integrating validated coastal monitoring datasets.
- Adding explicit coordinate reference system checks.
- Expanding spatial validation and geometry-quality checks.
- Comparing tidal-zone patterns across real geographic locations.
- Improving temporal trend analysis.
- Adding reproducible data-quality reports.
- Expanding dashboard filtering and map interactions.
- Documenting data provenance and analytical assumptions.
- Adding automated tests for core processing functions.
- Creating a more comprehensive deployment and reproducibility guide.

## Project Purpose

This project demonstrates a practical combination of GIS concepts and Python-based data analytics. It is intended as a portfolio example for roles such as:

- GIS Analyst
- Geospatial Data Analyst
- Junior Data Analyst
- GIS and Environmental Data Analytics Specialist

The project emphasizes structured data processing, spatial analysis, temporal exploration, scientific visualization, and transparent interpretation of results.

## Author

**Aram Mehraban**

GIS & Data Analytics Portfolio

- **Live Dashboard:** [Coastal Tidal Zones Analysis](https://gis-tidal-zones-analysis-project.streamlit.app/)
- **GitHub Repository:** [GIS-Tidal-Zones-Analysis-Project](https://github.com/AramMehraban/GIS-Tidal-Zones-Analysis-Project)

---

*This project is intended for portfolio and learning purposes. All analytical conclusions must be interpreted in the context of the synthetic dataset and its documented limitations.*

---

## License & Copyright

**Copyright © 2026 Aram Mehraban. All rights reserved.**

This project, including its original source code, scripts, documentation, project structure, and visualizations, is the intellectual property of Aram Mehraban, unless otherwise stated.

You may view this repository for personal learning, evaluation, and portfolio review. Copying, reproducing, modifying, redistributing, republishing, or commercially using the original materials without prior written permission is not permitted, except as permitted by applicable law.

Third-party libraries, datasets, and other materials remain subject to their respective licenses and terms of use.

**No license to reuse the original materials is granted by making this repository publicly available.**
