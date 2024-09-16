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

from ansible.module_utils.appliance_api_client.models.chain_brief import ChainBrief

class TestChainBrief(unittest.TestCase):
    """ChainBrief unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ChainBrief:
        """Test ChainBrief
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ChainBrief`
        """
        model = ChainBrief()
        if include_optional:
            return ChainBrief(
                id = 'fa53a04a',
                subject = '1-ff00:0:110',
                issuer = '1-ff00:0:110',
                validity = ansible.module_utils.appliance_api_client.models.validity_period.Validity period(
                    not_before = '2021-01-04T09:59:33Z', 
                    not_after = '2022-01-04T09:59:33Z', ),
                chain = '',
                blob = ''
            )
        else:
            return ChainBrief(
                id = 'fa53a04a',
                subject = '1-ff00:0:110',
                issuer = '1-ff00:0:110',
                validity = ansible.module_utils.appliance_api_client.models.validity_period.Validity period(
                    not_before = '2021-01-04T09:59:33Z', 
                    not_after = '2022-01-04T09:59:33Z', ),
        )
        """

    def testChainBrief(self):
        """Test ChainBrief"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
