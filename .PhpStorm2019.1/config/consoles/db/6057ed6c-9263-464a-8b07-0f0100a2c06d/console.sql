SELECT DISTINCT id FROM participant_players_capped WHERE id NOT IN (SELECT id FROM participant_players_capped GROUP BY participant_id, player_id HAVING count(*) > 1);
SELECT @@sql_mode;
SET GLOBAL sql_mode=(SELECT REPLACE(@@sql_mode, 'ONLY_FULL_GROUP_BY', ''));