-- create a stored procedure
-- computes and stores average weighted score for a student

DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser;

DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUser (
	IN user_id INT
)

BEGIN
	DECLARE weighted_average FLOAT;
	SELECT SUM(score * weight) / SUM(weight) INTO weighted_average
	FROM corrections as c
	JOIN projects AS p ON c.project_id=p.id
	WHERE c.user_id = user_id;

	UPDATE users SET average_score = weighted_average
	WHERE id = user_id;
END $$
DELIMITER ;
