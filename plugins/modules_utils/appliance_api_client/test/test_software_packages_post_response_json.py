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

from openapi_client.models.software_packages_post_response_json import SoftwarePackagesPostResponseJson

class TestSoftwarePackagesPostResponseJson(unittest.TestCase):
    """SoftwarePackagesPostResponseJson unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SoftwarePackagesPostResponseJson:
        """Test SoftwarePackagesPostResponseJson
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SoftwarePackagesPostResponseJson`
        """
        model = SoftwarePackagesPostResponseJson()
        if include_optional:
            return SoftwarePackagesPostResponseJson(
                package = openapi_client.models.package_information.Package information(
                    version = 'v0.25.12', 
                    url = 'https://localhost:42000/api/v1/software/scion/packages/local/v0.25.12', )
            )
        else:
            return SoftwarePackagesPostResponseJson(
                package = openapi_client.models.package_information.Package information(
                    version = 'v0.25.12', 
                    url = 'https://localhost:42000/api/v1/software/scion/packages/local/v0.25.12', ),
        )
        """

    def testSoftwarePackagesPostResponseJson(self):
        """Test SoftwarePackagesPostResponseJson"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
