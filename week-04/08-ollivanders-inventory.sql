-- https://www.hackerrank.com/challenges/harry-potter-and-wands/problem

Select w.id, wp.age, w.coins_needed, w.power 
FROM Wands as w inner join Wands_Property as wp
ON w.code = wp.code where wp.is_evil = 0 AND w.coins_needed 
IN (
    SELECT Min(w1.coins_needed) 
    from Wands w1 join Wands_Property wp1 
    on w1.code=wp1.code 
    where wp1.age = wp.age and w1.power = w.power
) 
order by w.power DESC , wp.age DESC;