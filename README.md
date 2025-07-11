# Online-Sales-Analytics-Using-Pure-SQL-SQLite-in-Colab


# 📊 Online Sales SQL Analysis using Google Colab & SQLite

This project performs end-to-end sales data analysis using pure SQL queries within Google Colab. The dataset includes online transaction data with date, product details, revenue, region, and more.

---

## 📁 Dataset Features

The dataset contains the following columns:

- `Transaction ID`
- `Date`
- `Product Category`
- `Product Name`
- `Units Sold`
- `Unit Price`
- `Total Revenue`
- `Region`
- `Payment Method`

---

## 🧠 Objective

- Analyze online sales using SQL-only queries
- Extract key business KPIs like monthly revenue, top-performing regions, and volume of transactions
- Use **SQLite in-memory engine** for efficient querying inside Google Colab

---

## 🛠️ Tools Used

- Google Colab (Python environment)
- SQLite (via `sqlite3` library)
- Pandas (for data display only)
- Google Drive integration (for dataset access)

---

## 🔍 SQL Queries Performed

1. **Group by Month and Year**  
   → Analyze monthly sales trends

2. **COUNT vs COUNT(DISTINCT)**  
   → Understand total records vs unique transactions

3. **Monthly Revenue Calculation**  
   → Sum of revenue per month

4. **Aggregate Functions (SUM, AVG, MIN, MAX, COUNT)**  
   → Analyze business metrics

5. **Handling NULLs with COALESCE**  
   → Clean null values in calculations

6. **Region-Wise Revenue (ORDER BY + GROUP BY)**  
   → Rank regions by performance

7. **Top 3 Months by Revenue**  
   → Identify peak performance periods

---

## 📈 Sample Output

| Month     | Revenue     | Orders |
|-----------|-------------|--------|
| 2023-07   | ₹85,000     | 240    |
| 2023-06   | ₹78,000     | 210    |
| 2023-05   | ₹72,000     | 198    |

---



## ✅ Conclusion

This notebook demonstrates how SQL-based analytics can be seamlessly run in a Python environment without relying on manual Python logic. It is ideal for data analysts, students, or professionals preparing for SQL interviews or performing business reporting tasks.

---

## 📂 Folder Structure

```

├── Online Sales Data.csv
├── sales\_analysis.ipynb
├── images/
│   ├── monthly\_revenue.png
│   └── top\_regions.png
├── README.md

```

---

## ✍️ Author

**Kandukuri Jaswanth**  
_Data Analyst | SQL Enthusiast | Power BI Explorer_




