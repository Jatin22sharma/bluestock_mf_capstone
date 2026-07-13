import pandas as pd, numpy as np

df = pd.read_csv("F:\\Project\\data\\raw\\07_scheme_performance.csv")
print("Shape:", df.shape)
print("Nulls:\n", df.isnull().sum())

numeric_cols = ['return_1yr_pct','return_3yr_pct','return_5yr_pct','benchmark_3yr_pct',
                'alpha','beta','sharpe_ratio','sortino_ratio','std_dev_ann_pct',
                'max_drawdown_pct','aum_crore','expense_ratio_pct']
for c in numeric_cols:
    df[c] = pd.to_numeric(df[c], errors='coerce')

# Flag negative Sharpe (don't drop, just flag)
df['sharpe_flag'] = df['sharpe_ratio'] < 0
print("Negative Sharpe count:", df['sharpe_flag'].sum())

# Check expense_ratio range 0.1% - 2.5%
out_range = df[(df['expense_ratio_pct'] < 0.1) | (df['expense_ratio_pct'] > 2.5)]
print("Expense ratio out of range:", out_range[['scheme_name','expense_ratio_pct']])

df = df.drop_duplicates()
df.to_csv("F:\\Project\\data\\processed\\clean_performance.csv", index=False)
print("Saved clean_performance.csv | Shape:", df.shape)