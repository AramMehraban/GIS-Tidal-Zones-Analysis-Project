
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from pathlib import Path

try:
    import geopandas as gpd
    GEOPANDAS_AVAILABLE = True
except ImportError:
    gpd = None
    GEOPANDAS_AVAILABLE = False


# =========================================================
# 1. CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="Coastal Tidal Zones | Aram Mehraban",
    page_icon="🌊",
    layout="wide",
    initial_sidebar_state="expanded",
)

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
FIGURES_DIR = BASE_DIR / "figures"

CSV_PATH = DATA_DIR / "tidal_data.csv"
GPKG_PATH = DATA_DIR / "tidal_data.gpkg"

GITHUB_URL = (
    "https://github.com/"
    "AramMehraban/GIS-Tidal-Zones-Analysis-Project"
)

# Fixed zone colors across the complete application
TIDAL_ZONE_COLORS = {
    "Intertidal Zone": "#E9B949",
    "Subtidal Zone": "#2585C7",
    "Supratidal Zone": "#D95757",
}

TIDAL_ZONE_ALIASES = {
    "intertidal": "#E9B949",
    "intertidal zone": "#E9B949",
    "subtidal": "#2585C7",
    "subtidal zone": "#2585C7",
    "supratidal": "#D95757",
    "supratidal zone": "#D95757",
}


# =========================================================
# 2. STYLE
# =========================================================

