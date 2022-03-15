# Serverless Application Development

## Onderwerpen

> Serverless, AWS Lambda, Serverless Application Model, API Gateway, DynamoDB

## Materiaal

- Install Python: <https://realpython.com/installing-python/>
- Install AWS CLI: <https://aws.amazon.com/cli/>
- Install AWS SAM CLI: <https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html>
- Install Docker: <https://docs.docker.com/engine/install/>
- Tutorial: Deploying a Hello World application: <https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-getting-started-hello-world.html>

## Opdrachtomschrijving

In deze opdracht maken we gebruik van het Serverless Application Model (SAM) om een simple forum applicatie met maken met AWS Lambda, API Gateway en DynamoDB.
Om een eenvoudige start te hebben voor de applicatie maken we gebruik van het hello-world template van SAM.
Hiermee is ook snel de basis ervaring met SAM CLI op te doen.
Hierna zullen we deze applicatie uitbreiden met een forum POST endpoint voor het publiceren van een bericht en een GET endpoint voor het uitlezen van de berichten op de fora.
De instructies hiervoor worden stapsgewijs gegeven in deze tutorial.
Mochten er vragen of problemen zijn dan is het mogelijk om de uitwerking van de opdracht te bekijken in de `uitwerking` folder.

We zullen de applicatie impleme

### Maak het SAM hello-world project aan

Gebruik `sam init` om het _Hello World Example_ project aan te maken.
Geeft het project de naam die jij er aan wilt geven. 

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

Het SAM project is nu aangemaakt en gaan even kijken naar een aantal folders en bestanden.
De `README.md` bevat de standaard beschrijving en instructies voor de Hello World applicatie.
Deze inhoud is niet direct nodig voor deze tutorial, maar biedt ook enkele toevoegingen zoals het deployen naar de AWS cloud.
Het `template.yaml` bevat de SAM template en specificeerd uit welke serverless onderdelen het project bestaat.
Hierover zo meer.
De `hello_world` folder bevat de python implementatie van de AWS Lambda.
De `test` folder met unit- en integratie testen laten we in deze tutorial buiten beschouwing.
Dit is een workshop op zich.
In de `events` folder staan Lambda events examples die gebruikt kunnen worden voor het lokaal testen van een Lambda.

We gaan nu het project _bouwen_ zodat we het lokaal kunnen gaan uitvoeren. 

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

Wat staat er in de Lambda code?
```python
def lambda_handler(event, context):
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world"
        }),
    }
```
