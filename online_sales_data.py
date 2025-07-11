# -*- coding: utf-8 -*-
"""Online Sales Data.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1pgAMWjw2_N521VgGoI4xmSNMaaCEGbFe
"""

from google.colab import drive
drive.mount('/content/drive')

import pandas as pd
import sqlite3

# Load the CSV file from your Google Drive path
file_path = "/content/drive/MyDrive/ELEVATE LABS/Online Sales Data.csv"

# Read the file into a DataFrame
df = pd.read_csv(file_path)

# Show first few rows
df.head()

# Clean column names
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

# Convert 'date' to datetime
df['date'] = pd.to_datetime(df['date'], errors='coerce')

# Drop rows with invalid or missing dates
df = df.dropna(subset=['date'])

# Preview cleaned data
df.head()

# Connect to in-memory SQLite database
conn = sqlite3.connect(":memory:")

# Save DataFrame to SQL table
df.to_sql("sales", conn, index=False, if_exists='replace')

# SQL query: monthly revenue and order volume
query = """
SELECT
  STRFTIME('%Y', date) AS year,
  STRFTIME('%m', date) AS month,
  SUM(total_revenue) AS total_revenue,
  COUNT(DISTINCT transaction_id) AS transaction_volume
FROM sales
GROUP BY year, month
ORDER BY year ASC, month ASC
LIMIT 12;
"""

# Run query
result = pd.read_sql(query, conn)

# Clean up result
result['month'] = result['month'].astype(int)
result['year'] = result['year'].astype(int)

# Display result
result

print("1️⃣ Group by Month and Year")
display(pd.read_sql("""
SELECT
  STRFTIME('%Y', date) AS year,
  STRFTIME('%m', date) AS month,
  SUM(total_revenue) AS monthly_revenue
FROM sales
GROUP BY year, month
ORDER BY year, month;
""", conn))

# COUNT(*) vs COUNT(DISTINCT transaction_id)

print("2️⃣ COUNT(*) vs COUNT(DISTINCT transaction_id)")
display(pd.read_sql("""
SELECT
  COUNT(*) AS total_rows,
  COUNT(DISTINCT transaction_id) AS unique_transactions
FROM sales;
""", conn))

# Monthly Revenue Calculation

print("3️⃣ Monthly Revenue")
display(pd.read_sql("""
SELECT
  STRFTIME('%Y-%m', date) AS month_year,
  SUM(total_revenue) AS monthly_revenue
FROM sales
GROUP BY month_year
ORDER BY month_year;
""", conn))

# Aggregate Functions (SUM, AVG, MIN, MAX, COUNT)
print("4️⃣ Aggregate Functions Example")
display(pd.read_sql("""
SELECT
  SUM(total_revenue) AS total_sales,
  AVG(unit_price) AS avg_price,
  MIN(total_revenue) AS min_sale,
  MAX(total_revenue) AS max_sale,
  COUNT(*) AS total_transactions
FROM sales;
""", conn))

# Handling NULLs with COALESCE

print("5️⃣ Handling NULLs in Aggregates")
display(pd.read_sql("""
SELECT
  SUM(COALESCE(total_revenue, 0)) AS total_revenue_no_nulls,
  AVG(COALESCE(unit_price, 0)) AS avg_price_no_nulls
FROM sales;
""", conn))

# ORDER BY + GROUP BY – Region Revenue

print("6️⃣ ORDER BY and GROUP BY Example (Region Revenue)")
display(pd.read_sql("""
SELECT
  region,
  SUM(total_revenue) AS region_revenue
FROM sales
GROUP BY region
ORDER BY region_revenue DESC;
""", conn))

# 3 Months by Revenue

print("7️⃣ Top 3 Months by Sales")
display(pd.read_sql("""
SELECT
  STRFTIME('%Y-%m', date) AS month_year,
  SUM(total_revenue) AS monthly_revenue
FROM sales
GROUP BY month_year
ORDER BY monthly_revenue DESC
LIMIT 3;
""", conn))

conn.close()

"""# **conclusion**
All queries were executed as pure SQL using SQLite inside Google Colab — no manual Python calculations were used.

The workflow is efficient, scalable, and reflects real-world SQL problem-solving for BI and data analyst roles.

This format is highly recommended for SQL interviews, assignments, or case studies
"""

