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

from ansible.module_utils.appliance_api_client.models.config_scion_tunneling_endpoint import ConfigScionTunnelingEndpoint

class TestConfigScionTunnelingEndpoint(unittest.TestCase):
    """ConfigScionTunnelingEndpoint unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ConfigScionTunnelingEndpoint:
        """Test ConfigScionTunnelingEndpoint
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ConfigScionTunnelingEndpoint`
        """
        model = ConfigScionTunnelingEndpoint()
        if include_optional:
            return ConfigScionTunnelingEndpoint(
                allowed_interfaces = [
                    ansible.module_utils.appliance_api_client.models.config_scion_tunneling_endpoint_allowed_interfaces.Config_ScionTunneling_Endpoint_AllowedInterfaces(
                        interfaces = [2,3], 
                        isd_as = '', )
                    ],
                control_port = 40201,
                data_port = 40200,
                description = '',
                disable_auto_allowed_interfaces = True,
                disable_urpf = True,
                enable_scion_rss = True,
                enabled = True,
                ip = '192.168.1.100',
                probe_port = 40202
            )
        else:
            return ConfigScionTunnelingEndpoint(
        )
        """

    def testConfigScionTunnelingEndpoint(self):
        """Test ConfigScionTunnelingEndpoint"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
