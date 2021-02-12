"""
Entry script for the worker service.
"""
import os
import sys

from celery import Celery

from configurations.settings import INSTALLED_APPS

app = Celery('app', broker='redis://localhost:6379/0')
# To include sibling directories for auto discovery.
sys.path.insert(
    0,
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            '../worker_service'
        )
    )
)
app.autodiscover_tasks(lambda: INSTALLED_APPS, related_name='router')

