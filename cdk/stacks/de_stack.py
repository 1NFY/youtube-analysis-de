from aws_cdk import (
    Environmnet, 
    IStackSynthesizer, 
    Stack
)
from constructs import Construct
from cdk.stacks.lambda_stack import LambdaStack

class DEProjStack(Stack):
    def __init__(
            self,
            scope : Construct,
            construct_id : str,
            *,
            env : Environment,
            synthesizer : IStackSynthesizer,
            **kwargs,
    ) -> None:
        super().__init__(scope, construct_id, env = env, **kwargs)

        print("Deploying Lambdas")
        lambda_stack = LambdaStack(self, "DELambdaStack", env = env, synthesizer = synthesizer)
        
