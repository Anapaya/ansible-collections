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

from ansible.module_utils.appliance_api_client.models.config_management_remote_repository_cloudsmith import ConfigManagementRemoteRepositoryCloudsmith

class TestConfigManagementRemoteRepositoryCloudsmith(unittest.TestCase):
    """ConfigManagementRemoteRepositoryCloudsmith unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ConfigManagementRemoteRepositoryCloudsmith:
        """Test ConfigManagementRemoteRepositoryCloudsmith
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ConfigManagementRemoteRepositoryCloudsmith`
        """
        model = ConfigManagementRemoteRepositoryCloudsmith()
        if include_optional:
            return ConfigManagementRemoteRepositoryCloudsmith(
                access_token = 'APIKEY#ENTITLEMENTTOKEN',
                url = 'https://cloudsmith.io/anapaya/repos/external'
            )
        else:
            return ConfigManagementRemoteRepositoryCloudsmith(
        )
        """

    def testConfigManagementRemoteRepositoryCloudsmith(self):
        """Test ConfigManagementRemoteRepositoryCloudsmith"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
