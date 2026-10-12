from analysis import run_analysis
from gis_processing import create_gis_data
from visualization import create_plots

def main():
    print("Starting Tidal Zones Analysis...")

    df = run_analysis()
    gdf = create_gis_data(df)
    create_plots(df, gdf)

    print("Project completed successfully.")

if __name__ == "__main__":
    main()