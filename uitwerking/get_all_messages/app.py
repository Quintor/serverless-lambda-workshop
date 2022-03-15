import json
import boto3
import os

dynamodb = boto3.resource('dynamodb', endpoint_url=os.environ['AWS_DYNAMODB_ENDPOINT']) 

def lambda_handler(event, context):
    table = dynamodb.Table('SimpleTopicTable')

    data = table.scan()

    print('Scanned messages: ' + str(data['Count']))

    return {
        "statusCode": 200,
        "body": data['Items']
    }
