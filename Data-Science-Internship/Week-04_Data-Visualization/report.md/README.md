# Week 4 – Complete Data Analysis Project

## Project Overview
For this project, I selected a dataset from Kaggle and performed a complete data analysis workflow. This included loading the dataset, cleaning missing values, exploring basic statistics, and visualizing the data using Python libraries. Clear and structured graphs were plotted to reveal meaningful insights from the data.

---

## Setup and Installation

1. Anaconda was installed to provide a Python environment.
2. Jupyter Notebook was launched using Anaconda Navigator.
3. Required libraries were installed using pip:
   - pandas
   - matplotlib
   - seaborn
   - plotly
4. Libraries were imported in the notebook using Python `import` statements.
5. The London Weather dataset was loaded from a CSV file using Pandas.

---

## Code Structure Explanation

The project follows a simple and organized structure:

- **Data_visualization.ipynb**  
  Contains the Python code for data loading, cleaning, analysis, and visualization.

- **london_weather.csv**  
  Dataset used for analysis.

- **analysis_report.md**  
  Documentation explaining the analysis process and findings.

- **screenshots/**  
  Folder containing screenshots of program output and visualizations.

---

## Technical Requirements Fulfilled

- Used Pandas to load and analyze data  
- Checked and handled missing values using different imputation strategies  
- Removed unnecessary columns  
- Calculated multiple metrics including:
  - Maximum temperature across months
  - Cloud cover across months
  - Snow depth across months
  - Global radiation across months
- Created visualizations using box plots and bar charts  
- Added comments to explain analysis steps

---

## Screenshots of Working Application

Screenshots were taken to demonstrate:

- Dataset loading
- Summary statistics
- Analysis output
- Data visualizations

All screenshots are stored in the **screenshots/** folder.

---

## Initial Data Analysis

The London Weather dataset from Kaggle contains **15,341 rows and 10 columns** with integer and float data types. Several columns contained missing values, making data cleaning a crucial preprocessing step.

Different imputation techniques were applied based on the nature of each feature:

- Mean imputation
- Median imputation
- Forward fill
- Backward fill

After cleaning the dataset, exploratory data analysis was performed. This included generating summary statistics, examining data distributions, and creating visualizations such as line charts, box plots, and distribution plots. These analyses helped identify seasonal patterns, temperature variations, and overall weather trends.

---

## Conclusion

This project successfully demonstrates a complete data analysis workflow—from data loading and preprocessing to visualization and insight generation. The use of multiple visualization techniques and proper handling of missing data enabled meaningful interpretation of weather trends, fulfilling all technical and documentation requirements of Week 4.

