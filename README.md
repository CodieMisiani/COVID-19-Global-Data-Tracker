# COVID-19-Global-Data-Tracker

# Data Analysis Assignment

## Project Overview

This project involves analyzing a dataset using Python. The analysis includes:

- Loading the dataset
- Handling missing values
- Computing basic statistics
- Visualizing the data
- Documenting findings

## Steps Performed

1. **Load Data**: The dataset is loaded using `pandas.read_csv()`.
2. **Handle Missing Values**: Missing values are handled using `dropna()` or `fillna()`.
3. **Compute Statistics**: Basic statistics are computed using `describe()` and `groupby()`.
4. **Visualize Data**:
   - **Line Chart**: Sepal length over samples.
   - **Bar Chart**: Average petal length by species.
   - **Histogram**: Distribution of sepal width.
   - **Scatter Plot**: Sepal length vs petal length.
5. **Document Findings**:
   - The petal length increases with sepal length.
   - Species 1 shows a wider variation in sepal width.

## Tools Used

- **pandas**: For data loading and manipulation.
- **matplotlib.pyplot**: For visualizations.
- **seaborn** (optional): For enhanced visualizations.
- **git + GitHub**: For version control and backup.

## Git Commit Messages

| Task               | Commit Message                                   |
| ------------------ | ------------------------------------------------ |
| Load data          | `Load Iris dataset into dataframe`               |
| Clean data         | `Handle missing values using dropna()`           |
| Compute statistics | `Compute basic statistics and group by species`  |
| Visualize data     | `Create 4 charts: line, bar, histogram, scatter` |
| Document findings  | `Document findings and insights from analysis`   |

## Final Steps

- Ensure all visualizations have proper titles, labels, and legends.
- Push all changes to GitHub.
- Submit the `.py` file or `.ipynb` file to your lecturer.

## Folder Structure

data-analysis-assignment/ │ ├── analysis.py ├── iris_analysis.py ├── README.md ├── data/ │ └── yourfile.csv
