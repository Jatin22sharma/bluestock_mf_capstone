import sqlite3
import pandas as pd
import os

print("Starting full data load into SQLite...")

# 1. Connect to SQLite
conn = sqlite3.connect('bluestock_mf.db')
cursor = conn.cursor()

# 2. Execute schema.sql from the sql folder
schema_path = os.path.join('sql', 'schema.sql')
try:
    with open(schema_path, 'r') as file:
        schema_script = file.read()
    cursor.executescript(schema_script)
    print("✅ Schema built successfully from sql/schema.sql.")
except Exception as e:
    print(f"❌ Error executing schema: {e}")

# 3. Define your separate Raw and Processed directories
RAW_DIR = os.path.join("data", "raw")
PROCESSED_DIR = os.path.join("data", "processed")

try:
    # --- Load Raw Data ---
    df_fund = pd.read_csv(os.path.join(RAW_DIR, "01_fund_master.csv"))
    df_port = pd.read_csv(os.path.join(RAW_DIR, "09_portfolio_holdings.csv"))

    # --- Load Processed Data ---
    # Remember to map 'date' to 'nav_date' for the schema
    df_nav = pd.read_csv(os.path.join(PROCESSED_DIR, "clean_nav.csv")).rename(columns={'date': 'nav_date'})
    df_perf = pd.read_csv(os.path.join(PROCESSED_DIR, "clean_performance.csv"))
    df_tx = pd.read_csv(os.path.join(PROCESSED_DIR, "clean_transactions.csv"))

    # 4. Write DataFrames to SQL Tables
    df_fund.to_sql('dim_fund', conn, if_exists='append', index=False)
    print(f"✅ Loaded {len(df_fund)} rows into 'dim_fund'")
    
    df_nav.to_sql('fact_nav', conn, if_exists='append', index=False)
    print(f"✅ Loaded {len(df_nav)} rows into 'fact_nav'")
    
    df_perf.to_sql('fact_performance', conn, if_exists='append', index=False)
    print(f"✅ Loaded {len(df_perf)} rows into 'fact_performance'")
    
    df_tx.to_sql('fact_transactions', conn, if_exists='append', index=False)
    print(f"✅ Loaded {len(df_tx)} rows into 'fact_transactions'")
    
    df_port.to_sql('fact_portfolio_holdings', conn, if_exists='append', index=False)
    print(f"✅ Loaded {len(df_port)} rows into 'fact_portfolio_holdings'")

    print("\n✅ All 5 tables successfully populated into bluestock_mf.db!")

except Exception as e:
    print(f"\n❌ Error loading data to tables: {e}")

# 5. Commit and Close
conn.commit()
conn.close()
print("\n🎉 Task 5 Complete: Database is locked, loaded, and ready!")