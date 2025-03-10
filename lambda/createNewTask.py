import json
import boto3
import uuid
from datetime import datetime

# Initialize a DynamoDB resource
dynamodb = boto3.resource('dynamodb')
# Reference the 'Tasks' table
table = dynamodb.Table('Tasks')

def lambda_handler(event, context):
    # Parse the JSON body of the incoming request
    body = json.loads(event['body'])
    
    # Generate a unique task ID using UUID
    task_id = str(uuid.uuid4())
    
    # Create a task dictionary with necessary attributes
    task = {
        'taskId': task_id,  # Unique identifier for the task
        'taskName': body['taskName'],  # Name of the task from the request body
        'description': body.get('description', ''),  # Description of the task, defaults to an empty string if not provided
        'taskStatus': 'pending',  # Default status of the task
        'dueDate': body.get('dueDate', ''),  # Due date of the task, defaults to an empty string if not provided
        'createdTimeStamp': datetime.now().isoformat()  # Timestamp of task creation
    }
    
    # Store the new task in the DynamoDB table
    table.put_item(Item=task)
    
    # Return a response with status code 200 and a message indicating successful task creation
    return {
        'statusCode': 200,
        'body': json.dumps({'message': 'Task created', 'taskId': task_id})
    }

