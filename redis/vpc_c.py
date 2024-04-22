from aws_cdk import (Stack,IAspect, RemovalPolicy, Aspects, CfnOutput, TreeInspector,CfnParameter)
from constructs import Construct
import  aws_cdk.aws_s3 as s3
import aws_cdk.aws_ec2 as ec2

from aws_cdk.aws_ec2 import Vpc, CfnKeyPair, Instance, InstanceClass, MachineImage
from constructs import Construct, IConstruct

import aws_cdk.aws_iam as iam




class vpconcl(Construct):

    @property
    def vpcconstruct(self):
        return self._vpcconstruct

    @property
    def subnetconstruct1(self):
        return self._subnetconstruct1

    @property
    def subnetconstruct2(self):
        return self._subnetconstruct2

    def __init__(self, scope: Construct, construct_id: str,  **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

 

## VPC definitions
        self._vpcconstruct= ec2.Vpc(self, "vpcconstructid",  availability_zones=["us-east-1a", "us-east-1b" ], create_internet_gateway=False,
                                    subnet_configuration=[ec2.SubnetConfiguration(subnet_type=ec2.SubnetType.PUBLIC, name="public")])

##        self._subnetconstruct1=self._vpcconstruct.isolated_subnets[0]
##        self._subnetconstruct2=self._vpcconstruct.isolated_subnets[1]

        self._subnetconstruct1=self._vpcconstruct.public_subnets[0]
        self._subnetconstruct2=self._vpcconstruct.public_subnets[1]


        

        
##        self._subnetconstruct1= ec2.Subnet(self, "subscontructID1",  availability_zone="us-east-1a", cidr_block="10.1.1.0/27",  vpc_id=self._vpcconstruct.vpc_id, map_public_ip_on_launch= False)
##        self._subnetconstruct2= ec2.Subnet(self, "subscontructID2" , availability_zone="us-east-1b", cidr_block="10.1.1.64/27",  vpc_id=self._vpcconstruct.vpc_id, map_public_ip_on_launch= False)



## Destroy policies        
        self._vpcconstruct.apply_removal_policy(RemovalPolicy.DESTROY)



