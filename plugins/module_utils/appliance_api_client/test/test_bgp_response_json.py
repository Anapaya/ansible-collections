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

from ansible.module_utils.appliance_api_client.models.bgp_response_json import BGPResponseJson  # noqa: E501

class TestBGPResponseJson(unittest.TestCase):
    """BGPResponseJson unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BGPResponseJson:
        """Test BGPResponseJson
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BGPResponseJson`
        """
        model = BGPResponseJson()  # noqa: E501
        if include_optional:
            return BGPResponseJson(
                configuration = ansible.module_utils.appliance_api_client.models.bgp_config.BGPConfig(
                    asn = 56, 
                    router_id = '', 
                    neighbors = [
                        ansible.module_utils.appliance_api_client.models.bgp_neighbor.BGPNeighbor(
                            remote_asn = 56, 
                            remote_address = '', 
                            timers = ansible.module_utils.appliance_api_client.models.bgp_timers.BGPTimers(
                                keepalive_interval = 56, 
                                hold_time = 56, 
                                connect_retry = 56, 
                                minimum_advertisement_interval = 56, ), )
                        ], 
                    networks = [
                        ''
                        ], )
            )
        else:
            return BGPResponseJson(
                configuration = ansible.module_utils.appliance_api_client.models.bgp_config.BGPConfig(
                    asn = 56, 
                    router_id = '', 
                    neighbors = [
                        ansible.module_utils.appliance_api_client.models.bgp_neighbor.BGPNeighbor(
                            remote_asn = 56, 
                            remote_address = '', 
                            timers = ansible.module_utils.appliance_api_client.models.bgp_timers.BGPTimers(
                                keepalive_interval = 56, 
                                hold_time = 56, 
                                connect_retry = 56, 
                                minimum_advertisement_interval = 56, ), )
                        ], 
                    networks = [
                        ''
                        ], ),
        )
        """

    def testBGPResponseJson(self):
        """Test BGPResponseJson"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
