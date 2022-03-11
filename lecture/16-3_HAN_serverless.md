<!-- .slide: data-background="images/skyline_light.jpg", data-background-transition="slide" -->
<!-- .slide: data-background="images/skyline_dark.png", data-background-transition="slide" -->

# ![](images/logo.png) <!-- .element: width="400" style="border:0; background: transparent; box-shadow: none" -->

## Welkom
### Serverless Lambda Workshop

---

## Programma vandaag

- Theorie deel 1
- Hands-on opdracht 1
- Theorie deel 2
- Hands-on opdracht 2

--

## Programma deel 1

- Serverless Architecture
- Function-as-a-Service
- Architectuur
- Testruns
- Concurrency/limits

---

## Serverless Architecture

When we run our own servers:

- We are charged for keeping the server up even when we are not serving out any requests. <!-- .element: class="fragment" -->
- We are responsible for uptime and maintenance of the server and all its resources. <!-- .element: class="fragment" -->
- We are also responsible for applying the appropriate security updates to the server. <!-- .element: class="fragment" -->
- As our usage scales we need to manage scaling up our server as well. And as a result manage scaling it down when we don’t have as much usage. <!-- .element: class="fragment" -->

--

## Serverless Architecture

What if we don't need to bother about servers? <!-- .element: class="fragment" -->

What if we only create the system parts we care about? <!-- .element: class="fragment" -->

CaaS, Paas, FaaS, DBaaS, TaaS, QaaS, ... <!-- .element: class="fragment" -->

> Serverless != FaaS, but are best friends! <!-- .element: class="fragment" -->

--

## Serverless Architecture
### Advantages

- Focus: Less infrastructure management, more application development <!-- .element: class="fragment" -->
- Turnaround: Can significantly cut time to market <!-- .element: class="fragment" -->
- Scaling: Simplified scalability provided by serverless providers <!-- .element: class="fragment" -->
- Costs: Don't pay for unused space, memory or idle CPU time <!-- .element: class="fragment" -->

Note:

What are the advantages of serverless computing?
Lower costs - Serverless computing is generally very cost-effective, as traditional cloud providers of backend services (server allocation) often result in the user paying for unused space or idle CPU time.
Simplified scalability - Developers using serverless architecture don’t have to worry about policies to scale up their code. The serverless vendor handles all of the scaling on demand.
Quicker turnaround - Serverless architecture can significantly cut time to market. Instead of needing a complicated deploy process to roll out bug fixes and new features, developers can add and modify code on a piecemeal basis.

--

## Serverless Architecture
### Disadvantages

- Vendor lock-in is a risk
- Testing and debugging become more challenging
- Serverless computing introduces new security concerns
- Serverless architectures are often not built for long-running processes
- Performance may be affected

Note: 

<https://www.cloudflare.com/learning/serverless/why-use-serverless/>

--

<!-- .slide: data-background="white" -->

## Serverless Architecture
### Costs

# ![](images/serverless-costs.svg) <!-- .element: width="800" -->

--

## Serverless Architecture
### Costs

# ![](images/Lambda_EC2_cost.png) <!-- .element: width="800" -->

Note:

<https://cloudserviceevaluation.com/2017/02/02/lambda-or-ec2-which-one-do-you-use-to-save-the-most-money/>

--

## Serverless Architecture

# ![](images/GCP-ComputeOptions.jpg) <!-- .element: width="800" -->

--

## Serverless Architecture

# ![](images/serverless-scooby.jpg) <!-- .element: width="400" -->

--

<!-- .slide: data-background="white" -->

# ![](images/AWS-Serverless-Archit.png) <!-- .element: width="900" -->

---

## Function-as-a-Service

- Run modular chunks of functionality -> Single purpose
- Executed and scaled independently <!-- .element: class="fragment" -->
- Not bothered by complex infrastructure -> Serverless <!-- .element: class="fragment" -->

> Serverless != FaaS, but are best friends! <!-- .element: class="fragment" -->

--

## Function-as-a-Service
### Application Granularity

# ![](images/Functions-Application-Granularity.png) <!-- .element: width="900" -->

--

## Function-as-a-Service
### Advantages

- Serverless -> More focus on application development
- Stateless functions are inherently scalable
- Scale down to 0 -> Don't pay for idle resources
- Built in availability and fault tolerance
- Business logic in minimal shippable unit sizes

--

## Function-as-a-Service
### Disadvantages

- Decreased transparency
- Potentially tough to debug
- Potentially tough to manage costs
- Decreased oversight of your system
- Increased chances of failures 

Note:
Decreased transparency. Someone else is managing your infrastructure so it can be tough to understand the entire system.
Potentially tough to debug. There are tools that allow remote debugging and some services (i.e. Azure) provide a mirrored local development environment but there is still a need for improved tooling.
Auto-scaling of function calls often means auto-scaling of cost. This can make it tough to gauge your business expenses.
You now have a ton of functions deployed and it can be tough to keep track of them. This comes down to a need for better tooling (developmental: scripts, frameworks, diagnostic: step-through debugging, local runtimes, cloud debugging, and visualization: user interfaces, analytics, monitoring).
Solutions for caching resources between stateless requests (i.e. DB connections) and recycling network requests are still pending.

