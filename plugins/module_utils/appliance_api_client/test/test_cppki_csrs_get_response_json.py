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

from ansible.module_utils.appliance_api_client.models.cppki_csrs_get_response_json import CppkiCsrsGetResponseJson

class TestCppkiCsrsGetResponseJson(unittest.TestCase):
    """CppkiCsrsGetResponseJson unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CppkiCsrsGetResponseJson:
        """Test CppkiCsrsGetResponseJson
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CppkiCsrsGetResponseJson`
        """
        model = CppkiCsrsGetResponseJson()
        if include_optional:
            return CppkiCsrsGetResponseJson(
                certificate_signing_requests = [
                    ansible.module_utils.appliance_api_client.models.certificate_signing_request_information.Certificate signing request information(
                        subject = ansible.module_utils.appliance_api_client.models.subject_of_a_certificate_signing_request/.Subject of a certificate signing request.(
                            isd_as = '1-ff00:0:110', 
                            common_name = 'Anapaya Switzerland AS', 
                            country = 'CH', 
                            locality = 'Zurich', 
                            organization = 'Anapaya Systems AG', 
                            organizational_unit = 'Anapaya Systems Engineering Department', 
                            postal_code = '8005', 
                            province = 'Zurich', 
                            serial_number = 'CHE 123.456.789', 
                            street_address = 'Hardturmstrasse 253, 8005 Zurich', ), 
                        creation_time = '2021-01-04T09:59:33Z', 
                        id = 'fa53a04a', )
                    ]
            )
        else:
            return CppkiCsrsGetResponseJson(
                certificate_signing_requests = [
                    ansible.module_utils.appliance_api_client.models.certificate_signing_request_information.Certificate signing request information(
                        subject = ansible.module_utils.appliance_api_client.models.subject_of_a_certificate_signing_request/.Subject of a certificate signing request.(
                            isd_as = '1-ff00:0:110', 
                            common_name = 'Anapaya Switzerland AS', 
                            country = 'CH', 
                            locality = 'Zurich', 
                            organization = 'Anapaya Systems AG', 
                            organizational_unit = 'Anapaya Systems Engineering Department', 
                            postal_code = '8005', 
                            province = 'Zurich', 
                            serial_number = 'CHE 123.456.789', 
                            street_address = 'Hardturmstrasse 253, 8005 Zurich', ), 
                        creation_time = '2021-01-04T09:59:33Z', 
                        id = 'fa53a04a', )
                    ],
        )
        """

    def testCppkiCsrsGetResponseJson(self):
        """Test CppkiCsrsGetResponseJson"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
