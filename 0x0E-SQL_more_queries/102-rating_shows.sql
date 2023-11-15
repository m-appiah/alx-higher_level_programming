-- lists all shows from hbtn_0d_tvshows_rate by their rating.

SELECT CONCAT(tv_shows.title, ' - ', SUM(ratings.rating)) AS "Show - Rating Sum"
FROM tv_shows
JOIN ratings ON tv_shows.id = ratings.show_id
GROUP BY tv_shows.title
ORDER BY SUM(ratings.rating) DESC;
