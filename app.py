import aws_cdk as cdk
import os
from aws_cdk import DefaultStackSynthesizer, Environment
from cdk.stacks.de_stack import DEProjStack
app = cdk.App()
account_id = os.environ.get("AWS_ACCOUNT_ID")
deploy_env = Environment(
    account = account_id,
    region = "ap-northeast-1"
)
project_synth = DefaultStackSynthesizer(
    # ARN of the role assumed by the CLI and Pipeline to deploy here
            deploy_role_arn= f"arn:aws:iam::{account_id}:role/cdk-hnb659fds-deploy-role-{account_id}-ap-northeast-1",
            # Name of the S3 bucket for file assets
            file_assets_bucket_name= f"cdk-hnb659fds-assets-{account_id}-ap-northeast-1",
            bucket_prefix="cdk",
            # ARN of the role used for file asset publishing (assumed from the CLI role)
            file_asset_publishing_role_arn=f"arn:aws:iam::{account_id}:role/cdk-hnb659fds-file-publishing-role-{account_id}-ap-northeast-1",
            # ARN of the role used for Docker asset publishing (assumed from the CLI role)
            image_asset_publishing_role_arn=f"arn:aws:iam::{account_id}:role/cdk-hnb659fds-image-publishing-role-{account_id}-ap-northeast-1",
            image_assets_repository_name=f"cdk-hnb659fds-container-assets-{account_id}-ap-northeast-1",
            # ARN of the role passed to CloudFormation to execute the deployments
            cloud_formation_execution_role=f"arn:aws:iam::{account_id}:role/cdk-hnb659fds-cfn-exec-role-{account_id}-ap-northeast-1",
            # ARN of the role used to look up context information in an environment
            lookup_role_arn=f"arn:aws:iam::{account_id}:role/cdk-hnb659fds-lookup-role-{account_id}-ap-northeast-1"
)

DEProjStack(
    app,
    'IrisCdkStack_dev',
    stack_name='DEProjStack',
    synthesizer=project_synth,
    env=deploy_env
)


