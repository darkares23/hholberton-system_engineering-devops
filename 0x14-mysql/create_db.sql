-- Write a script that creates a table second_table in the database
-- hbtn_0c_0 in your MySQL server and add multiples rows.
CREATE DATABASE IF NOT EXISTS tyrell_corp;
CREATE TABLE `nexus6` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(256) NOT NULL,
  PRIMARY KEY (`id`)
);
INSERT INTO `nexus6` VALUES (1, "John"), (2, "Alex");
GRANT SELECT ON tyrell_corp.* TO CREATE TABLE IF NOT EXISTS nexus6 (id INT NOT NULL AUTO_INCREMENT,
@'localhost';

CHANGE MASTER TO MASTER_HOST='34.74.164.242',MASTER_USER='replica_user', MASTER_PASSWORD='replica', MASTER_LOG_FILE='mysql-bin.000001', MASTER_LOG_POS=  107;