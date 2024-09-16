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

from ansible.module_utils.appliance_api_client.models.config_management_api import ConfigManagementApi  # noqa: E501

class TestConfigManagementApi(unittest.TestCase):
    """ConfigManagementApi unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ConfigManagementApi:
        """Test ConfigManagementApi
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ConfigManagementApi`
        """
        model = ConfigManagementApi()  # noqa: E501
        if include_optional:
            return ConfigManagementApi(
                basic_auth = ansible.module_utils.appliance_api_client.models.config_management_api_basic_auth.Config_Management_Api_BasicAuth(
                    enabled = True, 
                    users = [
                        ansible.module_utils.appliance_api_client.models.config_management_api_basic_auth_user.Config_Management_Api_BasicAuth_User(
                            password_hashed = '$2y$10$QNodxwKFABMWu4XlFPmZDOSfqxrsqNvrSn487lCi7tJ/4nTsT/f02', 
                            username = 'admin', )
                        ], ),
                listeners = [
                    ansible.module_utils.appliance_api_client.models.config_management_api_listener.Config_Management_Api_Listener(
                        address = '127.0.0.1:443', 
                        description = '', )
                    ],
                oauth = ansible.module_utils.appliance_api_client.models.config_management_api_oauth.Config_Management_Api_Oauth(
                    enabled = True, 
                    identity_providers = [
                        ansible.module_utils.appliance_api_client.models.config_management_api_oauth_identity_provider.Config_Management_Api_Oauth_IdentityProvider(
                            base_auth_url = 'https://anapaya.eu.auth0.com/', 
                            client_id = '', 
                            client_secret = '', 
                            id = '', 
                            metadata_url = 'https://anapaya.eu.auth0.com/.well-known/openid-configuration', 
                            tenant_id = '', 
                            type = 'GENERIC', )
                        ], 
                    roles = [
                        ansible.module_utils.appliance_api_client.models.config_management_api_oauth_role.Config_Management_Api_Oauth_Role(
                            aliases = [
                                ''
                                ], 
                            role = '', )
                        ], 
                    token_verification_keys = [
                        ansible.module_utils.appliance_api_client.models.config_management_api_oauth_token_verification_key.Config_Management_Api_Oauth_TokenVerificationKey(
                            id = 'anapaya.auth0', 
                            jwks_url = 'https://anapaya.eu.auth0.com/.well-known/jwks.json', )
                        ], ),
                unprotected = True
            )
        else:
            return ConfigManagementApi(
        )
        """

    def testConfigManagementApi(self):
        """Test ConfigManagementApi"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
