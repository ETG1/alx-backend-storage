-- SQL script to create a table called users
-- The table has the following fields: id, email, name, and country

-- Create the users table if it does not already exist
CREATE TABLE IF NOT EXISTS users(
	id int NOT NULL PRIMARY KEY AUTO_INCREMENT,
	email varchar(255) NOT NULL UNIQUE,
	name varchar(255),
	country ENUM('US', 'CO', 'TN') DEFAULT 'US' NOT NULL
);
