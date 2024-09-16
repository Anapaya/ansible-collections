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

from ansible.module_utils.appliance_api_client.models.domain_traffic_policy_has_paths_wrapped import DomainTrafficPolicyHasPathsWrapped  # noqa: E501

class TestDomainTrafficPolicyHasPathsWrapped(unittest.TestCase):
    """DomainTrafficPolicyHasPathsWrapped unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DomainTrafficPolicyHasPathsWrapped:
        """Test DomainTrafficPolicyHasPathsWrapped
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DomainTrafficPolicyHasPathsWrapped`
        """
        model = DomainTrafficPolicyHasPathsWrapped()  # noqa: E501
        if include_optional:
            return DomainTrafficPolicyHasPathsWrapped(
                component = 'appliance',
                service_name = ''
            )
        else:
            return DomainTrafficPolicyHasPathsWrapped(
                component = 'appliance',
                service_name = '',
        )
        """

    def testDomainTrafficPolicyHasPathsWrapped(self):
        """Test DomainTrafficPolicyHasPathsWrapped"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
