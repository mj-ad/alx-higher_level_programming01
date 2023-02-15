-- lists all records of the table second_table
SELECT DISTINCT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
