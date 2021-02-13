from aws_cdk import core
from aws_cdk import aws_ecs_patterns as ecs_patterns

from .networks import Network
from .storage import Storage


class EC2ApplicationStack(core.Stack):
    """
    An abstract stack for applications to be deployed
    in an EC2 instance.
    """

    service_id = ''
    service_name = ''
    public = False
    redirectHTTP = False

    def __init__(
            self, scope: core.Construct, construct_id: str,
            network: Network, storage: Storage,
            env_vars: dict, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        self.network = network
        self.storage = storage
        self._declare_defaults()
        self.define()

    def define(self):
        """
        An abstract method for defining the ec2 stack.
        """
        raise NotImplementedError

    def _declare_defaults(self):
        """
        """
        self.ec2_service = ApplicationLoadBalancedEc2Service(
            self,
            self.service_id,
            service_name=self.service_name,
            vpc=self.network.vpc,
            desired_count=1,
            publicLoadBalancer=self.public,
            redirectHTTP=self.redirectHTTP
        )
        self.endpoint = self.ec2_service.load_balancer.loadBalancerDnsName
