
'''
This function will loop through all the instances in the message list and delete them from the queue.
'''

def delete_messages(sqs_connection, messages):
    for m in messages:
        sqs_connection.delete_message(
            QueueUrl='http://localhost:4566/000000000000/login-queue',
            ReceiptHandle=m["ReceiptHandle"]
        )