-- Drop the tables if they already exist
DROP TABLE IF EXISTS mart.dim_user_interaction;


-- Create the dimensional model
CREATE TABLE mart.dim_user_interaction AS
SELECT
    u.gender,
    u.nat AS nationality,
    -- Add other relevant columns
FROM
    raw.Users u;
