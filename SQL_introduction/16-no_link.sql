-- List all records (score, name) of the second_table table
-- where the name field is not NULL
SELECT score, name FROM second_table ORDER BY score DESC WHERE name IS NOT NULL;
