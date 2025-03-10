import json
import boto3

# Initialize a DynamoDB resource
dynamodb = boto3.resource('dynamodb')
# Reference the 'Tasks' table
table = dynamodb.Table('Tasks')

def lambda_handler(event, context):
    # Scan the DynamoDB table to retrieve all tasks
    response = table.scan()
    # Extract the list of tasks from the response
    tasks = response.get('Items', [])
    
    # Return a response with status code 200 and the list of tasks in JSON format
    return {
        'statusCode': 200,
        'body': json.dumps(tasks)
    }

