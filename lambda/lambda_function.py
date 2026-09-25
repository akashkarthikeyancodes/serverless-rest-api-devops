import json
import os
import boto3

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table(os.environ["DYNAMODB_TABLE"])


def lambda_handler(event, context):

    http_method = event.get("requestContext", {}).get("http", {}).get("method", "GET")

    if http_method == "GET":
        response = table.scan()

        return {
            "statusCode": 200,
            "body": json.dumps(response["Items"])
        }

    if http_method == "POST":
        body = json.loads(event.get("body", "{}"))

        item = {
            "id": body["id"],
            "name": body["name"],
            "message": body["message"]
        }

        table.put_item(Item=item)

        return {
            "statusCode": 200,
            "body": json.dumps({
                "message": "Item added successfully",
                "item": item
            })
        }

    return {
        "statusCode": 400,
        "body": json.dumps({
            "message": "Unsupported HTTP method"
        })
    }