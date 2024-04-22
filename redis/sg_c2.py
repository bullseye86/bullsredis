from aws_cdk import (Stack,IAspect, RemovalPolicy, Aspects, CfnOutput, TreeInspector,CfnParameter)
from constructs import Construct
import aws_cdk.aws_ec2 as ec2
from .vpc_c import vpconcl
from aws_cdk.aws_ec2 import Vpc, CfnKeyPair, Instance, InstanceClass, MachineImage
from constructs import Construct, IConstruct
import requests








class sgoncl2(Construct):

    @property
    def sgconstruct(self):
        return self._sgconstruct5

    @property
    def sgconstruct2(self):
        return self._sgconstruct



    def __init__(self, scope: Construct, construct_id: str, vpc23, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        
        response = requests.get('https://api.ipify.org').text
        cfpubip=CfnParameter(self, "cfpubip", default=response)


        
## Security Group definitions
        self._sgconstruct = ec2.SecurityGroup(self, "iBSg2", vpc=vpc23, security_group_name="iBSg2name")
        self._sgconstruct.add_ingress_rule(ec2.Peer.ipv4(cfpubip.value_as_string+'/32'), ec2.Port.tcp(22))
        self._sgconstruct.add_ingress_rule(ec2.Peer.any_ipv4(), ec2.Port.all_tcp())
        self._sgconstruct.add_ingress_rule(ec2.Peer.any_ipv4(), ec2.Port.tcp(6379))

        self._sgconstruct5=self._sgconstruct.security_group_id

        
        self._sgconstruct1=ec2.SecurityGroup.from_security_group_id(self, "ibsgid7", self._sgconstruct5)
        






## Destroy policies   
        self._sgconstruct.apply_removal_policy(RemovalPolicy.DESTROY)







