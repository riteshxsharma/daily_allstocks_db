import pandas as pd
import psycopg2

def create_table_from_csv(csv_file_path, table_name, cursor, connection):
    df = pd.read_csv(csv_file_path)
    columns = df.columns

    create_table_query = f"""
    CREATE TABLE IF NOT EXISTS {table_name} (
        {", ".join([f"{col} TEXT" for col in columns])}
    );
    """
    cursor.execute(create_table_query)
    connection.commit()
    print(f"Table {table_name} created successfully.")

def load_data_into_table(csv_file_path, table_name, cursor, connection):
    df = pd.read_csv(csv_file_path)
    for _, row in df.iterrows():
        columns = ', '.join(row.index)
        values = ', '.join([f"'{str(val).replace('\'', '')}'" for val in row.values])
        insert_query = f"INSERT INTO {table_name} ({columns}) VALUES ({values});"
        cursor.execute(insert_query)
    connection.commit()
    print(f"Data loaded into table {table_name} successfully.")
