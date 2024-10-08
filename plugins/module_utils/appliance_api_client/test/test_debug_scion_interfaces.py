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

from ansible.module_utils.appliance_api_client.models.debug_scion_interfaces import DebugScionInterfaces

class TestDebugScionInterfaces(unittest.TestCase):
    """DebugScionInterfaces unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DebugScionInterfaces:
        """Test DebugScionInterfaces
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DebugScionInterfaces`
        """
        model = DebugScionInterfaces()
        if include_optional:
            return DebugScionInterfaces(
                interfaces = [
                    ansible.module_utils.appliance_api_client.models.debug_scion_interface.DebugScionInterface(
                        local = ansible.module_utils.appliance_api_client.models.scion_interface_endpoint.ScionInterfaceEndpoint(
                            isd_as = '1-ff00:0:110', 
                            address = '', 
                            interface_id = 56, ), 
                        remote = ansible.module_utils.appliance_api_client.models.scion_interface_endpoint.ScionInterfaceEndpoint(
                            isd_as = '1-ff00:0:110', 
                            address = '', 
                            interface_id = 56, ), 
                        relationship = 'CHILD', 
                        mtu = 56, 
                        state = 'UP', )
                    ],
                sibling_interfaces = [
                    ansible.module_utils.appliance_api_client.models.debug_scion_sibling_interface.DebugScionSiblingInterface(
                        mtu = 56, 
                        relationship = 'CHILD', 
                        remote_isd_as = '1-ff00:0:110', 
                        local_isd_as = '1-ff00:0:110', 
                        local_interface_id = 56, 
                        next_hop_address = '', )
                    ]
            )
        else:
            return DebugScionInterfaces(
                interfaces = [
                    ansible.module_utils.appliance_api_client.models.debug_scion_interface.DebugScionInterface(
                        local = ansible.module_utils.appliance_api_client.models.scion_interface_endpoint.ScionInterfaceEndpoint(
                            isd_as = '1-ff00:0:110', 
                            address = '', 
                            interface_id = 56, ), 
                        remote = ansible.module_utils.appliance_api_client.models.scion_interface_endpoint.ScionInterfaceEndpoint(
                            isd_as = '1-ff00:0:110', 
                            address = '', 
                            interface_id = 56, ), 
                        relationship = 'CHILD', 
                        mtu = 56, 
                        state = 'UP', )
                    ],
                sibling_interfaces = [
                    ansible.module_utils.appliance_api_client.models.debug_scion_sibling_interface.DebugScionSiblingInterface(
                        mtu = 56, 
                        relationship = 'CHILD', 
                        remote_isd_as = '1-ff00:0:110', 
                        local_isd_as = '1-ff00:0:110', 
                        local_interface_id = 56, 
                        next_hop_address = '', )
                    ],
        )
        """

    def testDebugScionInterfaces(self):
        """Test DebugScionInterfaces"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
