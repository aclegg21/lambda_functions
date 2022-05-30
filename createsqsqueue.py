import boto3

sqs = boto3.resource('sqs')

queue = sqs.create_queue(QueueName = 'Week16_project')

print(queue.url)