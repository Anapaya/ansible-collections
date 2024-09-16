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

from ansible.module_utils.appliance_api_client.models.config_management_ssh import ConfigManagementSsh

class TestConfigManagementSsh(unittest.TestCase):
    """ConfigManagementSsh unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ConfigManagementSsh:
        """Test ConfigManagementSsh
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ConfigManagementSsh`
        """
        model = ConfigManagementSsh()
        if include_optional:
            return ConfigManagementSsh(
                enable_password_login = True,
                users = [
                    ansible.module_utils.appliance_api_client.models.config_management_ssh_user.Config_Management_Ssh_User(
                        ssh_keys = [
                            ansible.module_utils.appliance_api_client.models.config_management_ssh_user_ssh_key.Config_Management_Ssh_User_SshKey(
                                description = '', 
                                key = 'ssh-rsa AAAAB3NzaC1yc2', )
                            ], 
                        username = 'anapaya', )
                    ]
            )
        else:
            return ConfigManagementSsh(
        )
        """

    def testConfigManagementSsh(self):
        """Test ConfigManagementSsh"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
