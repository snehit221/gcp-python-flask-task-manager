import json
import boto3

# Initialize a DynamoDB resource
dynamodb = boto3.resource('dynamodb')
# Reference the 'Tasks' table
table = dynamodb.Table('Tasks')

def lambda_handler(event, context):
    # Retrieve the taskId from the path parameters of the request
    task_id = event['pathParameters']['taskId']
    
    # Delete the item with the specified taskId from the DynamoDB table
    table.delete_item(Key={'taskId': task_id})
    
    # Return a response with status code 200 and a message indicating successful task deletion
    return {
        'statusCode': 200,
        'body': json.dumps({'message': 'Task successfully deleted'})
    }
