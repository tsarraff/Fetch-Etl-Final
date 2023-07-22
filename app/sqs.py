import boto3
import os
from helpers.sqsHelper import delete_messages
from constants import queue_url

#random keys because boto3 requires it
os.environ["AWS_ACCESS_KEY_ID"] = "randomaccess"
os.environ["AWS_SECRET_ACCESS_KEY"] = "randomsecret"
#aws connection
sqs_connection = boto3.client("sqs", endpoint_url="http://localhost:4566",
                   region_name="us-east-1")


'''
This function will read through the queue and add it to messages list and return it. Then it will remove it from the queue.
If this fails it means there is an error when reading from the queue.
'''
def read_queue(max_messages=100):
    messages = []
    try:
        res = sqs_connection.receive_message(
            QueueUrl=queue_url,
            MaxNumberOfMessages=max_messages
        )
        
        if "Messages" in res:
            messages = res["Messages"]
            delete_messages(sqs_connection, messages) 

    except:
        print("Could not read from SQS.")

    return messages