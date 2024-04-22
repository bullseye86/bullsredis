from aws_cdk import (Stack, CfnTag,  aws_ec2 as ec2, aws_elasticache as el, RemovalPolicy, CfnOutput, aws_iam as iam)

from constructs import Construct
from .vpc_c import vpconcl
from .sg_c import sgoncl
from .sg_c2 import sgoncl2
from .redis_c import Rediscon
from .sng_c import sngcon
from .log_c import logcon
from .scg_c import scgcon

class RedisStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)


## vpc construct 
        vpcimported= vpconcl(self, "vpcimportedID", )

## sg construct 
        sgimported= sgoncl(self, "sgimportedID", vpc23= vpcimported.vpcconstruct)
        sgimported2= sgoncl2(self, "sgimportedID2", vpc23= vpcimported.vpcconstruct)
        vpcimported.vpcconstruct.add_interface_endpoint("ELASTICACHE_ENDPOINT", private_dns_enabled=True,service=ec2.InterfaceVpcEndpointAwsService.ELASTICACHE, security_groups=[sgimported.sgconstruct])


## Subnet group 
        sngimported=sngcon(self, "sngconID",  sn1=vpcimported.subnetconstruct1.subnet_id, sn2=vpcimported.subnetconstruct2.subnet_id)

## Log group 
        logGroupImported=logcon(self, "logGroupImported")

## Cache security group
        #cachescgimported=scgcon(self, "CachescgimportedID", sgn=sgimported2.sgconstruct)
        


## Replication group 
        replication_group=Rediscon(self, "replication_groupID", scgid= sgimported2.sgconstruct, sng=sngimported.sng.cache_subnet_group_name)




## Outputs
        CfnOutput(self, "replication_group_endpoint1",value=replication_group.rg.attr_configuration_end_point_address)
        CfnOutput(self, "replication_group_endpoint2",value=replication_group.rg.attr_configuration_end_point_port)


        










## Removal policy
        replication_group.rg.apply_removal_policy(RemovalPolicy.DESTROY)

        
##        pg = el.CfnParameterGroup(self, "pgID", cache_parameter_group_family="redis3.2", description="the redis 3.2 group",
##                                           properties={"properties_key": "properties"})

##        vpcimported.vpcconstruct.select_subnets(subnet_type=ec2.SubnetType.PRIVATE_WITH_EGRESS).subnet_group_name.to_string()
##        redis_cluster = el.CfnCacheCluster(self, "redis_clusterID", engine="redis", cache_node_type="cache.t3.small", num_cache_nodes=2,
##                                                    cache_subnet_group_name= (vpcimported.vpcconstruct.private_subnets[0]).to_string() , vpc_security_group_ids=[sgimported.sgconstruct.security_group_id],
##                                                    tags=[CfnTag(key="cost", value="redis_cluster")], log_delivery_configurations=
##                                           [el.CfnCacheCluster.LogDeliveryConfigurationRequestProperty(destination_details=el.CfnCacheCluster.DestinationDetailsProperty
##                                                                                                       (cloud_watch_logs_details=el.CfnCacheCluster.CloudWatchLogsDestinationDetailsProperty(log_group="redisCluster")),destination_type="cloudwatch-logs",
##                                                                                                       log_format="JSON", log_type="slow-log")])



##
##        el.CfnReplicationGroup(self, "replication_groupID",  replication_group_description= "replication groups for 2 node cluster", automatic_failover_enabled= True, cache_node_type = "cache.t3.small", num_node_groups=2, 
##                                                 cache_parameter_group_name ="default.redis3.2.cluster.on", security_group_ids =[sgimported2.sgconstruct],
##                                                 cache_subnet_group_name=vpcimported.subnetconstruct1.subnet_id, cluster_mode= "Enabled", engine="Redis", replicas_per_node_group=2,
##                                                 node_group_configuration =[el.CfnReplicationGroup.NodeGroupConfigurationProperty(node_group_id="7000", primary_availability_zone="us-east-1a", replica_availability_zones=["us-east-1b", "us-east-1a"]),
##                                                                            el.CfnReplicationGroup.NodeGroupConfigurationProperty(node_group_id="6001", primary_availability_zone="us-east-1a", replica_availability_zones=["us-east-1b", "us-east-1a"])],
##                                                 tags=[CfnTag(key="cost", value="redis_cluster")], log_delivery_configurations=
##                                                 [el.CfnReplicationGroup.LogDeliveryConfigurationRequestProperty(destination_details=el.CfnReplicationGroup.DestinationDetailsProperty
##                                                                                                             (cloud_watch_logs_details=el.CfnReplicationGroup.CloudWatchLogsDestinationDetailsProperty(log_group="redisCluster")),destination_type="cloudwatch-logs",
##                                                                                                             log_format="JSON", log_type="slow-log")])
##

