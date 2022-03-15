import json
import boto3

dynamodb = boto3.resource('dynamodb', endpoint_url="http://172.17.0.1:8000") 

def lambda_handler(event, context):
    table = dynamodb.Table('SimpleTopicTable')

    data = table.scan()

    print('Scanned messages: ' + str(data['Count']))

    return {
        "statusCode": 200,
        "body": data['Items']
    }
