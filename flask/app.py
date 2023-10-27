from flask import Flask, render_template, request
import os
from dotenv import load_dotenv
from pandas import read_sql
from sqlalchemy import create_engine, text 

load_dotenv() 

# Database connection settings from environment variables
DB_HOST = os.getenv("DB_HOST")
DB_DATABASE = os.getenv("DB_DATABASE")
DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")
# Connection string
conn_string = (
    f"mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}/{DB_DATABASE}"
)

# Create a database engine
engine = create_engine(conn_string, echo=False)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/patients')
def patients():
    with engine.connect() as connection:
        query1 = text('SELECT * FROM patients')
        result1 = connection.execute(query1)
        db_data1 = result1.fetchall()
    return render_template('patients.html', data1=db_data1)

@app.route('/doctors')
def doctors():
    with engine.connect() as connection:
        query2 = text('SELECT * FROM doctors')
        result2 = connection.execute(query2)
        db_data2 = result2.fetchall()
    return render_template('doctors.html', data2=db_data2)

if __name__ == '__main__':
    app.run(debug=True)