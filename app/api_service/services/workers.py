import json

import requests

from django.conf import settings

from core.aws_utils.sqs import send_to_sqs
from core.services import Service


class WorkerService(Service):
    """
    A one way interaction with the worker
    service through an HTTP request.
    """

    PROXY_URL = settings.WORKER_SERVICE_PROXY_URL

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
        response = requests.request(
            'POST',
            self.PROXY_URL,
            data=payload
        )
        return response
