# 📈 Bluestock Mutual Fund Analytics Platform

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![SQLite](https://img.shields.io/badge/SQLite-Database-lightgrey.svg)
![Power BI](https://img.shields.io/badge/Power_BI-Dashboard-yellow.svg)
![Data Science](https://img.shields.io/badge/Data_Science-Analytics-success.svg)

---

## 📝 Project Overview

This repository contains an end-to-end Data Engineering and Business Intelligence capstone project focused on the Indian Mutual Fund industry. Over a simulated 5-day sprint, raw financial data spanning 4.5 years was ingested, transformed, and modeled to evaluate 40 specific mutual fund schemes.

The project culminates in a highly interactive Power BI dashboard designed to empower retail investors and analysts with data-driven insights into historical performance, risk-adjusted returns, and demographic investment trends.

---

## 🚀 Key Features & Deliverables

- **ETL Data Pipeline:** Automated ingestion and cleaning of public AMFI NAV data, investor transactions, and SIP inflows using **Pandas**.
- **Relational Database (SQL):** Designed and deployed a 5-table Star Schema database in SQLite (`dim_fund`, `fact_nav`, `fact_transactions`, `fact_performance`, `fact_portfolio_holdings`).
- **Exploratory Data Analysis (EDA):** Deep-dive analysis highlighting AUM industry consolidation, SIP growth trends, and geographical investor demographics.
- **Quantitative Risk Analytics:** Engineered financial metrics including 1Y/3Y/5Y CAGR, Sharpe Ratio, Sortino Ratio, Alpha, Beta, and Maximum Drawdown using **NumPy** and **SciPy**.
- **Composite Fund Scorecard:** Built a weighted ranking model to objectively score and recommend mutual funds based on risk-adjusted performance.
- **Interactive BI Dashboard:** A 4-page Power BI dashboard featuring drill-throughs, DAX measures, KPIs, and custom tooltips.

---

## 🧰 Tech Stack

| Category | Technologies |
|----------|--------------|
| Programming | Python 3.10+ |
| Data Analysis | Pandas, NumPy, SciPy |
| Visualization | Matplotlib, Seaborn, Plotly |
| Database | SQLite3, SQL |
| Business Intelligence | Power BI Desktop |

---

## 📁 Repository Structure

```text
Bluestock_MF_Capstone/
│
├── data/
│   ├── raw/                        # Original CSV files and raw API pulls
│   └── processed/                  # Cleaned datasets and calculated metrics
│
├── sql/
│   ├── bluestock_mf.db             # SQLite Database
│   ├── schema.sql                  # Star Schema creation script
│   └── queries.sql                 # Analytical SQL queries
│
├── notebooks/
│   ├── EDA_Analysis.ipynb          # Data exploration
│   └── Performance_Analytics.ipynb # Risk metrics & scorecard
│
├── dashboard/
│   ├── bluestock_mf_dashboard.pbix # Power BI Dashboard
│   └── screenshots/                # Dashboard screenshots
│
├── Final_Report.pdf                # Executive summary
└── README.md                       # Project documentation
```

---

## ⚙️ Setup & Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/Bluestock_MF_Capstone.git
cd Bluestock_MF_Capstone
```

### 2️⃣ Install Dependencies

```bash
pip install pandas numpy scipy matplotlib seaborn plotly sqlalchemy
```

### 3️⃣ Run the Project

Launch **Jupyter Notebook** or **VS Code** and open:

- `notebooks/EDA_Analysis.ipynb`
- `notebooks/Performance_Analytics.ipynb`

### 4️⃣ View the Dashboard

Open:

```
dashboard/bluestock_mf_dashboard.pbix
```

using **Microsoft Power BI Desktop**.

---

## 📊 Dashboard Preview

![Dashboard Overview](https://github.com/Jatin22sharma/bluestock_mf_capstone/blob/main/dashboard/Project_screenshots/Industry%20Overview.png)

![Fund Performance](https://github.com/Jatin22sharma/bluestock_mf_capstone/blob/main/dashboard/Project_screenshots/Fund%20Performance.png)

![Inevstor Analytics](https://github.com/Jatin22sharma/bluestock_mf_capstone/blob/main/dashboard/Project_screenshots/Investor%20Analytics.png)

![SIP & Makret Trends](https://github.com/Jatin22sharma/bluestock_mf_capstone/blob/main/dashboard/Project_screenshots/SIP%20%26%20Market%20Trends.png)


## 📈 Project Highlights

- ✅ Automated ETL Pipeline
- ✅ Financial Risk Analytics
- ✅ SQLite Star Schema
- ✅ Power BI Dashboard
- ✅ DAX Measures
- ✅ Investor Demographics Analysis
- ✅ Fund Ranking Model
- ✅ Executive Report

---

## 👨‍💻 Author

**Jatin Sharma**

**Data Analyst | Python | SQL | Power BI**

- LinkedIn: https://www.linkedin.com/in/jatin-sharma-647801225/
- GitHub: https://github.com/Jatin22sharma

---

## ⭐ Support

If you found this project helpful, consider giving it a **⭐ Star** on GitHub.

Feedback and suggestions are always welcome!