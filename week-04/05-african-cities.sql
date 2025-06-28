-- https://www.hackerrank.com/challenges/african-cities/problem

SELECT CITY.NAME
FROM CITY
LEFT JOIN COUNTRY
ON CITY.COUNTRYCODE = COUNTRY.CODE
WHERE COUNTRY.CONTINENT = 'Africa';