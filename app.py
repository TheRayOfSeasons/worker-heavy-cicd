#!/usr/bin/env python3

from aws_cdk import core

from cloud_infrastructure.cloud_infrastructure_stack import CloudInfrastructureStack


app = core.App()
CloudInfrastructureStack(app, "cloud-infrastructure")

app.synth()
