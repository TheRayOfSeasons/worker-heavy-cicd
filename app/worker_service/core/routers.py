from .loggers import logger
from .tasks import Task


routers = []


class TaskRouter:
    """
    Manages the routing of celery tasks.
    """

    tasks = {}

    def __init__(self, *args, **kwargs):
        routers.append(self)

    def __dict__(self):
        return self.tasks

    def register(self, task: Task):
        """
        Registers the task under the router.
        """
        key = task.get_task_name()
        celery_task = task.as_celery_task()
        tasks[key] = celery_task


def do_task(task_name, *args, **kwargs):
    """
    Triggers a task
    """
    for router in routers:
        run_task = router.get(task_name)
        if not run_task:
            continue
        try:
            assert issubclass(run_task, Task)
        except AssertionError:
            logger.error(
                f'Warning: {task_name} is not a sub class of task, '
                f'but it identifies as a task based on the router.'
            )
        run_task(*args, **kwargs)
