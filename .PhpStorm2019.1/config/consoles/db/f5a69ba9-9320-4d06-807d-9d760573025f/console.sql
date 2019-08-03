SELECT id FROM participant_players_capped GROUP BY player_id, participant_id HAVING count(*) > 1;
DELETE FROM participant_players_capped WHERE id NOT IN (SELECT id FROM participant_players_capped GROUP BY player_id, participant_id HAVING count(*) > 1) AND id NOT IN (SELECT id FROM participant_players_capped GROUP BY player_id, participant_id HAVING count(*) = 1);
