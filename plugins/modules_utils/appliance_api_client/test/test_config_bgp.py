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

from openapi_client.models.config_bgp import ConfigBgp

class TestConfigBgp(unittest.TestCase):
    """ConfigBgp unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ConfigBgp:
        """Test ConfigBgp
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ConfigBgp`
        """
        model = ConfigBgp()
        if include_optional:
            return ConfigBgp(
                var_global = openapi_client.models.config_bgp_global.Config_Bgp_Global(
                    as = 56, 
                    networks = [
                        ''
                        ], 
                    router_id = '', 
                    src_address = '', ),
                neighbors = [
                    openapi_client.models.config_bgp_neighbor.Config_Bgp_Neighbor(
                        auth_password = '', 
                        bfd = openapi_client.models.config_bgp_neighbor_bfd.Config_Bgp_Neighbor_Bfd(
                            desired_minimum_tx_interval = 10, 
                            detection_multiplier = 2, 
                            enabled = True, 
                            local_address = '', 
                            minimum_ttl = 1, 
                            multihop = True, 
                            required_minimum_receive = 10, ), 
                        description = '', 
                        ebgp_multihop = 56, 
                        enabled = True, 
                        local_as = 56, 
                        neighbor_address = '', 
                        peer_as = 56, 
                        timers = openapi_client.models.config_bgp_neighbor_timers.Config_Bgp_Neighbor_Timers(
                            connect_retry = 56, 
                            hold_time = 56, 
                            keepalive_interval = 56, 
                            minimum_advertisement_interval = 56, ), 
                        transport = openapi_client.models.config_bgp_neighbor_transport.Config_Bgp_Neighbor_Transport(
                            local_address = '', ), 
                        ttl_security = 56, )
                    ]
            )
        else:
            return ConfigBgp(
        )
        """

    def testConfigBgp(self):
        """Test ConfigBgp"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
