# SELECT DISTINCT name, id FROM players GROUP BY name
# SELECT count(*), name, id, country_id FROM players GROUP BY name, country_id HAVING count(*) > 1
# SELECT count(*), name, id, country_id FROM players GROUP BY LEFT(name, locate(' ', name )) HAVING count(*) > 1
# SELECT DISTINCT name, id, country_id FROM players GROUP BY LEFT(name, locate(' ', name )), country_id HAVING count(*) > 1
# SELECT count(*), country_id FROM players GROUP BY country_id
# SELECT * FROM players GROUP BY LEFT(' ', name), country_id HAVING count(*) > 1
# SELECT players1.* FROM players AS players1 JOIN (SELECT * FROM players GROUP BY LEFT(' ', name), country_id HAVING count(*) > 1) as players2 ON players1.name LIKE "%players2.name%"
# SELECT * FROM players WHERE name IN (SELECT name FROM players WHERE id<1921) ORDER BY name ASC
# SELECT count(*), name FROM players WHERE name IN (SELECT name FROM players WHERE id<1921) GROUP BY name HAVING count(*) > 1 ORDER BY country_id ASC
# SELECT count(*), image, id, name FROM players WHERE image != '' GROUP BY image HAVING count(*) > 1
# SELECT pl1.id, pl1.name, pl1.country_id FROM players AS pl1 JOIN (SELECT name FROM players WHERE id < 1921 GROUP BY name HAVING count(*) > 1) AS pl2 ON pl1.name = pl2.name;
# SELECT players.name, countries.name FROM players, countries WHERE players.country_id = countries.id;
# SELECT name, id FROM players GROUP BY name HAVING count(*) = 1;
# SELECT count(*), name, country_id FROM players GROUP BY name, country_id HAVING count(*) > 1;

# SELECT players.id, players.name, players.dob, players.image, countries.name
# FROM players
#          JOIN countries ON players.country_id = countries.id
# WHERE players.name NOT IN (SELECT name FROM players GROUP BY name, country_id HAVING count(*) > 1);


SELECT name FROM players GROUP BY name, country_id HAVING count(*) > 1;
SELECT name FROM players GROUP BY CONCAT(name, '_' , country_id) HAVING count(*) > 1;
SELECT name FROM players GROUP BY name HAVING count(*) > 1;

SELECT players.id, players.name, players.image, players.dob, countries.name AS country_name
FROM players JOIN countries ON countries.id = players.country_id
WHERE players.name IN (SELECT name FROM players GROUP BY CONCAT(name, '_', country_id) HAVING count(*) > 1);

SELECT players.id, players.name, players.image, players.dob, countries.name AS country_name
FROM players JOIN countries ON countries.id = players.country_id
WHERE players.name IN (SELECT DISTINCT name FROM players GROUP BY name, country_id HAVING count(*)>1);
