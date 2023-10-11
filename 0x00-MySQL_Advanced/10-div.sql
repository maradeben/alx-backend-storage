-- create function SafeDiv
-- takes two parameters and returns first/second
-- return 0 if second is zero

DROP FUNCTION IF EXISTS SafeDiv;

DELIMITER $$
CREATE FUNCTION SafeDiv(a INT, b INT)
RETURNS FLOAT DETERMINISTIC
BEGIN
	IF (b = 0) THEN
		RETURN (0);
	ELSE
		RETURN (a / b);
	END IF;
END $$
DELIMITER ;
