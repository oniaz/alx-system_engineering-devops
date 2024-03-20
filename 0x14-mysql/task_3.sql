-- task 3
-- createing the user "replica_user" granted permission to check the primary/replica status of the databases with password set to "spice"
-- granting the user holberton_user the SELECT permission on the mysql.user table.

CREATE USER IF NOT EXISTS 'replica_user'@'%' IDENTIFIED BY 'spice';
GRANT REPLICATION SLAVE ON *.* TO 'replica_user'@'%';
GRANT SELECT ON mysql.`user` to 'holberton_user'@`localhost`;
