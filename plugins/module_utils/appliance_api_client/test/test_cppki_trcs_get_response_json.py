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

from ansible.module_utils.appliance_api_client.models.cppki_trcs_get_response_json import CppkiTrcsGetResponseJson  # noqa: E501

class TestCppkiTrcsGetResponseJson(unittest.TestCase):
    """CppkiTrcsGetResponseJson unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CppkiTrcsGetResponseJson:
        """Test CppkiTrcsGetResponseJson
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CppkiTrcsGetResponseJson`
        """
        model = CppkiTrcsGetResponseJson()  # noqa: E501
        if include_optional:
            return CppkiTrcsGetResponseJson(
                trcs = [
                    ansible.module_utils.appliance_api_client.models.trc_information.TRC Information(
                        id = ansible.module_utils.appliance_api_client.models.trc_identifier.TRC Identifier(
                            isd = 15, 
                            base_number = 1, 
                            serial_number = 3, ), 
                        validity = ansible.module_utils.appliance_api_client.models.validity_period.Validity period(
                            not_before = '2021-01-04T09:59:33Z', 
                            not_after = '2022-01-04T09:59:33Z', ), 
                        core_ases = [
                            '1-ff00:0:110'
                            ], 
                        authoritative_ases = [
                            '1-ff00:0:110'
                            ], 
                        description = '', 
                        blob = '', )
                    ]
            )
        else:
            return CppkiTrcsGetResponseJson(
                trcs = [
                    ansible.module_utils.appliance_api_client.models.trc_information.TRC Information(
                        id = ansible.module_utils.appliance_api_client.models.trc_identifier.TRC Identifier(
                            isd = 15, 
                            base_number = 1, 
                            serial_number = 3, ), 
                        validity = ansible.module_utils.appliance_api_client.models.validity_period.Validity period(
                            not_before = '2021-01-04T09:59:33Z', 
                            not_after = '2022-01-04T09:59:33Z', ), 
                        core_ases = [
                            '1-ff00:0:110'
                            ], 
                        authoritative_ases = [
                            '1-ff00:0:110'
                            ], 
                        description = '', 
                        blob = '', )
                    ],
        )
        """

    def testCppkiTrcsGetResponseJson(self):
        """Test CppkiTrcsGetResponseJson"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
