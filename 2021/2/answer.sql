CREATE TABLE day2 (
    key serial PRIMARY KEY,
    command text
);

\copy day2 (command) FROM '2021/2/input.csv';
WITH cte AS (
    SELECT
        substring(command FROM 'forward #"[0-9]+#"' FOR '#')::int AS forward,
        substring(command FROM 'up #"[0-9]+#"' FOR '#')::int AS up,
        substring(command FROM 'down #"[0-9]+#"' FOR '#')::int AS down
    FROM
        day2
)
SELECT
    (sum(up * - 1) + sum(down)) * sum(FORWARD)
FROM
    cte;

WITH cte AS (
    SELECT
        key,
        coalesce(substring(command FROM 'forward #"[0-9]+#"' FOR '#')::int, 0) AS forward,
        coalesce(substring(command FROM 'up #"[0-9]+#"' FOR '#')::int, 0) AS up,
        coalesce(substring(command FROM 'down #"[0-9]+#"' FOR '#')::int, 0) AS down
    FROM
        day2
    ORDER BY
        key
),
cte2 AS (
    SELECT
        FORWARD,
        sum(down - up) OVER (ORDER BY key) AS aim
    FROM
        cte
)
SELECT
    sum(FORWARD) * sum(FORWARD * aim)
FROM
    cte2;
