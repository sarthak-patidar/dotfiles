SELECT * FROM ges_2019.registration.data;
;-- -. . -..- - / . -. - .-. -.--
SELECT * FROM auth_user WHERE is_superuser = 1;
;-- -. . -..- - / . -. - .-. -.--
SELECT * FROM auth_user WHERE is_superuser = 0;
;-- -. . -..- - / . -. - .-. -.--
SELECT count(city), city FROM registration_data;
;-- -. . -..- - / . -. - .-. -.--
SELECT * FROM registration.data;
;-- -. . -..- - / . -. - .-. -.--
SELECT count(city), city FROM registration_data GROUP BY city;
;-- -. . -..- - / . -. - .-. -.--
SELECT * FROM registration_data;
;-- -. . -..- - / . -. - .-. -.--
SELECT count(*) FROM registration_data WHERE category='Startup';