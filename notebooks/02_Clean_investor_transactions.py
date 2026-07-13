import pandas as pd

df = pd.read_csv("F:\\Project\\data\\raw\\08_investor_transactions.csv")
df['transaction_date'] = pd.to_datetime(df['transaction_date']).dt.strftime('%Y-%m-%d')
# Standardise casing
df['transaction_type'] = df['transaction_type'].str.strip().str.title()
df['kyc_status'] = df['kyc_status'].str.strip().str.title()
df['gender'] = df['gender'].str.strip().str.title()
# Keep only amount > 0
df = df[df['amount_inr'] > 0].drop_duplicates().reset_index(drop=True)
print("Shape after:", df.shape)
df.to_csv("F:\\Project\\data\\processed\\clean_transactions.csv", index=False)
print("Saved clean_transactions.csv")