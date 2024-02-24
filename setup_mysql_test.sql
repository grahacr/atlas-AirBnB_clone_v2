-- Create database hbnb_test_db
-- New user hbnb_test(local host)
-- password hbnb_test_pwd
-- All priv on database hbnb_test_db
-- only Select priv from database performance schema
-- if the database or user doesn't exist, don't error. (Duh.)

-- Create database
CREATE DATABASE IF NOT EXiSTS hbnb_test_db;
-- Create User
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
-- Select that database
USE hbnb_test_db;
-- Add permissions
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
-- Update permissions
FLUSH PRIVILEGES;
