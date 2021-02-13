from aws_cdk import core

from stacks.networks import Networks
from stacks.storage import Storage


class CloudInfrastructureStack(core.Stack):

    def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        self.network = Network(self, 'Network')
        self.storage = Storage(self, 'Storage', network=self.network)
        
