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

from ansible.module_utils.appliance_api_client.models.trc_for_local_isd_available_info import TRCForLocalISDAvailableInfo

class TestTRCForLocalISDAvailableInfo(unittest.TestCase):
    """TRCForLocalISDAvailableInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TRCForLocalISDAvailableInfo:
        """Test TRCForLocalISDAvailableInfo
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TRCForLocalISDAvailableInfo`
        """
        model = TRCForLocalISDAvailableInfo()
        if include_optional:
            return TRCForLocalISDAvailableInfo(
                validity = ansible.module_utils.appliance_api_client.models.schemas_validity.schemas-Validity(
                    not_before = '2020-01-01T00:00Z', 
                    not_after = '2021-01-01T00:00Z', ),
                grace_period_end = '2020-01-01T00:00Z',
                data_type = 'available'
            )
        else:
            return TRCForLocalISDAvailableInfo(
                validity = ansible.module_utils.appliance_api_client.models.schemas_validity.schemas-Validity(
                    not_before = '2020-01-01T00:00Z', 
                    not_after = '2021-01-01T00:00Z', ),
                grace_period_end = '2020-01-01T00:00Z',
                data_type = 'available',
        )
        """

    def testTRCForLocalISDAvailableInfo(self):
        """Test TRCForLocalISDAvailableInfo"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
