# coding: utf-8

"""
    Appliance Management API

    Management API for the Anapaya EDGE, CORE and GATE appliances

    The version of the OpenAPI document: 0.1.0
    Contact: ops@anapaya.net
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from openapi_client.models.config_cluster_peer_scion_as import ConfigClusterPeerScionAS

class TestConfigClusterPeerScionAS(unittest.TestCase):
    """ConfigClusterPeerScionAS unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ConfigClusterPeerScionAS:
        """Test ConfigClusterPeerScionAS
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ConfigClusterPeerScionAS`
        """
        model = ConfigClusterPeerScionAS()
        if include_optional:
            return ConfigClusterPeerScionAS(
                control = openapi_client.models.config_cluster_peer_scion_as_control.Config_Cluster_Peer_Scion_AS_Control(
                    address = '192.168.1.1:30100', ),
                isd_as = '1-ff00:0:110',
                neighbors = [
                    openapi_client.models.config_cluster_peer_scion_as_neighbor.Config_Cluster_Peer_Scion_AS_Neighbor(
                        interfaces = [
                            openapi_client.models.config_cluster_peer_scion_as_neighbor_interface.Config_Cluster_Peer_Scion_AS_Neighbor_Interface(
                                interface_id = 1, 
                                next_hop = '169.254.0.1:30100', 
                                scion_mtu = 1472, )
                            ], 
                        neighbor_isd_as = '2-ff00:0:210', 
                        relationship = 'CORE', )
                    ],
                shard_id = 56
            )
        else:
            return ConfigClusterPeerScionAS(
                isd_as = '1-ff00:0:110',
        )
        """

    def testConfigClusterPeerScionAS(self):
        """Test ConfigClusterPeerScionAS"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
