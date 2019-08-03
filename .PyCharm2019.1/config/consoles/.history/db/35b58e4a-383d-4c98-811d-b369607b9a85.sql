SELECT * FROM registration_data JOIN auth_user ON auth_user.id = registration_data.user_id;
;-- -. . -..- - / . -. - .-. -.--
SELECT * FROM registration_data LEFT JOIN auth_user ON auth_user.id = registration_data.user_id WHERE auth_user.is_superuser=0;