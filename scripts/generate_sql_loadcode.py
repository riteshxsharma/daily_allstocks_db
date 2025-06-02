import pandas as pd


def generate_sql_inserts(csv_file_path, table_name, output_sql_file):
    # Load the cleaned CSV file
    df = pd.read_csv(csv_file_path)

    # Quote all column names to avoid conflicts with SQL reserved keywords
    quoted_columns = [f'"{col}"' for col in df.columns]
    columns = ',\n\t'.join(quoted_columns)

    # Start building the SQL insert statements
    insert_statements = [f"INSERT INTO {table_name} (\n\t{columns}\n) VALUES"]

    for index, row in df.iterrows():
        values = []
        for value in row.values:
            if isinstance(value, str):
                # Escape single quotes by doubling them
                escaped_value = value.replace("'", "''")
                values.append(f"'{escaped_value}'")
            elif pd.isna(value):
                values.append('NULL')
            else:
                values.append(str(value))
        values = ', '.join(values)
        sql = f"({values})"
        insert_statements.append(sql)

    # Combine all the statements into one large string
    final_sql = ',\n'.join(insert_statements) + ';'

    # Write the SQL statements to an output file
    with open(output_sql_file, 'w') as f:
        f.write(final_sql)

    print(f"SQL insert statements have been written to: {output_sql_file}")


# Test the SQL generation function
cleaned_csv_file = r'C:\Users\Owner\OneDrive\Documents\MacBookFiles\GoogleNotebook\All Stocks Data\All_Stocks_20240903PM12_cleaned.csv'
table_name = 'all_stocks_mldata'
output_sql_file = r'C:\Users\Owner\OneDrive\Documents\MacBookFiles\GoogleNotebook\All Stocks Data\All_Stocks_20240903PM12_inserts.sql'

generate_sql_inserts(cleaned_csv_file, table_name, output_sql_file)


