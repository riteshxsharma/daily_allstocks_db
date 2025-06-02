import os
import pandas as pd
import psycopg2
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Database connection setup
connection = psycopg2.connect(
    database=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT")
)
cursor = connection.cursor()

# Step 1: Data Cleaning
def clean_data(input_path, output_path):
    df = pd.read_csv(input_path, na_values='-')
    df.to_csv(output_path, index=False)
    print("Data cleaned and saved to:", output_path)
    return output_path

# Step 2: Generate SQL Create Table Statement
def generate_sql_create_table_statement(df, table_name):
    cols = []
    for column, dtype in zip(df.columns, df.dtypes):
        column = f'"{column}"'  # Enclose column name in double quotes
        if "int" in str(dtype):
            cols.append(f"{column} INTEGER")
        elif "float" in str(dtype):
            cols.append(f"{column} FLOAT")
        elif "datetime" in str(dtype):
            cols.append(f"{column} TIMESTAMP")
        else:
            cols.append(f"{column} TEXT")
    cols_str = ", ".join(cols)
    return f'CREATE TABLE "{table_name}" ({cols_str});'

# Paths and table names
input_csv_path = r'C:\\Users\\Owner\\OneDrive\\Documents\\MacBookFiles\\GoogleNotebook\\All Stocks Data\\All_Stocks_20240902PM12.csv'
cleaned_csv_path = r'C:\\Users\\Owner\\OneDrive\\Documents\\MacBookFiles\\GoogleNotebook\\All Stocks Data\\All_Stocks_20240902PM12_cleaned.csv'
table_name = 'all_stocks_one'

# Step 1: Clean the data
cleaned_csv_path = clean_data(input_csv_path, cleaned_csv_path)

# Step 2: Generate SQL statement
df_cleaned = pd.read_csv(cleaned_csv_path)
create_table_sql = generate_sql_create_table_statement(df_cleaned, table_name)
print("Generated SQL for table creation:\n", create_table_sql)

# Step 3: Create Table in PostgreSQL
cursor.execute(create_table_sql)
connection.commit()

# Step 4: Load data into the table
def load_data_into_table(csv_file_path, table_name, cursor, connection):
    df = pd.read_csv(csv_file_path)
    for _, row in df.iterrows():
        columns = ', '.join(row.index)
        values = ', '.join([f"'{str(val).replace(\"'\", '')}'" for val in row.values])
        insert_query = f"INSERT INTO {table_name} ({columns}) VALUES ({values});"
        cursor.execute(insert_query)
    connection.commit()
    print(f"Data loaded into table {table_name} successfully.")

load_data_into_table(cleaned_csv_path, table_name, cursor, connection)

# Step 5: (Optional) Create a view, or other operations

# Close the database connection
cursor.close()
connection.close()
