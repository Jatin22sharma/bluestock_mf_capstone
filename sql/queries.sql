-- ==========================================
-- Task 6: 10 Analytical SQL Queries
-- ==========================================

-- 1. Top 5 funds by AUM (Assets Under Management)
SELECT scheme_name, fund_house, aum_crore 
FROM fact_performance 
ORDER BY aum_crore DESC 
LIMIT 5;

-- 2. Average NAV per month across all funds
SELECT strftime('%Y-%m', nav_date) AS month, ROUND(AVG(nav), 2) AS avg_nav
FROM fact_nav
GROUP BY month
ORDER BY month;

-- 3. Total SIP Inflows by Year
SELECT strftime('%Y', transaction_date) AS year, SUM(amount_inr) AS total_sip_inflow
FROM fact_transactions
WHERE transaction_type = 'SIP'
GROUP BY year
ORDER BY year;

-- 4. Transaction volume and value by State
SELECT state, COUNT(transaction_id) AS total_transactions, SUM(amount_inr) AS total_amount
FROM fact_transactions
GROUP BY state
ORDER BY total_amount DESC;

-- 5. Funds with an Expense Ratio of less than 1%
SELECT scheme_name, category, expense_ratio_pct
FROM dim_fund
WHERE expense_ratio_pct < 1.0
ORDER BY expense_ratio_pct ASC;

-- 6. Top 5 most heavily invested stocks across all portfolios
SELECT stock_name, sector, SUM(market_value_cr) AS total_invested_cr
FROM fact_portfolio_holdings
GROUP BY stock_name, sector
ORDER BY total_invested_cr DESC
LIMIT 5;

-- 7. Best Performing Funds over 3 Years (Top 5)
SELECT scheme_name, category, return_3yr_pct
FROM fact_performance
ORDER BY return_3yr_pct DESC
LIMIT 5;

-- 8. Investment amounts by City Tier (T30 vs B30)
SELECT city_tier, COUNT(*) AS transaction_count, SUM(amount_inr) AS total_investment
FROM fact_transactions
GROUP BY city_tier
ORDER BY total_investment DESC;

-- 9. Number of schemes managed by each Fund House
SELECT fund_house, COUNT(amfi_code) AS total_schemes
FROM dim_fund
GROUP BY fund_house
ORDER BY total_schemes DESC;

-- 10. Average 1-Year Return by Mutual Fund Category
SELECT category, ROUND(AVG(return_1yr_pct), 2) AS avg_1yr_return
FROM fact_performance
GROUP BY category
ORDER BY avg_1yr_return DESC;