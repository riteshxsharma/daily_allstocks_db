import pandas as pd

# Configuration
csv_file = r'C:\\Users\\Owner\\OneDrive\\Documents\\MacBookFiles\\GoogleNotebook\\All Stocks Data\\All_Stocks_20240902PM12_cleaned.csv'  # Path to your cleaned CSV file
table_name = 'all_stocks_one'  # Name of the table you want to create

# Read the CSV file
df = pd.read_csv(csv_file)

# Generate the SQL create table statement
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

create_table_sql = generate_sql_create_table_statement(df, table_name)
print("Generated SQL:\n", create_table_sql)
