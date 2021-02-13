import logging

import boto3


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
ssm_client = boto3.client('ssm')


def get_parameter_from_ssm(name, decryption=True):
    """
    A generic function that will get a parameter on Amazon Systems
    Manager Agent(SSM) based on parameter name.

    How to use:
    value = get_parameter_from_ssm(name='/value/staging')
    """
    try:
        parameter = ssm_client.get_parameter(
            Name=str(name),
            WithDecryption=decryption
        )
        return parameter['Parameter']['Value']
    except Exception as e:
        logging.error('Failed to get the parameter from SSM.')
        raise e
