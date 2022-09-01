######################
#SendSQSMessage script
######################
import boto3

sqs = boto3.client('sqs')

def lambda_handler(event, context):
    queue_url = 'https://sqs.us-east-1.amazonaws.com/190954201355/lup-qa-sqs'

   # Send message to SQS queue
    response = sqs.send_message(
        QueueUrl=queue_url,
        DelaySeconds=10,
        MessageAttributes={
            'Title': {
                'DataType': 'String',
                'StringValue': 'Learning Lookup'
            },
            'Author': {
                'DataType': 'String',
                'StringValue': 'Naganandini'
            },
            'WeeksOn': {
                'DataType': 'Number',
                'StringValue': '6'
            }
        },
        MessageBody=(
            'Welcome to LearningLookup!'
        )
    )

    print(response['MessageId'])