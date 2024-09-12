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

from openapi_client.models.traceroute_hop_info import TracerouteHopInfo

class TestTracerouteHopInfo(unittest.TestCase):
    """TracerouteHopInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TracerouteHopInfo:
        """Test TracerouteHopInfo
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TracerouteHopInfo`
        """
        model = TracerouteHopInfo()
        if include_optional:
            return TracerouteHopInfo(
                isd_as = '1-ff00:0:110',
                ip = '10.0.0.1',
                interface_id = 42,
                round_trip_times = [
                    '300ms'
                    ]
            )
        else:
            return TracerouteHopInfo(
                isd_as = '1-ff00:0:110',
                ip = '10.0.0.1',
                interface_id = 42,
                round_trip_times = [
                    '300ms'
                    ],
        )
        """

    def testTracerouteHopInfo(self):
        """Test TracerouteHopInfo"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
