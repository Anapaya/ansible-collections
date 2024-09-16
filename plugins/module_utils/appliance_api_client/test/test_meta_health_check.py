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

from ansible.module_utils.appliance_api_client.models.meta_health_check import MetaHealthCheck  # noqa: E501

class TestMetaHealthCheck(unittest.TestCase):
    """MetaHealthCheck unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MetaHealthCheck:
        """Test MetaHealthCheck
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MetaHealthCheck`
        """
        model = MetaHealthCheck()  # noqa: E501
        if include_optional:
            return MetaHealthCheck(
                component = 'appliance',
                service_name = ''
            )
        else:
            return MetaHealthCheck(
                component = 'appliance',
                service_name = '',
        )
        """

    def testMetaHealthCheck(self):
        """Test MetaHealthCheck"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
