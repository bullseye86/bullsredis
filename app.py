#!/usr/bin/env python3
import os

import aws_cdk as cdk

from redis.redis_stack import RedisStack


app = cdk.App()
RedisStack(app, "RedisStack", env=cdk.Environment(account='003701616599', region='us-east-1'))

app.synth()
