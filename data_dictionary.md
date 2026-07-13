# Bluestock Mutual Fund Analytics - Data Dictionary

This document describes the schema, tables, and columns for the `bluestock_mf.db` SQLite database. The database is modeled using a star/snowflake schema approach with one central dimension table and four fact tables.

## 1. `dim_fund` (Dimension Table)
Stores static metadata and core details for each mutual fund scheme.
* **Primary Key:** `amfi_code`

| Column Name | Data Type | Description |
| :--- | :--- | :--- |
| `amfi_code` | INTEGER | Unique identifier for the mutual fund (AMFI assigned). |
| `fund_house` | TEXT | Name of the Asset Management Company (e.g., SBI, HDFC). |
| `scheme_name` | TEXT | Full name of the mutual fund scheme. |
| `category` | TEXT | Broad asset class (e.g., Equity, Debt, Hybrid). |
| `sub_category` | TEXT | Specific investment category (e.g., Large Cap, Liquid). |
| `plan` | TEXT | Investment plan type (Regular or Direct). |
| `launch_date` | DATE | Inception date of the fund (YYYY-MM-DD). |
| `benchmark` | TEXT | Index against which performance is measured (e.g., NIFTY 50). |
| `expense_ratio_pct` | REAL | Annual fee charged by the fund as a percentage. |
| `exit_load_pct` | REAL | Fee charged for early redemption as a percentage. |
| `min_sip_amount` | INTEGER | Minimum investment required for a SIP. |
| `min_lumpsum_amount`| INTEGER | Minimum investment required for a lumpsum. |
| `fund_manager` | TEXT | Name of the primary fund manager. |
| `risk_category` | TEXT | Risk classification (Low, Moderate, High, Very High). |
| `sebi_category_code`| TEXT | Standardized SEBI code for the fund category. |

## 2. `fact_nav` (Fact Table)
Stores the daily historical Net Asset Value (NAV) time-series data.
* **Primary Key:** Composite (`amfi_code`, `nav_date`)
* **Foreign Key:** `amfi_code` references `dim_fund`

| Column Name | Data Type | Description |
| :--- | :--- | :--- |
| `amfi_code` | INTEGER | Fund identifier (FK). |
| `nav_date` | DATE | Date of the NAV record (YYYY-MM-DD). |
| `nav` | REAL | The Net Asset Value per unit on that date. |
| `daily_return` | REAL | Day-over-day percentage change in NAV. |

## 3. `fact_transactions` (Fact Table)
Logs individual investor transactions (investments and redemptions).
* **Primary Key:** `transaction_id`
* **Foreign Key:** `amfi_code` references `dim_fund`

| Column Name | Data Type | Description |
| :--- | :--- | :--- |
| `transaction_id` | INTEGER | Auto-incremented unique ID for the transaction. |
| `investor_id` | TEXT | Unique identifier for the investor. |
| `transaction_date` | DATE | Date the transaction was executed. |
| `amfi_code` | INTEGER | Fund transacted in (FK). |
| `transaction_type` | TEXT | Type of transaction (SIP, Lumpsum, Redemption). |
| `amount_inr` | REAL | Transaction value in Indian Rupees. |
| `state` | TEXT | Indian State of the investor. |
| `city` | TEXT | City of the investor. |
| `city_tier` | TEXT | AMFI classification (T30 = Top 30, B30 = Beyond Top 30). |
| `age_group` | TEXT | Demographic age bracket. |
| `gender` | TEXT | Investor gender. |
| `annual_income_lakh`| REAL | Investor's self-reported income in Lakhs INR. |
| `payment_mode` | TEXT | Method of payment (UPI, Net Banking, Mandate, Cheque). |
| `kyc_status` | TEXT | KYC verification status (Verified, Pending). |

## 4. `fact_performance` (Fact Table)
Aggregated historical return and risk metrics for each fund.
* **Primary Key:** `amfi_code`
* **Foreign Key:** `amfi_code` references `dim_fund`

| Column Name | Data Type | Description |
| :--- | :--- | :--- |
| `amfi_code` | INTEGER | Fund identifier (FK & PK). |
| `scheme_name` | TEXT | Name of the fund. |
| `fund_house` | TEXT | Asset Management Company name. |
| `category` | TEXT | Broad asset class. |
| `plan` | TEXT | Regular or Direct plan. |
| `return_1yr_pct` | REAL | Trailing 1-year annualized return (%). |
| `return_3yr_pct` | REAL | Trailing 3-year annualized return (%). |
| `return_5yr_pct` | REAL | Trailing 5-year annualized return (%). |
| `benchmark_3yr_pct` | REAL | 3-year return of the benchmark index (%). |
| `alpha` | REAL | Excess return relative to benchmark risk. |
| `beta` | REAL | Volatility measure relative to the market. |
| `sharpe_ratio` | REAL | Risk-adjusted return metric. |
| `sortino_ratio` | REAL | Risk-adjusted return (downside risk only). |
| `std_dev_ann_pct` | REAL | Annualized standard deviation of returns (Volatility). |
| `max_drawdown_pct` | REAL | Maximum observed loss from peak to trough. |
| `aum_crore` | REAL | Total Assets Under Management in Crores INR. |
| `expense_ratio_pct` | REAL | Annual fund management fee. |
| `morningstar_rating`| INTEGER | 1 to 5 star rating. |
| `risk_grade` | TEXT | Overall risk assessment grade. |
| `negative_sharpe_flag`| INTEGER | Boolean flag (1=Negative Sharpe, 0=Positive). |

## 5. `fact_portfolio_holdings` (Fact Table)
Detailed breakdown of the underlying stocks and assets held by the funds.
* **Primary Key:** `holding_id`
* **Foreign Key:** `amfi_code` references `dim_fund`

| Column Name | Data Type | Description |
| :--- | :--- | :--- |
| `holding_id` | INTEGER | Auto-incremented unique ID for the holding record. |
| `amfi_code` | INTEGER | Fund identifier (FK). |
| `stock_symbol` | TEXT | Ticker symbol of the holding (e.g., HDFCBANK). |
| `stock_name` | TEXT | Full company or asset name. |
| `sector` | TEXT | Economic sector (e.g., IT, Banking, Pharma). |
| `weight_pct` | REAL | Percentage of the fund's total AUM invested in this asset. |
| `market_value_cr` | REAL | Total value of this holding in Crores INR. |
| `current_price_inr` | REAL | Current market price per share/unit. |
| `portfolio_date` | DATE | Date when the portfolio was disclosed. |