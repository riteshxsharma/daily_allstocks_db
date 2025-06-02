from downloader import download_csv
from db_manager import create_table_from_csv, load_data_into_table
from view_creator import create_view
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Paths and table names
csv_path = 'data.csv'
table_name = 'your_table_name'
view_name = 'your_view_name'

# Workflow steps
download_csv(os.getenv("CSV_URL"), csv_path)
create_table_from_csv(csv_path, table_name)
load_data_into_table(csv_path, table_name)
create_view(view_name, table_name)
