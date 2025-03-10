import json
import boto3
import csv
from io import StringIO

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Tasks')
s3 = boto3.client('s3')
bucket_name = 'exported-tasks'

def lambda_handler(event, context):
    response = table.scan()
    tasks = response.get('Items', [])
    
    # Convert tasks to CSV
    csv_file = StringIO()
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['taskId', 'taskName', 'description', 'taskStatus', 'dueDate', 'createdTimeStamp'])
    for task in tasks:
        csv_writer.writerow([
            task['taskId'],
            task['taskName'],
            task.get('description', ''),
            task['taskStatus'],
            task.get('dueDate', ''),
            task['createdTimeStamp']
        ])
    
    # Upload CSV to S3
    s3.put_object(
        Bucket=bucket_name,
        Key='tasks.csv',
        Body=csv_file.getvalue(),
        ContentType='text/csv'
    )
    
    return {
        'statusCode': 200,
        'body': json.dumps({'message': 'Tasks exported to CSV'})
    }

