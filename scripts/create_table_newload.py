import pandas as pd
import psycopg2
from dotenv import load_dotenv
import os


def determine_sql_type(value):
    """Determine the SQL data type based on the value."""
    if pd.api.types.is_integer_dtype(value):
        return "integer"
    elif pd.api.types.is_float_dtype(value):
        return "numeric(15,2)"  # Adjust precision as needed
    elif pd.api.types.is_datetime64_any_dtype(value):
        return "date"
    else:
        max_length = value.astype(str).str.len().max()
        return f"varchar({int(max_length)})" if max_length < 255 else "text"


def create_table_from_csv(csv_file_path, db_config, table_name):
    # Load the CSV file
    df = pd.read_csv(csv_file_path)

    # Start building the CREATE TABLE statement
    create_table_sql = f"CREATE TABLE {table_name} (\n\t_record_number SERIAL PRIMARY KEY,\n"

    for col in df.columns:
        col_name = f'"{col}"'
        sql_type = determine_sql_type(df[col])
        create_table_sql += f"\t{col_name} {sql_type},\n"

    # Remove the last comma and close the statement
    create_table_sql = create_table_sql.rstrip(',\n') + "\n);"

    print(f"Generated CREATE TABLE SQL:\n{create_table_sql}")

    # Connect to the database and execute the CREATE TABLE statement
    try:
        conn = psycopg2.connect(
            dbname=db_config['DB_NAME'],
            user=db_config['DB_USER'],
            password=db_config['DB_PASSWORD'],
            host=db_config['DB_HOST'],
            port=db_config['DB_PORT']
        )
        cursor = conn.cursor()
        cursor.execute(create_table_sql)
        conn.commit()
        print(f"Table {table_name} created successfully.")

        # Insert the data into the new table
        for index, row in df.iterrows():
            columns = ', '.join([f'"{col}"' for col in df.columns])
            values = []
            for val in row:
                if isinstance(val, str):
                    # Escape single quotes by doubling them
                    escaped_val = val.replace("'", "''")
                    values.append(f"'{escaped_val}'")
                elif pd.isna(val):
                    values.append('NULL')
                else:
                    values.append(str(val))
            values = ', '.join(values)
            insert_sql = f"INSERT INTO {table_name} ({columns}) VALUES ({values});"
            cursor.execute(insert_sql)

        conn.commit()
        print(f"Data inserted successfully into {table_name}.")

    except psycopg2.Error as e:
        print(f"Error creating table or inserting data: {e}")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()


def main():
    # Load environment variables
    load_dotenv()

    # Database configuration from .env
    db_config = {
        'DB_NAME': os.getenv('DB_NAME'),
        'DB_USER': os.getenv('DB_USER'),
        'DB_PASSWORD': os.getenv('DB_PASSWORD'),
        'DB_HOST': os.getenv('DB_HOST'),
        'DB_PORT': os.getenv('DB_PORT')
    }

    # File path to the CSV
    csv_file_path = r'C:\Users\Owner\OneDrive\Documents\MacBookFiles\GoogleNotebook\All Stocks Data\20240903PM15.csv'

    # Generate table name based on the file name
    table_name = f"all_stocks_{os.path.basename(csv_file_path).split('.')[0].replace('-', '_').replace(' ', '_')}"

    # Create the table based on the CSV structure and load data
    create_table_from_csv(csv_file_path, db_config, table_name)


if __name__ == "__main__":
    main()
