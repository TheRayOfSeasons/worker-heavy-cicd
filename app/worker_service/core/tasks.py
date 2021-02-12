from celery import shared_task

from .loggers import logger


class TaskInterface:
    """
    An interface for tasks.
    """

    def run(self, run_as_test=True, *args, **kwargs):
        """
        An abstract method that should contain the
        logic of a celery task.

            :param run_as_test: :type bool:
                - A boolean reference that the task logic
                can use to differentiate statements depending
                if the invocation is just a test or not. This
                is to prevent any potential cost-inducing or
                database manipulating events that should not
                be happening during a test.
        """
        raise NotImplementedError


class Task(TaskInterface):
    """
    A class based celery task.
    """

    task_name = ''

    def get_task_name(self, *args, **kwargs):
        """
        A virtual method that returns the task name.
        """
        return self.task_name or self.__class__.__name__

    def as_celery_task(
            self, run_as_test=False, safe_test=True,
            *args, **kwargs):
        """
        Returns the instance as a celery task.
        """
        instance = self.__class__(*args, **kwargs)
        task_name = self.get_task_name(*args, **kwargs)
        @shared_task(name=task_name)
        def task_wrapper(*task_args, **task_kwargs):
            if run_as_test:
                logger.info(f'{task_name} is invokeable.')
                if safe_test:
                    return True
                logger.info(f'Running {task_name} for testing purposes.')
            try:
                result = self.run(
                    run_as_test=run_as_test,
                    *task_args,
                    **task_kwargs
                )
            except Exception as e:
                if run_as_test:
                    logger.error(f'{task_name} encountered an error: {e}')
                    return False
                else:
                    raise e
            return result
        return task_wrapper

    def __call__(self, *args, **kwargs):
        celery_task = self.as_celery_task(*args, **kwargs)
        return celery_task.delay(*args, **kwargs)

