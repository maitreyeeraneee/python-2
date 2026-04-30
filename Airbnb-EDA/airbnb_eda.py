import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def load_data(file_path: str = "AB_NYC_2019.csv") -> pd.DataFrame:
    """Load the Airbnb NYC dataset."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Data file {file_path} not found.")
    df = pd.read_csv(file_path)
    print(f"Dataset loaded: {df.shape[0]} rows, {df.shape[1]} columns")
    print("\nDataset info:")
    print(df.dtypes)
    print("\nFirst few rows:")
    print(df.head())
    print("\nBasic stats:")
    print(df.describe())
    return df


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Clean the dataset: handle missing values and remove price outliers."""
    print("\nMissing values before cleaning:")
    print(df.isnull().sum())
    
    df_clean = df.copy()
    df_clean["host_name"] = df_clean["host_name"].fillna("Unknown")
    df_clean["name"] = df_clean["name"].fillna("No Name")
    df_clean["last_review"] = df_clean["last_review"].fillna("No Review")
    df_clean["reviews_per_month"] = df_clean["reviews_per_month"].fillna(0)
    
    print("\nMissing values after cleaning:")
    print(df_clean.isnull().sum())
    
    # Remove price outliers (<500 as in original)
    print(f"\nPrice stats before outlier removal:")
    print(df_clean["price"].describe())
    df_clean = df_clean[df_clean["price"] < 500]
    print(f"Shape after outlier removal: {df_clean.shape}")
    print(f"Price stats after outlier removal:")
    print(df_clean["price"].describe())
    
    print("\nUnique neighbourhood_groups:", df_clean["neighbourhood_group"].unique())
    print("Unique room_types:", df_clean["room_type"].unique())
    
    return df_clean


def analyze(df: pd.DataFrame) -> dict:
    """Perform EDA analyses and return results."""
    results = {}
    
    # Average price by neighbourhood group
    results["avg_price_neigh"] = df.groupby("neighbourhood_group")["price"].mean()
    print("\nAverage Price by Neighbourhood Group:")
    print(results["avg_price_neigh"])
    
    # Room type distribution
    results["room_dist"] = df["room_type"].value_counts()
    print("\nRoom Type Distribution:")
    print(results["room_dist"])
    
    # Top 10 reviewed listings
    results["top_reviews"] = df.sort_values("number_of_reviews", ascending=False)[
        ["name", "room_type", "neighbourhood_group", "number_of_reviews"]
    ].head(10)
    print("\nTop 10 Reviewed Listings:")
    print(results["top_reviews"])
    
    # Average availability by neighbourhood group
    results["avg_availability"] = df.groupby("neighbourhood_group")["availability_365"].mean()
    print("\nAverage Availability by Neighbourhood Group:")
    print(results["avg_availability"])
    
    # Top 10 most expensive neighbourhoods
    results["expensive_neigh"] = df.groupby("neighbourhood")["price"].mean().sort_values(ascending=False).head(10)
    print("\nTop 10 Most Expensive Neighbourhoods:")
    print(results["expensive_neigh"])
    
    # Pivot table: avg price by room_type x neighbourhood_group
    results["pivot_table"] = pd.pivot_table(
        df, values="price", index="room_type", columns="neighbourhood_group", aggfunc="mean"
    )
    print("\nPivot Table (Avg Price by Room Type x Neighbourhood Group):")
    print(results["pivot_table"])
    
    # Price stats per neighbourhood_group (optimized with groupby.describe().unstack())
    results["price_stats_per_group"] = df.groupby("neighbourhood_group")["price"].describe().unstack()
    print("\nPrice Statistics per Neighbourhood Group (Q1, median, Q3):")
    print(results["price_stats_per_group"][["25%", "50%", "75%"]])
    
    # Top 10 most reviewed listings (nlargest as original) + avg price
    results["top_reviewed_listings"] = df.nlargest(10, "number_of_reviews")[["name", "host_name", "neighbourhood_group", "room_type", "number_of_reviews", "price"]]
    print("\nTop 10 Most Reviewed Listings (detailed):")
    print(results["top_reviewed_listings"])
    print(f"Average price of top reviewed: ${results['top_reviewed_listings']['price'].mean():.2f}")
    
    return results


