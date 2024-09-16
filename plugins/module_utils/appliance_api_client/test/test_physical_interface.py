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

from ansible.module_utils.appliance_api_client.models.physical_interface import PhysicalInterface  # noqa: E501

class TestPhysicalInterface(unittest.TestCase):
    """PhysicalInterface unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PhysicalInterface:
        """Test PhysicalInterface
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PhysicalInterface`
        """
        model = PhysicalInterface()  # noqa: E501
        if include_optional:
            return PhysicalInterface(
                name = 'eth0',
                pcie_bdf = '0000:00:1f.0',
                uuid = '0022481C-3BE5-0022-481C-3BE50022481C',
                driver = 'vfio-pci',
                num_vfs = 0
            )
        else:
            return PhysicalInterface(
                name = 'eth0',
                driver = 'vfio-pci',
                num_vfs = 0,
        )
        """

    def testPhysicalInterface(self):
        """Test PhysicalInterface"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
