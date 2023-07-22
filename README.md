# Fetch-Etl-Final
Data Engineering Take Home: ETL off a SQS Queue

The objective of this project is to read the JSON data containing user login behavior from an AWS SQS Queue, mask this data, and then add to a Postgres database.

## Pre-Requisites
Need to have these installed:
- python 3.9
- Docker
- aws cli
- docker-compose
- postgres

## Assumption
We are assuming that the database table is already created in postgres. If its not please create it by following these steps.
- Run this command to connect to the database
```
psql -d postgres -U postgres -p 5432 -h localhost -W
```
-Once inside the database create the table by running this command
```
CREATE TABLE IF NOT EXISTS user_logins( user_id varchar(128), device_type varchar(32), masked_ip varchar(256), masked_device_id varchar(256), locale varchar(32), app_version integer, create_date date );
```


## How to run this application

1. Clone this repository

2. All the necessary modules are in requirements.txt. Please install them by running pip install -r requirements.txt.
```
pip install -r requirements.txt
```

3. After installing the modules you want to start the development environment by running docker-compose up on a new terminal window.
```
docker-compose up
```

4. After the enviroment is running we want to call the command that reads through the SQS, masks id and device_id, and add then add this to a Postgres database.
```
python main.py
```

5. Finally we want to see if the data was added successfully in the postgres database.
- First we want to login in to the database. 
```
psql -d postgres -U postgres -p 5432 -h localhost -W
```
- Then we run this command to see if the data is present.
```
SELECT * FROM user_logins;
```




