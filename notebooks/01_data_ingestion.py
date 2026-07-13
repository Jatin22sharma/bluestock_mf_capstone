import pandas as pd
import os

DATA_PATH = "F:\\Project\\data\\raw"

files = [f for f in os.listdir(DATA_PATH) if f.endswith(".csv")]

for file in files:
    path = os.path.join(DATA_PATH, file)

    df = pd.read_csv(path)

    print("\n" + "="*50)
    print("File:", file)
    print("Shape:", df.shape)

    print("\nData Types:")
    print(df.dtypes)

    print("\nFirst 5 Rows:")
    print(df.head())