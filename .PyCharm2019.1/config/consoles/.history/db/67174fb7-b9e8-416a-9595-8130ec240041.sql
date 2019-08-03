CREATE SCHEMA new_schema;
;-- -. . -..- - / . -. - .-. -.--
SELECT auth_user.email, registration_data.category FROM registration_data INNER JOIN auth_user ON registration_data.user_id = auth_user.id;
;-- -. . -..- - / . -. - .-. -.--
SELECT auth_user.email, registration_data.category, registration_data.name FROM registration_data INNER JOIN auth_user ON registration_data.user_id = auth_user.id;
;-- -. . -..- - / . -. - .-. -.--
SELECT registration_data.name, auth_user.email, registration_data.category FROM registration_data INNER JOIN auth_user ON registration_data.user_id = auth_user.id;
;-- -. . -..- - / . -. - .-. -.--
SELECT registration_data.name, auth_user.email, registration_data.category 
FROM registration_data 
INNER JOIN auth_user ON registration_data.user_id = auth_user.id;
;-- -. . -..- - / . -. - .-. -.--
INNER JOIN auth_user ON registration_data.user_id = auth_user.id
WHERE auth_user.is_superuser = 0;
;-- -. . -..- - / . -. - .-. -.--
SELECT registration_data.name, auth_user.email, registration_data.category
FROM registration_data
INNER JOIN auth_user ON registration_data.user_id = auth_user.id
WHERE auth_user.is_superuser='0';