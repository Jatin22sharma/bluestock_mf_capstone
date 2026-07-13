import pandas as pd

df = pd.read_csv("F:\\Project\\data\\raw\\02_nav_history.csv")
df['date'] = pd.to_datetime(df['date'])
df = df.sort_values(['amfi_code', 'date']).reset_index(drop=True)

# Forward-fill missing NAV for holidays 
full = []
for code, grp in df.groupby('amfi_code'):
    grp = grp.set_index('date').asfreq('B')  # business days
    grp['amfi_code'] = code
    grp['nav'] = grp['nav'].ffill()
    full.append(grp.reset_index())

df_clean = pd.concat(full, ignore_index=True)
df_clean = df_clean[df_clean['nav'] > 0].drop_duplicates()
df_clean['date'] = df_clean['date'].dt.strftime('%Y-%m-%d')
df_clean = df_clean[['amfi_code','date','nav']]

print("Shape after:", df_clean.shape)
print("Nulls:", df_clean.isnull().sum().sum())
df_clean.to_csv("F:\\Project\\data\\processed\\clean_nav.csv", index=False)
print("Saved clean_nav.csv")