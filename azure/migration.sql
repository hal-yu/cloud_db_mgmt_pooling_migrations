CREATE TABLE alembic_version (
    version_num VARCHAR(32) NOT NULL, 
    CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num)
);

-- Running upgrade  -> 1206094c43a9

ALTER TABLE patients ADD COLUMN phone_number VARCHAR(15);

ALTER TABLE patients ADD COLUMN gender VARCHAR(30);

INSERT INTO alembic_version (version_num) VALUES ('1206094c43a9');

