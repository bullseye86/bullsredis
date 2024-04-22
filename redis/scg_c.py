from aws_cdk import (Stack, CfnTag,  aws_ec2 as ec2, aws_elasticache as el, RemovalPolicy, CfnOutput, aws_iam as iam)

from constructs import Construct

class scgcon(Construct):

    @property
    def scg(self):
        return self._scg

    @property
    def scgn(self):
        return self._scgn
    

    def __init__(self, scope: Construct, construct_id: str, sgn:str,  **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)



        

        self._scg = el.CfnSecurityGroupIngress(self, "scgID", cache_security_group_name="cachescg", ec2_security_group_name=sgn)
        self._scgn=self._scg.cache_security_group_name









        






## Removal policy
        self._scg.apply_removal_policy(RemovalPolicy.DESTROY)


##          cache_parameter_group_name ="default.redis3.2.cluster.on",
        
##        pg = el.CfnParameterGroup(self, "pgID", cache_parameter_group_family="redis3.2", description="the redis 3.2 group",
##                                           properties={"properties_key": "properties"})

##        vpcimported.vpcconstruct.select_subnets(subnet_type=ec2.SubnetType.PRIVATE_WITH_EGRESS).subnet_group_name.to_string()
##        redis_cluster = el.CfnCacheCluster(self, "redis_clusterID", engine="redis", cache_node_type="cache.t3.small", num_cache_nodes=2,
##                                                    cache_subnet_group_name= (vpcimported.vpcconstruct.private_subnets[0]).to_string() , vpc_security_group_ids=[sgimported.sgconstruct.security_group_id],
##                                                    tags=[CfnTag(key="cost", value="redis_cluster")], log_delivery_configurations=
##                                           [el.CfnCacheCluster.LogDeliveryConfigurationRequestProperty(destination_details=el.CfnCacheCluster.DestinationDetailsProperty
##                                                                                                       (cloud_watch_logs_details=el.CfnCacheCluster.CloudWatchLogsDestinationDetailsProperty(log_group="redisCluster")),destination_type="cloudwatch-logs",
##                                                                                                       log_format="JSON", log_type="slow-log")])
