-- Drop the tables if they already exist
DROP TABLE IF EXISTS mart.dim_nationality;

CREATE TABLE mart.dim_nationality AS
SELECT
    DISTINCT nationality AS nationality_name
FROM
    mart.dim_user;
