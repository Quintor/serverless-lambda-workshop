import json
import boto3
import os

dynamodb = boto3.resource('dynamodb', endpoint_url=os.environ['AWS_DYNAMODB_ENDPOINT']) 

def lambda_handler(event, context):
    table = dynamodb.Table('SimpleTopicTable')

    # topicFilter = event['queryStringParameters']['topic']


    data = table.scan()
    items = data['Items']

    print('Scanned messages: ' + str(data['Count']))

    # if topicFilter:
    #     print('Received topicFilter: ' + topicFilter)
    #     items = { key:value for (key,value) in items if key == 'topic' value == topicFilter}

    return {
        "statusCode": 200,
        "body": items
    }
