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

from ansible.module_utils.appliance_api_client.models.scion_tunneling_sgrp_local_prefixes_json import ScionTunnelingSGRPLocalPrefixesJSON

class TestScionTunnelingSGRPLocalPrefixesJSON(unittest.TestCase):
    """ScionTunnelingSGRPLocalPrefixesJSON unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ScionTunnelingSGRPLocalPrefixesJSON:
        """Test ScionTunnelingSGRPLocalPrefixesJSON
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ScionTunnelingSGRPLocalPrefixesJSON`
        """
        model = ScionTunnelingSGRPLocalPrefixesJSON()
        if include_optional:
            return ScionTunnelingSGRPLocalPrefixesJSON(
                local_prefixes = ansible.module_utils.appliance_api_client.models.scion_tunneling_sgrp_local_prefixes.ScionTunnelingSGRPLocalPrefixes(
                    static = ansible.module_utils.appliance_api_client.models.scion_tunneling_sgrp_local_prefixes_static.ScionTunnelingSGRPLocalPrefixesStatic(
                        prefixes = [
                            ''
                            ], ), 
                    static_probed = [
                        ansible.module_utils.appliance_api_client.models.scion_tunneling_sgrp_local_prefixes_static_probed.ScionTunnelingSGRPLocalPrefixesStaticProbed(
                            next_hop = '', 
                            reachable = True, 
                            last_success = '', 
                            prefixes = [
                                ''
                                ], 
                            error = '', )
                        ], 
                    bgp = ansible.module_utils.appliance_api_client.models.scion_tunneling_sgrp_local_prefixes_bgp.ScionTunnelingSGRPLocalPrefixesBGP(
                        prefixes = , ), )
            )
        else:
            return ScionTunnelingSGRPLocalPrefixesJSON(
                local_prefixes = ansible.module_utils.appliance_api_client.models.scion_tunneling_sgrp_local_prefixes.ScionTunnelingSGRPLocalPrefixes(
                    static = ansible.module_utils.appliance_api_client.models.scion_tunneling_sgrp_local_prefixes_static.ScionTunnelingSGRPLocalPrefixesStatic(
                        prefixes = [
                            ''
                            ], ), 
                    static_probed = [
                        ansible.module_utils.appliance_api_client.models.scion_tunneling_sgrp_local_prefixes_static_probed.ScionTunnelingSGRPLocalPrefixesStaticProbed(
                            next_hop = '', 
                            reachable = True, 
                            last_success = '', 
                            prefixes = [
                                ''
                                ], 
                            error = '', )
                        ], 
                    bgp = ansible.module_utils.appliance_api_client.models.scion_tunneling_sgrp_local_prefixes_bgp.ScionTunnelingSGRPLocalPrefixesBGP(
                        prefixes = , ), ),
        )
        """

    def testScionTunnelingSGRPLocalPrefixesJSON(self):
        """Test ScionTunnelingSGRPLocalPrefixesJSON"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
