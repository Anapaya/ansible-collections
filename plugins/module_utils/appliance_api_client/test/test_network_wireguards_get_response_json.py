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

from ansible.module_utils.appliance_api_client.models.network_wireguards_get_response_json import NetworkWireguardsGetResponseJson

class TestNetworkWireguardsGetResponseJson(unittest.TestCase):
    """NetworkWireguardsGetResponseJson unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> NetworkWireguardsGetResponseJson:
        """Test NetworkWireguardsGetResponseJson
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `NetworkWireguardsGetResponseJson`
        """
        model = NetworkWireguardsGetResponseJson()
        if include_optional:
            return NetworkWireguardsGetResponseJson(
                interfaces = [
                    ansible.module_utils.appliance_api_client.models.network_wireguards_interface_get_response_json.NetworkWireguardsInterfaceGetResponseJson(
                        name = 'wg0', 
                        public_key = 'SqLwwTSYHBwQljJDqx7aUVWVDFN6ir6FQL/m3VfmhhQ=', )
                    ]
            )
        else:
            return NetworkWireguardsGetResponseJson(
                interfaces = [
                    ansible.module_utils.appliance_api_client.models.network_wireguards_interface_get_response_json.NetworkWireguardsInterfaceGetResponseJson(
                        name = 'wg0', 
                        public_key = 'SqLwwTSYHBwQljJDqx7aUVWVDFN6ir6FQL/m3VfmhhQ=', )
                    ],
        )
        """

    def testNetworkWireguardsGetResponseJson(self):
        """Test NetworkWireguardsGetResponseJson"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
