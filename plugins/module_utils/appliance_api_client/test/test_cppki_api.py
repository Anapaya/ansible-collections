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

from ansible.module_utils.appliance_api_client.api.cppki_api import CppkiApi


class TestCppkiApi(unittest.TestCase):
    """CppkiApi unit test stubs"""

    def setUp(self) -> None:
        self.api = CppkiApi()

    def tearDown(self) -> None:
        pass

    def test_cppki_certificate_blob_get(self) -> None:
        """Test case for cppki_certificate_blob_get

        Get the certificate chain blob
        """
        pass

    def test_cppki_certificate_get(self) -> None:
        """Test case for cppki_certificate_get

        Get the certificate chain
        """
        pass

    def test_cppki_certificates_get(self) -> None:
        """Test case for cppki_certificates_get

        List the certificate chains
        """
        pass

    def test_cppki_certificates_post(self) -> None:
        """Test case for cppki_certificates_post

        Add an AS certificate chain
        """
        pass

    def test_cppki_certificates_renew_post(self) -> None:
        """Test case for cppki_certificates_renew_post

        Manually renew an AS certificate chain
        """
        pass

    def test_cppki_certificates_request_post(self) -> None:
        """Test case for cppki_certificates_request_post

        Manually request an AS certificate chain for a given CSR
        """
        pass

    def test_cppki_csr_blob_get(self) -> None:
        """Test case for cppki_csr_blob_get

        Get the certificate signing request blob
        """
        pass

    def test_cppki_csr_get(self) -> None:
        """Test case for cppki_csr_get

        Get the certificate signing request
        """
        pass

    def test_cppki_csrs_get(self) -> None:
        """Test case for cppki_csrs_get

        List the certificate signing requests
        """
        pass

    def test_cppki_csrs_post(self) -> None:
        """Test case for cppki_csrs_post

        Create an AS certificate signing request
        """
        pass

    def test_cppki_trc_blob_get(self) -> None:
        """Test case for cppki_trc_blob_get

        Get the TRC blob
        """
        pass

    def test_cppki_trc_get(self) -> None:
        """Test case for cppki_trc_get

        Get the TRC
        """
        pass

    def test_cppki_trcs_bundle_post(self) -> None:
        """Test case for cppki_trcs_bundle_post

        Add a bundle of TRC files
        """
        pass

    def test_cppki_trcs_get(self) -> None:
        """Test case for cppki_trcs_get

        List the TRC files
        """
        pass

    def test_cppki_trcs_post(self) -> None:
        """Test case for cppki_trcs_post

        Add a TRC file
        """
        pass


if __name__ == '__main__':
    unittest.main()
