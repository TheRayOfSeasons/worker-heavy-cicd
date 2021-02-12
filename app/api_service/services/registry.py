"""
This python script acts as a registry of
services, much like the urls.py for views.
"""
from .workers import WorkerService


class Services:
    """
    An enum of service instances.
    """

    Workers = WorkerService()
