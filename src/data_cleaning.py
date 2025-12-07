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
    df = pd.read_csv(file_path)
    return df
