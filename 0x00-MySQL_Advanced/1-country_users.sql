-- create TABLE users with:
-- id, email and name
-- scripts should run if table not exists
-- can be executed on any database
-- country, with US, CO and TN, US default, NOT NULL

CREATE TABLE IF NOT EXISTS users (
	id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	email VARCHAR(255) NOT NULL UNIQUE,
	name VARCHAR(255),
	country ENUM('US', 'CO', 'TN') NOT NULL
	)
