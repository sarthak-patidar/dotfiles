SELECT * FROM auth_user;
;-- -. . -..- - / . -. - .-. -.--
SELECT concat('DROP TABLE IF EXISTS `', table_name, '`;')
FROM information_schema.tables
WHERE table_schema = 'vitaldocz_blog';
;-- -. . -..- - / . -. - .-. -.--
SHOW TABLES;
;-- -. . -..- - / . -. - .-. -.--
SELECT id, email FROM accounts_user;