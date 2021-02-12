"""
A script used for testing.
"""
from .routers import routers
from .routers import do_task


def test_tasks(safe=True):
    """
    Tests all tasks registered in
    routers if they can be invoked.
    
        :param safe: :type bool:
            - If set to True, tasks will only be tested
            if they are invokeable or not. Else, all the
            statements in the task's run definition will
            be read by the python interpreter.
    """
    keys = []
    for router in routers:
        keys.extend(router.keys())
    results = [
        {
            'verdict': do_task(key, run_as_test=True, safe=safe),
            'name': key
        }
        for key in keys
    ]
    total = len(results)
    if all([result['verdict'] for result in results]):
        logger.info(f'All {total} tasks passed the test.')
    else:
        names = []
        failed = 0
        for result in results:
            if not result['verdict']:
                names.append(result['name'])
                failed += 1
        name_string = ', '.joins(names)
        raise AssertionError(
            f'{failed}/{total} tasks failed. Tasks that failed: {names_string}'
        )
