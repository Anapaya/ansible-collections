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

from ansible.module_utils.appliance_api_client.models.cppki_certificates_get_response_json import CppkiCertificatesGetResponseJson

class TestCppkiCertificatesGetResponseJson(unittest.TestCase):
    """CppkiCertificatesGetResponseJson unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CppkiCertificatesGetResponseJson:
        """Test CppkiCertificatesGetResponseJson
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CppkiCertificatesGetResponseJson`
        """
        model = CppkiCertificatesGetResponseJson()
        if include_optional:
            return CppkiCertificatesGetResponseJson(
                certificate_chains = [
                    ansible.module_utils.appliance_api_client.models.certificate_chain_information.Certificate chain information(
                        id = 'fa53a04a', 
                        subject = '1-ff00:0:110', 
                        issuer = '1-ff00:0:110', 
                        validity = ansible.module_utils.appliance_api_client.models.validity_period.Validity period(
                            not_before = '2021-01-04T09:59:33Z', 
                            not_after = '2022-01-04T09:59:33Z', ), 
                        chain = '', 
                        blob = '', )
                    ]
            )
        else:
            return CppkiCertificatesGetResponseJson(
                certificate_chains = [
                    ansible.module_utils.appliance_api_client.models.certificate_chain_information.Certificate chain information(
                        id = 'fa53a04a', 
                        subject = '1-ff00:0:110', 
                        issuer = '1-ff00:0:110', 
                        validity = ansible.module_utils.appliance_api_client.models.validity_period.Validity period(
                            not_before = '2021-01-04T09:59:33Z', 
                            not_after = '2022-01-04T09:59:33Z', ), 
                        chain = '', 
                        blob = '', )
                    ],
        )
        """

    def testCppkiCertificatesGetResponseJson(self):
        """Test CppkiCertificatesGetResponseJson"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
