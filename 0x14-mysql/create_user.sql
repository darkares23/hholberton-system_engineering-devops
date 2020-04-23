-- script that creates the MySQL server user user_0d_1.
CREATE USER IF NOT EXISTS 'holberton_user'@'localhost' IDENTIFIED BY 'projectcorrection280hbtn';
GRANT REPLICATION CLIENT ON *.* TO 'holberton_user'@'localhost';

CREATE USER IF NOT EXISTS 'replica_user'@'%' IDENTIFIED BY 'replica';
GRANT REPLICATION CLIENT ON nexus6 TO 'replica_user'@'%';
GRANT REPLICATION SLAVE ON tyrell_corp.nexus6 TO 'slave_user'@'%' IDENTIFIED BY 'password';

pwd = projectcorrection280hbtn