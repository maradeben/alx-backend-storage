-- creates stored procedure that computes average score for student
-- takes 1 input, the user_id

DELIMITER $$
CREATE PROCEDURE ComputeAverageScoreForUser (
	IN user_id INT
)

BEGIN
	DECLARE average FLOAT;
	SELECT AVG(score) INTO average 
	FROM corrections c
	WHERE c.user_id = user_id;

	UPDATE users SET average_score = average WHERE user_id = id;
END $$
DELIMITER ;
