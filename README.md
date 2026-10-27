# CodeNova Task 1: Palmer Penguins Exploratory Data Analysis

## Project Overview

This project performs Exploratory Data Analysis (EDA) on the Palmer Penguins dataset as part of the CodeNova AI/ML internship.

The analysis explores penguin measurements across three species: Adelie, Chinstrap, and Gentoo. It includes data profiling, missing-value treatment, duplicate checks, IQR-based outlier detection, summary statistics, and visualizations.

## Dataset

The dataset contains 344 rows and 8 columns, including species, island, bill measurements, flipper length, body mass, sex, and year.

## Tech Stack

- Python
- pandas
- Matplotlib
- Seaborn
- Jupyter Notebook

## Project Structure

```text
CodeNova-Task1-Penguins-EDA/
├── data/
│   └── penguins.csv
├── src/
│   └── penguins_eda.py
├── notebooks/
│   └── penguins_eda.ipynb
├── outputs/
│   ├── figures/
│   ├── penguins_cleaned.csv
│   ├── penguins_missing_values.csv
│   ├── penguins_outlier_report.csv
│   └── penguins_species_summary.csv
└── README.md
```

## Analysis Performed

- Inspected dataset dimensions, data types, and summary statistics.
- Checked for missing values and duplicate rows.
- Filled missing numerical values using column medians and missing categorical values using the mode.
- Detected potential outliers using the 1.5 × IQR rule.
- Generated a correlation heatmap, feature distribution histograms, species-based boxplots, and pairwise scatterplots.
- Compared average numerical measurements across species.

## Key Findings

- The original dataset contains 19 missing cells and no duplicate rows.
- After imputation, the cleaned dataset contains no missing cells.
- The IQR method detected zero potential outliers in the four numerical measurements examined.
- Gentoo penguins had the highest average body mass, approximately 5,067.74 g, compared with 3,702.96 g for Adelie and 3,733.09 g for Chinstrap penguins.

## How to Run

Install the required packages:

```bash
python -m pip install pandas matplotlib seaborn jupyter
```

Run the analysis script from the project root:

```bash
python src/penguins_eda.py
```

Alternatively, open `notebooks/penguins_eda.ipynb` in VS Code or Jupyter Notebook and run the cells.

## Output Files

The `outputs/` directory contains the cleaned dataset, missing-value report, outlier report, species summary, and four visualization images in `outputs/figures/`.

## Limitations

This is a descriptive analysis. Missing-value imputation may affect distributions and correlations, and the absence of IQR-flagged outliers does not prove that every observation is free of anomalies. The analysis does not establish causal relationships.
