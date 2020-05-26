-- script that creates the MySQL server user user_0d_1.
CREATE USER IF NOT EXISTS 'holberton_user'@'localhost' IDENTIFIED BY 'projectcorrection280hbtn';
GRANT REPLICATION CLIENT ON *.* TO 'holberton_user'@'localhost';

CREATE USER IF NOT EXISTS 'replica_user'@'%' IDENTIFIED BY 'replica';
GRANT REPLICATION CLIENT ON nexus6 TO 'replica_user'@'%';
GRANT REPLICATION SLAVE ON tyrell_corp.nexus6 TO 'slave_user'@'%' IDENTIFIED BY 'password';

pwd = projectcorrection280hbtn

	CHANGE MASTER TO MASTER_HOST='34.74.164.242', MASTER_USER='replica_user', MASTER_PASSWORD='replica', MASTER_LOG_FILE='mysql-bin.000009', MASTER_LOG_POS=597;