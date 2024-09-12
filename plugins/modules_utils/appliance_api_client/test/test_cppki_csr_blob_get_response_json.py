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

from openapi_client.models.cppki_csr_blob_get_response_json import CppkiCsrBlobGetResponseJson

class TestCppkiCsrBlobGetResponseJson(unittest.TestCase):
    """CppkiCsrBlobGetResponseJson unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CppkiCsrBlobGetResponseJson:
        """Test CppkiCsrBlobGetResponseJson
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CppkiCsrBlobGetResponseJson`
        """
        model = CppkiCsrBlobGetResponseJson()
        if include_optional:
            return CppkiCsrBlobGetResponseJson(
                csr = '-----BEGIN CERTIFICATE REQUEST-----\nCertificateSigningRequest ...\n-----END CERTIFICATE REQUEST-----'
            )
        else:
            return CppkiCsrBlobGetResponseJson(
                csr = '-----BEGIN CERTIFICATE REQUEST-----\nCertificateSigningRequest ...\n-----END CERTIFICATE REQUEST-----',
        )
        """

    def testCppkiCsrBlobGetResponseJson(self):
        """Test CppkiCsrBlobGetResponseJson"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
