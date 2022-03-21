<!-- .slide: data-background="images/skyline_light.jpg", data-background-transition="slide" -->
<!-- .slide: data-background="images/skyline_dark.png", data-background-transition="slide" -->

# ![](images/logo.png) <!-- .element: width="400" style="border:0; background: transparent; box-shadow: none" -->

## Welkom
### Serverless Lambda Workshop

---

## Even voorstellen

<h4>Pim Otte</h4>
<div class="columns two">
  <div class="left">
    <ul>
      <li>Consultant @ Quintor</li>
    </ul>
    <br>
    <ul>
      <li>Email: p.otte@quintor.nl</li>
      <li>LinkedIn: <a href="https://www.linkedin.com/in/pim-otte-95b4ba124/">pim-otte-95b4ba124</a></li>
    </ul>

  </div>
  <div class="right">
    <img src="images/pim-otte.jpeg" style="max-height: none" height="200px">
     <ul>
      <li><u>Specialisaties:</u></li>
      <li>Fullstack Java Development</li>
      <li>Cloud Native Software Development</li>
      <li>Blockchain Development</li>
    </ul>
  </div>
</div>

--

<img src="images/logo.png" style="max-height: none; border:0; background: transparent; box-shadow: none" height="100px">

<div class="columns two">
  <div class="left">
    <ul>
      <li>Java</li>
      <li>.Net</li>
      <li>Frontend</li>
      <li>Platform Engineering</li>
      <li>Security</li>
      <li>Agile Analyse</li>
    </ul>

  </div>
  <div class="right">
     <ul>
      <li>Den Haag</li>
      <li>Den Bosch</li>
      <li>Amersfoort</li>
      <li>Deventer</li>
      <li>Groningen</li>
    </ul>
  </div>
</div> 
<br/>
<a href="https://quintor.nl/">https://quintor.nl/</a>

--

<img src="images/logo.png" style="max-height: none; border:0; background: transparent; box-shadow: none" height="100px">

- Minor Cloud-Native Software Development 
  - <https://quintor.nl/minors/>
- Afstuderen bij Quintor 
  - <https://quintor.nl/student/>
- Young Professional Programma 
  - <https://quintor.nl/young-professional/>

---

## Programma vandaag

- Theorie
- Hands-on opdracht

--

## Programma

- Serverless Architecture
- Function-as-a-Service
- AWS Lambda
- Serverless Application Model
- API Gateway
- DynamoDB

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

- Vendor lock-in is a risk <!-- .element: class="fragment" -->
- Testing and debugging become more challenging <!-- .element: class="fragment" -->
- Serverless computing introduces new security concerns <!-- .element: class="fragment" -->
- Serverless architectures are often not built for long-running processes <!-- .element: class="fragment" -->
- Performance may be affected <!-- .element: class="fragment" -->

Note: 

<https://www.cloudflare.com/learning/serverless/why-use-serverless/>

--

<!-- .slide: data-background="white" -->

## Serverless Architecture
### Costs

# ![](images/serverless-costs.svg) <!-- .element: width="800" -->

--

## Serverless Architecture

# ![](images/GCP-ComputeOptions.jpg) <!-- .element: width="800" -->

---

## Function-as-a-Service
### Application Granularity

# ![](images/Functions-Application-Granularity.png) <!-- .element: width="900" -->

--

## Function-as-a-Service
### Advantages

- Serverless -> More focus on application development <!-- .element: class="fragment" -->
- Stateless functions are inherently scalable <!-- .element: class="fragment" -->
- Scale down to 0 -> Don't pay for idle resources <!-- .element: class="fragment" -->
- Built in availability and fault tolerance <!-- .element: class="fragment" -->
- Business logic in minimal shippable unit sizes <!-- .element: class="fragment" -->

--

## Function-as-a-Service
### Disadvantages

- Decreased transparency <!-- .element: class="fragment" -->
- Potentially tough to debug <!-- .element: class="fragment" -->
- Potentially tough to manage costs <!-- .element: class="fragment" -->
- Decreased oversight of your system <!-- .element: class="fragment" -->
- Increased chances of failures <!-- .element: class="fragment" -->

Note:
Decreased transparency. Someone else is managing your infrastructure so it can be tough to understand the entire system.
Potentially tough to debug. There are tools that allow remote debugging and some services (i.e. Azure) provide a mirrored local development environment but there is still a need for improved tooling.
Auto-scaling of function calls often means auto-scaling of cost. This can make it tough to gauge your business expenses.
You now have a ton of functions deployed and it can be tough to keep track of them. This comes down to a need for better tooling (developmental: scripts, frameworks, diagnostic: step-through debugging, local runtimes, cloud debugging, and visualization: user interfaces, analytics, monitoring).
Solutions for caching resources between stateless requests (i.e. DB connections) and recycling network requests are still pending.

