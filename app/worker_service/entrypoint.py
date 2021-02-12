import json

from flask import Flask
from flask import request

from core.routers import do_task


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
    result = do_task(task, run_as_test=False, *args, **kwargs)
    if result:
        status = 200
        message = 'Task found!'
    else:
        status = 301
        message = 'Task not found.'
    return json.dumps({
        'status': status,
        'message': message
    })
