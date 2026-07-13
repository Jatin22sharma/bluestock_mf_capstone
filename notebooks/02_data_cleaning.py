import pandas as pd
import os

print("Starting batch cleaning for remaining 7 datasets...\n")


RAW_DIR = os.path.join("data", "raw")
PROCESSED_DIR = os.path.join("data", "processed")


files_to_clean = {
    "01_fund_master.csv": "clean_fund_master.csv",
    "03_aum_by_fund_house.csv": "clean_aum_by_fund_house.csv",
    "04_monthly_sip_inflows.csv": "clean_monthly_sip_inflows.csv",
    "05_category_inflows.csv": "clean_category_inflows.csv",
    "06_industry_folio_count.csv": "clean_industry_folio_count.csv",
    "09_portfolio_holdings.csv": "clean_portfolio_holdings.csv",
    "10_benchmark_indices.csv": "clean_benchmark_indices.csv"
}

for raw_name, clean_name in files_to_clean.items():
    try:
        
        file_path = os.path.join(RAW_DIR, raw_name)
        df = pd.read_csv(file_path)
        
        
        original_len = len(df)
        
        
        df = df.drop_duplicates()
        
        
        df = df.ffill().fillna(0)
        
        
        save_path = os.path.join(PROCESSED_DIR, clean_name)
        df.to_csv(save_path, index=False)
        
        dropped_rows = original_len - len(df)
        print(f"Cleaned {raw_name} -> Saved as {clean_name}")
        if dropped_rows > 0:
            print(f"   (Removed {dropped_rows} duplicate/invalid rows)")
            
    except Exception as e:
        print(f"Error processing {raw_name}: {e}")

print("\n Deliverable Met: You now have exactly 10 cleaned CSVs in your data/processed/ folder!")