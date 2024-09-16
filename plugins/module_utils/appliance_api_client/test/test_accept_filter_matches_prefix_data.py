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

from ansible.module_utils.appliance_api_client.models.accept_filter_matches_prefix_data import AcceptFilterMatchesPrefixData  # noqa: E501

class TestAcceptFilterMatchesPrefixData(unittest.TestCase):
    """AcceptFilterMatchesPrefixData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AcceptFilterMatchesPrefixData:
        """Test AcceptFilterMatchesPrefixData
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AcceptFilterMatchesPrefixData`
        """
        model = AcceptFilterMatchesPrefixData()  # noqa: E501
        if include_optional:
            return AcceptFilterMatchesPrefixData(
                domain = '',
                prefixes = [
                    ''
                    ],
                count = 56
            )
        else:
            return AcceptFilterMatchesPrefixData(
                domain = '',
                prefixes = [
                    ''
                    ],
                count = 56,
        )
        """

    def testAcceptFilterMatchesPrefixData(self):
        """Test AcceptFilterMatchesPrefixData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
