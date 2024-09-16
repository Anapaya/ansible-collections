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

from ansible.module_utils.appliance_api_client.models.certificate_chain_for_as_available_data import CertificateChainForASAvailableData  # noqa: E501

class TestCertificateChainForASAvailableData(unittest.TestCase):
    """CertificateChainForASAvailableData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CertificateChainForASAvailableData:
        """Test CertificateChainForASAvailableData
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CertificateChainForASAvailableData`
        """
        model = CertificateChainForASAvailableData()  # noqa: E501
        if include_optional:
            return CertificateChainForASAvailableData(
                isd_as = '1-ff00:0:110',
                subject_key_id = 'F2 C5 22 BA 99 4B 1C 0C EC AF 00 BE 42 B4 0D A5 E2 4D 67 48',
                issuer = '1-ff00:0:110',
                valid_until = '2021-01-01T00:00Z',
                in_grace_period = False,
                validity = ansible.module_utils.appliance_api_client.models.schemas_validity.schemas-Validity(
                    not_before = '2020-01-01T00:00Z', 
                    not_after = '2021-01-01T00:00Z', ),
                trc = ansible.module_utils.appliance_api_client.models.trc_info.TRCInfo(
                    id = 'ISD64-B1-S3', 
                    isd = 64, 
                    base = 1, 
                    serial = 3, ),
                data_type = 'not_found'
            )
        else:
            return CertificateChainForASAvailableData(
                isd_as = '1-ff00:0:110',
                subject_key_id = 'F2 C5 22 BA 99 4B 1C 0C EC AF 00 BE 42 B4 0D A5 E2 4D 67 48',
                issuer = '1-ff00:0:110',
                valid_until = '2021-01-01T00:00Z',
                in_grace_period = False,
                validity = ansible.module_utils.appliance_api_client.models.schemas_validity.schemas-Validity(
                    not_before = '2020-01-01T00:00Z', 
                    not_after = '2021-01-01T00:00Z', ),
                trc = ansible.module_utils.appliance_api_client.models.trc_info.TRCInfo(
                    id = 'ISD64-B1-S3', 
                    isd = 64, 
                    base = 1, 
                    serial = 3, ),
                data_type = 'not_found',
        )
        """

    def testCertificateChainForASAvailableData(self):
        """Test CertificateChainForASAvailableData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
