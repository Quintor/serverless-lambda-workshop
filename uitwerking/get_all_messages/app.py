import json
import boto3
import os

dynamodb = boto3.resource('dynamodb', endpoint_url=os.environ['AWS_DYNAMODB_ENDPOINT']) 

def lambda_handler(event, context):
    table = dynamodb.Table('ForumTable')

    topicfilter = None
    if event['queryStringParameters']:
        topicfilter = event['queryStringParameters'].get('topic')

    if topicfilter:
        print("Returning the messages for topic {}".format(topicfilter))
    else:
        print("No topic filter specified. Returning all messages")

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
