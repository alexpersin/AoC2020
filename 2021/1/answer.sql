CREATE TABLE day1 IF NOT EXISTS (
    key serial PRIMARY KEY,
    depth integer
);

COPY day1
FROM
    'input.csv';

WITH cte AS (
    SELECT
        depth,
        lag(depth, 1) OVER (ORDER BY key) prev
    FROM day1
)
SELECT
    sum((depth > prev)::int)
FROM
    cte;

WITH cte AS (
    SELECT
        row_number() OVER (ORDER BY key ROWS BETWEEN 2 PRECEDING AND CURRENT ROW) rn,
        depth,
        sum(depth) OVER (ORDER BY key ROWS BETWEEN 2 PRECEDING AND CURRENT ROW) win3
    FROM day1
),
cte2 AS (
    SELECT
        win3,
        lag(win3, 1) OVER (ORDER BY rn) prev
    FROM cte
    WHERE rn >= 3
)
SELECT
    sum((win3 > prev)::int)
FROM
    cte2;
