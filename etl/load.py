import logging
import pandas as pd
from sqlalchemy import create_engine
from config.df_config import mysql_url, postgres_url

def load_to_mysql(csv_path):
    try:
        df = pd.read_csv(csv_path)
        engine = create_engine(mysql_url)
        df.to_sql('customers', con=engine, if_exists='append', index=False)
        logging.info(f"Loaded into MySQL: {csv_path}")
    except Exception as e:
        logging.error(f"Failed to load into MySQL: {e}", exc_info=True)

def load_to_postgres(csv_path):
    try:
        df = pd.read_csv(csv_path)
        engine = create_engine(postgres_url)
        df.to_sql('customers', con=engine, if_exists='append', index=False)
        logging.info(f"Loaded into PostgreSQL: {csv_path}")
    except Exception as e:
        logging.error(f"Failed to load into PostgreSQL: {e}", exc_info=True)