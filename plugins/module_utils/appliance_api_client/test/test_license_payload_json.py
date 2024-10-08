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

from ansible.module_utils.appliance_api_client.models.license_payload_json import LicensePayloadJson

class TestLicensePayloadJson(unittest.TestCase):
    """LicensePayloadJson unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> LicensePayloadJson:
        """Test LicensePayloadJson
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `LicensePayloadJson`
        """
        model = LicensePayloadJson()
        if include_optional:
            return LicensePayloadJson(
                license_id = '',
                appliance_id = '',
                type = ansible.module_utils.appliance_api_client.models.license_type.LicenseType(
                    product = 'edge', 
                    tier = 'lite', ),
                issued = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                validity = ansible.module_utils.appliance_api_client.models.license_validity.LicenseValidity(
                    effective_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    final_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
            )
        else:
            return LicensePayloadJson(
                license_id = '',
                appliance_id = '',
                type = ansible.module_utils.appliance_api_client.models.license_type.LicenseType(
                    product = 'edge', 
                    tier = 'lite', ),
                issued = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                validity = ansible.module_utils.appliance_api_client.models.license_validity.LicenseValidity(
                    effective_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    final_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ),
        )
        """

    def testLicensePayloadJson(self):
        """Test LicensePayloadJson"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
