import pandas as pd
import sqlite3
from pathlib import Path

def recommend_funds(risk_appetite):
    print(f"\n🔍 Searching for top funds for a '{risk_appetite}' risk profile...\n")
    
    # Path logic exactly matching your F: drive
    db_path = Path(r"F:\bluestock_mf_capstone\data\db\bluestock_mf.db")
    conn = sqlite3.connect(db_path)
    
    # Load performance and metadata (FIXED SQL QUERY)
    df_perf = pd.read_sql("SELECT amfi_code, return_3yr_pct, sharpe_ratio FROM fact_performance", conn)
    df_funds = pd.read_sql("SELECT amfi_code, scheme_name, risk_category AS risk_grade, category FROM dim_fund", conn)
    
    # Merge
    df_master = df_funds.merge(df_perf, on='amfi_code')
    
    # Map User Risk to Fund Risk Grades
    risk_mapping = {
        'Low': ['Low', 'Low to Moderate'],
        'Moderate': ['Moderate', 'Moderately High'],
        'High': ['High', 'Very High']
    }
    
    if risk_appetite not in risk_mapping:
        print("Invalid Risk Profile. Choose Low, Moderate, or High.")
        conn.close()
        return
        
    allowed_grades = risk_mapping[risk_appetite]
    
    # Filter
    df_filtered = df_master[df_master['risk_grade'].isin(allowed_grades)].copy()
    
    if df_filtered.empty:
        print(f"No funds found matching risk grade {allowed_grades}.")
        conn.close()
        return
        
    # Rank by Sharpe Ratio
    df_ranked = df_filtered.sort_values(by='sharpe_ratio', ascending=False).head(3)
    
    # Print Table
    print(f"{'Scheme Name':<50} | {'Category':<15} | {'Risk':<15} | {'3Y Ret':<8} | {'Sharpe'}")
    print("-" * 105)
    for _, row in df_ranked.iterrows():
        print(f"{row['scheme_name'][:48]:<50} | {row['category'][:13]:<15} | {row['risk_grade']:<15} | {row['return_3yr_pct']:>6.2f}% | {row['sharpe_ratio']:>6.2f}")
    
    conn.close()

# Test the recommender
recommend_funds('Moderate')
recommend_funds('High')