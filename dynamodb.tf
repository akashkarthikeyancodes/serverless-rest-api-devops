resource "aws_dynamodb_table" "items" {
  name         = "serverless-api-table"
  billing_mode = "PAY_PER_REQUEST"
  hash_key     = "id"

  attribute {
    name = "id"
    type = "S"
  }

  tags = {
    Name = "serverless-api-table"
  }
}