# 23-3_HAN_serverless

## Onderwerpen

## Materiaal

- Install Python: <https://realpython.com/installing-python/>
- Install AWS CLI: <https://aws.amazon.com/cli/>
- Install AWS SAM CLI: <https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html>
- Install Docker: <https://docs.docker.com/engine/install/>
- Tutorial: Deploying a Hello World application: <https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-getting-started-hello-world.html>

## Opdrachtomschrijving

### Maak SAM hello-world project aan

```bash
% sam init

You can preselect a particular runtime or package type when using the `sam init` experience.
Call `sam init --help` to learn more.

Which template source would you like to use?
        1 - AWS Quick Start Templates
        2 - Custom Template Location
Choice: 1

Choose an AWS Quick Start application template
        1 - Hello World Example
        2 - Multi-step workflow
        3 - Serverless API
        4 - Scheduled task
        5 - Standalone function
        6 - Data processing
        7 - Infrastructure event management
        8 - Machine Learning
Template: 1

 Use the most popular runtime and package type? (Python and zip) [y/N]: y

Project name [sam-app]: sam-app

Cloning from https://github.com/aws/aws-sam-cli-app-templates (process may take a moment)

    -----------------------
    Generating application:
    -----------------------
    Name: uitwerking
    Runtime: python3.9
    Architectures: x86_64
    Dependency Manager: pip
    Application Template: hello-world
    Output Directory: .
    
    Next steps can be found in the README file at ./uitwerking/README.md
```

```bash
% sam build
Your template contains a resource with logical ID "ServerlessRestApi", which is a reserved logical ID in AWS SAM. It could result in unexpected behaviors and is not recommended.
Building codeuri: /Users/awassink/git/serverless-lambda-workshop/uitwerking/hello_world runtime: python3.9 metadata: {} architecture: x86_64 functions: ['HelloWorldFunction']
Running PythonPipBuilder:ResolveDependencies
Running PythonPipBuilder:CopySource

Build Succeeded

Built Artifacts  : .aws-sam/build
Built Template   : .aws-sam/build/template.yaml
```
```bash
% sam local invoke HelloWorldFunction --event events/event.json
Invoking app.lambda_handler (python3.9)
Image was not found.
Removing rapid images for repo public.ecr.aws/sam/emulation-python3.9
Building image..................................................................................................................................................................................................................................................................................................................................................................
Skip pulling image and use local one: public.ecr.aws/sam/emulation-python3.9:rapid-1.40.1-x86_64.

Mounting /Users/awassink/git/serverless-lambda-workshop/uitwerking/.aws-sam/build/HelloWorldFunction as /var/task:ro,delegated inside runtime container
START RequestId: 6e0167cd-c9e2-4af8-af4c-90d67af7e724 Version: $LATEST
{"statusCode": 200, "body": "{\"message\": \"hello world\"}"}END RequestId: 6e0167cd-c9e2-4af8-af4c-90d67af7e724
REPORT RequestId: 6e0167cd-c9e2-4af8-af4c-90d67af7e724  Init Duration: 0.76 ms  Duration: 179.69 ms     Billed Duration: 180 ms Memory Size: 128 MB     Max Memory Used: 128 MB 
```

```bash
% sam local start-api
Mounting HelloWorldFunction at http://127.0.0.1:3000/hello [GET]
You can now browse to the above endpoints to invoke your functions. You do not need to restart/reload SAM CLI while working on your functions, changes will be reflected instantly/automatically. You only need to restart SAM CLI if you update your AWS SAM template
2022-03-15 20:15:24  * Running on http://127.0.0.1:3000/ (Press CTRL+C to quit)
% curl http://localhost:3000/hello
{"message": "hello world"}%
```

Wat staat er in de SAM template?
```yaml
Resources:
  HelloWorldFunction:
    Type: AWS::Serverless::Function # More info about Function Resource: https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#awsserverlessfunction
    Properties:
      CodeUri: hello_world/
      Handler: app.lambda_handler
      Runtime: python3.9
      Architectures:
        - x86_64
      Events:
        HelloWorld:
          Type: Api # More info about API Event Source: https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#api
          Properties:
            Path: /hello
            Method: get
```
