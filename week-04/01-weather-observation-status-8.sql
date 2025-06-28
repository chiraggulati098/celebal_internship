-- https://www.hackerrank.com/challenges/weather-observation-station-8/problem

SELECT DISTINCT CITY
FROM STATION
WHERE LOWER(LEFT(CITY, 1)) IN ('a','e','i','o','u') AND LOWER(RIGHT(CITY, 1))
IN ('a','e','i','o','u');