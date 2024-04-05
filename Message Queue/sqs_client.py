import boto3

# Initialize SQS client
sqs = boto3.client('sqs', region_name='your-region', aws_access_key_id='your-access-key', aws_secret_access_key='your-secret-key')