st.markdown(
    """
    <style>
    .block-container {
        padding-top: 1.5rem;
        padding-bottom: 2rem;
        max-width: 1500px;
    }

    [data-testid="stMetric"] {
        background: rgba(100, 130, 160, 0.08);
        border: 1px solid rgba(100, 130, 160, 0.20);
        padding: 16px;
        border-radius: 12px;
    }

    [data-testid="stSidebar"] {
        border-right: 1px solid rgba(100, 130, 160, 0.20);
    }

    .hero {
        padding: 26px 30px;
        border-radius: 16px;
        margin-bottom: 16px;
        background: linear-gradient(120deg, #102A43, #126E82);
        color: white;
    }

    .hero h1 {
        color: white;
        font-size: 2.1rem;
        margin-bottom: 8px;
    }

    .hero p {
        color: #E2F3F5;
        font-size: 1rem;
        margin-bottom: 5px;
    }

    .author-line {
        margin: 0 0 18px 2px;
        font-size: 0.94rem;
        color: #526579;
    }

    .author-line strong {
        color: #126E82;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


# =========================================================
# 3. HELPER FUNCTIONS
# =========================================================

@st.cache_data
def load_csv(path, modified_time):
    return pd.read_csv(path)


@st.cache_data
def load_gpkg(path, modified_time):
    return gpd.read_file(path)


def find_column(columns, keywords):
    for col in columns:
        name = (
            str(col)
            .lower()
            .replace("_", " ")
            .replace("-", " ")
        )
        if any(word in name for word in keywords):
            return col
    return None


def format_number(value, decimals=2):
    if pd.isna(value):
        return "N/A"
    return f"{value:,.{decimals}f}"


def get_zone_colors(values):
    """Use stable colors for known tidal zones."""
    result = {}

    for value in values:
        label = str(value)
        key = label.strip().lower()

        if key in TIDAL_ZONE_ALIASES:
            result[label] = TIDAL_ZONE_ALIASES[key]
        elif label in TIDAL_ZONE_COLORS:
            result[label] = TIDAL_ZONE_COLORS[label]
        else:
            result[label] = "#64748B"

    return result


def get_color_column(data, preferred_col):
    if preferred_col and preferred_col in data.columns:
        return preferred_col
    return None


def style_chart(fig):
    fig.update_layout(
        template="plotly_white",
        margin=dict(l=20, r=20, t=65, b=30),
        font=dict(family="Arial", size=12),
        legend_title_text="Tidal Zone",
    )
    return fig


def show_chart(fig):
    st.plotly_chart(
        style_chart(fig),
        use_container_width=True,
    )


def download_csv_button(dataframe, label, filename):
    st.download_button(
        label=label,
        data=dataframe.to_csv(
            index=False
        ).encode("utf-8-sig"),
        file_name=filename,
        mime="text/csv",
    )


def add_zone_color_args(data, zone_column):
    """Build consistent Plotly color arguments."""
    if zone_column and zone_column in data.columns:
        values = data[zone_column].dropna().astype(str).unique()
        return {
            "color": zone_column,
            "color_discrete_map": get_zone_colors(values),
        }
    return {}


# =========================================================
# 4. LOAD DATA
# =========================================================

if not CSV_PATH.exists():
    st.error("CSV-Datei nicht gefunden.")
    st.code(str(CSV_PATH))
    st.info(
        "Bitte prüfe, ob data/tidal_data.csv "
        "im Projektordner vorhanden ist."
    )
    st.stop()

try:
    df = load_csv(
        str(CSV_PATH),
        CSV_PATH.stat().st_mtime,
    )
except Exception as exc:
    st.error("Die CSV-Datei konnte nicht gelesen werden.")
    st.exception(exc)
    st.stop()

if df.empty:
    st.warning("Die CSV-Datei enthält keine Datensätze.")
    st.stop()

df.columns = [str(col).strip() for col in df.columns]

numeric_cols = df.select_dtypes(
    include=np.number
).columns.tolist()

date_col = find_column(
    df.columns,
    ["date", "year", "time", "period", "timestamp"],
)

zone_col = find_column(
    df.columns,
    ["tidal zone", "intertidal", "zone", "classification"],
)

basin_col = find_column(
    df.columns,
    ["basin", "region", "coastal area", "location"],
)

height_col = find_column(
    numeric_cols,
    ["height", "elevation", "level", "depth"],
)

area_col = find_column(
    numeric_cols,
    ["area", "surface"],
)


# =========================================================
# 5. SIDEBAR AND FILTERS
# =========================================================

st.sidebar.title("🌊 Coastal GIS")
st.sidebar.caption("Spatial & Temporal Analytics")
st.sidebar.caption("Author: Aram Mehraban")
st.sidebar.divider()

page = st.sidebar.radio(
    "Navigate",
    [
        "Executive Overview",
        "GIS & Spatial Analysis",
        "Temporal Analysis",
        "Statistical Analysis",
        "Data Quality",
        "Data Explorer",
        "Project Information",
    ],
)

st.sidebar.divider()
st.sidebar.caption("Portfolio project")
st.sidebar.caption("Synthetic dataset — demonstration only")

filtered = df.copy()

with st.sidebar.expander("Data Filters", expanded=True):

    if zone_col:
        zone_values = sorted(
            df[zone_col].dropna().astype(str).unique().tolist()
        )

        selected_zones = st.multiselect(
            "Tidal zone",
            options=zone_values,
            default=zone_values,
        )

        filtered = filtered[
            filtered[zone_col].astype(str).isin(selected_zones)
        ]

    if basin_col:
        basin_values = sorted(
            df[basin_col].dropna().astype(str).unique().tolist()
        )

        selected_basins = st.multiselect(
            "Basin / Region",
            options=basin_values,
            default=basin_values,
        )

        filtered = filtered[
            filtered[basin_col].astype(str).isin(selected_basins)
        ]


# =========================================================
# 6. GLOBAL HEADER
# =========================================================

st.markdown(
    """
    <div class="hero">
        <h1>Coastal Tidal Zones Analysis</h1>
        <p>GIS · Spatial Analysis · Temporal Data Analytics</p>
        <p>Interactive exploration of coastal tidal-zone data</p>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="author-line">
        <strong>Aram Mehraban</strong>
        &nbsp;| Author · GIS & Data Analytics Portfolio Project
    </div>
    """,
    unsafe_allow_html=True,
)

st.info(
    "Data transparency: This project uses synthetic data. "
    "Visual patterns demonstrate analytical methods and must not "
    "be interpreted as real-world environmental measurements."
)

if filtered.empty:
    st.warning(
        "No records match the selected filters. "
        "Adjust the filters in the sidebar."
    )
    st.stop()


# =========================================================
# 7. EXECUTIVE OVERVIEW
# =========================================================

if page == "Executive Overview":

    st.subheader("Executive Overview")
    st.write(
        "A high-level summary of the dataset, data completeness, "
        "numeric variables and project visualizations."
    )

    total_cells = filtered.size
    total_missing = int(filtered.isna().sum().sum())

    completeness = (
        100 * (1 - total_missing / total_cells)
        if total_cells
        else 0
    )

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Filtered records", f"{len(filtered):,}")
    c2.metric("Dataset columns", f"{len(df.columns):,}")
    c3.metric("Numeric variables", f"{len(numeric_cols):,}")
    c4.metric("Data completeness", f"{completeness:.1f}%")

    st.divider()

    left, right = st.columns(2)

    with left:
        st.markdown("#### Dataset Preview")
        st.dataframe(
            filtered.head(10),
            use_container_width=True,
            hide_index=True,
        )

    with right:
        st.markdown("#### Missing Values by Column")

        # Compatible with older pandas versions
        missing = filtered.isna().sum().reset_index()
        missing.columns = ["Column", "Missing Values"]
        missing = missing.sort_values(
            "Missing Values",
            ascending=False,
        )

        fig = px.bar(
            missing,
            x="Column",
            y="Missing Values",
            title="Missing values by column",
            color="Missing Values",
            color_continuous_scale="Teal",
        )
        fig.update_layout(xaxis_tickangle=-35)
        show_chart(fig)

    if numeric_cols:
        st.markdown("#### Numeric Data Summary")
        st.dataframe(
            filtered[numeric_cols].describe().T.round(3),
            use_container_width=True,
        )

    st.divider()
    st.markdown("#### Project Visualizations")

    image_files = (
        sorted(FIGURES_DIR.glob("*.png"))
        if FIGURES_DIR.exists()
        else []
    )

    if image_files:
        for start in range(0, len(image_files), 2):
            image_columns = st.columns(2)

            for offset, image_path in enumerate(
                image_files[start:start + 2]
            ):
                with image_columns[offset]:
                    st.image(
                        str(image_path),
                        caption=image_path.stem.replace("-", " "),
                        use_container_width=True,
                    )
    else:
        st.info("No PNG images were found in the figures folder.")


# =========================================================
# 8. GIS & SPATIAL ANALYSIS
# =========================================================

elif page == "GIS & Spatial Analysis":

    st.subheader("GIS & Spatial Analysis")

    if not GEOPANDAS_AVAILABLE:
        st.warning(
            "GeoPandas is not installed. Install requirements.txt "
            "and restart the application."
        )

    elif not GPKG_PATH.exists():
        st.warning("data/tidal_data.gpkg was not found.")

    else:
        try:
            gdf = load_gpkg(
                str(GPKG_PATH),
                GPKG_PATH.stat().st_mtime,
            )

            if gdf is None:
                st.warning("GeoPandas could not be loaded.")
                st.stop()

            geometry_types = (
                gdf.geometry.geom_type.dropna().unique().tolist()
                if not gdf.empty
                else []
            )

            valid_count = (
                int(gdf.geometry.is_valid.sum())
                if not gdf.empty
                else 0
            )

            c1, c2, c3 = st.columns(3)
            c1.metric("Spatial features", f"{len(gdf):,}")
            c2.metric("Valid geometries", f"{valid_count:,}")
            c3.metric("Geometry types", f"{len(geometry_types):,}")

            st.write("**Coordinate reference system:**", str(gdf.crs))
            st.write(
                "**Geometry types:**",
                ", ".join(geometry_types) if geometry_types else "N/A",
            )

            if gdf.empty or gdf.geometry.isna().all():
                st.warning("No usable geometry was found.")

            else:
                map_gdf = gdf[
                    gdf.geometry.notna()
                    & ~gdf.geometry.is_empty
                ].copy()

                if map_gdf.crs is not None:
                    map_gdf = map_gdf.to_crs("EPSG:4326")

                geometry_set = set(
                    map_gdf.geometry.geom_type.dropna().unique()
                )

                if geometry_set and geometry_set.issubset(
                    {"Point", "MultiPoint"}
                ):
                    st.markdown("#### Spatial Point Map")

                    point_gdf = map_gdf[
                        map_gdf.geometry.geom_type == "Point"
                    ].copy()

                    if not point_gdf.empty:
                        point_gdf["longitude"] = (
                            point_gdf.geometry.x
                        )
                        point_gdf["latitude"] = (
                            point_gdf.geometry.y
                        )

                        hover_cols = [
                            col for col in point_gdf.columns
                            if col not in [
                                "geometry",
                                "latitude",
                                "longitude",
                            ]
                        ][:8]

                        if zone_col and zone_col in point_gdf.columns:
                            fig = px.scatter_map(
                                point_gdf,
                                lat="latitude",
                                lon="longitude",
                                color=zone_col,
                                color_discrete_map=get_zone_colors(
                                    point_gdf[zone_col].dropna().unique()
                                ),
                                hover_data=hover_cols,
                                zoom=3,
                                height=520,
                                title="Spatial distribution of features",
                            )
                        else:
                            fig = px.scatter_map(
                                point_gdf,
                                lat="latitude",
                                lon="longitude",
                                hover_data=hover_cols,
                                zoom=3,
                                height=520,
                                title="Spatial distribution of features",
                            )

                        show_chart(fig)

                else:
                    st.info(
                        "The GeoPackage contains line or polygon "
                        "geometries. The saved GIS visualization is "
                        "shown below if available."
                    )

                    map_image = (
                        FIGURES_DIR
                        / "Tidal-Zone-GIS-Visualization.png"
                    )

                    if map_image.exists():
                        st.image(
                            str(map_image),
                            caption="Tidal Zone GIS Visualization",
                            use_container_width=True,
                        )

                st.markdown("#### Spatial Attribute Table")

                attributes = map_gdf.drop(
                    columns="geometry",
                    errors="ignore",
                )

                st.dataframe(
                    attributes.head(1000),
                    use_container_width=True,
                    hide_index=True,
                )

                download_csv_button(
                    attributes,
                    "Download spatial attributes as CSV",
                    "tidal_spatial_attributes.csv",
                )

        except Exception as exc:
            st.error("The GeoPackage could not be processed.")
            st.exception(exc)


# =========================================================
# 9. TEMPORAL ANALYSIS
# =========================================================

elif page == "Temporal Analysis":

    st.subheader("Temporal Analysis")

    if not date_col:
        st.warning("No likely date or year column was detected.")
        st.write("Available columns:", df.columns.tolist())

    elif not numeric_cols:
        st.warning("No numeric variables are available.")

    else:
        temporal = filtered.copy()

        temporal["_time"] = pd.to_datetime(
            temporal[date_col],
            errors="coerce",
        )

        if temporal["_time"].notna().sum() == 0:
            temporal["_time"] = pd.to_numeric(
                temporal[date_col],
                errors="coerce",
            )

        temporal = temporal.dropna(subset=["_time"])

        if temporal.empty:
            st.warning("No valid time values were found.")

        else:
            default_index = (
                numeric_cols.index(height_col)
                if height_col in numeric_cols
                else 0
            )

            chart_value = st.selectbox(
                "Variable to analyze",
                numeric_cols,
                index=default_index,
            )

            aggregation = st.selectbox(
                "Aggregation",
                ["Mean", "Median", "Sum", "Minimum", "Maximum"],
            )

            operation = {
                "Mean": "mean",
                "Median": "median",
                "Sum": "sum",
                "Minimum": "min",
                "Maximum": "max",
            }[aggregation]

            group_cols = ["_time"]
            if zone_col:
                group_cols.append(zone_col)

            trend = (
                temporal.groupby(
                    group_cols,
                    dropna=False,
                )[chart_value]
                .agg(operation)
                .reset_index()
            )

            color_args = add_zone_color_args(trend, zone_col)

            fig = px.line(
                trend,
                x="_time",
                y=chart_value,
                markers=True,
                title=f"{aggregation} {chart_value} over time",
                **color_args,
            )

            show_chart(fig)

            st.markdown("#### Aggregated Data")
            st.dataframe(
                trend,
                use_container_width=True,
                hide_index=True,
            )

            download_csv_button(
                trend,
                "Download temporal results",
                "tidal_temporal_analysis.csv",
            )


# =========================================================
# 10. STATISTICAL ANALYSIS
# =========================================================

elif page == "Statistical Analysis":

    st.subheader("Statistical Analysis")

    if not numeric_cols:
        st.warning("No numeric columns were detected.")

    else:
        default_index = (
            numeric_cols.index(height_col)
            if height_col in numeric_cols
            else 0
        )

        variable = st.selectbox(
            "Select numeric variable",
            numeric_cols,
            index=default_index,
        )

        c1, c2, c3, c4 = st.columns(4)

        c1.metric("Mean", format_number(filtered[variable].mean()))
        c2.metric("Median", format_number(filtered[variable].median()))
        c3.metric("Minimum", format_number(filtered[variable].min()))
        c4.metric("Maximum", format_number(filtered[variable].max()))

        color_args = add_zone_color_args(filtered, zone_col)

        left, right = st.columns(2)

        with left:
            fig = px.histogram(
                filtered,
                x=variable,
                marginal="box",
                title=f"Distribution of {variable}",
                barmode="overlay",
                opacity=0.75,
                **color_args,
            )

            show_chart(fig)

        with right:
            if zone_col:
                fig = px.box(
                    filtered,
                    x=zone_col,
                    y=variable,
                    color=zone_col,
                    color_discrete_map=get_zone_colors(
                        filtered[zone_col].dropna().unique()
                    ),
                    title=f"{variable} by tidal zone",
                )

                show_chart(fig)

            elif basin_col:
                fig = px.box(
                    filtered,
                    x=basin_col,
                    y=variable,
                    title=f"{variable} by basin",
                )

                show_chart(fig)

            else:
                st.info(
                    "No zone or basin column was detected "
                    "for group comparison."
                )

        if basin_col:
            st.markdown("#### Basin Comparison")

            comparison = (
                filtered.groupby(
                    basin_col,
                    dropna=False,
                )[variable]
                .agg(["count", "mean", "median", "min", "max"])
                .reset_index()
            )

            fig = px.bar(
                comparison,
                x=basin_col,
                y="mean",
                title=f"Mean {variable} by basin",
                color="mean",
                color_continuous_scale="Teal",
            )

            show_chart(fig)

            st.dataframe(
                comparison,
                use_container_width=True,
                hide_index=True,
            )


# =========================================================
# 11. DATA QUALITY
# =========================================================

elif page == "Data Quality":

    st.subheader("Data Quality Assessment")

    quality = pd.DataFrame({
        "Column": df.columns.tolist(),
        "Data type": [
            str(df[col].dtype) for col in df.columns
        ],
        "Missing values": [
            int(df[col].isna().sum()) for col in df.columns
        ],
        "Missing (%)": [
            round(df[col].isna().mean() * 100, 2)
            for col in df.columns
        ],
        "Unique values": [
            int(df[col].nunique(dropna=True))
            for col in df.columns
        ],
    })

    total_missing = int(df.isna().sum().sum())
    total_cells = df.size

    completeness = (
        100 * (1 - total_missing / total_cells)
        if total_cells
        else 0
    )

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Total rows", f"{len(df):,}")
    c2.metric("Total columns", f"{len(df.columns):,}")
    c3.metric("Missing cells", f"{total_missing:,}")
    c4.metric("Completeness", f"{completeness:.2f}%")

    st.metric(
        "Duplicate rows",
        f"{int(df.duplicated().sum()):,}",
    )

    st.markdown("#### Column-Level Quality")

    st.dataframe(
        quality,
        use_container_width=True,
        hide_index=True,
    )

    fig = px.bar(
        quality,
        x="Column",
        y="Missing (%)",
        title="Missing percentage by column",
        color="Missing (%)",
        color_continuous_scale="Teal",
    )

    fig.update_layout(xaxis_tickangle=-35)
    show_chart(fig)

    if numeric_cols:
        st.markdown("#### Numeric Summary")
        st.dataframe(
            df[numeric_cols].describe().T.round(3),
            use_container_width=True,
        )


# =========================================================
# 12. DATA EXPLORER
# =========================================================

elif page == "Data Explorer":

    st.subheader("Data Explorer")

    st.caption(
        f"Showing {len(filtered):,} filtered rows "
        f"out of {len(df):,} total rows."
    )

    search = st.text_input(
        "Search across text columns",
        placeholder="Enter a keyword...",
    )

    display_df = filtered.copy()

    if search.strip():
        text_cols = display_df.select_dtypes(
            include=["object", "string"]
        ).columns.tolist()

        if text_cols:
            mask = (
                display_df[text_cols]
                .astype(str)
                .apply(
                    lambda col: col.str.contains(
                        search,
                        case=False,
                        na=False,
                        regex=False,
                    )
                )
                .any(axis=1)
            )

            display_df = display_df[mask]
        else:
            st.info("No text columns are available for keyword search.")

    st.dataframe(
        display_df,
        use_container_width=True,
        height=480,
        hide_index=True,
    )

    download_csv_button(
        display_df,
        "Download filtered data as CSV",
        "tidal_data_filtered.csv",
    )


# =========================================================
# 13. PROJECT INFORMATION
# =========================================================

elif page == "Project Information":

    st.subheader("About This Project")

    st.markdown(
        """
        This portfolio project demonstrates a Python-based GIS and
        data analytics workflow for exploring coastal tidal-zone data.

        **Data transparency:** The dataset is synthetic and is used to
        demonstrate analytical methods. It is not a real-world coastal
        monitoring dataset.

        **Project focus**
        - Data exploration and quality assessment
        - Spatial feature inspection using GeoPandas
        - Temporal aggregation and trend visualization
        - Statistical distribution analysis
        - Interactive data exploration with Streamlit
        """
    )

    st.markdown("#### Author")
    st.write("Aram Mehraban")
    st.write("GIS & Data Analytics Portfolio Project")

    st.markdown("#### Technologies")
    st.write(
        "Python · Pandas · NumPy · GeoPandas · Shapely · "
        "Plotly · Streamlit · GeoPackage"
    )

    st.markdown("#### GitHub Repository")
    st.markdown(f"[View source code on GitHub]({GITHUB_URL})")

    st.markdown("#### Project Files")
    st.write("CSV available:", CSV_PATH.exists())
    st.write("GeoPackage available:", GPKG_PATH.exists())
    st.write("Figures directory available:", FIGURES_DIR.exists())


# =========================================================
# 14. FOOTER
# =========================================================

st.divider()

st.caption(
    "Coastal Tidal Zones Analysis | Aram Mehraban | "
    "GIS & Data Analytics Portfolio | "
    "Synthetic data — demonstration only"
)
