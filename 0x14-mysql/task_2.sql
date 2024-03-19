-- creates the database tyrell_corp and the table nexus6

CREATE DATABASE IF NOT EXISTS tyrell_corp;
USE tyrell_corp;
CREATE TABLE IF NOT EXISTS nexus6 (id INT AUTO_INCREMENT, name VARCHAR(256), PRIMARY KEY (id));
INSERT INTO nexus6 (name) VALUES ('Leon');
GRANT SELECT ON tyrell_corp.`nexus6` to 'holberton_user'@`localhost`;
