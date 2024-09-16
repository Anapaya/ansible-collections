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

from ansible.module_utils.appliance_api_client.models.trc_for_local_isd_available_in_daemon_data import TRCForLocalISDAvailableInDaemonData

class TestTRCForLocalISDAvailableInDaemonData(unittest.TestCase):
    """TRCForLocalISDAvailableInDaemonData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TRCForLocalISDAvailableInDaemonData:
        """Test TRCForLocalISDAvailableInDaemonData
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TRCForLocalISDAvailableInDaemonData`
        """
        model = TRCForLocalISDAvailableInDaemonData()
        if include_optional:
            return TRCForLocalISDAvailableInDaemonData(
                id = 'ISD64-B1-S3',
                isd = 64,
                base = 1,
                serial = 3,
                not_before = '2020-01-01T00:00Z',
                not_after = '2021-01-01T00:00Z'
            )
        else:
            return TRCForLocalISDAvailableInDaemonData(
                isd = 64,
        )
        """

    def testTRCForLocalISDAvailableInDaemonData(self):
        """Test TRCForLocalISDAvailableInDaemonData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
