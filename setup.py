import setuptools


with open("README.md") as fp:
    long_description = fp.read()


setuptools.setup(
    name="cloud_infrastructure",
    version="0.0.1",

    description="An empty CDK Python app",
    long_description=long_description,
    long_description_content_type="text/markdown",

    author="author",

    package_dir={"": "cloud_infrastructure"},
    packages=setuptools.find_packages(where="cloud_infrastructure"),

    install_requires=[
        "attrs==20.3.0",
        "aws-cdk.assets==1.89.0",
        "aws-cdk.aws-apigateway==1.89.0",
        "aws-cdk.aws-apigatewayv2==1.89.0",
        "aws-cdk.aws-applicationautoscaling==1.89.0",
        "aws-cdk.aws-autoscaling==1.89.0",
        "aws-cdk.aws-autoscaling-common==1.89.0",
        "aws-cdk.aws-autoscaling-hooktargets==1.89.0",
        "aws-cdk.aws-certificatemanager==1.89.0",
        "aws-cdk.aws-cloudformation==1.89.0",
        "aws-cdk.aws-cloudfront==1.89.0",
        "aws-cdk.aws-cloudwatch==1.89.0",
        "aws-cdk.aws-codebuild==1.89.0",
        "aws-cdk.aws-codecommit==1.89.0",
        "aws-cdk.aws-codedeploy==1.89.0",
        "aws-cdk.aws-codeguruprofiler==1.89.0",
        "aws-cdk.aws-codepipeline==1.89.0",
        "aws-cdk.aws-cognito==1.89.0",
        "aws-cdk.aws-ec2==1.89.0",
        "aws-cdk.aws-ecr==1.89.0",
        "aws-cdk.aws-ecr-assets==1.89.0",
        "aws-cdk.aws-ecs==1.89.0",
        "aws-cdk.aws-efs==1.89.0",
        "aws-cdk.aws-elasticloadbalancing==1.89.0",
        "aws-cdk.aws-elasticloadbalancingv2==1.89.0",
        "aws-cdk.aws-events==1.89.0",
        "aws-cdk.aws-iam==1.89.0",
        "aws-cdk.aws-kms==1.89.0",
        "aws-cdk.aws-lambda==1.89.0",
        "aws-cdk.aws-logs==1.89.0",
        "aws-cdk.aws-rds==1.89.0",
        "aws-cdk.aws-route53==1.89.0",
        "aws-cdk.aws-route53-targets==1.89.0",
        "aws-cdk.aws-s3==1.89.0",
        "aws-cdk.aws-s3-assets==1.89.0",
        "aws-cdk.aws-sam==1.89.0",
        "aws-cdk.aws-secretsmanager==1.89.0",
        "aws-cdk.aws-servicediscovery==1.89.0",
        "aws-cdk.aws-sns==1.89.0",
        "aws-cdk.aws-sns-subscriptions==1.89.0",
        "aws-cdk.aws-sqs==1.89.0",
        "aws-cdk.aws-ssm==1.89.0",
        "aws-cdk.cloud-assembly-schema==1.89.0",
        "aws-cdk.core==1.89.0",
        "aws-cdk.custom-resources==1.89.0",
        "aws-cdk.cx-api==1.89.0",
        "aws-cdk.region-info==1.89.0",
        "awscli==1.19.6",
        "botocore==1.20.6",
        "cattrs==1.1.2",
        "colorama==0.4.3",
        "constructs==3.3.19",
        "docutils==0.15.2",
        "jmespath==0.10.0",
        "jsii==1.20.1",
        "publication==0.0.3",
        "pyasn1==0.4.8",
        "python-dateutil==2.8.1",
        "PyYAML==5.3.1",
        "rsa==4.5",
        "s3transfer==0.3.4",
        "six==1.15.0",
        "typing-extensions==3.7.4.3",
        "urllib3==1.26.3",
    ],

    python_requires=">=3.6",

    classifiers=[
        "Development Status :: 4 - Beta",

        "Intended Audience :: Developers",

        "License :: OSI Approved :: Apache Software License",

        "Programming Language :: JavaScript",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",

        "Topic :: Software Development :: Code Generators",
        "Topic :: Utilities",

        "Typing :: Typed",
    ],
)
