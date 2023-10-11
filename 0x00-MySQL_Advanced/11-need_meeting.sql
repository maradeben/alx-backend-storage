-- create a view need_meeting
-- shows all students with score below 80
-- and last_meeting is none or greater than 1 month

DROP VIEW IF EXISTS need_meeting;

CREATE VIEW need_meeting AS
SELECT name FROM students
	WHERE score < 80 AND
	(last_meeting IS NULL OR
	last_meeting < ADDDATE(CURDATE(), INTERVAL - 1 MONTH));
