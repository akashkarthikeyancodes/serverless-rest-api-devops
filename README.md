# Serverless REST API - AWS

A serverless REST API built using AWS Lambda, API Gateway, and DynamoDB.

Infrastructure is managed using Terraform, while GitHub Actions automates Terraform validation and planning using secure AWS OIDC authentication.

---

## Architecture

### Application Architecture

```text
                         USER
                           |
                           | HTTP GET / POST
                           v
                  +-------------------+
                  |    API Gateway    |
                  |     HTTP API      |
                  +---------+---------+
                            |
                            v
                  +-------------------+
                  |      Lambda       |
                  |    Python 3.12    |
                  +---------+---------+
                            |
                            v
                  +-------------------+
                  |     DynamoDB      |
                  | serverless-api-   |
                  |      table        |
                  +-------------------+
```

### DevOps / CI Flow

```text
                     DEVELOPER
                         |
                         | git push
                         v
                  +---------------+
                  |    GitHub     |
                  +-------+-------+
                          |
                          v
                  +---------------+
                  | GitHub Actions|
                  +-------+-------+
                          |
                          | OIDC
                          v
                  +---------------+
                  |    AWS IAM    |
                  | GitHubActions |
                  | TerraformRole |
                  +-------+-------+
                          |
                          v
                  +---------------+
                  |   Terraform   |
                  | Init          |
                  | Validate      |
                  | Plan          |
                  +-------+-------+
                          |
                          v
                         AWS
```

---

## Technologies Used

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

---

## API Endpoints

### GET /items

Returns all items stored in DynamoDB.

Example:

```text
GET /items
```

Example response:

```json
[
  {
    "id": "101",
    "name": "Akash",
    "message": "Learning DevOps"
  }
]
```

### POST /items

Adds a new item to DynamoDB.

Example request:

```json
{
  "id": "102",
  "name": "DevOps",
  "message": "Learning AWS"
}
```

Example response:

```json
{
  "message": "Item added successfully",
  "item": {
    "id": "102",
    "name": "DevOps",
    "message": "Learning AWS"
  }
}
```

---

## AWS Infrastructure

Terraform provisions:

- API Gateway HTTP API
- AWS Lambda function
- DynamoDB table
- IAM role for Lambda
- DynamoDB permissions
- CloudWatch logging permissions
- API Gateway to Lambda integration
- Lambda permission for API Gateway

---

## IAM Security

The Lambda function uses an IAM role with the required permissions to access DynamoDB and CloudWatch Logs.

DynamoDB permissions include:

- GetItem
- PutItem
- DeleteItem
- Scan

GitHub Actions authenticates with AWS using GitHub OIDC federation instead of storing long-lived AWS access keys.

---

## GitHub Actions CI

The workflow runs automatically when code is pushed to the `main` branch or when a pull request targets `main`.

```text
Git Push
   |
   v
Checkout Repository
   |
   v
Setup Terraform
   |
   v
AWS Authentication using OIDC
   |
   v
Terraform Init
   |
   v
Terraform Validate
   |
   v
Terraform Plan
```

---

## Terraform Commands

Initialize Terraform:

```bash
terraform init
```

Validate the configuration:

```bash
terraform validate
```

Preview infrastructure changes:

```bash
terraform plan
```

Apply infrastructure:

```bash
terraform apply
```

---

## Testing

### GET Request

PowerShell:

```powershell
Invoke-RestMethod -Method Get -Uri "https://YOUR_API_URL/items"
```

### POST Request

PowerShell:

```powershell
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
```

---

## Project Structure

```text
serverless-rest-api-devops/
|
+-- .github/
|   +-- workflows/
|       +-- terraform.yml
|
+-- lambda/
|   +-- lambda_function.py
|
+-- api_gateway.tf
+-- dynamodb.tf
+-- iam.tf
+-- lambda.tf
+-- outputs.tf
+-- provider.tf
+-- .gitignore
+-- .terraform.lock.hcl
+-- README.md
```

---

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

---

## Project Outcome

This project demonstrates a serverless REST API built and managed using AWS and Terraform.

GitHub Actions automates Terraform initialization, validation, and planning.

AWS OIDC federation provides secure authentication between GitHub Actions and AWS without storing long-lived AWS access keys.

The API supports GET and POST operations through API Gateway, with Lambda processing requests and DynamoDB storing application data.

---

## Author

**Akash K**