---

## Architectuur

> Run code without provisioning or managing servers. 

> Pay only for the compute time you consume.

--

## Architectuur

- Runs your code in response to events
- Manages the underlying compute resources
- Create your own back-end services
- Used to extend other AWS services with custom logic
- Runs your code on high-availability compute infrastructure
- Automatic scaling
- Only pay for what you use

Note:

<https://aws.amazon.com/lambda/features/>

--

## Architectuur
### Ttriggers

# ![](images/AWS-lambda-destinations.png) <!-- .element: width="800"  -->


--

## Architectuur
### Simpel voorbeeld

# ![](images/Lambda-HelloWorld.png)


--


## Architectuur
### Uitgebreid voorbeeld

```javascript
import AWS from 'aws-sdk';
import { ok } from './utils/response';

const dynamoDB = new AWS.DynamoDB.DocumentClient();

export async function list() {
  // Note: Using scan is inefficient and should normally be avoided.
  const accountsResult = await dynamoDB.scan({
    TableName: process.env.ACCOUNT_TABLE,
  }).promise();

  const accounts = accountsResult.Items;
  console.log('List Accounts:', accounts);

  return ok({ accounts });
}
```

--

## Architectuur
### Pricing

# ![](images/AWS-lambda-pricing.png) <!-- .element: width="700"  -->

--

## Architectuur
### Security

- Lambda's assumen een IAM Role
    - Moet rechten hebben op eventuele event trigger sources
    - Moet rechten hebben op eventuele gebruikte resources

---

## Talen

- JavaScript / TypeScript <!-- .element: class="fragment" -->
- Python <!-- .element: class="fragment" -->
- Ruby <!-- .element: class="fragment" -->
- Go <!-- .element: class="fragment" -->
- PowerShell <!-- .element: class="fragment" -->
- C# (.NET Core) <!-- .element: class="fragment" -->
- Java <!-- .element: class="fragment" -->
- Custom Runtime API <!-- .element: class="fragment" -->

---

## Testruns

# ![](images/Lambda-Console-actions.png)  <!-- .element: width="600"  -->

# ![](images/Lambda-Config-test.png)  <!-- .element: width="600"  -->

--

## Testruns

# ![](images/Lambda-Test-Result.png)

---

## Concurrency

- Maximaal 1000 executies tegelijkertijd <!-- .element: class="fragment" -->
- Reserved Concurrency per functie => 1 verwerking per Lambda instantie<!-- .element: class="fragment" -->
- Elke invocatie over limiet resulteert in Throttle <!-- .element: class="fragment" -->
- Batched verwerking <!-- .element: class="fragment" -->

--

## Concurrency
### Throttle

- Throttle gedrag <!-- .element: class="fragment" -->
    - Synchrone incovatie -> ThrottleError - HTTP 429 <!-- .element: class="fragment" -->
    - Asynchrone invocatie -> opnieuw, uiteindelijk DLQ <!-- .element: class="fragment" -->

--

## Concurrency
### Lifecycle

# ![](images/AWS-lambda-lifecycle.png) <!-- .element: height="480" -->

--

## Concurrency
### Cold Start

- Nieuwe instantie -> code inladen en code buiten handler uitvoeren (init) <!-- .element: class="fragment" -->
- Init kan even duren als veel wordt geïnitialiseerd (code, dependencies, SDK). <!-- .element: class="fragment" -->
- Eerste request van nieuwe instantie heeft hogere latency <!-- .element: class="fragment" -->

--

## Concurrency
### Cold Start

# ![](images/Lambda-Init.png)

--

<!-- .slide: data-background="white" -->

## Concurrency
### Cold Start

# ![](images/AWS-lambda-Cold-Starts.jpg) <!-- .element: height="480" -->

---

## Limits
### Uitvoeren

- RAM: 128 MB - 3008 MB (in stappen van 64 MB) <!-- .element: class="fragment" -->
- Maximale duur: 900 seconden (15 min) <!-- .element: class="fragment" -->
- 4 KB aan Environment Variables <!-- .element: class="fragment" -->
- 1000 concurrent executies <!-- .element: class="fragment" -->

--

## Limits
### Deployen

- Online Lambda code: 3 MB <!-- .element: class="fragment" -->
- Grootte Lambda function bij deployment (.zip): 50 MB <!-- .element: class="fragment" -->
- Maximale grootte code + dependencies: 250 MB <!-- .element: class="fragment" -->

---

<!-- .slide: data-background="images/skyline_dark.png", data-background-transition="slide" -->

<br>
<br>

### Vragen?

> Einde deel 1

---

## Opdracht 1

> 

---

## Programma deel 2

