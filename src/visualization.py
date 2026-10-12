import matplotlib.pyplot as plt
import seaborn as sns

def create_plots(df, gdf):

    # ================= Trend Plot =================
    plt.figure(figsize=(8,5))

    for zone in df["Zone"].unique():
        subset = df[df["Zone"] == zone]
        trend = subset.groupby("Year")["Area"].mean()
        plt.plot(trend.index, trend.values, marker="o", label=zone)

    plt.title("Coastal Zone Area Change Over Time")
    plt.xlabel("Year")
    plt.ylabel("Area")
    plt.legend()
    plt.grid()
    plt.show()

    # ================= Boxplot =================
    plt.figure(figsize=(8,5))
    sns.boxplot(data=gdf, x="Zone", y="Height")
    plt.title("Height Distribution by Zone")
    plt.show()

    # ================= Violin =================
    plt.figure(figsize=(8,5))
    sns.violinplot(data=gdf, x="Zone", y="Height", inner="quartile")
    plt.title("Height Distribution Shape")
    plt.show()