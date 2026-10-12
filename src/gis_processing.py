import geopandas as gpd
from shapely.geometry import Point
from pathlib import Path

def create_gis_data(df):
    base_path = Path(__file__).resolve().parents[1]
    data_path = base_path / "data"

    coords = {
        "Subtidal": (2, 2),
        "Intertidal": (1, 1),
        "Supratidal": (3, 3)
    }

    df["geometry"] = df["Zone"].map(lambda z: Point(coords[z]))

    gdf = gpd.GeoDataFrame(df, geometry="geometry", crs="EPSG:4326")

    gdf.to_file(data_path / "tidal_data.gpkg", layer="tidal_zones", driver="GPKG")

    return gdf