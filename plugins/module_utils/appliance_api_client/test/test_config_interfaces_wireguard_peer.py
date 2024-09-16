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

from ansible.module_utils.appliance_api_client.models.config_interfaces_wireguard_peer import ConfigInterfacesWireguardPeer

class TestConfigInterfacesWireguardPeer(unittest.TestCase):
    """ConfigInterfacesWireguardPeer unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ConfigInterfacesWireguardPeer:
        """Test ConfigInterfacesWireguardPeer
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ConfigInterfacesWireguardPeer`
        """
        model = ConfigInterfacesWireguardPeer()
        if include_optional:
            return ConfigInterfacesWireguardPeer(
                allowed_ips = [
                    ''
                    ],
                endpoint = '',
                public_key = ''
            )
        else:
            return ConfigInterfacesWireguardPeer(
                endpoint = '',
                public_key = '',
        )
        """

    def testConfigInterfacesWireguardPeer(self):
        """Test ConfigInterfacesWireguardPeer"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
