-- logar com:  psql postgres

CREATE DATABASE oscar;
CREATE USER gabrielsousa WITH PASSWORD '36531590';
GRANT ALL PRIVILEGES ON DATABASE oscar TO gabrielsousa;
