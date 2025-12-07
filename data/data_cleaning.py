"""
data_cleaning.py
----------------
Purpose:
This script loads a messy sales dataset and applies a series of data cleaning 
steps including standardizing column names, stripping whitespace, handling 
missing values, and removing invalid rows. The cleaned dataset is saved to 
data/processed/sales_data_clean.csv.

This file also includes several functions that were initially generated using 
GitHub Copilot and then modified for clarity and correctness.
"""

import pandas as pd

# Function: load_data
# Copilot-assisted: YES
# What it does: Loads a CSV file into a pandas DataFrame.
# Why: Centralizes file loading and lets the project scale easily.

def load_data(file_path: str) -> pd.DataFrame:
    df = pd.read_csv("data\sales_data_raw.csv")
    return df

# Function: clean_column_names
# Copilot-assisted: YES
# What it does: Standardizes column names to lowercase and underscores.
# Why: Ensures consistency and prevents key errors later in cleaning steps.

def clean_column_names(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df.columns = (
        df.columns.str.strip()
        .str.lower()
        .str.replace(" ", "_")
        .str.replace("-", "_")
    )
    return df

# Function: handle_missing_values
# Copilot-assisted: YES
# What it does: Handles missing values in price and quantity.
# Why: Missing numerical values break calculations and indicate incomplete data.

def handle_missing_values(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    # Strip text fields (product, category)
    str_cols = df.select_dtypes(include="object").columns
    for col in str_cols:
        df[col] = df[col].astype(str).str.strip()

    # Drop rows where price or quantity is missing
    df = df.dropna(subset=["price", "qty"]) 

    return df

# Function: remove_invalid_rows
# Copilot-assisted: YES
# What it does: Removes negative prices and quantities.
# Why: Negative values are data entry errors and cannot represent real sales.

def remove_invalid_rows(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df = df[df["price"] >= 0]
    df = df[df["quantity"] >= 0]
    return df

# Main execution block
# Allows script to be run end-to-end.

if __name__ == "__main__":
    raw_path = "data\sales_data_raw.csv"
    cleaned_path = "data\processed\sales_data_clean.csv"

    df_raw = load_data(raw_path)
    df_clean = clean_column_names(df_raw)
    df_clean = handle_missing_values(df_clean)
    df_clean = remove_invalid_rows(df_clean)

    df_clean.to_csv(cleaned_path, index=False)
    
    print("Cleaning complete. First few rows:")
    print(df_clean.head())

    # I am encountering some errors in the code and was not able to generate the cleaned csv file 
    # after trying to fix errors many times.