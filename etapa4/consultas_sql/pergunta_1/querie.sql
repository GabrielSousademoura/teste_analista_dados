SELECT o.year, o.ceremony, m.title
FROM tbl_nominees n
JOIN tbl_oscar o ON n.oscar_id = o.id
JOIN tbl_category c ON n.category_id = c.id
JOIN tbl_movie m ON n.movie_id = m.id
WHERE c.description ILIKE 'best picture'
ORDER BY o.year, m.title;
