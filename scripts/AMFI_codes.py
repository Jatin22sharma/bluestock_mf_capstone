import pandas as pd

fund_master = pd.read_csv(
    "F:/Project/data/raw/01_fund_master.csv"
)

nav_history = pd.read_csv(
    "F:/Project/data/raw/02_nav_history.csv"
)

# unique AMFI codes
fund_codes = set(fund_master["amfi_code"])

nav_codes = set(nav_history["amfi_code"])

# missing codes
missing_codes = fund_codes - nav_codes

print("Total Fund Master Codes:", len(fund_codes))
print("Total NAV Codes:", len(nav_codes))
print("Missing Codes Count:", len(missing_codes))

if len(missing_codes) == 0:
    print("\n✓ All AMFI codes are present in NAV history.")
else:
    print("\nMissing Codes:")
    print(sorted(missing_codes))