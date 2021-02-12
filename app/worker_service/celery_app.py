"""
Entry script for the worker service.
"""
from celery import Celery

app = Celery('app')

app.config_from_object('configurations:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