def visualize(df: pd.DataFrame, results: dict):
    """Create and save all visualizations."""
    # Ensure output dir exists (current cwd)
    os.makedirs("plots", exist_ok=True)
    
    # 1. Violin plot: price density by neighbourhood_group
    plt.figure(figsize=(10, 6))
    sns.violinplot(data=df, x="neighbourhood_group", y="price")
    plt.title("Density and Distribution of Prices by Neighbourhood Group")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("plots/neighbourhood_price_density.png", dpi=300, bbox_inches="tight")
    plt.show()
    plt.close()
    
    # 2. Catplot: count by top 10 neighbourhoods x room_type x group
    top_neigh = df["neighbourhood"].value_counts().head(10).index.tolist()
    sub_top = df[df["neighbourhood"].isin(top_neigh)]
    g = sns.catplot(x="neighbourhood", hue="neighbourhood_group", col="room_type", 
                    data=sub_top, kind="count", height=4, aspect=1.5)
    g.set_xticklabels(rotation=45)
    g.tight_layout()
    g.savefig("plots/top_neigh_room_dist.png", dpi=300, bbox_inches="tight")
    plt.close()
    
    # 3. Price distribution histogram
    plt.figure(figsize=(10, 6))
    sns.histplot(df["price"], bins=50, kde=True)
    plt.title("Price Distribution of Airbnb Listings")
    plt.xlabel("Price ($)")
    plt.tight_layout()
    plt.savefig("plots/price_distribution.png", dpi=300, bbox_inches="tight")
    plt.show()
    plt.close()
    
    # 4. Room type distribution
    plt.figure(figsize=(8, 6))
    sns.countplot(x="room_type", data=df)
    plt.title("Room Type Distribution")
    plt.tight_layout()
    plt.savefig("plots/room_type_distribution.png", dpi=300, bbox_inches="tight")
    plt.show()
    plt.close()
    
    # 5. Average price by neighbourhood group
    plt.figure(figsize=(10, 6))
    sns.barplot(x="neighbourhood_group", y="price", data=df)
    plt.title("Average Price by Neighbourhood Group")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("plots/neighbourhood_price.png", dpi=300, bbox_inches="tight")
    plt.show()
    plt.close()
    
    # 6. Correlation heatmap
    numeric_df = df.select_dtypes(include="number")
    plt.figure(figsize=(12, 10))
    sns.heatmap(numeric_df.corr(), annot=True, cmap="coolwarm", center=0, fmt=".2f")
    plt.title("Feature Correlation Heatmap")
    plt.tight_layout()
    plt.savefig("plots/correlation_heatmap.png", dpi=300, bbox_inches="tight")
    plt.show()
    plt.close()
    
    # 7. Geo scatter: lat/long colored by price
    plt.figure(figsize=(12, 8))
    df.plot(kind="scatter", x="longitude", y="latitude", c="price",
            cmap="jet", colorbar=True, alpha=0.5, s=10)
    plt.title("Geographical Distribution Colored by Price")
    plt.xlabel("Longitude")
    plt.ylabel("Latitude")
    plt.tight_layout()
    plt.savefig("plots/geo_price_scatter.png", dpi=300, bbox_inches="tight")
    plt.show()
    plt.close()
    
    print("\nAll visualizations saved as PNG files.")


def main():
    """Main function to run the Airbnb NYC EDA."""
    try:
        df = load_data()
        df_clean = clean_data(df)
        analysis_results = analyze(df_clean)
        visualize(df_clean, analysis_results)
        print("\nEDA complete! Check console outputs and PNG files.")
    except Exception as e:
        print(f"Error during EDA: {e}")


if __name__ == "__main__":
    main()

