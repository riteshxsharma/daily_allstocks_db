# load_data_into_allstocksml.py

import pandas as pd
import string

# Load your data
df = pd.read_csv('your_data.csv')  # Adjust this to your actual data source

print(f"Dataframe shape before processing: {df.shape}")

expected_columns = 173
if df.shape[1] > expected_columns:
    df = df.iloc[:, :expected_columns]

printable = set(string.printable)

df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)
df = df.apply(lambda x: x.apply(lambda y: ''.join(filter(lambda z: z in printable, y)) if isinstance(y, str) else y))

print(f"Dataframe shape after processing: {df.shape}")

# Further processing of df as needed
