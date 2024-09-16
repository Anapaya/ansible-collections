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

from ansible.module_utils.appliance_api_client.models.config_management_api_oauth_role import ConfigManagementApiOauthRole

class TestConfigManagementApiOauthRole(unittest.TestCase):
    """ConfigManagementApiOauthRole unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ConfigManagementApiOauthRole:
        """Test ConfigManagementApiOauthRole
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ConfigManagementApiOauthRole`
        """
        model = ConfigManagementApiOauthRole()
        if include_optional:
            return ConfigManagementApiOauthRole(
                aliases = [
                    ''
                    ],
                role = ''
            )
        else:
            return ConfigManagementApiOauthRole(
        )
        """

    def testConfigManagementApiOauthRole(self):
        """Test ConfigManagementApiOauthRole"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