---

## AWS Lambda

> Run code without provisioning or managing servers. 

> Pay only for the compute time you consume.

--

## AWS Lambda

- Runs your code in response to events <!-- .element: class="fragment" -->
- Manages the underlying compute resources <!-- .element: class="fragment" -->
- Create your own back-end services <!-- .element: class="fragment" -->
- Used to extend other AWS services with custom logic <!-- .element: class="fragment" -->
- Runs your code on high-availability compute infrastructure <!-- .element: class="fragment" -->
- Automatic scaling <!-- .element: class="fragment" -->
- Only pay for what you use <!-- .element: class="fragment" -->

Note:

<https://aws.amazon.com/lambda/features/>

--

## AWS Lambda
### Triggers

# ![](images/AWS-lambda-destinations.png) <!-- .element: width="800"  -->


--

## AWS Lambda
### Simple example

# ![](images/Lambda-HelloWorld.png)


--


## AWS Lambda
### DynamoDB Example

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

## AWS Lambda
### Pricing

# ![](images/AWS-lambda-pricing.png) <!-- .element: width="700"  -->

--

## AWS Lambda
### Runtimes

- JavaScript / TypeScript (Node.js)
- Python <!-- .element: class="fragment" -->
- Ruby <!-- .element: class="fragment" -->
- Java <!-- .element: class="fragment" -->
- Go <!-- .element: class="fragment" -->
- C# (.NET Core) <!-- .element: class="fragment" -->
- Custom Runtime <!-- .element: class="fragment" -->

Note:

<https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html>

--

## AWS Lambda
### Lifecycle

# ![](images/AWS-lambda-lifecycle.png) <!-- .element: height="480" -->

Note:

- Nieuwe instantie -> code inladen en code buiten handler uitvoeren (init) 
- Init kan even duren als veel wordt geïnitialiseerd (code, dependencies, SDK). 
- Eerste request van nieuwe instantie heeft hogere latency 

---

## Serverless Application Model

- Open-source framework
- Build serverless applications on AWS <!-- .element: class="fragment" -->
- AWS SAM template specification <!-- .element: class="fragment" -->
- AWS SAM command line interface (AWS SAM CLI) <!-- .element: class="fragment" -->

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

- sam init - Initializes a serverless project
- sam build - Builds a serverless application
- sam local invoke - Invokes a local Lambda function once
- sam local start-api - Runs your serverless application locally
- sam deploy - Deploy a serverless application
- sam logs - Fetches logs that are generated
- sam validate - Verifies whether an SAM template file is valid

Note:

<https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-command-reference.html>

---

## API Gateway

- Fully managed service for serving and managing APIs
- HTTP, RESTful and WebSocket APIs <!-- .element: class="fragment" -->
- Frontdoor to application <!-- .element: class="fragment" -->
    - Request proxying too AWS Lambda targets

# ![](images/AWS-APIGateway.png) <!-- .element: class="fragment" width="800" -->

--

## API Gateway
### SAM Example


```yaml
...
Resources:
  microservicehttpendpointpython3:
    Type: 'AWS::Serverless::Function'
    Properties:
      ...
      Events:
        Api1:
          Type: Api
          Properties:
            Path: /MyResource
            Method: GET
```

---

## DynamoDB

> DynamoDB is een fully managed (Serverless) widecolumn non-relational database

- Geoptimaliseerd voor schaal en performance
- Flexibel schema
- JSON en key-value data structuren
- Availability, durability, en scalability built-in

--

## DynamoDB

- Maak tabellen zonder na te denken over hardware of zelfs DBMS
  - DynamoDB tabellen kunnen elke hoeveelheid data en verkeer verwerken
  - Voorzie tabellen van resources aan de hand van
    - Read Capacity Units (RCU)
    - Write Capacity Units (WCU)

---

<!-- .slide: data-background="white" -->

# ![](images/AWS-Serverless-Archit.png) <!-- .element: width="900" -->

---

### Vragen?

---

## Hand-on Opdracht

> [https://github.com/Quintor/serverless-lambda-workshop/blob/main/assignment/serverless.md](https://github.com/Quintor/serverless-lambda-workshop/blob/main/assignment/serverless.md)
