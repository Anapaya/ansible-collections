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

from ansible.module_utils.appliance_api_client.models.chain import Chain  # noqa: E501

class TestChain(unittest.TestCase):
    """Chain unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Chain:
        """Test Chain
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Chain`
        """
        model = Chain()  # noqa: E501
        if include_optional:
            return Chain(
                as_certificate = ansible.module_utils.appliance_api_client.models.certificate_information.Certificate information(
                    distinguished_name = '', 
                    isd_as = '1-ff00:0:110', 
                    validity = ansible.module_utils.appliance_api_client.models.validity_period.Validity period(
                        not_before = '2021-01-04T09:59:33Z', 
                        not_after = '2022-01-04T09:59:33Z', ), 
                    subject_key_algo = 'ECDSA', 
                    subject_key_id = '89 B9 49 C2 2F 2F 9C DD 0D 2A 57 A9 DE 8E 2F 95 F3 09 10 D1', ),
                ca_certificate = ansible.module_utils.appliance_api_client.models.certificate_information.Certificate information(
                    distinguished_name = '', 
                    isd_as = '1-ff00:0:110', 
                    validity = ansible.module_utils.appliance_api_client.models.validity_period.Validity period(
                        not_before = '2021-01-04T09:59:33Z', 
                        not_after = '2022-01-04T09:59:33Z', ), 
                    subject_key_algo = 'ECDSA', 
                    subject_key_id = '89 B9 49 C2 2F 2F 9C DD 0D 2A 57 A9 DE 8E 2F 95 F3 09 10 D1', )
            )
        else:
            return Chain(
                as_certificate = ansible.module_utils.appliance_api_client.models.certificate_information.Certificate information(
                    distinguished_name = '', 
                    isd_as = '1-ff00:0:110', 
                    validity = ansible.module_utils.appliance_api_client.models.validity_period.Validity period(
                        not_before = '2021-01-04T09:59:33Z', 
                        not_after = '2022-01-04T09:59:33Z', ), 
                    subject_key_algo = 'ECDSA', 
                    subject_key_id = '89 B9 49 C2 2F 2F 9C DD 0D 2A 57 A9 DE 8E 2F 95 F3 09 10 D1', ),
                ca_certificate = ansible.module_utils.appliance_api_client.models.certificate_information.Certificate information(
                    distinguished_name = '', 
                    isd_as = '1-ff00:0:110', 
                    validity = ansible.module_utils.appliance_api_client.models.validity_period.Validity period(
                        not_before = '2021-01-04T09:59:33Z', 
                        not_after = '2022-01-04T09:59:33Z', ), 
                    subject_key_algo = 'ECDSA', 
                    subject_key_id = '89 B9 49 C2 2F 2F 9C DD 0D 2A 57 A9 DE 8E 2F 95 F3 09 10 D1', ),
        )
        """

    def testChain(self):
        """Test Chain"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
