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

## Next Steps
1. Add some decoding function to help employees decode the hashed attributes.
2. Add exceptional handling to avoid certain bugs.
3. Implement end to end tests.
4. Add logging.
5. Add a scheduling algorithm to run this application at certain times in a day.


## Production
We can use Kubernetes to deploy this application. Kubernetes simplifies app deployment, scaling, and management with built-in features for high availability, service discovery, and self-healing. It's a popular choice for cloud-native apps.

## Production Ready Components
To make this production ready we would have to add:
1. CI/CD pipeline. We would need this because it would be easier for us to test, build, and deploy.
2. Prometheus to track the application (health and performence).
3. Check if psycopg2-binary can be used in a production environment. (Have to install other dependencies otherwise).


## Scale With A Growing Dataset
1. To scale this application with a growing dataset we can first do vertical scaling. This approach can handle moderate growth in the dataset and processing requirements because we will be adding more cpu, memory, etc.
2. If vertical scaling does not work we can do horizontal scaling. This is where you add more servers or nodes to the ETL cluster. Horizontal scaling allows you to distribute the workload across multiple machines, providing better performance and higher capacity. This allows us to process the data concurrently.
3. Optimize the ETL code. My optimizing the code we can have better performance and efficiency, especially in the data transformation and loading steps.


## PII Recovery
If you need to be able to recover the original PII for specific purposes we can use encryption instead of hashing. Unlike hashing, encryption is a two-way process, where data is transformed using a key, and it can be decrypted back to its original form using the same key.


## Assumption
1. We are assuming that the database table is already created in postgres. If its not please create it by following these steps.
- Run this command to connect to the database
```
psql -d postgres -U postgres -p 5432 -h localhost -W
```
-Once inside the database create the table by running this command
```
CREATE TABLE IF NOT EXISTS user_logins( user_id varchar(128), device_type varchar(32), masked_ip varchar(256), masked_device_id varchar(256), locale varchar(32), app_version integer, create_date date );
```
2. The data from the SQS queue has consistent data. There is no missing data in it.
3. This program will run with just "python main.py".
4. No extra configuration is needed when creating the environment.
5. No need to have any extra Error Handling.
6. The PII can be hashed with a one-way hashing algorithm.









