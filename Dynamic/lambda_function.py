import json

def lambda_handler(event, context):
    # This Lambda function just returns a message
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda Verion5. This is directly coming from Lambda via API. !!!')
    }
