-- Drop the tables if they already exist
DROP TABLE IF EXISTS mart.dim_age;

CREATE TABLE mart.dim_age AS
SELECT
    user_id,
    CASE
        WHEN dob_age LIKE '%-24%' THEN '18-24'
        WHEN dob_age LIKE '%-34%' THEN '25-34'
        -- Add more age ranges as needed
        ELSE 'Unknown'
    END AS age_range
FROM
    mart.dim_user;

