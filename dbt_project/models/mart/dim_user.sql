-- Drop the tables if they already exist
DROP TABLE IF EXISTS mart.dim_user;

-- Dimension Tables
CREATE TABLE mart.dim_user AS
SELECT
    id_value AS user_id,
    gender,
    email,
    phone,
    cell,
    nat AS nationality,
    title,
    first,
    last,
    street_number,
    street_name,
    city,
    state,
    country,
    postcode,
    latitude,
    longitude,
    timezone_offset,
    timezone_description,
    username,
    password,
    salt,
    md5,
    sha1,
    sha256,
    dob_date,
    dob_age,
    registered_date,
    registered_age,
    id_name,
    uuid,
    picture_large,
    picture_medium,
    picture_thumbnail
FROM
    raw.Users;