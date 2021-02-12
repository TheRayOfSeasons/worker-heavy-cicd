import json

from django.conf import settings

from core.aws_utils.sqs import send_to_sqs
from core.services import Service


class WorkerService(Service):
    """
    A one way interaction with the worker
    service by publishing a message in a
    FIFO SQS queue.
    """

    SQS_ARN = settings.SQS_WORKER_QUEUE

    def send_payload(self, task: str, *args, **kwargs):
        """
        Passes a message to the SQS queue to be recieved
        by a lambda function which eventually sends the
        message to the worker service.

            :param task: :type str:
                - The name of the task that will be invoked
                asyncronously in the worker service.

        All args and kwargs will also be passed with the message.
        The message will have the following structure:

        ```
        {
            'task': 'run_my_task',
            'args': [],
            'kwargs': {}
        }
        ```
        """
        payload = json.dumps({
            'task': task,
            'args': args,
            'kwargs': kwargs
        })
        return send_to_sqs(self.SQS_ARN, payload)
