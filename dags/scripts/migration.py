from pathlib import Path
from sqlalchemy import text
import config
from model import Connection

# Initialize directory and csv file
# create them if does not exist programatically
def init_csv_file():
    # Get the directory path
    csv_dir = Path(config.CSV_FILE_DIR)
    # Create the directory if it does not exist
    csv_dir.mkdir(parents=True, exist_ok=True)
    # Get the file path
    csv_file_path = csv_dir / "random_user.csv"
    print(f"CSV file and directory initialized at: {csv_file_path}")

# Initialize schema and table
def init_db():
    # Establish a db connection
    # get db session
    # create a schema named raw
    # create users table in schema raw with appropiate columns
    # commit db
    # close db
    db_connection = Connection()
    engine = db_connection.get_engine()
    # Get a DB session
    #db_connection.get_session ( )
    connection = engine.connect()
    trans = connection.begin()
    try:
        connection.execute(text("CREATE SCHEMA IF NOT EXISTS raw;"))
        query = text("""
            CREATE TABLE IF NOT EXISTS raw.Users(
                id_value UUID PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL,
                gender VARCHAR(10),
                email VARCHAR(255),
                phone VARCHAR(20),
                cell VARCHAR(255),
                nat VARCHAR(50),
                title VARCHAR(10),
                first VARCHAR(50),
                last VARCHAR(50),
                street_number VARCHAR(255),
                street_name VARCHAR(255),
                city VARCHAR(255),
                state VARCHAR(255),
                country VARCHAR(255),
                postcode VARCHAR(20),
                latitude VARCHAR(50),
                longitude VARCHAR(50),
                timezone_offset VARCHAR(50),
                timezone_description VARCHAR(50),
                username VARCHAR(50),
                password VARCHAR(255),
                salt VARCHAR(255),
                md5 VARCHAR(255),
                sha1 VARCHAR(255),
                sha256 VARCHAR(255),
                dob_date VARCHAR(50),
                dob_age VARCHAR(100),
                registered_date VARCHAR(50),
                registered_age VARCHAR(100),
                id_name VARCHAR(50),
                uuid VARCHAR(255),
                picture_large VARCHAR(255),
                picture_medium VARCHAR(255),
                picture_thumbnail VARCHAR(255)
            );
        """)
        connection.execute(query)
        trans.commit()
    except Exception:
        trans.rollback()
        raise
    # Close db
    trans.close()

if __name__ == '__main__':
    init_csv_file()
    init_db()
