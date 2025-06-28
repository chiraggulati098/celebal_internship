-- https://www.hackerrank.com/challenges/contest-leaderboard/problem

SELECT hacker_id,name,SUM(max_score) AS total_score
FROM (
    SELECT s.hacker_id,h.name,challenge_id,MAX(score) AS max_score
FROM submissions s
left join hackers h
    ON s.hacker_id=h.hacker_id
GROUP BY s.hacker_id,h.name,challenge_id
HAVING MAX(score)>0) AS max_count
GROUP BY hacker_id,name
GROUP BY total_score DESC,hacker_id ASC