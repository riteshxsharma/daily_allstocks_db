import pandas as pd
import os


def clean_and_validate_csv(file_path, expected_columns=173):
    # Load the CSV file
    df = pd.read_csv(file_path)

    # Check the number of columns
    if df.shape[1] != expected_columns:
        print(f"CSV file has {df.shape[1]} columns, expected {expected_columns}. Attempting to fix...")

        # Add missing columns if necessary
        if df.shape[1] < expected_columns:
            for i in range(df.shape[1], expected_columns):
                df[f'Unknown_{i}'] = None

        # Trim extra columns if too many
        if df.shape[1] > expected_columns:
            df = df.iloc[:, :expected_columns]

    # Fill missing values with appropriate defaults based on column dtype
    df = df.apply(lambda col: col.fillna('') if col.dtype == 'object' else col.fillna(0) if col.dtype in ['float64',
                                                                                                          'int64'] else col.fillna(
        method='ffill'))

    # Output the cleaned CSV to a new file for validation
    output_file_path = file_path.replace('.csv', '_cleaned.csv')
    df.to_csv(output_file_path, index=False)
    print(f"Cleaned CSV file saved to: {output_file_path}")

    return output_file_path


# Test the cleaning function
file_path = r'C:\Users\Owner\OneDrive\Documents\MacBookFiles\GoogleNotebook\All Stocks Data\All_Stocks_20240903PM12.csv'
cleaned_file = clean_and_validate_csv(file_path)
