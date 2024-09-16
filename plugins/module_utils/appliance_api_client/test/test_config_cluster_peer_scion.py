# coding: utf-8

"""
    Appliance Management API

    Management API for the Anapaya EDGE, CORE and GATE appliances

    The version of the OpenAPI document: v0.37.1
    Contact: ops@anapaya.net
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from ansible.module_utils.appliance_api_client.models.config_cluster_peer_scion import ConfigClusterPeerScion  # noqa: E501

class TestConfigClusterPeerScion(unittest.TestCase):
    """ConfigClusterPeerScion unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ConfigClusterPeerScion:
        """Test ConfigClusterPeerScion
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ConfigClusterPeerScion`
        """
        model = ConfigClusterPeerScion()  # noqa: E501
        if include_optional:
            return ConfigClusterPeerScion(
                ases = [
                    ansible.module_utils.appliance_api_client.models.config_cluster_peer_scion_as.Config_Cluster_Peer_Scion_AS(
                        control = ansible.module_utils.appliance_api_client.models.config_cluster_peer_scion_as_control.Config_Cluster_Peer_Scion_AS_Control(
                            address = '192.168.1.1:30100', ), 
                        isd_as = '1-ff00:0:110', 
                        neighbors = [
                            ansible.module_utils.appliance_api_client.models.config_cluster_peer_scion_as_neighbor.Config_Cluster_Peer_Scion_AS_Neighbor(
                                interfaces = [
                                    ansible.module_utils.appliance_api_client.models.config_cluster_peer_scion_as_neighbor_interface.Config_Cluster_Peer_Scion_AS_Neighbor_Interface(
                                        interface_id = 1, 
                                        next_hop = '169.254.0.1:30100', 
                                        scion_mtu = 1472, )
                                    ], 
                                neighbor_isd_as = '2-ff00:0:210', 
                                relationship = 'CORE', )
                            ], 
                        shard_id = 56, )
                    ]
            )
        else:
            return ConfigClusterPeerScion(
        )
        """

    def testConfigClusterPeerScion(self):
        """Test ConfigClusterPeerScion"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
