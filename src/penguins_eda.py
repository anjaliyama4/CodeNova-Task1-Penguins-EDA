
from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Project folders
PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = PROJECT_DIR / "data" / "penguins.csv"
OUTPUT_DIR = PROJECT_DIR / "outputs"
FIGURE_DIR = OUTPUT_DIR / "figures"

OUTPUT_DIR.mkdir(exist_ok=True)
FIGURE_DIR.mkdir(parents=True, exist_ok=True)

sns.set_theme(style="whitegrid")

# 1. Load and profile the dataset
df = pd.read_csv(DATA_FILE)

print("\n===== ORIGINAL DATASET PROFILE =====")
print("Shape:", df.shape)
print("\nData types:\n", df.dtypes)
print("\nMissing values:\n", df.isnull().sum())
print("\nDuplicate rows:", df.duplicated().sum())
print("\nSummary statistics:\n", df.describe(include="all"))

# Save the original missing-value report
df.isnull().sum().rename("missing_count").to_csv(
    OUTPUT_DIR / "penguins_missing_values.csv"
)

# 2. Remove exact duplicate rows
cleaned = df.drop_duplicates().copy()
print("\nRows after duplicate removal:", len(cleaned))

# Numerical measurements used for EDA
measurements = [
    "bill_length_mm",
    "bill_depth_mm",
    "flipper_length_mm",
    "body_mass_g",
]
measurements = [c for c in measurements if c in cleaned.columns]

# 3. Detect potential outliers using the IQR method
outlier_rows = []

for column in measurements:
    values = cleaned[column].dropna()
    q1 = values.quantile(0.25)
    q3 = values.quantile(0.75)
    iqr = q3 - q1
    lower = q1 - 1.5 * iqr
    upper = q3 + 1.5 * iqr
    count = int(((values < lower) | (values > upper)).sum())

    outlier_rows.append({
        "feature": column,
        "Q1": q1,
        "Q3": q3,
        "IQR": iqr,
        "lower_bound": lower,
        "upper_bound": upper,
        "potential_outlier_count": count,
    })

outlier_report = pd.DataFrame(outlier_rows)
outlier_report.to_csv(OUTPUT_DIR / "penguins_outlier_report.csv", index=False)
print("\n===== POTENTIAL OUTLIERS =====")
print(outlier_report.to_string(index=False))

# 4. Handle missing values
missing_before = int(cleaned.isnull().sum().sum())

for column in cleaned.columns:
    if cleaned[column].isnull().any():
        if pd.api.types.is_numeric_dtype(cleaned[column]):
            cleaned[column] = cleaned[column].fillna(
                cleaned[column].median()
            )
        else:
            mode_values = cleaned[column].mode(dropna=True)
            if not mode_values.empty:
                cleaned[column] = cleaned[column].fillna(mode_values.iloc[0])

missing_after = int(cleaned.isnull().sum().sum())

print("\nMissing cells before imputation:", missing_before)
print("Missing cells after imputation:", missing_after)

cleaned.to_csv(OUTPUT_DIR / "penguins_cleaned.csv", index=False)

# 5. Correlation heatmap
if len(measurements) >= 2:
    plt.figure(figsize=(9, 7))
    sns.heatmap(
        cleaned[measurements].corr(),
        annot=True,
        fmt=".2f",
        cmap="coolwarm",
        vmin=-1,
        vmax=1,
    )
    plt.title("Penguin Measurement Correlation Heatmap")
    plt.tight_layout()
    plt.savefig(FIGURE_DIR / "01_correlation_heatmap.png", dpi=300)
    plt.close()

# 6. Feature distributions
if measurements:
    cleaned[measurements].hist(
        figsize=(11, 8), bins=20, edgecolor="black"
    )
    plt.suptitle("Distributions of Penguin Measurements")
    plt.tight_layout()
    plt.savefig(FIGURE_DIR / "02_feature_distributions.png", dpi=300)
    plt.close()

# 7. Boxplots by species
if measurements and "species" in cleaned.columns:
    plot_data = cleaned.melt(
        id_vars="species",
        value_vars=measurements,
        var_name="measurement",
        value_name="value",
    )
    plt.figure(figsize=(12, 7))
    sns.boxplot(data=plot_data, x="measurement", y="value", hue="species")
    plt.title("Penguin Measurements by Species")
    plt.xlabel("Measurement")
    plt.ylabel("Value (original units)")
    plt.xticks(rotation=15)
    plt.tight_layout()
    plt.savefig(FIGURE_DIR / "03_boxplots_by_species.png", dpi=300)
    plt.close()

# 8. Pairwise scatterplots
if len(measurements) >= 2:
    pair_columns = measurements.copy()
    if "species" in cleaned.columns:
        pair_columns.append("species")

    pair_plot = sns.pairplot(
        cleaned[pair_columns],
        hue="species" if "species" in cleaned.columns else None,
        diag_kind="hist",
        corner=True,
    )
    pair_plot.fig.suptitle(
        "Pairwise Relationships Between Penguin Measurements", y=1.02
    )
    pair_plot.savefig(
        FIGURE_DIR / "04_pairwise_scatterplots.png", dpi=300
    )
    plt.close("all")

# 9. Species summary
if "species" in cleaned.columns and measurements:
    species_summary = cleaned.groupby("species")[measurements].mean()
    species_summary.to_csv(OUTPUT_DIR / "penguins_species_summary.csv")
    print("\n===== MEAN MEASUREMENTS BY SPECIES =====")
    print(species_summary)

# 10. Final checks
print("\n===== FINAL DATA QUALITY CHECK =====")
print("Final shape:", cleaned.shape)
print("Remaining missing cells:", cleaned.isnull().sum().sum())
print("Remaining duplicate rows:", cleaned.duplicated().sum())
print("\nCleaned data and reports saved in:", OUTPUT_DIR)
print("Charts saved in:", FIGURE_DIR)
print("\nAnalysis complete!")
