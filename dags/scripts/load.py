import csv
import os
import uuid
from model import Connection, Users
import dags.scripts.config as config


def get_file_path():
    # should return a os file path with correct destination.
    # Do not change file name
    # filename = "random_user.csv"
    # write your code here
    filename = 'random_user.csv'
    filepath = os.path.join(config.CSV_FILE_DIR, filename)
    print(filepath)
    return filepath


def main():
    filename = get_file_path()
    data_insert = []

    # read the csv file
    # Create user object
    # insert the user object in the array
    with open(filename, encoding='utf-8') as csvf:
        csvreader = csv.reader(csvf)
        header = next(csvreader)
        for row in csvreader:
            print('row', row[header.index('firstname')])
            # Create user object
            user = Users(
                gender=row[header.index('gender')],
                email=row[header.index('email')],
                phone=row[header.index('phone')],
                cell=row[header.index('cell')],
                nat=row[header.index('nat')],
                title=row[header.index('title')],
                first=row[header.index('firstname')],
                last=row[header.index('lastname')],
                street_number=row[header.index('street_number')],
                street_name=row[header.index('street_name')],
                city=row[header.index('city')],
                state=row[header.index('state')],
                country=row[header.index('country')],
                postcode=row[header.index('postcode')],
                latitude=row[header.index('latitude')],
                longitude=row[header.index('longitude')],
                timezone_offset=row[header.index('timezone_offset')],
                timezone_description=row[header.index('timezone_description')],
                username=row[header.index('username')],
                password=row[header.index('password')],
                salt=row[header.index('salt')],
                uuid=row[header.index('uuid')],
                md5=row[header.index('md5')],
                sha1=row[header.index('sha1')],
                sha256=row[header.index('sha256')],
                dob_date=row[header.index('dob_date')],
                dob_age=row[header.index('dob_age')],
                registered_date=row[header.index('registered_date')],
                registered_age=row[header.index('registered_age')],
                id_name=row[header.index('id_name')],
                id_value=str(uuid.uuid4()),
                picture_large=row[header.index('picture_large')],
                picture_medium=row[header.index('picture_medium')],
                picture_thumbnail=row[header.index('picture_thumbnail')]
            )
            # Append the Users object to the array
            data_insert.append(user)

    # Connect with the db
    db_connection = Connection()

    session = db_connection.get_session()
    # First delete all previous users table data from schema raw
    session.query(Users).delete()
    #session.bulk_save_objects(data_insert, return_defaults=True)
    session.bulk_save_objects(data_insert, return_defaults=True)

    # Commit db
    session.commit()

    # Close db
    session.close()


if __name__ == '__main__':
    main()