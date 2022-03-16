import json
import boto3
import uuid
import os

dynamodb = boto3.resource('dynamodb', endpoint_url=os.environ['AWS_DYNAMODB_ENDPOINT']) 

def lambda_handler(event, context):
    body = json.loads(event['body'])
    message = body['message']
    topic = body['topic']

    print('Input message: ' + message + " for topic: " + topic)

    recordId = str(uuid.uuid4())
    print('Generating new DynamoDB record, with ID: ' + recordId)
    item = {
        'id' : recordId,
        'message' : message,
        'topic': topic
    }

    # Creating new record in DynamoDB table
    table = dynamodb.Table('ForumTable')
    table.put_item(
        Item=item
    )

    return {
        "statusCode": 200,
        "body": str(item)
    }
