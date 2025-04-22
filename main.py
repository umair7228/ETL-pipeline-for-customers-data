from etl.extract import extract_data
from etl.transform import clean_data, save_by_country

def main():
    # Step 1: Extract
    df = extract_data("raw-data/messy_customers_data.xlsx")
    
    # Step 2: Transform
    cleaned_df = clean_data(df)
    
    # Step 3: Save Cleaned Data
    save_by_country(cleaned_df)

if __name__ == "__main__":
    main()
