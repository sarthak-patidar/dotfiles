SHOW TABLES;
;-- -. . -..- - / . -. - .-. -.--
SELECT * FROM players GROUP BY 'name';
;-- -. . -..- - / . -. - .-. -.--
SELECT * FROM players DISTINCT name;
;-- -. . -..- - / . -. - .-. -.--
SELECT DISTINCT 'name', 'id' FROM players;
;-- -. . -..- - / . -. - .-. -.--
SELECT DISTINCT name, id FROM players;
;-- -. . -..- - / . -. - .-. -.--
SELECT DISTINCT id FROM players GROUP BY name;
;-- -. . -..- - / . -. - .-. -.--
SELECT count(*), name, id FROM players GROUP BY name HAVING count(*) > 1;
;-- -. . -..- - / . -. - .-. -.--
SELECT count(*), name, id FROM players GROUP BY name, country_id HAVING count(*) > 1;
;-- -. . -..- - / . -. - .-. -.--
SELECT DISTINCT name, id FROM players GROUP BY name;
;-- -. . -..- - / . -. - .-. -.--
SELECT count(*), name, id, country_id FROM players GROUP BY name, country_id HAVING count(*) > 1;
;-- -. . -..- - / . -. - .-. -.--
SELECT count(*), name, id, country_id FROM players GROUP BY LEFT(name, CHARINDEX(' ', name + ' ')-1);
;-- -. . -..- - / . -. - .-. -.--
SELECT count(*), name, id, country_id FROM players GROUP BY LEFT(name, locate(' ', name )-1);
;-- -. . -..- - / . -. - .-. -.--
SELECT count(*), name, id, country_id FROM players GROUP BY LEFT(name, locate(' ', name )-1) HAVING count(*) > 1;
;-- -. . -..- - / . -. - .-. -.--
SELECT count(*), name, id, country_id FROM players GROUP BY LEFT(name, locate(' ', name )) HAVING count(*) > 1;
;-- -. . -..- - / . -. - .-. -.--
SELECT count(*), name, id, country_id FROM players GROUP BY LEFT(name, locate(' ', name )), country_id HAVING count(*) > 1;
;-- -. . -..- - / . -. - .-. -.--
SELECT DISTINCT name, id, country_id FROM players GROUP BY LEFT(name, locate(' ', name )), country_id HAVING count(*) > 1;
;-- -. . -..- - / . -. - .-. -.--
SELECT count(*), country_id, name FROM players GROUP BY country_id;
;-- -. . -..- - / . -. - .-. -.--
SELECT count(*), country_id FROM players GROUP BY country_id;
;-- -. . -..- - / . -. - .-. -.--
SELECT players1.* FROM players AS players1 JOIN (SELECT id FROM players GROUP BY LEFT(' ', name), country_id HAVING count(*) > 1) as players2 ON players1.id = players2.id;
;-- -. . -..- - / . -. - .-. -.--
SELECT players1.* FROM players AS players1 JOIN (SELECT id FROM players GROUP BY LEFT(' ', name) HAVING count(*) > 1) as players2 ON players1.id = players2.id;
;-- -. . -..- - / . -. - .-. -.--
SELECT players1.* FROM players AS players1 JOIN (SELECT DISTINCT id FROM players GROUP BY LEFT(' ', name) HAVING count(*) > 1) as players2 ON players1.id = players2.id;
;-- -. . -..- - / . -. - .-. -.--
SELECT DISTINCT id FROM players GROUP BY LEFT(' ', name) HAVING count(*) > 1;
;-- -. . -..- - / . -. - .-. -.--
SELECT DISTINCT id FROM players GROUP BY LEFT(' ', name), country_id HAVING count(*) > 1;
;-- -. . -..- - / . -. - .-. -.--
SELECT players1.* FROM players AS players1 JOIN (SELECT * FROM players GROUP BY LEFT(' ', name), country_id HAVING count(*) > 1) as players2 ON players1.country_id = players2.country_id;
;-- -. . -..- - / . -. - .-. -.--
SELECT players1.* FROM players AS players1 JOIN (SELECT * FROM players GROUP BY LEFT(' ', name), country_id HAVING count(*) > 1) as players2 ON players1.name LIKE '%"players2.name"%';
;-- -. . -..- - / . -. - .-. -.--
SELECT * FROM players GROUP BY LEFT(' ', name), country_id HAVING count(*) > 1;
;-- -. . -..- - / . -. - .-. -.--
SELECT players1.* FROM players AS players1 JOIN (SELECT * FROM players GROUP BY LEFT(' ', name), country_id HAVING count(*) > 1) as players2 ON players1.name LIKE "%players2.name%";
;-- -. . -..- - / . -. - .-. -.--
SELECT * FROM players WHERE name IN (SELECT name FROM players WHERE id<1921) ORDER BY name ASC GROUP BY name HAVING count(*) > 1;
;-- -. . -..- - / . -. - .-. -.--
SELECT * FROM players WHERE name IN (SELECT name FROM players WHERE id<1921) GROUP BY name HAVING count(*) > 1 ORDER BY name ASC;
;-- -. . -..- - / . -. - .-. -.--
SELECT * FROM players WHERE name IN (SELECT name FROM players WHERE id<1921) GROUP BY name HAVING count(*) > 1;
;-- -. . -..- - / . -. - .-. -.--
SELECT * FROM players WHERE name IN (SELECT name FROM players WHERE id<1921) ORDER BY name ASC;
;-- -. . -..- - / . -. - .-. -.--
SELECT count(*), image, id, name FROM players GROUP BY image HAVING count(*) > 1;
;-- -. . -..- - / . -. - .-. -.--
SELECT * FROM players WHERE name IN (SELECT DISTINCT name FROM players WHERE id<1921) GROUP BY name HAVING count(*) > 1;
;-- -. . -..- - / . -. - .-. -.--
SELECT * FROM players WHERE name IN (SELECT DISTINCT name FROM players WHERE id<1921) HAVING count(*) > 1;
;-- -. . -..- - / . -. - .-. -.--
SELECT * FROM players WHERE name IN (SELECT DISTINCT name FROM players WHERE id<1921) ORDER BY country_id ASC;
;-- -. . -..- - / . -. - .-. -.--
SELECT count(*), * FROM players WHERE name IN (SELECT DISTINCT name FROM players WHERE id<1921) ORDER BY country_id ASC;
;-- -. . -..- - / . -. - .-. -.--
SELECT count(*) FROM players WHERE name IN (SELECT DISTINCT name FROM players WHERE id<1921) GROUP BY name ORDER BY country_id ASC;
;-- -. . -..- - / . -. - .-. -.--
SELECT count(*), name FROM players WHERE name IN (SELECT DISTINCT name FROM players WHERE id<1921) GROUP BY name HAVING count(*) > 1 ORDER BY country_id ASC;