<!-- .slide: data-background="images/skyline_light.jpg", data-background-transition="slide" -->
<!-- .slide: data-background="images/skyline_dark.png", data-background-transition="slide" -->

# ![](images/HUxQ.png) <!-- .element: width="400" style="border:0; background: transparent; box-shadow: none" -->

## Welkom
### Cloud Native Software Development Minor

> Module 2 les 2-1 <br>
> Serverless Architecture

---

## Programma vandaag

- Serverless Architecture
- Serverless AWS Services
- Function-as-a-Service

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

## AWS Serverless

# ![](images/aws-serverless-overview.png) <!-- .element: width="800" -->

--

## AWS Serverless
### SQS

# ![](images/AWS-SQS.png) <!-- .element: width="800" -->

--

## AWS Serverless
### SNS

# ![](images/AWS-SNS.png) <!-- .element: width="600" -->

--

## AWS Serverless
### Fargate

# ![](images/AWS-Fargate.png) <!-- .element: width="800" -->

--

## AWS Serverless
### Lambda

# ![](images/AWS-Lambda.png) <!-- .element: width="800" -->

--

## AWS Serverless
### S3

# ![](images/AWS-S3.png) <!-- .element: width="600" -->

--

## AWS Serverless
### DynamoDB

# ![](images/AWS-DynamoDB.png)

--

## AWS Serverless
### Aurora Serverless

# ![](images/AWS-Aurora.png) <!-- .element: width="800" -->

--

## AWS Serverless
### API Gateway

# ![](images/AWS-APIGateway.png) <!-- .element: width="800" -->

--

## AWS Serverless
### Step Functions

# ![](images/AWS-StepFunctions.png) <!-- .element: width="800" -->

--

## AWS Serverless
### Kinesis

# ![](images/AWS-kinesis.png) <!-- .element: width="800" -->

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

--

## Function-as-a-Service
### Hosted platforms

# ![](images/faas-hosted-platforms.png) <!-- .element: width="1000" -->

Note:

<https://landscape.cncf.io/format=serverless>

--

## Function-as-a-Service
### Installable platforms

# ![](images/faas-installable-platforms.png) <!-- .element: width="1000" -->

--

## Function-as-a-Service
### Frameworks

# ![](images/faas-frameworks.png) <!-- .element: width="1000" -->

---

<!-- .slide: data-background="images/skyline_dark.png", data-background-transition="slide" -->

<br>
<br>

### Vragen?

---

## Opdracht

> <http://cloud-native-minor.s3-website.eu-central-1.amazonaws.com/assignment-2-2-1_Serverless_Architecture.html>
