from config import POSTGRES_CONNECTION
from sqs import read_queue
from helpers.mainHelper import create_record_objects
from postgres import add_data


'''
In this file we will read all the records from the SQS and create proper record objects and add them to the postgres database.
'''

if __name__ == "__main__":
    messages = read_queue()

    records = create_record_objects(messages)

    add_data(POSTGRES_CONNECTION, records)


