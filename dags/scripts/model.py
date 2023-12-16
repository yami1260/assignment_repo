import config
import uuid
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, String
from uuid import uuid4


class Connection(object):
    def __init__(self):
        # create a db connection
        #print(config.DB_CONNECTION_STRING_WAREHOUSE)
        engine = create_engine(config.DB_CONNECTION_STRING_WAREHOUSE, pool_pre_ping=True)
        self.engine = engine

    def get_session(self):
        Session = sessionmaker(bind=self.engine)
        return Session()

    def get_engine(self):
        return self.engine


Base = declarative_base()


def init_db():
    # create a db connection
    engine = create_engine(config.DB_CONNECTION_STRING_WAREHOUSE, pool_pre_ping=True)
    Base.metadata.create_all(bind=engine)

class Users(Base):
    __tablename__ = 'Users'
    id_value = Column (String, primary_key=True, nullable=False)
    gender = Column(String(10))
    email = Column(String(255))
    phone = Column(String(20))
    cell = Column(String(255))
    nat = Column(String(50))
    title = Column(String(10))
    firstname = Column(String(50))
    lastname = Column(String(50))
    street_number = Column(String(255))
    street_name = Column(String(255))
    city = Column(String(255))
    state = Column(String(255))
    country = Column(String(255))
    postcode = Column(String(20))
    latitude = Column(String(50))
    longitude = Column(String(50))
    timezone_offset = Column(String(50))
    timezone_description = Column(String(50))
    username = Column(String(50))
    password = Column(String(255))
    uuid = Column (String (255))
    salt = Column(String(255))
    md5 = Column(String(255))
    sha1 = Column(String(255))
    sha256 = Column(String(255))
    dob_date = Column(String(50))
    dob_age = Column(String(100))
    registered_date = Column(String(50))
    registered_age = Column(String(100))
    id_name = Column(String(50))
    #id_value = Column(String, primary_key=True)
    picture_large = Column(String(255))
    picture_medium = Column(String(255))
    picture_thumbnail = Column(String(255))

    def __init__(self, gender, email, phone, cell, nat, title, first, last, street_number, street_name,
                 city, state, country, postcode, latitude, longitude, timezone_offset, timezone_description,
                 uuid, username, password, salt, md5, sha1, sha256, dob_date, dob_age, registered_date,
                 registered_age, id_name, id_value, picture_large, picture_medium, picture_thumbnail):
        self.gender = gender
        self.email = email
        self.phone = phone
        self.cell = cell
        self.nat = nat
        self.title = title
        self.first = first
        self.last = last
        self.street_number = street_number
        self.street_name = street_name
        self.city = city
        self.state = state
        self.country = country
        self.postcode = postcode
        self.latitude = latitude
        self.longitude = longitude
        self.timezone_offset = timezone_offset
        self.timezone_description = timezone_description
        self.uuid = uuid
        self.username = username
        self.password = password
        self.salt = salt
        self.md5 = md5
        self.sha1 = sha1
        self.sha256 = sha256
        self.dob_date = dob_date
        self.dob_age = dob_age
        self.registered_date = registered_date
        self.registered_age = registered_age
        self.id_name = id_name
        self.id_value = id_value
        self.picture_large = picture_large
        self.picture_medium = picture_medium
        self.picture_thumbnail = picture_thumbnail



init_db()