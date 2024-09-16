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

from ansible.module_utils.appliance_api_client.models.ping_run import PingRun  # noqa: E501

class TestPingRun(unittest.TestCase):
    """PingRun unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PingRun:
        """Test PingRun
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PingRun`
        """
        model = PingRun()  # noqa: E501
        if include_optional:
            return PingRun(
                destination_host = '',
                destination_isd_as = '1-ff00:0:110',
                count = 1,
                source_isd_as = '1-ff00:0:110',
                max_mtu = True,
                payload_size = 8,
                sequence = '',
                timeout = '1s'
            )
        else:
            return PingRun(
                destination_host = '',
                destination_isd_as = '1-ff00:0:110',
        )
        """

    def testPingRun(self):
        """Test PingRun"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
