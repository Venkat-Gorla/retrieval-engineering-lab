from aws_cdk import App
from stacks.oss_cost_stack import OpenSearchServerlessCostStack

app = App()
OpenSearchServerlessCostStack(app, "OpenSearchServerlessCostStack")
app.synth()
