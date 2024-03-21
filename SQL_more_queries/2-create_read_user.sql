-- Create hbtn_0d_2 database if not exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- Create new user user_0d_2 if he doesn't exit with password user_0d_2_pwd
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
-- Give only SELECT privilege for the database hbtn_0d_2 to user_0d_2
-- and update them
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
FLUSH PRIVILEGES;
