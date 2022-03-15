# Uitwerking notes

## Use hello world api 
- Start hello world api _sam local start-api_
- Invoke /hello endpoint

## Create simple message board.
- Create simple table resource in template.yaml
- Create read lambda to read all records from table
- Create write lambda to write message to table
- Start dynamodb local
    - > docker run -p 8000:8000 amazon/dynamodb-local
- Add dynamodb local to lambda function environment
    - > Environment:
        Variables:
          AWS_DYNAMODB_ENDPOINT: http://localhost:8000
        