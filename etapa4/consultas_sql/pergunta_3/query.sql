SELECT n.name, COUNT(*) indicacoes
FROM tbl_nominees n
WHERE n.name IS NOT NULL
GROUP BY n.name
HAVING COUNT(*) > 3
ORDER BY indicacoes DESC;
