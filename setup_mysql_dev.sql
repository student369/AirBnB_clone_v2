-- Create the database hbnb_dev_db
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- Use the previous database
USE hbnb_dev_db;
-- Create the specific user to this database
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
-- Give the priviliges to this database to the user
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
-- Use other database
USE performance_schema;
-- Give privileges to this other database.
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
