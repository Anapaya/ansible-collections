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

from ansible.module_utils.appliance_api_client.models.config_interfaces_bond_neighbor import ConfigInterfacesBondNeighbor  # noqa: E501

class TestConfigInterfacesBondNeighbor(unittest.TestCase):
    """ConfigInterfacesBondNeighbor unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ConfigInterfacesBondNeighbor:
        """Test ConfigInterfacesBondNeighbor
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ConfigInterfacesBondNeighbor`
        """
        model = ConfigInterfacesBondNeighbor()  # noqa: E501
        if include_optional:
            return ConfigInterfacesBondNeighbor(
                address = '',
                comment = '',
                mac = '',
                sequence_id = 3
            )
        else:
            return ConfigInterfacesBondNeighbor(
                address = '',
                sequence_id = 3,
        )
        """

    def testConfigInterfacesBondNeighbor(self):
        """Test ConfigInterfacesBondNeighbor"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
