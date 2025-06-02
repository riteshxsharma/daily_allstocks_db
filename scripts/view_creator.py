def create_view(view_name, table_name, cursor, connection):
    create_view_query = f"""
    CREATE OR REPLACE VIEW {view_name} AS
    SELECT * FROM {table_name}
    ORDER BY some_column;  # Replace 'some_column' with the actual column you want to sort by
    """
    cursor.execute(create_view_query)
    connection.commit()
    print(f"View {view_name} created successfully.")
