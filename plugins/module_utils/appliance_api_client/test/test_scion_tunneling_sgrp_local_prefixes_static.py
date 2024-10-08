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

from ansible.module_utils.appliance_api_client.models.scion_tunneling_sgrp_local_prefixes_static import ScionTunnelingSGRPLocalPrefixesStatic

class TestScionTunnelingSGRPLocalPrefixesStatic(unittest.TestCase):
    """ScionTunnelingSGRPLocalPrefixesStatic unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ScionTunnelingSGRPLocalPrefixesStatic:
        """Test ScionTunnelingSGRPLocalPrefixesStatic
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ScionTunnelingSGRPLocalPrefixesStatic`
        """
        model = ScionTunnelingSGRPLocalPrefixesStatic()
        if include_optional:
            return ScionTunnelingSGRPLocalPrefixesStatic(
                prefixes = [
                    ''
                    ]
            )
        else:
            return ScionTunnelingSGRPLocalPrefixesStatic(
                prefixes = [
                    ''
                    ],
        )
        """

    def testScionTunnelingSGRPLocalPrefixesStatic(self):
        """Test ScionTunnelingSGRPLocalPrefixesStatic"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
