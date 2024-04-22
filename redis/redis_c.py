from aws_cdk import (Stack, CfnTag,  aws_ec2 as ec2, aws_elasticache as el, RemovalPolicy, CfnOutput, aws_iam as iam, aws_logs as logs)

from constructs import Construct

class Rediscon(Construct):

    @property
    def rg(self):
        return self._replication_groupc
    

    def __init__(self, scope: Construct, construct_id: str, scgid, sng,  **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)






## Replication group 
        self._replication_groupc=el.CfnReplicationGroup(self, "replicationgroupcID",  replication_group_description= "replication groups for 3 node cluster", automatic_failover_enabled= True, cache_node_type = "cache.t3.small",
                                                        num_node_groups=3, replication_group_id ="r-70-86", security_group_ids =[scgid], cache_subnet_group_name=sng, cluster_mode= "Enabled", engine="Redis", replicas_per_node_group=2,
                                                        tags=[CfnTag(key="cost", value="redis_cluster")], multi_az_enabled=True, log_delivery_configurations=
                                                        [el.CfnReplicationGroup.LogDeliveryConfigurationRequestProperty(destination_details=el.CfnReplicationGroup.DestinationDetailsProperty
                                                                                                             (cloud_watch_logs_details=el.CfnReplicationGroup.CloudWatchLogsDestinationDetailsProperty(log_group="redisCluster7")),destination_type="cloudwatch-logs",
                                                                                                             log_format="JSON", log_type="slow-log")])

##                self._replication_groupc=el.CfnReplicationGroup(self, "replicationgroupcID",  replication_group_description= "replication groups for 2 node cluster", automatic_failover_enabled= True, cache_node_type = "cache.t3.small",
##                                                        num_node_groups=3, replication_group_id ="r-70-86", security_group_ids =[scgid], cache_subnet_group_name=sng, cluster_mode= "Enabled", engine="Redis", replicas_per_node_group=2,
##                                                 node_group_configuration =[el.CfnReplicationGroup.NodeGroupConfigurationProperty(node_group_id="7000", primary_availability_zone="us-east-1a", replica_availability_zones=["us-east-1b", "us-east-1a"]),
##                                                                            el.CfnReplicationGroup.NodeGroupConfigurationProperty(node_group_id="6001"),
##                                                                            el.CfnReplicationGroup.NodeGroupConfigurationProperty(node_group_id="5002")],
##                                                 tags=[CfnTag(key="cost", value="redis_cluster")], multi_az_enabled=True, log_delivery_configurations=
##                                                 [el.CfnReplicationGroup.LogDeliveryConfigurationRequestProperty(destination_details=el.CfnReplicationGroup.DestinationDetailsProperty
##                                                                                                             (cloud_watch_logs_details=el.CfnReplicationGroup.CloudWatchLogsDestinationDetailsProperty(log_group="redisCluster7")),destination_type="cloudwatch-logs",
##                                                                                                             log_format="JSON", log_type="slow-log")])




## Removal policy
        self._replication_groupc.apply_removal_policy(RemovalPolicy.DESTROY)









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
