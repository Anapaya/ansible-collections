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

from ansible.module_utils.appliance_api_client.models.config_interfaces_ethernet_route import ConfigInterfacesEthernetRoute

class TestConfigInterfacesEthernetRoute(unittest.TestCase):
    """ConfigInterfacesEthernetRoute unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ConfigInterfacesEthernetRoute:
        """Test ConfigInterfacesEthernetRoute
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ConfigInterfacesEthernetRoute`
        """
        model = ConfigInterfacesEthernetRoute()
        if include_optional:
            return ConfigInterfacesEthernetRoute(
                comment = '',
                var_from = '',
                metric = 56,
                sequence_id = 3,
                to = '',
                via = ''
            )
        else:
            return ConfigInterfacesEthernetRoute(
                sequence_id = 3,
                to = '',
                via = '',
        )
        """

    def testConfigInterfacesEthernetRoute(self):
        """Test ConfigInterfacesEthernetRoute"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
