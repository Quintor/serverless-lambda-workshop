import json
import boto3
import uuid

dynamodb = boto3.resource('dynamodb', endpoint_url="http://172.17.0.1:8000") 

def lambda_handler(event, context):
    recordId = str(uuid.uuid4())
    body = json.loads(event['body'])
    message = body['message']

    print('Generating new DynamoDB record, with ID: ' + recordId)
    print('Input message: ' + message)

    #Creating new record in DynamoDB table
    table = dynamodb.Table('SimpleTopicTable')
    table.put_item(
        Item={
            'id' : recordId,
            'message' : message,
        }
    )

    return {
        "statusCode": 200,
        "body": str(recordId)
    }
