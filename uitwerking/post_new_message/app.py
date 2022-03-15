import json
import boto3
import uuid
import os

dynamodb = boto3.resource('dynamodb', endpoint_url=os.environ['AWS_DYNAMODB_ENDPOINT']) 

def lambda_handler(event, context):
    recordId = str(uuid.uuid4())
    body = json.loads(event['body'])
    message = body['message']
    topic = body['topic']

    print('Generating new DynamoDB record, with ID: ' + recordId)
    print('Input message: ' + message)

    #Creating new record in DynamoDB table
    table = dynamodb.Table('SimpleTopicTable')
    table.put_item(
        Item={
            'id' : recordId,
            'message' : message,
            'topic': topic
        }
    )

    return {
        "statusCode": 200,
        "body": str(recordId)
    }
