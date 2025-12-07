# ism2411-data-cleaning-copilot

This project is a small, GitHub-ready data cleaning pipeline built for ISM2411.  
It demonstrates Python data cleaning, responsible use of AI coding tools, and a clean project structure.

## Project Goal
The script takes a messy sales CSV file and cleans it by:
- Standardizing column names  
- Removing whitespace  
- Handling missing values  
- Removing invalid rows (negative prices or quantities)  
- Exporting a processed CSV ready for analysis  

## Project Structure
ism2411-data-cleaning-copilot/
├── data/
│   ├── raw/
│   │   └── sales_data_raw.csv
│   └── processed/
│       └── sales_data_clean.csv
├── src/
│   └── data_cleaning.py            
├── README.md                           
└── reflection.md                       

## How to Run
From the project root, run:
python src/data_cleaning.py

The cleaned file will be created at:
data/processed/sales_data_clean.csv

## Requirements
- Python 3.9+
- pandas
