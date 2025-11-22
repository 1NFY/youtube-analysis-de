import os 
from aws_cdk import (
    Stack,
    aws_iam as iam,
    aws_lambda as _lambda,
    Duration as _duration,
    Environment
)
from constructs import Construct


class LambdaStack(Stack):
    def __init__(
            self,
            scope : Construct,
            construct_id : str,
            *,
            env : Environment,
            **kwargs,
    ) -> None:
        super().__init__(scope, construct_id, env = env, **kwargs)
    
    root_dir = os.path.dirname(os.path.abspath('README.md'))
    lambdarole = iam.Role.from_role_name(id = "LambdaRole", role_name = "lambdarole")

    data_clean_lambda = _lambda.Function(
        id = "DataCleanLambda",
        runtime = _lambda.Runtime.PYTHON_3_12,
        function_name = "data_clean_lambda",
        code = _lambda.Code.from_asset(
            f"{root_dir}/lambda/data-clean"
        ),
        handler = 'app.lambda_handler',
        role = lambdarole,
        timeout = _duration.minutes(1)
    )
    






