import os

API_URL = os.getenv("API_URL", "https://randomuser.me/api/?seed={}")
CSV_FILE_DIR = os.getenv("CSV_FILE_DIR", "/opt/airflow/dags/datasets/")
SEED = 'ABCD'

PSQL_DB = os.getenv("PSQL_DB", "airflow")
PSQL_USER = os.getenv("PSQL_USER", "airflow")
PSQL_PASSWORD = os.getenv("PSQL_PASSWORD", "airflow")
PSQL_PORT = os.getenv("PSQL_PORT", "5432")
PSQL_HOST = os.getenv("PSQL_HOST", "localhost")
DB_CONNECTION_STRING_POSTGRES = os.getenv("DB_CONNECTION_STRING", "postgresql+psycopg2://airflow:airflow@postgres/airflow")
DB_CONNECTION_STRING_WAREHOUSE = os.getenv("DB_CONNECTION_STRING", "postgresql+psycopg2://admin:admin@localhost/warehouse")
