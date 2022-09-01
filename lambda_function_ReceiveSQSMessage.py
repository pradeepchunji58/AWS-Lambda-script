##################
#ReceiveSQSMessage
##################
import json
import boto3

sqs = boto3.client('sqs')

def lambda_handler(event,conte):
    response = sqs.receive_message(
        QueueUrl="https://sqs.us-east-1.amazonaws.com/190954201355/test-sqs",
        MaxNumberOfMessages=5,
        WaitTimeSeconds=20,
    )

    print(f"Number of messages received: {len(response.get('Messages', []))}")

    for message in response.get("Messages", []):
        message_body = message["Body"]
        print(f"Message body: {message_body}")
        print(f"Receipt Handle: {message['ReceiptHandle']}")
