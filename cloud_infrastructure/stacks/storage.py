from aws_cdk import core
from aws_cdk import aws_ec2 as ec2
from aws_cdk import aws_rds as rds
from aws_cdk import aws_s3 as s3

from .networks import Network


class Storage(core.Stack):
    """
    A stack that defines the data and file storages.
    """

    def __init__(
            self, scope: core.Construct, construct_id: str,
            network: Network, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        self.network = network
        self.database_cluster = self._define_database()
        self.buckets = self._create_buckets()

    def _define_database(self):
        """
        Defines the databases.
        """
        version = rds.PostgresEngineVersion.VER_12_4
        engine = rds.DatabaseInstanceEngine.postgres(version=version)
        cluster = rds.DatabaseInstance(
            self,
            'postgresql_database',
            engine=engine,
            allocated_storage=20, # 20 GB
            max_allocated_storage=100, # 100 GB
            vpc=self.network.vpc,
            multi_az=True
        )
        return cluster

    def _create_buckets(self):
        """
        Define S3 buckets.
        """
        static_bucket = s3.Bucket(
            self,
            'static_bucket',
            bucket_name='worker-heavy-api-static-bucket',
            removal_policy=core.RemovalPolicy.DESTROY
        )
        media_bucket = s3.Bucket(
            self,
            'media_bucket',
            bucket_name='worker-heavy-api-media-bucket',
            removal_policy=core.RemovalPolicy.DESTROY
        )
        reports_bucket = s3.Bucket(
            self,
            'reports_bucket',
            bucket_name='worker-heavy-reports-bucket',
            removal_policy=core.RemovalPolicy.DESTROY
        )
        buckets = {
            'static': static_bucket,
            'media': media_bucket,
            'reports': reports_bucket
        }
        return buckets

    def output(self):
        """
        Build cloudformation generated from this construct.
        """
        core.CfnOutput(
            self,
            'RDS_Database',
            value=self.rds_database.instance_arn
        )
        for key, bucket in self.buckets.items():
            bucket_identifier = f'{key.upper()}_S3_Bucket'
            core.CfnOutput(self, bucket_identifier, value=bucket.bucket_arn)

