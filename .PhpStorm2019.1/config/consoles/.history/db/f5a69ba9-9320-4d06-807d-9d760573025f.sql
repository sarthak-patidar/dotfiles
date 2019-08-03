SELECT @@sql_mode;
;-- -. . -..- - / . -. - .-. -.--
SELECT id FROM participant_players_capped WHERE id NOT IN (SELECT id FROM participant_players_capped GROUP BY player_id, participant_id HAVING count(*) > 1);
;-- -. . -..- - / . -. - .-. -.--
SELECT id FROM participant_players_capped WHERE * NOT IN (SELECT id FROM participant_players_capped GROUP BY player_id, participant_id HAVING count(*) > 1);
;-- -. . -..- - / . -. - .-. -.--
SELECT * FROM participant_players_capped WHERE id NOT IN (SELECT id FROM participant_players_capped GROUP BY player_id, participant_id HAVING count(*) > 1);
;-- -. . -..- - / . -. - .-. -.--
SELECT id FROM participant_players_capped GROUP BY player_id, participant_id HAVING count(*) > 1;
;-- -. . -..- - / . -. - .-. -.--
SELECT DISTINCT id FROM participant_players_capped GROUP BY participant_id, player_id;
;-- -. . -..- - / . -. - .-. -.--
SELECT DISTINCT id FROM participant_players_capped WHERE id NOT IN (SELECT id FROM participant_players_capped GROUP BY participant_id, player_id);
;-- -. . -..- - / . -. - .-. -.--
SELECT id FROM participant_players_capped WHERE id NOT IN (SELECT DISTINCT id FROM participant_players_capped GROUP BY participant_id, player_id);
;-- -. . -..- - / . -. - .-. -.--
SELECT * FROM participant_players_capped WHERE id NOT IN (SELECT id FROM participant_players_capped GROUP BY player_id, participant_id HAVING count(*) > 1) AND id NOT IN (SELECT id FROM participant_players_capped GROUP BY player_id, participant_id HAVING count(*) = 1);
;-- -. . -..- - / . -. - .-. -.--
DELETE FROM participant_players_capped WHERE id NOT IN (SELECT id FROM participant_players_capped GROUP BY player_id, participant_id HAVING count(*) > 1) AND id NOT IN (SELECT id FROM participant_players_capped GROUP BY player_id, participant_id HAVING count(*) = 1);