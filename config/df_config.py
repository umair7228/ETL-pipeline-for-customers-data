from sqlalchemy.engine import URL

mysql_url = URL.create(
    drivername="mysql+pymysql",
    username="root",
    password="umair",
    host="localhost",
    database="customer_us_db"
)

postgres_url = URL.create(
    drivername="postgresql+psycopg2",
    username="postgres",
    password="umair",
    host="localhost",
    port=5432,
    database="customer_global_db"
)