#  Coastal Tidal Zones Analysis

### GIS + Python Spatial & Temporal Analysis

##  Overview

This project analyzes the **spatial and temporal characteristics of coastal tidal zones** using Python-based GIS, statistical analysis, database integration, and scientific visualization.

The analysis focuses on three ecological coastal zones:

* 🟡 **Intertidal**
* 🔵 **Subtidal**
* 🔴 **Supratidal**

The project demonstrates an end-to-end GIS and data analytics workflow, from data generation and statistical analysis to spatial data processing and visualization.

---

## Project Objectives

The main objectives of this project are to:

* Analyze changes in coastal tidal zones over time
* Explore temporal trends between **1982 and 2018**
* Create and process spatial GIS data using Python
* Store analytical data in a SQLite database
* Generate statistical and scientific visualizations
* Demonstrate an end-to-end **GIS + Python + Data Analytics** workflow

---

## 🗺️ Tidal Zone Definitions

| Zone              | Description                         |
| ----------------- | ----------------------------------- |
| 🔵 **Subtidal**   | Permanently underwater coastal zone |
| 🟡 **Intertidal** | Area between high and low tide      |
| 🔴 **Supratidal** | Area above normal tidal influence   |

---

## Tools & Technologies

### Programming & Data Analysis

* Python
* Pandas
* NumPy

### GIS & Spatial Analysis

* GeoPandas
* Shapely
* GeoPackage

### Database

* SQLite

### Visualization

* Matplotlib
* Seaborn

---

## Project Workflow

```text
Raw / Generated Data
        ↓
Data Preparation
        ↓
Statistical Analysis
        ↓
SQLite Database
        ↓
GeoDataFrame Creation
        ↓
Spatial Processing
        ↓
Visualization
        ↓
Key Insights
```

---

## Analysis

The project includes:

### 1. Data Generation

A synthetic coastal tidal dataset covering the period **1982–2018** is generated for the three tidal zones.

### 2. Temporal Analysis

Time-series analysis is used to investigate changes and variability in tidal zones over time.

### 3. Statistical Analysis

The dataset is analyzed using Python statistical and data-processing libraries.

### 4. GIS Data Processing

Tabular data is converted into spatial data using **GeoPandas and Shapely**.

### 5. Database Integration

The analytical dataset is stored and managed using **SQLite**.

### 6. Visualization

Scientific visualizations are generated using **Matplotlib and Seaborn**.

---

## Key Insights

The analysis indicates that:

* 🔵 **Subtidal zones** remain relatively stable over the analyzed period.
* 🟡 **Intertidal zones** show greater temporal variability.
* 🔴 **Supratidal zones** demonstrate higher environmental sensitivity.

> These findings are based on the synthetic dataset created for this portfolio project and are intended to demonstrate the analytical workflow rather than represent observations from a specific real-world coastal monitoring program.

---

## Project Structure

```text
Coastal-Tidal-Zones-Analysis/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── src/
│   └── main.py
│
├── outputs/
│   └── figures/
│
├── tidal_data.csv
├── tidal.db
├── tidal_data.gpkg
│
├── requirements.txt
├── README.md
└── LICENSE
```

---

## Output Files

The project generates the following outputs:

* `tidal_data.csv` — analytical dataset
* `tidal.db` — SQLite database
* `tidal_data.gpkg` — GIS spatial dataset
* PNG figures — statistical and time-series visualizations

---

## How to Run

Clone the repository and install the required Python packages:

```bash
pip install -r requirements.txt
```

Run the main analysis:

```bash
python src/main.py
```

The generated datasets and visualizations will be saved in the corresponding project directories.

---

## Skills Demonstrated

This project demonstrates practical experience in:

* GIS data processing
* Spatial data analysis
* Temporal data analysis
* Python data analytics
* GeoPandas
* Shapely
* Pandas & NumPy
* SQLite database integration
* Scientific visualization
* Reproducible analytical workflows

---

## Portfolio Value

This project combines **GIS expertise with modern Python data analytics**, demonstrating how spatial datasets can be transformed into structured analytical outputs, databases, visualizations, and interpretable insights.

It is designed as a portfolio project for **GIS Analyst, Geospatial Data Analyst, Junior Data Analyst, and GIS/Data Analytics** positions.

---

## Author

**Aram Mehraban**

GIS & Data Analytics Portfolio Project

---

## License

This project is licensed under the **MIT License**.

See the `LICENSE` file for details.
