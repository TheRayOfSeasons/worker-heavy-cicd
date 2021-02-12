import uuid

import boto3


sqs = boto3.resource('sqs')


def send_to_sqs(sqs_name, message):
    """
    Sends a message to an SQS queue.
    """
    queue = sqs.get_queue_by_name(QueueName=sqs_name)
    message_group_id = str(uuid.uuid4())
    deduplication_id = str(uuid.uuid4())
    response = queue.send_message(
        MessageBody=message,
        MessageGroupId=message_group_id,
        MessageDeduplicationId=deduplication_id
    )
    return response
