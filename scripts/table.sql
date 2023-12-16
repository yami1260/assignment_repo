-- Drop the table if it already exists
DROP TABLE IF EXISTS raw.Users;

-- Create users table under raw schema
CREATE TABLE IF NOT EXISTS raw.Users (
    id_value VARCHAR(50) PRIMARY KEY NOT NULL,
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


