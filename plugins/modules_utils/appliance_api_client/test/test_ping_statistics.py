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

from openapi_client.models.ping_statistics import PingStatistics

class TestPingStatistics(unittest.TestCase):
    """PingStatistics unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PingStatistics:
        """Test PingStatistics
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PingStatistics`
        """
        model = PingStatistics()
        if include_optional:
            return PingStatistics(
                sent = 56,
                received = 56,
                packet_loss = 1.337,
                time = 56
            )
        else:
            return PingStatistics(
                sent = 56,
                received = 56,
                packet_loss = 1.337,
                time = 56,
        )
        """

    def testPingStatistics(self):
        """Test PingStatistics"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
