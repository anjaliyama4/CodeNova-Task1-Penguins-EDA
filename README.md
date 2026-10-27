# CodeNova AI/ML Internship — Task 1: Exploratory Data Analysis

## Project overview
This project performs exploratory data analysis (EDA) on the public Iris flower dataset. It profiles the dataset, checks missing values and duplicates, detects potential numeric outliers using the interquartile range (IQR), creates the four required visualization types, and records observations supported by the data.

## Dataset
- **Name:** Iris flower dataset
- **Source:** `sklearn.datasets.load_iris`, a public educational dataset distributed with scikit-learn.
- **Observations:** 150 flower samples in the standard dataset.
- **Features:** sepal length, sepal width, petal length, and petal width (centimeters).
- **Label:** species (`setosa`, `versicolor`, `virginica`).
- **External download/API:** not required; the dataset is bundled with scikit-learn.
- The script exports a local CSV copy to `data/iris.csv` so it can be inspected and reused.

## Tech stack
- Python
- Pandas and NumPy
- Matplotlib and Seaborn
- scikit-learn (dataset loader)
- Jupyter Notebook

## Project structure
```text
CodeNova-Task1-EDA/
├── data/
│   └── iris.csv                 # generated when analysis runs
├── notebooks/
│   └── CodeNova_Task1_EDA.ipynb # executed notebook
├── outputs/
│   ├── figures/                 # high-resolution PNG charts
│   ├── outlier_report.csv
│   └── species_mean_measurements.csv
├── src/
│   └── eda_analysis.py          # repeatable Python analysis script
├── .gitignore
├── README.md
└── requirements.txt
```

## Setup in VS Code

### 1. Create and activate a virtual environment
**Windows PowerShell**
```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**macOS/Linux**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 2. Install dependencies
```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 3. Run the analysis script
```bash
python src/eda_analysis.py
```

The script creates `data/iris.csv`, the four PNG charts under `outputs/figures/`, and summary CSV files under `outputs/`.

### 4. Open and run the notebook
Open `notebooks/CodeNova_Task1_EDA.ipynb` in VS Code. Select the `.venv` Python kernel and use **Run All**. The notebook includes code, outputs, and Markdown commentary.

## Analysis workflow
1. Load the dataset and inspect its shape, columns, types, and summary statistics.
2. Count missing values and exact duplicate rows.
3. Apply a documented duplicate-handling decision; do not impute missing values when none are present.
4. Detect potential outliers using the 1.5 × IQR rule. IQR flags are review signals, not proof that a value is erroneous.
5. Create:
   - Correlation heatmap
   - Feature distribution plots
   - Boxplots grouped by species
   - Pairwise scatter plots
6. Compare mean measurements by species and report empirical patterns.

## Findings (verify against the notebook output)
- The standard Iris dataset contains 150 observations, four numerical measurements, and a species label.
- The three species have 50 observations each in the standard dataset.
- Petal length and petal width show a strong positive relationship in this dataset.
- Pairwise plots and grouped boxplots help show that petal measurements distinguish the species more clearly than some sepal measurements.
- IQR flags are reported by feature. Do not automatically delete flagged observations: a statistical outlier can be a valid flower measurement.
- Missing values and duplicates are measured at runtime. The cleaning report should be updated if the input data changes.

Use the exact numerical outputs from your executed notebook when writing final conclusions. Avoid claiming correlation proves causation.

## Deliverables checklist
- [x] Executable Python analysis script
- [x] Jupyter notebook with code, executed outputs, and Markdown commentary
- [x] Dataset profiling and data quality checks
- [x] IQR outlier detection report
- [x] Four high-resolution visualization types
- [x] README with setup, methodology, and findings
- [ ] Run all notebook cells in your own VS Code environment and verify outputs
- [ ] Review charts and tailor findings to observed values
- [ ] Push the project to a **public** GitHub repository
- [ ] Add screenshots or a demo link if applicable
- [ ] Check Git history for credentials (none are needed for this project)

## Reproducibility and limitations
The dataset is small and curated for learning. It is useful for demonstrating EDA but does not represent all real-world data quality problems. Outlier flags depend on the IQR rule and should be interpreted with domain context. Correlation describes association, not causation. No paid API, paid software, or paid hosting is required.

## License and attribution
The Iris dataset is distributed through scikit-learn. See the [scikit-learn dataset documentation](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_iris.html) for details. This repository's code is provided for educational use; retain appropriate dataset attribution when redistributing.
