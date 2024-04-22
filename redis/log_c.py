from aws_cdk import (Stack, CfnTag,  aws_ec2 as ec2, aws_elasticache as el, RemovalPolicy, CfnOutput, aws_iam as iam, aws_logs as logs)

from constructs import Construct

class logcon(Construct):

##    @property
##    def rg(self):
##        return self._replication_groupc
    

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)


        replication_grp_log_group = logs.LogGroup(self, "replication_grp_log_groupID", log_group_class=logs.LogGroupClass("INFREQUENT_ACCESS"), log_group_name="redisCluster7", retention=logs.RetentionDays.FIVE_DAYS)

        replication_grp_log_group.grant_write(iam.ServicePrincipal("elasticache.amazonaws.com"))



## Removal policy

        replication_grp_log_group.apply_removal_policy(RemovalPolicy.DESTROY)


