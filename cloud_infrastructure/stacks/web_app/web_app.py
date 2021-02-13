import json

from aws_cdk import aws_iam as iam
from aws_cdk import aws_s3 as s3
from aws_cdk import core

from stacks.networks import Network


def get_bucket_policy():
    """
    Retrieves and parses the IAM policy as a dictionary.
    """
    data = {}
    with open('bucket_policy.json') as policy:
        data = json.loads(policy)
    return data


class WebApp(core.Stack):
    """
    A stack that defines the cloud foundations of the
    frontend web application.
    """

    def __init__(
            self, scope: core.Construct, construct_id: str,
            network: Network, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        self.api_endpoint = (
            network
            .api_service_load_balancer
            .load_balancer_dns_name
        )
        self.bucket = self.define_bucket()
        self.output()

    def define_bucket(self):
        """
        This defines the S3 bucket where the
        Angular application will be hosted from.
        """
        policy = get_bucket_policy()
        bucket_name = 'worker-heavy-angular-web-application-host'
        bucket = s3.Bucket(
            self,
            'angular_app_bucket',
            access_control=s3.BucketAccessControl.PUBLIC,
            block_public_access=s3.BlockPublicAccess(
                block_public_acls=False,
                block_public_policy=False
            ),
            bucket_name=bucket_name,
            public_read_access=True,
            removal_policy=core.RemovalPolicy.DESTROY,
            versioned=True,
        )
        resource = (
            policy['Statement']['Resource']
            .replace('${bucket_name}', bucket_name)
        )
        bucket.addToResourcePolicy(
            iam.PolicyStatement(
                actions=policy['Statement']['Action'],
                effect=policy['Statement']['Effect'],
                principals=policy['Statement']['Principal']
                sid=policy['Statement']['Sid'],
                resources=resources
            )
        )
        return bucket

    def output(self):
        """
        Build cloudformation generated from this construct.
        """
        core.CfnOutput(
            self
            'webapp',
            value=self.bucket.bucket_arn
        )
