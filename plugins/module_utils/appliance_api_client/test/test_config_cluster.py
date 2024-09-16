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

from ansible.module_utils.appliance_api_client.models.config_cluster import ConfigCluster

class TestConfigCluster(unittest.TestCase):
    """ConfigCluster unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ConfigCluster:
        """Test ConfigCluster
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ConfigCluster`
        """
        model = ConfigCluster()
        if include_optional:
            return ConfigCluster(
                features = ansible.module_utils.appliance_api_client.models.config_cluster_features.Config_Cluster_Features(
                    scion_rss = True, ),
                peers = [
                    ansible.module_utils.appliance_api_client.models.config_cluster_peer.Config_Cluster_Peer(
                        description = '', 
                        features = ansible.module_utils.appliance_api_client.models.config_cluster_peer_features.Config_Cluster_Peer_Features(
                            scion_rss = True, ), 
                        name = '', 
                        scion = ansible.module_utils.appliance_api_client.models.config_cluster_peer_scion.Config_Cluster_Peer_Scion(
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
                                ], ), 
                        scion_tunneling = ansible.module_utils.appliance_api_client.models.config_cluster_peer_scion_tunneling.Config_Cluster_Peer_ScionTunneling(
                            endpoint = ansible.module_utils.appliance_api_client.models.config_cluster_peer_scion_tunneling_endpoint.Config_Cluster_Peer_ScionTunneling_Endpoint(
                                allowed_interfaces = [
                                    ansible.module_utils.appliance_api_client.models.config_cluster_peer_scion_tunneling_endpoint_allowed_interfaces.Config_Cluster_Peer_ScionTunneling_Endpoint_AllowedInterfaces(
                                        isd_as = '', )
                                    ], 
                                control_port = 40201, 
                                data_port = 40200, 
                                disable_auto_allowed_interfaces = True, 
                                ip = '192.168.1.100', 
                                probe_port = 40202, ), ), 
                        synchronization = ansible.module_utils.appliance_api_client.models.config_cluster_peer_synchronization.Config_Cluster_Peer_Synchronization(
                            address = '192.168.1.1:30100', ), )
                    ],
                synchronization = ansible.module_utils.appliance_api_client.models.config_cluster_synchronization.Config_Cluster_Synchronization(
                    address = '192.0.2.3:40000', 
                    node_synchronization_interval = '1m', )
            )
        else:
            return ConfigCluster(
        )
        """

    def testConfigCluster(self):
        """Test ConfigCluster"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
