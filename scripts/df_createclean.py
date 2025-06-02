import pandas as pd

# Specify the path to your CSV file
file_path = r'C:\\Users\\Owner\\OneDrive\\Documents\\MacBookFiles\\GoogleNotebook\\All Stocks Data\\All_Stocks_20240902PM12.csv'

# Read the CSV file, treating '-' as NaN
df = pd.read_csv(file_path, na_values='-')

# Specify the output file path
file_path_out = r'C:\\Users\\Owner\\OneDrive\\Documents\\MacBookFiles\\GoogleNotebook\\All Stocks Data\\All_Stocks_20240902PM12_cleaned.csv'

# Write the cleaned data to a new CSV file
df.to_csv(file_path_out, index=False)
print("Data types after cleaning:\n", df.dtypes)
