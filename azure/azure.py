import sqlalchemy as db
from sqlalchemy import create_engine, inspect, Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.orm import declarative_base
import os
from dotenv import load_dotenv

load_dotenv()

# Database connection settings from environment variables
DB_HOST = os.getenv("DB_HOST")
DB_DATABASE = os.getenv("DB_DATABASE")
DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_PORT = int(os.getenv("DB_PORT", 3306))
DB_CHARSET = os.getenv("DB_CHARSET", "utf8mb4")

Base = declarative_base() 
 
class Doctors(Base):
    __tablename__ = 'doctors'
    
    doctor_id = Column(Integer, primary_key=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    specialization = Column(String(50), nullable=False)
    contact_number = Column(String(15))
    drtable = relationship('patients', back_populates='doctors')
 
class patients(Base):
    __tablename__ = 'patients'

    patient_id = Column(Integer, primary_key=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50))
    date_of_birth = Column(Date, nullable=False)
    contact_number = Column(String(15))    
    primary_doctor_id = Column(Integer, ForeignKey('doctors.doctor_id'), nullable=False) 
    phone_number = Column(String(15))
    gender = Column(String(30))    

    pxtable = relationship('doctors', back_populates='patients')

connect_args={'ssl':{'fake_flag_to_enable_tls': True}}
connection_string = (f'mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_DATABASE}'
                    f"?charset={DB_CHARSET}")
                    
engine = create_engine(
        connection_string,
        connect_args=connect_args)

inspector = inspect(engine)
inspector.get_table_names()

# Create tables using sqlalchemy models
Base.metadata.create_all(engine)



