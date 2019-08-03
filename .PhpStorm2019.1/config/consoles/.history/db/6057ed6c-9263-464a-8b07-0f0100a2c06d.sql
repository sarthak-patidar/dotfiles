SELECT id FROM participant_players_capped group by participant_id, player_id having count(*) > 1;
;-- -. . -..- - / . -. - .-. -.--
SELECT id FROM participant_players_capped group by participant_id having count(*) > 1;
;-- -. . -..- - / . -. - .-. -.--
SET GLOBAL sql_mode=(SELECT REPLACE(@@sql_mode,'ONLY_FULL_GROUP_BY',''));
;-- -. . -..- - / . -. - .-. -.--
SELECT id FROM participant_players_capped GROUP BY participant_id HAVING count(*) > 1;
;-- -. . -..- - / . -. - .-. -.--
SELECT * FROM participant_players_capped GROUP BY participant_id HAVING count(*) > 1;
;-- -. . -..- - / . -. - .-. -.--
SELECT participant_id FROM participant_players_capped GROUP BY participant_id HAVING count(*) > 1;
;-- -. . -..- - / . -. - .-. -.--
SELECT id, participant_id, player_id FROM participant_players_capped GROUP BY participant_id, player_id HAVING count(*) > 1;
;-- -. . -..- - / . -. - .-. -.--
SELECT participant_id, player_id FROM participant_players_capped GROUP BY participant_id, player_id HAVING count(*) > 1;
;-- -. . -..- - / . -. - .-. -.--
WITH cte AS (
    SELECT participant_id , player_id ,
           row_number() OVER(PARTITION BY participant_id , player_id order by id ) AS [rn]
FROM participant_player_capped
);
;-- -. . -..- - / . -. - .-. -.--
SELECT DISTINCT id FROM participant_players_capped WHERE id NOT IN (SELECT id FROM participant_players_capped GROUP BY participant_id, player_id HAVING count(*) > 1);
;-- -. . -..- - / . -. - .-. -.--
SET GLOBAL sql_mode=(SELECT REPLACE(@@sql_mode, 'ONLY_FULL_GROUP_BY', ''));
;-- -. . -..- - / . -. - .-. -.--
SELECT @@sql_mode;