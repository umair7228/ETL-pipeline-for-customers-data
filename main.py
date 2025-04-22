from etl.metadata import generate_metadata
from config.logging_config import setup_logger
import logging
from etl.extract import extract_data
from etl.transform import clean_data, save_by_country
from etl.load import load_to_mysql, load_to_postgres

def main():
    setup_logger()
    logging.info("ETL Pipeline started")

    try:
        df = extract_data("raw-data/messy_customers_data.xlsx")
        logging.info("Data extracted successfully")

        cleaned_df = clean_data(df)
        logging.info("Data cleaned")

        cleaned_df = clean_data(df)
        generate_metadata(cleaned_df)

        save_by_country(cleaned_df)
        logging.info("Cleaned CSVs saved")

        load_to_mysql("final_data/country_usa.csv")
        load_to_postgres("final_data/country_uk.csv")
        load_to_postgres("final_data/country_india.csv")
        logging.info("Data loaded into both databases")

    except Exception as e:
        logging.error(f"ETL failed: {e}", exc_info=True)

if __name__ == "__main__":
    main()