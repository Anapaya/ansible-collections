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

from openapi_client.models.bgp_config import BGPConfig

class TestBGPConfig(unittest.TestCase):
    """BGPConfig unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BGPConfig:
        """Test BGPConfig
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BGPConfig`
        """
        model = BGPConfig()
        if include_optional:
            return BGPConfig(
                asn = 56,
                router_id = '',
                neighbors = [
                    openapi_client.models.bgp_neighbor.BGPNeighbor(
                        remote_asn = 56, 
                        remote_address = '', 
                        timers = openapi_client.models.bgp_timers.BGPTimers(
                            keepalive_interval = 56, 
                            hold_time = 56, 
                            connect_retry = 56, 
                            minimum_advertisement_interval = 56, ), )
                    ],
                networks = [
                    ''
                    ]
            )
        else:
            return BGPConfig(
                asn = 56,
                router_id = '',
                neighbors = [
                    openapi_client.models.bgp_neighbor.BGPNeighbor(
                        remote_asn = 56, 
                        remote_address = '', 
                        timers = openapi_client.models.bgp_timers.BGPTimers(
                            keepalive_interval = 56, 
                            hold_time = 56, 
                            connect_retry = 56, 
                            minimum_advertisement_interval = 56, ), )
                    ],
                networks = [
                    ''
                    ],
        )
        """

    def testBGPConfig(self):
        """Test BGPConfig"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
