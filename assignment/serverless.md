# AWS Serverless Application Development workshop

## Onderwerpen

> Serverless, AWS Lambda, Serverless Application Model, API Gateway, DynamoDB

## Materiaal

- Install Python: <https://realpython.com/installing-python/>
- Install AWS CLI: <https://aws.amazon.com/cli/>
- Install AWS SAM CLI: <https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html>
- Install Docker: <https://docs.docker.com/engine/install/>
- Tutorial: Deploying a Hello World application: <https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-getting-started-hello-world.html>

## Opdrachtomschrijving

In deze opdracht maken we gebruik van het Serverless Application Model (SAM) om een simpele forum applicatie met maken met AWS Lambda, API Gateway en DynamoDB.
Om een eenvoudige start te hebben voor de applicatie maken we gebruik van het hello-world template van SAM.
Hiermee is snel de basis ervaring met SAM CLI op te doen.
Daarna zullen we de applicatie uitbreiden met een forum POST endpoint voor het publiceren van een bericht en een GET endpoint voor het uitlezen van de berichten op het forum.
De instructies hiervoor worden stapsgewijs gegeven in deze tutorial.
Mochten er vragen of problemen zijn dan is het mogelijk om de uitwerking van de opdracht te bekijken in de `uitwerking` folder.

### Voorbereiding

