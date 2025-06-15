import pandas as pd
import os

def load_data(file_path):
    """
    Load data from a CSV file.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"{file_path} does not exist.")
    return pd.read_csv(file_path)

def clean_data(df):
    """
    Clean the data by handling missing values, duplicates, and inconsistent formats.
    """
    # Handle missing values
    df = df.dropna(subset=['ClaimID', 'PolicyID', 'ClaimAmount'])

    # Remove duplicates
    df = df.drop_duplicates()

    # Standardize date format
    if 'ClaimDate' in df.columns:
        df['ClaimDate'] = pd.to_datetime(df['ClaimDate'], errors='coerce')

    # Convert categorical data to consistent formats
    if 'VehicleType' in df.columns:
        df['VehicleType'] = df['VehicleType'].str.strip().str.lower()

    return df

def save_cleaned_data(df, output_path):
    """
    Save the cleaned data to a CSV file.
    """
    df.to_csv(output_path, index=False)
    print(f"Cleaned data saved to {output_path}")

if __name__ == "__main__":
    # Example usage
    raw_data_path = "data/raw/insurance_claims.csv"
    cleaned_data_path = "data/processed/cleaned_insurance_claims.csv"

    data = load_data(raw_data_path)
    cleaned_data = clean_data(data)
    save_cleaned_data(cleaned_data, cleaned_data_path)
