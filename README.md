# Serverless REST API - AWS

A serverless REST API built using AWS Lambda, API Gateway, and DynamoDB.

Infrastructure is managed using Terraform, and deployment validation is automated using GitHub Actions with AWS OIDC authentication.

---

## Architecture

### Application Flow

```text
                    USER
                      │
                      │ HTTP GET / POST
                      ▼
              ┌─────────────────┐
              │   API Gateway   │
              │   HTTP API      │
              └────────┬────────┘
                       │
                       ▼
              ┌─────────────────┐
              │     Lambda      │
              │    Python 3.12  │
              └────────┬────────┘
                       │
                       ▼
              ┌─────────────────┐
              │    DynamoDB     │
              │ serverless-api- │
              │     table       │
              └─────────────────┘
                                DEVELOPER
                      │
                      │ git push
                      ▼
              ┌─────────────────┐
              │     GitHub      │
              └────────┬────────┘
                       │
                       ▼
              ┌─────────────────┐
              │ GitHub Actions  │
              └────────┬────────┘
                       │
                       │ OIDC
                       ▼
              ┌─────────────────┐
              │    AWS IAM      │
              │ GitHubActions   │
              │ Terraform Role  │
              └────────┬────────┘
                       │
                       ▼
              ┌─────────────────┐
              │    Terraform    │
              │ Init / Validate │
              │      / Plan     │
              └────────┬────────┘
                       │
                       ▼
                    AWS
                    ## Technologies Used
```

- AWS Lambda
- Amazon API Gateway
- Amazon DynamoDB
- AWS IAM
- Amazon CloudWatch
- Terraform
- GitHub Actions
- GitHub OIDC
- Python
- Git
API Endpoints
GET /items

Returns all items stored in DynamoDB.

Example:
     [
  {
    "id": "101",
    "name": "Akash",
    "message": "Learning DevOps"
  }
]
POST /items

Adds a new item to DynamoDB.

Example request:{
  "id": "102",
  "name": "DevOps",
  "message": "Learning AWS"
}
Example response:
{
  "message": "Item added successfully",
  "item": {
    "id": "102",
    "name": "DevOps",
    "message": "Learning AWS"
  }
}
AWS Infrastructure

###Terraform provisions the following AWS resources:

API Gateway HTTP API
AWS Lambda function
DynamoDB table
IAM role for Lambda
DynamoDB permissions
CloudWatch logging permissions
API Gateway → Lambda integration
Lambda permission for API Gateway

AWS Infrastructure

Terraform provisions the following AWS resources:

API Gateway HTTP API
AWS Lambda function
DynamoDB table
IAM role for Lambda
DynamoDB permissions
CloudWatch logging permissions
API Gateway → Lambda integration
Lambda permission for API Gateway

IAM Security

The Lambda function uses an IAM role with permissions required to access DynamoDB and CloudWatch Logs.

DynamoDB permissions include:
GetItem
PutItem
DeleteItem
Scan
GitHub Actions authenticates with AWS using GitHub OIDC federation instead of storing long-lived AWS access keys.

This allows GitHub Actions to assume an AWS IAM role securely.

GitHub Actions CI

The GitHub Actions workflow automatically runs when code is pushed to the main branch or when a pull request targets main.

The workflow performs:
Git Push
   │
   ▼
Checkout Repository
   │
   ▼
Setup Terraform
   │
   ▼
AWS Authentication using OIDC
   │
   ▼
Terraform Init
   │
   ▼
Terraform Validate
   │
   ▼
Terraform Plan

Terraform

Initialize Terraform:
terraform init
Validate the Terraform configuration:
terraform validate
Preview infrastructure changes:
terraform plan
Apply the infrastructure:
terraform apply

Testing
GET Request
Invoke-RestMethod -Method Get -Uri "https://YOUR_API_URL/items"

POST Request
$body = @{
    id = "102"
    name = "DevOps"
    message = "Learning AWS"
} | ConvertTo-Json

Invoke-RestMethod `
    -Method Post `
    -Uri "https://YOUR_API_URL/items" `
    -ContentType "application/json" `
    -Body $body
    Project Structure
    serverless-rest-api-devops/
│
├── .github/
│   └── workflows/
│       └── terraform.yml
│
├── lambda/
│   └── lambda_function.py
│
├── api_gateway.tf
├── dynamodb.tf
├── iam.tf
├── lambda.tf
├── outputs.tf
├── provider.tf
├── .gitignore
├── .terraform.lock.hcl
└── README.md
## Key DevOps Concepts Demonstrated

- Infrastructure as Code using Terraform
- Serverless AWS architecture
- REST API development
- AWS Lambda
- Amazon API Gateway
- Amazon DynamoDB
- IAM least-privilege permissions
- Git and GitHub
- GitHub Actions CI
- AWS OIDC authentication
- Terraform automation
- Amazon CloudWatch logging
- Secure cloud authentication
- AWS service integration
Project Outcome

This project demonstrates the deployment and management of a serverless REST API using AWS and Terraform.

GitHub Actions automates Terraform initialization, validation, and planning.

AWS OIDC federation is used to authenticate GitHub Actions without storing long-lived AWS access keys.

The application successfully supports GET and POST operations through API Gateway, with Lambda handling the requests and DynamoDB storing the data.
Author

Akash K

DevOps / AWS Learning Project