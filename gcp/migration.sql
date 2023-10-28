CREATE TABLE alembic_version (
    version_num VARCHAR(32) NOT NULL, 
    CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num)
);

-- Running upgrade  -> 4f087dbc68c7

DROP TABLE medical_records;

ALTER TABLE patients ADD COLUMN patient_id INTEGER NOT NULL;

ALTER TABLE patients ADD COLUMN primary_doctor_id INTEGER NOT NULL;

ALTER TABLE patients MODIFY last_name VARCHAR(50) NULL;

ALTER TABLE patients ADD FOREIGN KEY(primary_doctor_id) REFERENCES doctors (doctor_id);

ALTER TABLE patients DROP COLUMN gender;

ALTER TABLE patients DROP COLUMN id;

INSERT INTO alembic_version (version_num) VALUES ('4f087dbc68c7');

