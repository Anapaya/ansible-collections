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

from ansible.module_utils.appliance_api_client.models.config_interfaces_loopback import ConfigInterfacesLoopback

class TestConfigInterfacesLoopback(unittest.TestCase):
    """ConfigInterfacesLoopback unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ConfigInterfacesLoopback:
        """Test ConfigInterfacesLoopback
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ConfigInterfacesLoopback`
        """
        model = ConfigInterfacesLoopback()
        if include_optional:
            return ConfigInterfacesLoopback(
                addresses = [
                    ''
                    ],
                name = ''
            )
        else:
            return ConfigInterfacesLoopback(
                name = '',
        )
        """

    def testConfigInterfacesLoopback(self):
        """Test ConfigInterfacesLoopback"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
