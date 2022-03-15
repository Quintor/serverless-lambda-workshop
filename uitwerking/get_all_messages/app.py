import json
import boto3

dynamodb = boto3.resource('dynamodb')

def lambda_handler(event, context):
    table = dynamodb.Table('SimpleTopicTable')

    data = table.scan()

    print('Scanned messages: ' + data.length)

    return {
        "statusCode": 200,
        "body": data
    }
