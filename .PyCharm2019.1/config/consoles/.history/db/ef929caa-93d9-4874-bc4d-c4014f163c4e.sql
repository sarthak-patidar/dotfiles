SELECT count(*), image, id, name FROM players GROUP BY image HAVING count(*) > 1;
;-- -. . -..- - / . -. - .-. -.--
SELECT count(*), image, id, name FROM players WHERE image is not NULL GROUP BY image HAVING count(*) > 1;
;-- -. . -..- - / . -. - .-. -.--
SELECT count(*), image, id, name FROM players WHERE image != '' GROUP BY image HAVING count(*) > 1;
;-- -. . -..- - / . -. - .-. -.--
SELECT count(*), name FROM players WHERE name IN (SELECT name FROM players WHERE id<1921) GROUP BY name HAVING count(*) > 1 ORDER BY country_id ASC;
;-- -. . -..- - / . -. - .-. -.--
SELECT DISTINCT players.name FROM players;
;-- -. . -..- - / . -. - .-. -.--
SELECT DISTINCT players.name, countries.name FROM players, countries WHERE players.country_id = countries.id;
;-- -. . -..- - / . -. - .-. -.--
SELECT DISTINCT players.id, players.name, countries.name FROM players, countries WHERE players.country_id = countries.id;
;-- -. . -..- - / . -. - .-. -.--
SELECT DISTINCT players.name, players.id, countries.name FROM players, countries WHERE players.country_id = countries.id;
;-- -. . -..- - / . -. - .-. -.--
SELECT unknown from countries;
;-- -. . -..- - / . -. - .-. -.--
LOAD XML;
;-- -. . -..- - / . -. - .-. -.--
SELECT * FROM failed_jobs;
;-- -. . -..- - / . -. - .-. -.--
SELECT * FROM jobs;
;-- -. . -..- - / . -. - .-. -.--
SELECT players.name, countries.name FROM players, countries WHERE players.country_id = countries.id;
;-- -. . -..- - / . -. - .-. -.--
SELECT pl1.* FROM players AS pl1 JOIN (SELECT name FROM players GROUP BY name HAVING count(*) > 1) AS pl2 ON pl1.name = pl2.name;
;-- -. . -..- - / . -. - .-. -.--
SELECT pl1.id, pl1.name, pl1.country_id FROM players AS pl1 JOIN (SELECT name FROM players GROUP BY name HAVING count(*) > 1) AS pl2 ON pl1.name = pl2.name;
;-- -. . -..- - / . -. - .-. -.--
SELECT pl1.id, pl1.name, pl1.country_id FROM players AS pl1 JOIN (SELECT name FROM players WHERE id < 1921 GROUP BY name HAVING count(*) > 1) AS pl2 ON pl1.name = pl2.name;
;-- -. . -..- - / . -. - .-. -.--
SELECT DISTINCT name, id FROM players GROUP BY name HAVING count(*) = 1;
;-- -. . -..- - / . -. - .-. -.--
SELECT DISTINCT name FROM players GROUP BY name HAVING count(*) = 1;
;-- -. . -..- - / . -. - .-. -.--
SELECT name, id FROM players GROUP BY name HAVING count(*) > 1;
;-- -. . -..- - / . -. - .-. -.--
SELECT name, id FROM players HAVING count(*) > 1;
;-- -. . -..- - / . -. - .-. -.--
SELECT DISTINCT name FROM players HAVING count(*) > 1;
;-- -. . -..- - / . -. - .-. -.--
SELECT DISTINCT name, id FROM players HAVING count(*) > 1;
;-- -. . -..- - / . -. - .-. -.--
SELECT DISTINCT name, id FROM players HAVING count(*) = 1;
;-- -. . -..- - / . -. - .-. -.--
SELECT name FROM players HAVING count(*) = 1;
;-- -. . -..- - / . -. - .-. -.--
SELECT name FROM players GROUP BY name HAVING count(*) = 1;
;-- -. . -..- - / . -. - .-. -.--
SELECT name, id FROM players GROUP BY name HAVING count(*) = 1;
;-- -. . -..- - / . -. - .-. -.--
SELECT count(DISTINCT name), name FROM players;
;-- -. . -..- - / . -. - .-. -.--
SELECT count(DISTINCT name), name FROM players GROUP BY name;
;-- -. . -..- - / . -. - .-. -.--
SELECT count(DISTINCT name), name FROM players GROUP BY name HAVING count(*) > 1;
;-- -. . -..- - / . -. - .-. -.--
SELECT count(DISTINCT name), name FROM players WHERE name !='' GROUP BY name HAVING count(DISTINCT name) > 1;
;-- -. . -..- - / . -. - .-. -.--
SELECT count(DISTINCT name), name FROM players WHERE name !='' GROUP BY name HAVING count(*) > 1;
;-- -. . -..- - / . -. - .-. -.--
SELECT count(DISTINCT name), name, id FROM players WHERE name IS NOT NULL GROUP BY name HAVING count(*) > 1;
;-- -. . -..- - / . -. - .-. -.--
SELECT count(DISTINCT name), name FROM players WHERE name IS NOT NULL GROUP BY name HAVING count(*) > 1;
;-- -. . -..- - / . -. - .-. -.--
SELECT count(name), name FROM players WHERE name IS NOT NULL GROUP BY name HAVING count(*) > 1;
;-- -. . -..- - / . -. - .-. -.--
SELECT player.id, player.name, player.dob, player.image, countries.id FROM players JOIN countries ON players.country_id = countries.id WHERE players.name IN (SELECT name FROM players GROUP BY name HAVING count(*) > 1);
;-- -. . -..- - / . -. - .-. -.--
SELECT players.id, players.name, players.dob, players.image, countries.id FROM players JOIN countries ON players.country_id = countries.id WHERE players.name IN (SELECT name FROM players GROUP BY name HAVING count(*) > 1);
;-- -. . -..- - / . -. - .-. -.--
SELECT players.id, players.name, players.dob, players.image, countries.name FROM players JOIN countries ON players.country_id = countries.id WHERE players.name IN (SELECT name FROM players GROUP BY name HAVING count(*) > 1);
;-- -. . -..- - / . -. - .-. -.--
SELECT name FROM players GROUP BY name, dob HAVING count(*) > 1;
;-- -. . -..- - / . -. - .-. -.--
SELECT count(*), name, dob FROM players GROUP BY name, dob HAVING count(*) > 1;
;-- -. . -..- - / . -. - .-. -.--
SELECT count(*), name, country_id FROM players GROUP BY name, country_id HAVING count(*) > 1;
;-- -. . -..- - / . -. - .-. -.--
SELECT players.id, players.name, players.dob, players.image, countries.name FROM players JOIN countries ON players.country_id = countries.id WHERE players.name IN (SELECT name FROM players GROUP BY name, country_id HAVING count(*) > 1);
;-- -. . -..- - / . -. - .-. -.--
SELECT players.id, players.name, players.dob, players.image, countries.name FROM players JOIN countries ON players.country_id = countries.id WHERE players.name NOT IN (SELECT name FROM players GROUP BY name, country_id HAVING count(*) > 1);
;-- -. . -..- - / . -. - .-. -.--
SELECT players.id, players.name, players.image, players.dob, countries.name FROM players JOIN countries ON countries.id = players.country_id WHERE players.name NOT IN (SELECT DISTINCT name FROM players GROUP BY name HAVING count(*)>1);
;-- -. . -..- - / . -. - .-. -.--
SELECT players.id, players.name, players.image, players.dob, countries.name FROM players JOIN countries ON countries.id = players.country_id WHERE players.name NOT IN (SELECT DISTINCT name FROM players GROUP BY name HAVING count(*)=1);
;-- -. . -..- - / . -. - .-. -.--
SELECT * FROM players WHERE name LIKE '%patidar%';
;-- -. . -..- - / . -. - .-. -.--
SELECT * FROM players WHERE name LIKE '%gunjan%';
;-- -. . -..- - / . -. - .-. -.--
SELECT * FROM players WHERE name LIKE '%sarthak%';
;-- -. . -..- - / . -. - .-. -.--
SELECT * FROM players WHERE name LIKE '%aparna%';
;-- -. . -..- - / . -. - .-. -.--
SELECT * FROM players WHERE name LIKE '%anjali%';
;-- -. . -..- - / . -. - .-. -.--
SELECT * FROM players WHERE name LIKE '%aayushi%';
;-- -. . -..- - / . -. - .-. -.--
SELECT players.id, players.name, players.image, players.dob, countries.name AS country_name FROM players JOIN countries ON countries.id = players.country_id WHERE players.name NOT IN (SELECT DISTINCT name FROM players GROUP BY name HAVING count(*)=1);
;-- -. . -..- - / . -. - .-. -.--
SELECT players.id, players.name, players.image, players.dob, countries.name AS country_name FROM players JOIN countries ON countries.id = players.country_id WHERE players.name NOT IN (SELECT DISTINCT name, country_id FROM players GROUP BY name HAVING count(*)=1);
;-- -. . -..- - / . -. - .-. -.--
SELECT players.id, players.name, players.image, players.dob, countries.name AS country_name FROM players JOIN countries ON countries.id = players.country_id WHERE players.name NOT IN (SELECT DISTINCT name FROM players GROUP BY name, country_id HAVING count(*)=1);
;-- -. . -..- - / . -. - .-. -.--
SELECT players.id, players.name, players.image, players.dob, countries.name AS country_name FROM players JOIN countries ON countries.id = players.country_id WHERE players.name NOT IN (SELECT DISTINCT name FROM players GROUP BY name, country_id HAVING count(*)>1);
;-- -. . -..- - / . -. - .-. -.--
SELECT name FROM players GROUP BY name HAVING count(*) > 1;
;-- -. . -..- - / . -. - .-. -.--
SELECT players.id, players.name, players.image, players.dob, countries.name AS country_name FROM players JOIN countries ON countries.id = players.country_id WHERE players.name IN (SELECT name FROM players GROUP BY name HAVING count(*) > 1);
;-- -. . -..- - / . -. - .-. -.--
SELECT name FROM players GROUP BY name and country_id HAVING count(*) > 1;
;-- -. . -..- - / . -. - .-. -.--
SELECT players.id, players.name, players.image, players.dob, countries.name AS country_name FROM players JOIN countries ON countries.id = players.country_id WHERE players.name IN (SELECT name FROM players GROUP BY name, country_id HAVING count(*) > 1);
;-- -. . -..- - / . -. - .-. -.--
SELECT name FROM players GROUP BY name, country_id HAVING count(*) > 1;
;-- -. . -..- - / . -. - .-. -.--
SELECT DISTINCT countries.name AS country_name, players.name, players.id, players.image, players.dob FROM players JOIN countries ON countries.id = players.country_id WHERE players.name IN (SELECT name FROM players GROUP BY name HAVING count(*) > 1);
;-- -. . -..- - / . -. - .-. -.--
SELECT countries.name AS country_name, players.name, players.id, players.image, players.dob FROM players JOIN countries ON countries.id = players.country_id WHERE players.name IN (SELECT name FROM players GROUP BY name, country_id WITH ROLLUP HAVING count(*) > 1);
;-- -. . -..- - / . -. - .-. -.--
SELECT players.id, players.name, players.image, players.dob, countries.name AS country_name FROM players JOIN countries ON countries.id = players.country_id WHERE players.name NOT IN (SELECT name FROM players GROUP BY CONCAT(name, '_', country_id) HAVING count(*) > 1);
;-- -. . -..- - / . -. - .-. -.--
SELECT name FROM players GROUP BY CONCAT(name, '_' , country_id) HAVING count(*) > 1;
;-- -. . -..- - / . -. - .-. -.--
SELECT players.id, players.name, players.image, players.dob, countries.name AS country_name FROM players JOIN countries ON countries.id = players.country_id WHERE players.name IN (SELECT DISTINCT name FROM players GROUP BY name, country_id HAVING count(*)>1);
;-- -. . -..- - / . -. - .-. -.--
SELECT players.id, players.name, players.image, players.dob, countries.name AS country_name FROM players JOIN countries ON countries.id = players.country_id WHERE players.name IN (SELECT name FROM players GROUP BY CONCAT(name, '_', country_id) HAVING count(*) > 1);
;-- -. . -..- - / . -. - .-. -.--
SELECT name FROM players WHERE CAST(LEFT(' ', name) AS BINARY) RLIKE '[A-Z]';
;-- -. . -..- - / . -. - .-. -.--
SELECT name FROM players WHERE LEFT(' ', name) LIKE 'JP';
;-- -. . -..- - / . -. - .-. -.--
SELECT name FROM players WHERE LEFT(' ', name) LIKE 'SJD';
;-- -. . -..- - / . -. - .-. -.--
SELECT LEFT(' ', name) FROM players WHERE name LIKE '%SJD%';
;-- -. . -..- - / . -. - .-. -.--
SELECT LEFT(name, '') FROM players WHERE name LIKE '%SJD%';
;-- -. . -..- - / . -. - .-. -.--
SELECT LEFT(name, ' ') FROM players WHERE name LIKE '%SJD%';
;-- -. . -..- - / . -. - .-. -.--
SELECT DISTINCT LEFT(name, ' ') FROM players;
;-- -. . -..- - / . -. - .-. -.--
SELECT SUBSTRING_INDEX(name, ' ', 1) FROM players;
;-- -. . -..- - / . -. - .-. -.--
SELECT name FROM players WHERE CAST(SUBSTRING_INDEX(name, ' ', 1) AS BINARY) RLIKE '[A-Z]';
;-- -. . -..- - / . -. - .-. -.--
SELECT name FROM players WHERE SUBSTRING_INDEX(name, ' ', 1) REGEXP '^[A-Z]+$';
;-- -. . -..- - / . -. - .-. -.--
SELECT name FROM players WHERE SUBSTRING_INDEX(name, ' ', 1) RLIKE '[A-Z]';
;-- -. . -..- - / . -. - .-. -.--
SELECT name FROM players WHERE SUBSTRING_INDEX(name, ' ', 1) COLLATE latin1_bin = UPPER(SUBSTRING_INDEX(name, ' ', 1));
;-- -. . -..- - / . -. - .-. -.--
SELECT name FROM players WHERE SUBSTRING_INDEX(name, ' ', 1) COLLATE latin1_general_ci = UPPER(SUBSTRING_INDEX(name, ' ', 1));
;-- -. . -..- - / . -. - .-. -.--
SELECT name FROM players WHERE SUBSTRING_INDEX(name, ' ', 1) = UPPER(SUBSTRING_INDEX(name, ' ', 1));
;-- -. . -..- - / . -. - .-. -.--
SELECT DISTINCT name FROM players WHERE SUBSTRING_INDEX(name, ' ', 1) = UPPER(SUBSTRING_INDEX(name, ' ', 1));