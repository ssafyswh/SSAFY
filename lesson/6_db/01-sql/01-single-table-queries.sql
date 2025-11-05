-- 01. Querying data
SELECT "FirstName" as 'Name' FROM employees;
-- 02. Sorting data
SELECT 
	Name,
	"Milliseconds" / 60000 AS '재생 시간(분)'
FROM
	tracks
ORDER BY
	"Milliseconds";
-- NULL 정렬 예시
SELECT
	ReportsTo
FROM
	employees
ORDER BY
	"ReportsTo";
-- 03. Filtering data
SELECT DISTINCT
	country
FROM
	customers
ORDER BY
	"Country";

SELECT
	LastName, FirstName, Company, Country
FROM
	customers
WHERE
	Company IS NULL
	OR "Country" = 'USA';

SELECT
	Name, Bytes
FROM
	tracks
WHERE
	-- "Bytes" BETWEEN 10000 AND 500000
	"Bytes" >= 10000
	AND "Bytes" <= 500000
ORDER BY
	"Bytes";

SELECT
	Lastname, Firstname, Country
FROM
	customers
WHERE
	"Country" NOT IN ('Canada', 'Germany', 'France');

SELECT
	Lastname, Firstname
FROM
	customers
WHERE
	"FirstName" LIKE '___a';

SELECT
	TrackId, Name, Bytes
FROM
	tracks
ORDER BY "Bytes" DESC
LIMIT 7;

SELECT
	TrackId, "Name", "Bytes"
FROM
	tracks
ORDER BY "Bytes" DESC
LIMIT 4 OFFSET 3;

-- 04. Grouping data

SELECT
	"Country", COUNT(*)
FROM
	customers
GROUP BY
	"Country";

SELECT
	"Composer",
	AVG("Bytes") AS avgOfBytes
FROM
	tracks
GROUP BY
	"Composer"
ORDER BY
	avgOfBytes DESC;

SELECT
"Composer",
AVG("Milliseconds" / 60000) AS avgofminute
FROM
tracks
WHERE
avgofminute < 10
GROUP BY
composer;
