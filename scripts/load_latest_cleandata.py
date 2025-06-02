import psycopg2
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

def execute_sql_file(sql_file_path, table_name):
    # Get database connection parameters from environment variables
    db_name = os.getenv('DB_NAME')
    db_user = os.getenv('DB_USER')
    db_password = os.getenv('DB_PASSWORD')
    db_host = os.getenv('DB_HOST')
    db_port = os.getenv('DB_PORT')

    # Connect to your PostgreSQL database
    try:
        conn = psycopg2.connect(
            dbname=db_name,
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port
        )
        cursor = conn.cursor()

        # Open and read the SQL file
        with open(sql_file_path, 'r') as sql_file:
            sql_commands = sql_file.read()

        # Split the SQL file into individual commands
        sql_commands = sql_commands.split(';')[:-1]  # Remove the last empty item after split
        sql_commands = [cmd.strip() + ';' for cmd in sql_commands]  # Re-add the semicolon

        # Execute each command
        for command in sql_commands:
            try:
                cursor.execute(command)
            except psycopg2.Error as e:
                print(f"Error executing command: {command}\n{e}")

        # Commit the transaction
        conn.commit()
        print(f"SQL file executed successfully for table {table_name}.")

    except psycopg2.Error as e:
        print(f"Database connection error: {e}")

    finally:
        # Close the cursor and connection
        if cursor:
            cursor.close()
        if conn:
            conn.close()

# Path to the SQL file
sql_file_path = r'C:\Users\Owner\OneDrive\Documents\MacBookFiles\GoogleNotebook\All Stocks Data\All_Stocks_20240903PM12_inserts.sql'
table_name = 'all_stocks_mldata'

# Execute the SQL file
execute_sql_file(sql_file_path, table_name)
