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

from ansible.module_utils.appliance_api_client.models.network_physical_interfaces_get_response_json import NetworkPhysicalInterfacesGetResponseJson

class TestNetworkPhysicalInterfacesGetResponseJson(unittest.TestCase):
    """NetworkPhysicalInterfacesGetResponseJson unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> NetworkPhysicalInterfacesGetResponseJson:
        """Test NetworkPhysicalInterfacesGetResponseJson
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `NetworkPhysicalInterfacesGetResponseJson`
        """
        model = NetworkPhysicalInterfacesGetResponseJson()
        if include_optional:
            return NetworkPhysicalInterfacesGetResponseJson(
                interfaces = [
                    ansible.module_utils.appliance_api_client.models.physical_interface.PhysicalInterface(
                        name = 'eth0', 
                        pcie_bdf = '0000:00:1f.0', 
                        uuid = '0022481C-3BE5-0022-481C-3BE50022481C', 
                        driver = 'vfio-pci', 
                        num_vfs = 0, )
                    ]
            )
        else:
            return NetworkPhysicalInterfacesGetResponseJson(
                interfaces = [
                    ansible.module_utils.appliance_api_client.models.physical_interface.PhysicalInterface(
                        name = 'eth0', 
                        pcie_bdf = '0000:00:1f.0', 
                        uuid = '0022481C-3BE5-0022-481C-3BE50022481C', 
                        driver = 'vfio-pci', 
                        num_vfs = 0, )
                    ],
        )
        """

    def testNetworkPhysicalInterfacesGetResponseJson(self):
        """Test NetworkPhysicalInterfacesGetResponseJson"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
