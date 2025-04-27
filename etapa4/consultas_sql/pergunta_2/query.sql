SELECT o.year, c.description, n.winner
FROM tbl_nominees n
JOIN tbl_oscar o ON n.oscar_id = o.id
JOIN tbl_category c ON n.category_id = c.id
JOIN tbl_movie m ON n.movie_id = m.id
WHERE m.title ILIKE 'toy story 3'
ORDER BY o.year, c.description;
