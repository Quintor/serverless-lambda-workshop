<!-- .slide: data-background="images/skyline_light.jpg", data-background-transition="slide" -->
<!-- .slide: data-background="images/skyline_dark.png", data-background-transition="slide" -->

# ![](images/logo.png) <!-- .element: width="400" style="border:0; background: transparent; box-shadow: none" -->

## Welkom
### Serverless Lambda Workshop

---

## Even voorstellen

<h4>Arjen Wassink</h4>
<div class="columns two">
  <div class="left">
    <ul>
      <li>Quintor</li>
      <li>Cloud Specialist</li>
      <li>IT Architect</li>
      <li>BAR HU</li>
    </ul>
    <br>
    <ul>
      <li>Email: awassink@quintor.nl</li>
      <li>Twitter: @ArjenWassink</li>
      <li>LinkedIn: <a href="https://www.linkedin.com/in/arjen-wassink-39204423/">arjen-wassink-39204423</a></li>
    </ul>

  </div>
  <div class="right">
    <img src="images/arjen-wassink.jpg" style="max-height: none" height="200px">
     <ul>
      <li><u>Specialisaties:</u></li>
      <li>IT Architectuur</li>
      <li>Container technologie</li>
      <li>Cloud technologie</li>
      <li>Java Developer (20 jaar)</li>
    </ul>
  </div>
</div>

--

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
    </ul>

  </div>
  <div class="right">
    <img src="images/pim-otte.jpeg" style="max-height: none" height="200px">
     <ul>
      <li><u>Specialisaties:</u></li>
      <li>Blockchain Development</li>
      <li>Fullstack Java Development</li>
      <li>Cloud Native Software Development</li>
    </ul>
  </div>
</div>

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

## AWS Lambda

> Run code without provisioning or managing servers. 

> Pay only for the compute time you consume.

--

## AWS Lambda

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

- Nieuwe instantie -> code inladen en code buiten handler uitvoeren (init) <!-- .element: class="fragment" -->
- Init kan even duren als veel wordt geïnitialiseerd (code, dependencies, SDK). <!-- .element: class="fragment" -->
- Eerste request van nieuwe instantie heeft hogere latency <!-- .element: class="fragment" -->

--

<!-- .slide: data-background="white" -->

## AWS Lambda
### Cold Start

# ![](images/AWS-lambda-Cold-Starts.jpg) <!-- .element: height="480" -->

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

- AWS::Serverless::Function
- AWS::Serverless::Api <!-- .element: class="fragment" -->
- AWS::Serverless::HttpApi <!-- .element: class="fragment" -->
- AWS::Serverless::StateMachine <!-- .element: class="fragment" -->
- AWS::Serverless::SimpleTable <!-- .element: class="fragment" -->

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

- Fully managed service for serving and managing APIs
- HTTP, RESTful and WebSocket APIs <!-- .element: class="fragment" -->
- Frontdoor to application <!-- .element: class="fragment" -->
    - Request proxying too AWS Lambda targets

# ![](images/AWS-APIGateway.png) <!-- .element: class="fragment" width="800" -->

--

## API Gateway
### SAM Example

---

<!-- .slide: data-background="white" -->

# ![](images/AWS-Serverless-Archit.png) <!-- .element: width="900" -->

---

### Vragen?

> Einde

---

## Hand-on Opdracht

> 
