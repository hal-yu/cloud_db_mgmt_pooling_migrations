# cloud_db_mgmt_pooling_migrations
Gain practical experience in managing a cloud-based MySQL database with a focus on implementing connection pooling and performing database migrations. You will work with both Azure and Google Cloud Platform (GCP) for this assignment.

## MySQL Instance Setups:
Azure: Create a flexible MySQL server with Standard_B1s (1 vCore, 1GiB memory, 400  max iops) compute size. In server parameterse, change max connections to 20 and connect timeout to 3. Add a Firewall rule with a public network with 0.0.0.0-255.255.255.255.
GCP: Create a MySQL server with the enterprise edition. Select Sandbox preset with a shared core using 1vCPI 0.614 Gb. For networks, allow all using 0.0.0.0/0. 

## Database Schema and Data
In both GCP and Azure MySQL database, I created a database named halyu and haley respectively. In order to create new tables, I connected it using with my own information.
```
f"mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_DATABASE}"
    f"?charset={DB_CHARSET}"
```
I connected it to MySQL Workbench to create an ERD diagram using the 2 tables: patients and doctors. 

## Migration
I created azure.py and gcp.py file. I inserted values into my tables. In case they weren't installed previously, I did pip install mysqlalchemy and pymysql into the terminal. After using ```alembic initmigrations``` into the terminal, an alembic.ini file and migrations appeared. In line 63 of the alembic.ini file, change it to ```sqlalchemy.url = mysql+mysqlconnector://username:password@host/database_name```. In the env.py file under migrations folder, change line 19 to the python file name, either azure or gcp, and ```target_metadata = Base.metadata```. Run ```alembic revision --autogenerate -m "create tables"``` into the terminal. Then run ```alembic upgrade head``` to run migrations and ```alembic upgrade head --sql > migration.sql``` to update and see the changes. 

## Flask
A flask app was connected to the MySQL instances and displayed the database doctors and patients with values from [values.sql](https://github.com/hal-yu/cloud_db_mgmt_pooling_migrations/blob/main/SQL%20Codes/values.sql). The python file was created which contains the code for the flask app. All the html files are in a templates folder. 
 
