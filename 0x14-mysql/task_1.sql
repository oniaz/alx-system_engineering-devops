-- task 1
-- createing the MySQL server user "holberton_user" granted permission to check the primary/replica status of the databases with password set to "projectcorrection280hbtn"

CREATE USER IF NOT EXISTS 'holberton_user'@'localhost' IDENTIFIED BY 'projectcorrection280hbtn';
GRANT REPLICATION CLIENT ON *.* TO 'holberton_user'@'localhost';