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

from openapi_client.models.config_interfaces_ethernet import ConfigInterfacesEthernet

class TestConfigInterfacesEthernet(unittest.TestCase):
    """ConfigInterfacesEthernet unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ConfigInterfacesEthernet:
        """Test ConfigInterfacesEthernet
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ConfigInterfacesEthernet`
        """
        model = ConfigInterfacesEthernet()
        if include_optional:
            return ConfigInterfacesEthernet(
                accept_ra = True,
                addresses = [
                    ''
                    ],
                driver = 'LINUX',
                gateway = openapi_client.models.config_interfaces_ethernet_gateway.Config_Interfaces_Ethernet_Gateway(
                    ipv4_gateway = '', 
                    ipv6_gateway = '', ),
                mac = '',
                mtu = 1472,
                name = '',
                neighbors = [
                    openapi_client.models.config_interfaces_ethernet_neighbor.Config_Interfaces_Ethernet_Neighbor(
                        address = '', 
                        comment = '', 
                        mac = '', 
                        sequence_id = 3, )
                    ],
                routes = [
                    openapi_client.models.config_interfaces_ethernet_route.Config_Interfaces_Ethernet_Route(
                        comment = '', 
                        from = '', 
                        metric = 56, 
                        sequence_id = 3, 
                        to = '', 
                        via = '', )
                    ],
                rx_queue_size = 2048,
                tx_queue_size = 2048,
                vpp = openapi_client.models.config_interfaces_ethernet_vpp.Config_Interfaces_Ethernet_Vpp(
                    vlan_strip_offload = True, ),
                vrrp = [
                    openapi_client.models.config_interfaces_ethernet_vrrp.Config_Interfaces_Ethernet_Vrrp(
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
            return ConfigInterfacesEthernet(
                name = '',
        )
        """

    def testConfigInterfacesEthernet(self):
        """Test ConfigInterfacesEthernet"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
