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

from ansible.module_utils.appliance_api_client.models.health_summary import HealthSummary

class TestHealthSummary(unittest.TestCase):
    """HealthSummary unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> HealthSummary:
        """Test HealthSummary
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `HealthSummary`
        """
        model = HealthSummary()
        if include_optional:
            return HealthSummary(
                status = 'passing',
                checks = [
                    ansible.module_utils.appliance_api_client.models.health_check/.Health Check.(
                        service = 'router', 
                        name = 'valid signer available', 
                        status = 'passing', 
                        data = { }, 
                        reason = '', 
                        detail = '', )
                    ]
            )
        else:
            return HealthSummary(
                status = 'passing',
                checks = [
                    ansible.module_utils.appliance_api_client.models.health_check/.Health Check.(
                        service = 'router', 
                        name = 'valid signer available', 
                        status = 'passing', 
                        data = { }, 
                        reason = '', 
                        detail = '', )
                    ],
        )
        """

    def testHealthSummary(self):
        """Test HealthSummary"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
