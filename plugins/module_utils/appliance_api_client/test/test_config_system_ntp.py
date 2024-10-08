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

from ansible.module_utils.appliance_api_client.models.config_system_ntp import ConfigSystemNtp

class TestConfigSystemNtp(unittest.TestCase):
    """ConfigSystemNtp unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ConfigSystemNtp:
        """Test ConfigSystemNtp
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ConfigSystemNtp`
        """
        model = ConfigSystemNtp()
        if include_optional:
            return ConfigSystemNtp(
                root_distance_max = '5s',
                servers = [
                    ansible.module_utils.appliance_api_client.models.config_system_ntp_servers.Config_System_Ntp_Servers(
                        address = '', )
                    ]
            )
        else:
            return ConfigSystemNtp(
        )
        """

    def testConfigSystemNtp(self):
        """Test ConfigSystemNtp"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
