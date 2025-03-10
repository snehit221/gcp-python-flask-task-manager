import json
import boto3

# Initialize a DynamoDB resource
dynamodb = boto3.resource('dynamodb')
# Reference the 'Tasks' table
table = dynamodb.Table('Tasks')

def lambda_handler(event, context):
    # Retrieve the taskId from the path parameters of the request
    task_id = event['pathParameters']['taskId']
    
    # Parse the JSON body of the incoming request
    body = json.loads(event['body'])
    
    # Initialize the update expression and the expression attribute values
    update_expression = "set "
    expression_attribute_values = {}
    
    # Construct the update expression and the attribute values
    for key, value in body.items():
        update_expression += f"{key} = :{key}, "  # Append each key-value pair to the update expression
        expression_attribute_values[f":{key}"] = value  # Add the attribute value
    
    # Remove the trailing comma and space from the update expression
    update_expression = update_expression.rstrip(", ")
    
    # Update the item in the DynamoDB table
    table.update_item(
        Key={'taskId': task_id}, 
        UpdateExpression=update_expression,  
        ExpressionAttributeValues=expression_attribute_values  
    )
    
    # Return a response with status code 200 and a message indicating successful task update
    return {
        'statusCode': 200,
        'body': json.dumps({'message': 'Task updated'})
    }

