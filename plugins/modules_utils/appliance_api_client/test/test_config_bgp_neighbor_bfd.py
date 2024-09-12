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

from openapi_client.models.config_bgp_neighbor_bfd import ConfigBgpNeighborBfd

class TestConfigBgpNeighborBfd(unittest.TestCase):
    """ConfigBgpNeighborBfd unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ConfigBgpNeighborBfd:
        """Test ConfigBgpNeighborBfd
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ConfigBgpNeighborBfd`
        """
        model = ConfigBgpNeighborBfd()
        if include_optional:
            return ConfigBgpNeighborBfd(
                desired_minimum_tx_interval = 10,
                detection_multiplier = 2,
                enabled = True,
                local_address = '',
                minimum_ttl = 1,
                multihop = True,
                required_minimum_receive = 10
            )
        else:
            return ConfigBgpNeighborBfd(
        )
        """

    def testConfigBgpNeighborBfd(self):
        """Test ConfigBgpNeighborBfd"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