- Serverless Application Model
- API Gateway
- Stages

---

## Serverless Application Model

> The AWS::Serverless transform, which is a macro hosted by AWS CloudFormation, takes an entire template written in the AWS Serverless Application Model (AWS SAM) syntax and transforms and expands it into a compliant AWS CloudFormation template

Note:

<https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/transform-aws-serverless.html>

--

## Serverless Application Model

- Open-source framework
- Build serverless applications on AWS <!-- .element: class="fragment" -->
- AWS SAM template specification <!-- .element: class="fragment" -->
- AWS SAM command line interface (AWS SAM CLI) <!-- .element: class="fragment" -->

--

## Serverless Application Model
### Benefits

- Single-deployment configuration
- Extension of AWS CloudFormation <!-- .element: class="fragment" -->
- Built-in best practices <!-- .element: class="fragment" -->
- Local debugging and testing <!-- .element: class="fragment" -->

--

## Serverless Application Model
### Template

- Closely follows the format of an AWS CloudFormation template file
- Transform declaration - `Transform: AWS::Serverless-2016-10-31` 
- Globals section - Defines properties that are common to all the resources 
- Resources section - Also AWS SAM resources 
- Parameters section - Causes `sam deploy --guided` to present additional prompts 

--

## Serverless Application Model
### SAM resources

- AWS::Serverless::Api
- AWS::Serverless::Application
- AWS::Serverless::Function
- AWS::Serverless::HttpApi
- AWS::Serverless::LayerVersion
- AWS::Serverless::SimpleTable
- AWS::Serverless::StateMachine

--

## Serverless Application Model

```yaml
AWSTemplateFormatVersion: '2010-09-09'
Transform: 'AWS::Serverless-2016-10-31'
Description: >-
  A simple backend (read/write to DynamoDB) with a RESTful API endpoint using Amazon API Gateway.
Parameters: 
  TableNameParameter: 
    Type: String

Globals:
  #https://github.com/awslabs/serverless-application-model/blob/develop/docs/globals.rst
  Function:
    Runtime: python3.6
    MemorySize: 512
    Environment:
      Variables:
        TABLE_NAME:
          Ref: Table

Resources:
  microservicehttpendpointpython3:
    Type: 'AWS::Serverless::Function'
    Properties:
      Handler: lambda_function.lambda_handler
      CodeUri: .
      Description: >-
        A simple backend (read/write to DynamoDB) with a RESTful API endpoint using Amazon API Gateway.
      Timeout: 10
      Policies:
        - DynamoDBCrudPolicy:
            TableName: !Ref TableNameParameter
      Events:
        Api1:
          Type: Api
          Properties:
            Path: /MyResource
            Method: ANY

  Table:
    Type: AWS::Serverless::SimpleTable
```

--

## Serverless Application Model
### CLI

- sam build - Builds a serverless application
- sam deploy - Deploy a serverless application
- sam init - Initializes a serverless project
- sam local invoke - Invokes a local Lambda function once
- sam local start-api - Runs your serverless application locally
- sam logs - Fetches logs that are generated
- sam validate - Verifies whether an SAM template file is valid

Note:

<https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-command-reference.html>

---

## API Gateway

- Fully managed service voor maken, aanbieden, beheren van API's <!-- .element: class="fragment" -->
- 'Voordeur' van een applicatie <!-- .element: class="fragment" -->
- RESTful en WebSocket APIs <!-- .element: class="fragment" -->

# ![](images/AWS-APIGateway.png) <!-- .element: class="fragment" width="800" -->

--

## API Gateway
### RESTful API

- Stateless frontend voor aanroepen AWS Service of HTTP endpoint <!-- .element: class="fragment" -->
- Communicatie alleen van client naar backend <!-- .element: class="fragment" -->
- Stuurt http aanvragen door naar ingestelde target <!-- .element: class="fragment" -->

---

## Stages

- Een stage is een snapshot van een API <!-- .element: class="fragment" -->
- Stages hebben eigen endpoints en instellingen <!-- .element: class="fragment" -->
- Stages kunnen naast elkaar beschikbaar zijn <!-- .element: class="fragment" -->
- Elke stage heeft versiebeheer <!-- .element: class="fragment" -->

# ![](images/AWS-APIGateway-stages.png) <!-- .element: class="fragment" -->

--

## Stages
### Stage variables

- De environment variables van API Gateway <!-- .element: class="fragment" -->
- Aanpassen configuration zonder nieuwe deployment <!-- .element: class="fragment" -->
- Bijvoorbeeld Lambda ARN of HTTP endpoint <!-- .element: class="fragment" -->
- Usecase: endpoints aanpassen per stage <!-- .element: class="fragment" -->
- Stage variables worden doorgegeven aan aangeroepen Lambda functie <!-- .element: class="fragment" -->

--

## Stages
### Stage variables

# ![](images/AWS-APIGateway-alias.png)

---

### Vragen?

> Einde deel 2

---

## Opdracht 2

> 
