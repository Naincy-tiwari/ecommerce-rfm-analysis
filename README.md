🛒 E-Commerce Sales & Customer Segmentation (RFM Analysis)

📌 Project Overview

This project performs an end-to-end analysis of e-commerce transactional data to uncover key business insights and segment customers using RFM (Recency, Frequency, Monetary) analysis.

The objective is to analyze sales performance, understand customer behavior, and provide actionable strategies to improve customer retention and revenue growth.

---

🎯 Objectives

* Analyze overall sales trends and revenue patterns
* Identify top-performing products and regions
* Understand customer purchasing behavior
* Segment customers using RFM analysis
* Build an interactive dashboard for data visualization

---

🛠️ Tech Stack

* **Python**: Pandas, NumPy, Matplotlib, Seaborn
* **SQL**: Aggregations, Joins, Group By
* **Streamlit**: Interactive dashboard
* **Dataset**: E-commerce transactional data (Excel)

---

📂 Project Structure

```
ecommerce-rfm-analysis/
│
├── data/
│   ├── raw/                # Original dataset (excluded due to size)
│   └── processed/          # Cleaned datasets
│
├── notebooks/
│   └── eda.ipynb           # Data analysis & EDA
│
├── sql/
│   └── queries.sql         # SQL queries for analysis
│
├── visuals/
│   └── charts/             # Generated charts & graphs
│
├── src/
│   └── dashboard.py        # Streamlit dashboard code
│
├── rfm_data.csv            # RFM calculated dataset
├── rfm_segments.csv        # Customer segments
├── requirements.txt
└── README.md
```

---

🧹 Data Cleaning & Preprocessing

* Removed missing Customer IDs
* Filtered out negative/invalid transactions
* Eliminated duplicate records
* Converted date columns to datetime format
* Created a new **Revenue** column

---

📊 Exploratory Data Analysis (EDA)

* Revenue trend analysis over time
* Top-selling products identification
* Country-wise sales performance
* Customer purchase behavior analysis

---

🧠 RFM Analysis (Core Feature)

RFM analysis was used to segment customers based on:

* **Recency (R)** → How recently a customer made a purchase
* **Frequency (F)** → How often they purchase
* **Monetary (M)** → How much they spend

 🔢 RFM Scoring

Customers were assigned scores (1–4) for each metric using quartiles.

👥 Customer Segments

* **VIP Customers** → High value, frequent, recent buyers
* **Loyal Customers** → Frequent buyers
* **At-Risk Customers** → Inactive customers
* **Regular Customers** → Average engagement

---

📈 Dashboard (Streamlit)

An interactive dashboard was developed using Streamlit to visualize:

* Sales trends over time
* Customer segments distribution
* Top products and regions

---

💡 Key Business Insights

* A small percentage of customers generate the majority of revenue (Pareto Principle)
* Certain products consistently outperform others
* Revenue is concentrated in specific regions
* Customer retention is critical for long-term growth

---

🚀 Business Recommendations

* Implement loyalty programs for VIP customers
* Re-engage at-risk customers through targeted campaigns
* Focus inventory on top-performing products
* Expand marketing efforts in high-revenue regions

---

📁 Dataset Note

The original dataset was large and is not included in this repository due to GitHub file size limitations.

A cleaned and processed dataset is provided for analysis.
The original dataset can be obtained from public sources such as Kaggle or UCI Machine Learning Repository.

---

▶️ How to Run the Project

1️⃣ Install dependencies

```
pip install -r requirements.txt
```

2️⃣ Run Streamlit dashboard

```
streamlit run src/dashboard.py
```

---

🔮 Future Improvements

* Customer churn prediction using Machine Learning
* Sales forecasting models
* Deployment of dashboard on cloud platforms

---

📌 Conclusion

This project demonstrates end-to-end data analysis capabilities including data cleaning, exploratory analysis, SQL querying, customer segmentation, and dashboard development, making it highly relevant for Data Analyst roles.

---

👤 Author

**Naincy Tiwari**
