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

from ansible.module_utils.appliance_api_client.models.announce_filter_matches_prefix_wrapped import AnnounceFilterMatchesPrefixWrapped  # noqa: E501

class TestAnnounceFilterMatchesPrefixWrapped(unittest.TestCase):
    """AnnounceFilterMatchesPrefixWrapped unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AnnounceFilterMatchesPrefixWrapped:
        """Test AnnounceFilterMatchesPrefixWrapped
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AnnounceFilterMatchesPrefixWrapped`
        """
        model = AnnounceFilterMatchesPrefixWrapped()  # noqa: E501
        if include_optional:
            return AnnounceFilterMatchesPrefixWrapped(
                component = 'appliance',
                service_name = ''
            )
        else:
            return AnnounceFilterMatchesPrefixWrapped(
                component = 'appliance',
                service_name = '',
        )
        """

    def testAnnounceFilterMatchesPrefixWrapped(self):
        """Test AnnounceFilterMatchesPrefixWrapped"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
