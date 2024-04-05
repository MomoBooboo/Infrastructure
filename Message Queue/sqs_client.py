import boto3

# Initialize SQS client
sqs = boto3.client('sqs', region_name='your-region', aws_access_key_id='your-access-key', aws_secret_access_key='your-secret-key')
queue_name = 'trade-data-queue'

# Create SQS queue
response = sqs.create_queue(
    QueueName=queue_name
)

queue_url = response['QueueUrl']
def send_trade_data_to_queue(user_id, volume):
    # Send trade data to SQS queue
    trade_data = {'user_id': user_id, 'volume': volume}
    response = sqs.send_message(
        QueueUrl=queue_url,
        MessageBody=json.dumps(trade_data)
    )

    if response['ResponseMetadata']['HTTPStatusCode'] == 200:
        print("Trade data sent to queue successfully.")
    else:
        print("Error sending trade data to queue:", response)
def consume_trade_data_from_queue():
    # Receive messages from the SQS queue
    response = sqs.receive_message(
        QueueUrl=queue_url,
        MaxNumberOfMessages=1
    )

    # Process received messages
    if 'Messages' in response:
        for message in response['Messages']:
            trade_data = json.loads(message['Body'])
            # Process trade data (e.g., send it to the Leaderboard Service)
            send_trade_data_to_leaderboard_service(trade_data['user_id'], trade_data['volume'])
            # Delete processed message from the queue
            sqs.delete_message(
                QueueUrl=queue_url,
                ReceiptHandle=message['ReceiptHandle']
            )
    else:
        print("No messages in the queue.")

