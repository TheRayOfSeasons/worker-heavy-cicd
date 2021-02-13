from aws_cdk import core
from aws_cdk import aws_ec2 as ec2
from aws_cdk import aws_ecs as ecs
from aws_cdk import aws_elasticloadbalancingv2 as elbv2


class Network(core.Stack):
    """
    A class that defines the networks for the infrastructure.
    """

    def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        # Adjust maxAzs as needed. But preferrably, it's much more
        # cost effective to start with just 1 unless if we intend
        # to remain highly available despite huge net traffic.
        self.vpc = ec2.vpc(self, 'worker-heavy-vpc', maxAzs=1)
        self.api_cluster = ecs.Cluster(self, 'api_cluster', vpc=self.vpc)
        self.worker_cluser = ecs.Cluster(self, 'worker_cluster', vpc=self.vpc)
        self.define_loadbalancers()
        self.output()

    def define_loadbalancers(self):
        """
        Defines all the load balancers available in the stack.
        These load balancers are defined here so we can reference
        their endpoints when assigning connections between each
        microservice.
        """
        self.api_service_load_balancer = elbv2.IApplicationLoadBalancer()
        self.worker_service_load_balancer = elbv2.IApplicationLoadBalancer()

    def output(self):
        """
        Returns the cloudformation template for the networks.
        """
        core.CfnOutput(
            self,
            'APIClusterARN',
            value=self.api_cluster.cluster_arn
        )
        core.CfnOutput(
            self,
            'WorkerClusterARN',
            value=self.worker_cluster.cluster_arn
        )
