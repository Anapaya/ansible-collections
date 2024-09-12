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

from openapi_client.models.sibling_interface_up import SiblingInterfaceUp

class TestSiblingInterfaceUp(unittest.TestCase):
    """SiblingInterfaceUp unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SiblingInterfaceUp:
        """Test SiblingInterfaceUp
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SiblingInterfaceUp`
        """
        model = SiblingInterfaceUp()
        if include_optional:
            return SiblingInterfaceUp(
                data = openapi_client.models.sibling_interface_up_data.SiblingInterfaceUpData(
                    local_isd_as = '1-ff00:0:110', 
                    local_interface = 56, 
                    internal_address = '', 
                    remote_isd_as = '1-ff00:0:110', 
                    relationship = 'CHILD', 
                    state = 'UP', 
                    bfd_enabled = True, )
            )
        else:
            return SiblingInterfaceUp(
                data = openapi_client.models.sibling_interface_up_data.SiblingInterfaceUpData(
                    local_isd_as = '1-ff00:0:110', 
                    local_interface = 56, 
                    internal_address = '', 
                    remote_isd_as = '1-ff00:0:110', 
                    relationship = 'CHILD', 
                    state = 'UP', 
                    bfd_enabled = True, ),
        )
        """

    def testSiblingInterfaceUp(self):
        """Test SiblingInterfaceUp"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
