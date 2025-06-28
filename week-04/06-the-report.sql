-- https://www.hackerrank.com/challenges/the-report/problem

SELECT (CASE WHEN Grade < 8 THEN 'NULL' ELSE Name end), Grade, Marks
FROM Students 
S JOIN Grades
ON (Marks <= Max_Mark and Marks >= Min_Mark)
ORDER BY Grade DESC, Name ASC;