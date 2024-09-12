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

from openapi_client.models.config_interfaces_bond import ConfigInterfacesBond

class TestConfigInterfacesBond(unittest.TestCase):
    """ConfigInterfacesBond unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ConfigInterfacesBond:
        """Test ConfigInterfacesBond
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ConfigInterfacesBond`
        """
        model = ConfigInterfacesBond()
        if include_optional:
            return ConfigInterfacesBond(
                accept_ra = True,
                addresses = [
                    ''
                    ],
                gateway = openapi_client.models.config_interfaces_bond_gateway.Config_Interfaces_Bond_Gateway(
                    ipv4_gateway = '', 
                    ipv6_gateway = '', ),
                interfaces = [
                    ''
                    ],
                mac = '',
                mtu = 1472,
                name = '',
                neighbors = [
                    openapi_client.models.config_interfaces_bond_neighbor.Config_Interfaces_Bond_Neighbor(
                        address = '', 
                        comment = '', 
                        mac = '', 
                        sequence_id = 3, )
                    ],
                routes = [
                    openapi_client.models.config_interfaces_bond_route.Config_Interfaces_Bond_Route(
                        comment = '', 
                        from = '', 
                        metric = 56, 
                        sequence_id = 3, 
                        to = '', 
                        via = '', )
                    ],
                rx_queue_size = 2048,
                tx_queue_size = 2048,
                vrrp = [
                    openapi_client.models.config_interfaces_bond_vrrp.Config_Interfaces_Bond_Vrrp(
                        addresses = [
                            ''
                            ], 
                        no_preempt = True, 
                        peers = [
                            ''
                            ], 
                        priority = 17, 
                        vrid = 3, )
                    ]
            )
        else:
            return ConfigInterfacesBond(
                interfaces = [
                    ''
                    ],
                name = '',
        )
        """

    def testConfigInterfacesBond(self):
        """Test ConfigInterfacesBond"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
