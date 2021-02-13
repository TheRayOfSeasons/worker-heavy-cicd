from aws_cdk import core
from aws_cdk import aws_ec2 as ec2
from aws_cdk import aws_ecs as ecs
from aws_cdk import aws_ecs_patterns as ecs_patterns


class ApiService(core.Stack):
    """
    A stack that defines the api service.
    """
