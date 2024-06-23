# Write your MySQL query statement below
SELECT results FROM (SELECT
    u.name as results
FROM
    MovieRating mr
    JOIN Users u on mr.user_id = u.user_id
GROUP BY u.name
ORDER BY COUNT(mr.movie_id) DESC, u.name
LIMIT 1 ) AS h_user
    UNION ALL
SELECT results FROM (SELECT
    m.title as results
FROM
    MovieRating as mr
    JOIN Movies m on mr.movie_id = m.movie_id
WHERE MONTH(mr.created_at) = 2 and YEAR(mr.created_at) = 2020
GROUP BY m.title
ORDER BY AVG(mr.rating) DESC, m.title
LIMIT 1) as h_movie