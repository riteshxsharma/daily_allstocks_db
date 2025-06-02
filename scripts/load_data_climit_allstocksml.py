import pandas as pd
import psycopg2
import string
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Database connection setup using environment variables
connection = psycopg2.connect(
    database=os.getenv('DB_NAME'),        # Database name from .env
    user=os.getenv('DB_USER'),            # Database username from .env
    password=os.getenv('DB_PASSWORD'),    # Database password from .env
    host=os.getenv('DB_HOST', 'localhost'), # Default to localhost if not set
    port=os.getenv('DB_PORT', '5432')     # Default to port 5432 if not set
)
cursor = connection.cursor()
cursor.execute("SELECT column_name FROM information_schema.columns WHERE table_name = 'all_stocks_ml'")
print(cursor.fetchall())

# Configuration
csv_file = r'C:\\Users\\Owner\\OneDrive\\Documents\\MacBookFiles\\GoogleNotebook\\All Stocks Data\\All_Stocks_20240902PM12_cleaned.csv'
table_name = 'all_stocks_ml'  # Make sure this matches the table you just created

# Load and clean the data
df = pd.read_csv(csv_file)
df = df.iloc[:, :173]  # Select the first 173 columns
printable = set(string.printable)

# Clean data
df = df.map(lambda x: x.strip() if isinstance(x, str) else x)
df = df.map(lambda x: ''.join(filter(lambda y: y in printable, x)) if isinstance(x, str) else x)

columns = ', '.join(df.columns)
placeholders = ', '.join(['%s'] * len(df.columns))

insert_query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"

for index, row in df.iterrows():
    row_data = tuple(row)
    print(f"Processing row {index}: length of row data = {len(row_data)}")

    # Print SQL query and row data for inspection
    print(f"SQL Query: {insert_query}")
    print(f"Values: {row_data}")

    try:
        print(f"Length of row data: {len(row_data)}, Number of columns: {len(columns)}")
        print(row_data)
        cursor.execute(insert_query, row_data)
    except psycopg2.Error as e:
        print(f"Error inserting row {index}: {e}")
        break  # Stop after the first error for inspection

connection.commit()
cursor.close()
connection.close()