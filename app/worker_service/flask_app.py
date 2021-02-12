import json

from flask import Flask
from flask import request

from celery_app import app as celery_app


app = Flask(__name__)


@app.route('/', methods=['POST'])
def entrypoint():
    """
    The single entrypoint for requests.
    """
    params = json.loads(request.body)
    task = params.get('task')
    args = params.get('args')
    kwargs = params.get('kwargs')
    result = celery_app.send_task(
        task,
        run_as_test=False,
        *args,
        **kwargs
    )
    if result:
        status = 200
        message = 'Task found!'
    else:
        status = 301
        message = 'Task not found.'
    return json.dumps({
        'status': status,
        'message': message,
        'task': task,
    })
