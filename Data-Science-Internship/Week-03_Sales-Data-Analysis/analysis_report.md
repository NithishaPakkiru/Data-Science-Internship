# Sales Data Analysis Report

## Project Overview
This project is part of Week 03 of the Data Science Internship.  
The goal of this project is to introduce basic data analysis using real-world sales data.  
The analysis focuses on understanding sales trends, customer behavior, and product performance using Python and Pandas.

---

## Objective
The objective of this project is to analyze a simple sales dataset obtained from Kaggle to uncover key business insights. The analysis includes:

- Loading and cleaning the dataset
- Identifying missing values, duplicates, and inconsistencies
- Removing unnecessary columns
- Examining sales performance across branches and genders
- Evaluating product-line performance
- Visualizing findings using bar charts and pie charts

The final goal is to help the business make informed, data-driven decisions to improve overall sales performance.

---

## Setup and Installation Instructions

1. Anaconda was installed to provide a Python environment.
2. Jupyter Notebook was launched using Anaconda Navigator.
3. Required libraries were installed using pip:
   - pandas
   - matplotlib
   - seaborn
4. Libraries were imported using Python import statements.
5. The dataset was loaded from a CSV file using Pandas.

---

## Code Structure Explanation

The project follows a simple and organized structure:

- **sales_analysis.py** – Python code for data loading, cleaning, analysis, and visualization
- **sales_data.csv** – Dataset used for analysis
- **analysis_report.md** – Documentation explaining analysis and findings
- **screenshots/** – Folder containing screenshots of output and visualizations

---

## Technical Requirements Fulfilled

- Used Pandas to load and analyze data
- Checked and handled missing values
- Removed unnecessary columns
- Calculated multiple metrics including:
  - Total sales
  - Sales by product line
  - Sales by branch
  - Sales by gender
- Created visualizations using bar charts and pie charts
- Added comments to explain analysis steps

---

## Screenshots of Working Application

Screenshots were taken to demonstrate:
- Dataset loading
- Summary statistics
- Sales analysis output
- Data visualizations

All screenshots are stored in the `screenshots` folder.

---

## Initial Dataset Exploration

After loading the dataset, the following observations were made:

- The dataset contains **1000 rows and 17 columns**
- There are no missing values or duplicates
- The dataset contains numerical, categorical, and date fields
- Unnecessary columns were removed to keep the dataset clean and focused
- Pandas, Matplotlib, and Seaborn were used for analysis and visualization

The data is clean and well-structured for analysis.

---

## Data Visualization and Insights

### Product Line Performance
A bar chart was used to compare sales across different product lines.

**Key Insight:**
- Food and Beverages generated the highest total sales
- Sports and Travel ranked second
- Health and Beauty had the lowest sales

---

### Sales Across Branches (Regions)

Sales were visualized for each branch.

**Key Insight:**
- Giza recorded the highest sales
- Cairo recorded the lowest sales

---

### Gender Impact on Sales

A pie chart was used to visualize sales by gender.

**Key Insight:**
- Females contributed slightly more to total sales than males

---

## Recommendations

### Product Strategy
- Expand and promote Food and Beverages
- Improve marketing for low-performing categories
- Evaluate customer feedback

### Regional Strategy
- Study customer preferences in low-performing regions
- Tailor inventory and promotions by region
- Increase local marketing efforts

### Gender-Based Strategy
- Continue targeting female customers
- Introduce strategies to engage male customers
- Explore gender-specific product offerings

---

## Conclusion

The analysis reveals valuable insights into product performance, gender-based purchasing behavior, and regional sales differences.  
These insights can help businesses design targeted strategies to maximize overall sales performance.
