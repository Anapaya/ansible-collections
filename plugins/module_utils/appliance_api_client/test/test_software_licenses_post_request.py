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

from ansible.module_utils.appliance_api_client.models.software_licenses_post_request import SoftwareLicensesPostRequest  # noqa: E501

class TestSoftwareLicensesPostRequest(unittest.TestCase):
    """SoftwareLicensesPostRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SoftwareLicensesPostRequest:
        """Test SoftwareLicensesPostRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SoftwareLicensesPostRequest`
        """
        model = SoftwareLicensesPostRequest()  # noqa: E501
        if include_optional:
            return SoftwareLicensesPostRequest(
                license = 'eyJ0eXAzI1NiJ9.yJpc3MiOiJqb2U.B92K27uhbUJU1p'
            )
        else:
            return SoftwareLicensesPostRequest(
                license = 'eyJ0eXAzI1NiJ9.yJpc3MiOiJqb2U.B92K27uhbUJU1p',
        )
        """

    def testSoftwareLicensesPostRequest(self):
        """Test SoftwareLicensesPostRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