Voordat je met de tutorial aan de slag gaat zal de benodige software geïnstalleerd moeten zijn op het lokale systeem.
- [Python](https://realpython.com/installing-python/)
- [AWS CLI](https://aws.amazon.com/cli/)
- [AWS SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html)
- [Docker](https://docs.docker.com/engine/install/)

Als alles beschikbaar is op het lokale systeem kunnen we aan de slag gaan.

### De eerste stappen met het SAM hello-world project

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
Deze inhoud is niet direct nodig voor deze tutorial, maar biedt ook enkele toevoegingen zoals het deployen naar de AWS-cloud.
Het `template.yaml` bevat de SAM template en specificeert uit welke serverless onderdelen het project bestaat.
Hierover zo meer.
De `hello_world` folder bevat de python implementatie van de AWS Lambda.
De `test` folder met unit- en integratie testen laten we in deze tutorial buiten beschouwing.
Dit is een workshop op zich.
In de `events` folder staan Lambda events examples die gebruikt kunnen worden voor het lokaal testen van een Lambda.

We gaan nu het project _bouwen_ (`sam build`) zodat we het lokaal kunnen gaan uitvoeren.
Het kan soms voorkomen dat de build faalt i.v.m. een versie conflict met python op je lokale systeem.
In dat geval kun je `sam build --use-container` gebruiken, wat een Docker container gebruikt met een specifieke compatible python versie.

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

Voor het uitvoeren van Lambda's op een lokaal systeem gebruikt SAM CLI Docker containers met een specifieke SAM emulation image.
Een Lambda functie is eenvoudig eenmalig uit te voeren via `sam local invoke`, waarbij de Lambda code aangeroepen wordt met het gegeven event.
Dit is een makkelijke manier om een specifieke aanroep van de functie te testen.

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

De `HelloWorldFunction` biedt ook een REST endpoint aan. 
Die kunnen we lokaal starten via `sam local start-api`.

```bash
% sam local start-api
Mounting HelloWorldFunction at http://127.0.0.1:3000/hello [GET]
You can now browse to the above endpoints to invoke your functions. You do not need to restart/reload SAM CLI while working on your functions, changes will be reflected instantly/automatically. You only need to restart SAM CLI if you update your AWS SAM template
2022-03-15 20:15:24  * Running on http://127.0.0.1:3000/ (Press CTRL+C to quit)
```

Eenmaal gestart kunnen we de gegeven endpoint aanroepen met bijvoorbeeld het `curl` commando hieronder, gebruikmakend van een browser of een andere tool zoals [Postman](https://www.postman.com/downloads/). 

```bash
% curl http://localhost:3000/hello
{"message": "hello world"}%
```

#### Wat staat er in de SAM `template.yaml`?

De SAM `template.yaml` specificeert uit welke resources (onderdelen) de applicatie bestaat en hoe die geconfigureerd dienen te zijn.
Het is wat men noemt een 'desired state' configuratie en kan gebruikt worden om de serverless applicatie exact zoals gespecificeerd is te configureren in de AWS-cloud.
SAM maakt hiervoor gebruik van [CloudFormation](https://aws.amazon.com/cloudformation/), een Infrastructure-as-Code oplossing, maar dat gaat buiten het doel van deze workshop.
Dezelfde SAM `template.yaml` kunnen we i.c.m. SAM CLI ook gebruiken om Lambda functies lokaal uit te voeren en dat is wat we in deze woorkshop doen.

De belangrijkste deel in de `template.yaml` is de `Resources` sectie.
Hierin worden alle serverless resources, Lambda functies in ons geval, gedefinieerd.
Zie hieronder het voorbeeld van de `HelloWorldFunction` welke van het type `AWS::Serverless::Function` (lambda) is.
Deze heeft een aantal properties:
- `CodeUri` geeft aan in welke folder van het project de sourcecode van de functie staat.
- `Handler` geeft aan welke file en methode voor de afhandeling van een invocatie uitgevoerd wordt.
- `Runtime` geeft de Lambda runtime aan die gebruikt moet worden.

Daarnaast kunnen de `Events` gespecificeerd worden die een invocatie van veroorzaken.
In dit geval is het `HelloWorld` event van het type `API`, wat betekend dat het een API Gateway mapping is van een REST/HTTP request met URL path `/hello` en HTTP Method `GET`.

Veel meer details over de SAM template is hier te vinden: <https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-specification-template-anatomy.html>

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

#### Wat staat er in de Lambda code?

In de `app.py` file staat de lambda functie implementatie.
Belangrijkste hierin is de `lambda_handler(event, context)` functie definitie.
Dit is de functie die door de Lambda runtime aangeroepen wordt, zoals geconfigureerd in de `ttemplate.yaml`.
Het `event` argument bevat de data van het event wat de lambda triggered.
In ons geval een HTTP request, zie ook [events/event.json](../uitwerking/events/event.json).
Om een HTTP response terug te geven wordt een object geretourneerd in de code met de properties benodigd voor de response.
Meer details over de Lambda handler functie in python is hier te vinden: <https://docs.aws.amazon.com/lambda/latest/dg/python-handler.html>.

```python
def lambda_handler(event, context):
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world"
        }),
    }
```

### Voeg een Lambda toe voor het posten van een message naar een forum topic

Voeg de nieuwe folder `post_new_message` toe voor de nieuwe lambda implementatie.
Kopieer de bestanden van de `hello_world` folder in deze folder.
Deze bestanden kunnen we als basis voor de lambda gebruiken.
Open het `app.py` bestand om de sourcecode aan te passen voor de implementatie van de functie.
In deze lambda verwachten we een request body in JSON-formaat met een message en topic waarde.
Bijvoorbeeld `{"message":"hello world","topic":"greetings"}`.
Deze body kunnen we uitlezen uit het lambda event dat als argument aan de handler functie meegegeven wordt.
We printen de ontvangen waarden naar de console zodat we kunnen controleren of deze goed geïnterpreteerd worden.

```python
def lambda_handler(event, context):
    body = json.loads(event['body'])
    message = body['message']
    topic = body['topic']

    print('Input message: ' + message + " for topic: " + topic)

    return {
        "statusCode": 200
    }
```

Nu we de basis implementatie gereed hebben kunnen we de SAM `template.yaml` aanpassen zodat de 

```yaml
  PostNewMessageFunction:
    Type: AWS::Serverless::Function
    Properties:
      CodeUri: post_new_message/
      Handler: app.lambda_handler
      Runtime: python3.8
      Events:
        PostMessages:
          Type: Api
          Properties:
            Path: /messages
            Method: post
```

Laten we de nieuwe endpoint testen.
Stop eerder applicatie versie, bouw de SAM applicatie (`sam build`) en start deze weer (`sam local start-api`).
Roep nu de `http://127.0.0.1:3000/messages` endpoint met een POST method en de verwachte request body aan.
Dit kan met het gegeven `curl` commando van hieronder, maar ook met andere tools zoals Postman.
Controleer dat de aanroep succesvol is en de juiste logging weergegeven wordt door de Lambda functie.

```bash
% curl -X POST http://127.0.0.1:3000/messages -H 'Content-Type: application/json' -d '{"message":"hello world","topic":"greetings"}'
```

### Gebruik DynamoDB om de forum messages op te slaan

Lambda functies zijn stateless en kunnen gestart en gestopt worden door het platform wanneer dat gewenst is.
Het is dus praktisch niet mogelijk om data vast te houden in een Lambda functie, daarvoor is database voor benodigd.
DynamoDB is een serverless column-based NoSQL database die goed te gebruiken is vanuit Lambda functies.
DynamoDB is ook lokaal te gebruiken, als Java applicatie of Docker container, zoals wij nu gaan doen.
Zie ook <https://hub.docker.com/r/amazon/dynamodb-local> voor meer informatie.

Start de `dynamodb-local` met het onderstaande `docker` commando.
Dit commando bind de DynamoDB applicatie in de container aan portnummer `8000` op het lokale systeem zodat wij die kunnen gebruiken.

```bash
% docker run -p 8000:8000 amazon/dynamodb-local -jar DynamoDBLocal.jar -sharedDb
```

We starten dynamodb-local met de `-sharedDb` optie om problemen te voorkomen door verschil van region configuratie tussen het lokale systeem en de lambda runtime.
Zie <https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DynamoDBLocal.UsageNotes.html> voor meer informatie.

Het eerste om nu te doen is de `ForumTable` table aanmaken in DynamoDB.
Dit kunnen we met het onderstaande commando.
Zie ook dat we hier verwijzen naar het lokale DynamoDB endpoint (`--endpoint-url http://localhost:8000`).
Het commando toont de beschrijving van de aangemaakte tabel en deze kan met `q` gesloten worden. 

```bash
% aws dynamodb create-table --table-name ForumTable --attribute-definitions AttributeName=id,AttributeType=S --key-schema AttributeName=id,KeyType=HASH --provisioned-throughput ReadCapacityUnits=1,WriteCapacityUnits=1 --endpoint-url http://localhost:8000
```

Met het onderstaande commando kunnen we controleren dat de tabel is aangemaakt en wat de inhoud is (leeg voor nu).

```bash
% aws dynamodb scan --table-name ForumTable --endpoint-url http://localhost:8000                                                                                                                                                                              
{
    "Items": [],
    "Count": 0,
    "ScannedCount": 0,
    "ConsumedCapacity": null
}
```

Binnen docker containers verwijst ip-adres `172.17.0.1` naar het host systeem waar de Docker engine zich op bevind.
Meer info hierover is te vinden op <https://www.baeldung.com/linux/docker-connecting-containers-to-host>.
Omdat we de lokale DynamoDB container aan port `8000` op het lokale systeem gebonden hebben, is de lokale DynamoDB endpoint te benaderen op `http://172.17.0.1:8000` vanuit een Docker container.
Voeg de `AWS_DYNAMODB_ENDPOINT` environment variabele toe aan de Lambda configuratie in de SAM `template.yaml` zodat we die kunnen gebruiken in onze lambda implementatie.

```yaml
  WriteNewMessageFunction:
    Type: AWS::Serverless::Function
    Properties:
      CodeUri: post_new_message/
      Environment:
        Variables:
          AWS_DYNAMODB_ENDPOINT: http://172.17.0.1:8000
      Handler: app.lambda_handler
      ...
```

Nu is het moment om de implementatie van de lambda functie uit te bereiden met de opslag in de `ForumTable`. 
Er zijn een drietal imports die toegevoegd dienen te worden voor `boto3`, `uuid` en `os`.
`boto3` is de AWS SDK voor python en kan gebruikt worden voor nagenoeg alle AWS services, o.a. voor DynamoDB zoals wij gaan toepassen.
<https://github.com/boto/boto3> geeft meer informatie over de `boto3` SDK.
Om acties uit te voeren op DynamoDB is er een client nodig.
Deze kan verkregen worden via `boto3.resource()`. Zie ook dat via de environment variabele `AWS_DYNAMODB_ENDPOINT` de eerder geconfigureerde lokaal endpoint gezet wordt voor de client.

```python
import boto3
import uuid
import os

dynamodb = boto3.resource('dynamodb', endpoint_url=os.environ['AWS_DYNAMODB_ENDPOINT']) 
```

Voeg de python code toe voor het opslaan van het forum message in de `ForumTable` en pas het return-statement aan zodat deze het opgeslagen object als body in de response meegegeven wordt.
Meer informatie over CRUD-operaties op DynamoDB tabellen met `boto3` is hier te vinden <https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GettingStarted.Python.03.html>.

```python

    recordId = str(uuid.uuid4())
    print('Generating new DynamoDB record, with ID: ' + recordId)
    item = {
        'id' : recordId,
        'message' : message,
        'topic': topic
    }

    # Creating new record in DynamoDB table
    table = dynamodb.Table('ForumTable')
    table.put_item(
        Item=item
    )

    return {
        "statusCode": 200,
        "body": str(item)
    }
```

Bouw en start de nieuwe versie van de functie en test het opslaan van geposte messages in de `ForumTable`. 

```bash
% aws dynamodb scan --table-name ForumTable --endpoint-url http://localhost:8000                                                                                                                                                                              
```

### Voeg een Lambda toe voor het ophalen van alle messages

Maak de `get_all_messages` folder aan in het project en voeg de `GetMessagesFunction` toe aan de `template.yaml` zoals dat bij de vorige lambda is gedaan.
Deze lambda zal verbonden moeten worden aan de `GET` method op URL pad `/messages`.

Het gebruikt de `table.scan()` method om alle records uit de `ForumTable` op te halen.
Deze records worden in de body van de response teruggegeven.

```python
    table = dynamodb.Table('ForumTable')

    data = table.scan()
    items = data['Items']

    print('Scanned messages: ' + str(data['Count']))

    return {
        "statusCode": 200,
        "body": items
    }
```

Bouw en start de nieuwe versie van de functie en test dat alle records in de tabel verkregen worden.

```bash
% curl http://127.0.0.1:3000/messages                                                                                                                                                                                                                         
[{'message': 'hello world', 'topic': 'greetings', 'id': '687aea2c-2eb1-4c4d-b5ec-dc5098105d45'}, {'message': 'hello world', 'topic': 'greeting', 'id': '0d698416-79a7-4353-b9d7-30b4551e4923'}]
```

### Pas de Lambda aan zodat alleen de messages van een gegeven topic opgehaald worden

Doe dit door een queryParameter mee te geven. Vervolgens kan je met behulp van een FilterExpression de scan beperken tot een bepaald topic.
