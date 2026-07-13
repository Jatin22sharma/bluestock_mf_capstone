import requests
import pandas as pd

amfi_code = 125497

url = f"https://api.mfapi.in/mf/{amfi_code}"

response = requests.get(url)

data = response.json()

nav_df = pd.DataFrame(data['data'])

nav_df.to_csv(
    "F:\\Project\\data\\raw\\hdfc_top100_nav.csv",
    index=False
)

print("NAV data saved successfully")