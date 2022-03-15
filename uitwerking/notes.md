# Uitwerking notes

## Use hello world api 
- Start hello world api _sam local start-api_
- Invoke /hello endpoint

## Create simple message board.
- Create simple table
    - > aws dynamodb create-table --table-name SimpleTopicTable --attribute-definitions AttributeName=id,AttributeType=S --key-schema AttributeName=id,KeyType=HASH --provisioned-throughput ReadCapacityUnits=1,WriteCapacityUnits=1 --endpoint-url http://localhost:8000
- Create read lambda to read all records from table
- Create write lambda to write message to table
- Start dynamodb local
    - > docker run -p 8000:8000 amazon/dynamodb-local
- Add dynamodb local to lambda function environment
    - > Environment:
        Variables:
          AWS_DYNAMODB_ENDPOINT: http://172.17.0.1:8000
        