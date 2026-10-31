# CodeNova Task 1 — Exploratory Data Analysis

## Project Overview
This project performs Exploratory Data Analysis (EDA) on the Palmer Penguins dataset. It examines data quality, handles missing values, checks duplicates, detects potential outliers, and explores relationships between penguin measurements.

## Dataset
The dataset contains 344 rows and 8 columns, including:
- Species and island
- Bill length and bill depth (mm)
- Flipper length (mm)
- Body mass (g)
- Sex and year

The dataset includes naturally occurring missing values.

## Analysis Performed
1. Dataset profiling: shape, data types, summary statistics, and missing-value counts.
2. Data cleaning: duplicate removal and missing-value imputation.
3. Outlier detection using the 1.5 × IQR rule.
4. Correlation heatmap for numerical measurements.
5. Feature distribution plots.
6. Boxplots comparing measurements by species.
7. Pairwise scatterplots of numerical measurements.
8. Mean measurement summaries by species.

## Missing-Value Handling
The original dataset contained 19 missing cells. Numerical columns with missing values were filled using their respective medians. Missing categorical values were filled using the most frequent category (mode). After cleaning, no missing cells remained.

The original dataset is preserved. The cleaned dataset is saved separately as `outputs/penguins_cleaned.csv`.

## Outlier Detection
Potential outliers were checked using the Interquartile Range (IQR) method. Values below Q1 − 1.5 × IQR or above Q3 + 1.5 × IQR were flagged. No potential outliers were detected in the four numerical measurements examined. No outliers were removed.

## Key Findings
- Gentoo penguins had the highest mean body mass, approximately 5,068 g.
- Adelie penguins had a mean body mass of approximately 3,703 g.
- Chinstrap penguins had a mean body mass of approximately 3,733 g.
- The correlation heatmap and scatterplots can be used to examine relationships between flipper length, body mass, and bill measurements.

## Project Structure
- `data/penguins.csv` — original dataset
- `src/penguins_eda.py` — analysis script
- `outputs/penguins_cleaned.csv` — cleaned dataset
- `outputs/penguins_missing_values.csv` — missing-value report
- `outputs/penguins_outlier_report.csv` — outlier report
- `outputs/penguins_species_summary.csv` — species mean measurements
- `outputs/figures/` — generated visualizations

## How to Run
From the project root, run:

```bash
python src/penguins_eda.py
```

Required Python packages: pandas, matplotlib, and seaborn.

## Conclusion
The analysis demonstrates dataset profiling, missing-value handling, duplicate checks, outlier detection, and visualization of penguin measurements. Visual findings should be interpreted in the context of the dataset and its limitations.

## Project Visualizations

### 1. Correlation Heatmap
![Correlation Heatmap](outputs/figures/01_correlation_heatmap.png)

### 2. Feature Distributions
![Feature Distributions](outputs/figures/02_feature_distributions.png)

### 3. Boxplots by Species
![Boxplots by Species](outputs/figures/03_boxplots_by_species.png)

### 4. Pairwise Scatterplots
![Pairwise Scatterplots](outputs/figures/04_pairwise_scatterplots.png)
