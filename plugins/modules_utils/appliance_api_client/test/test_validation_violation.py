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

from openapi_client.models.validation_violation import ValidationViolation

class TestValidationViolation(unittest.TestCase):
    """ValidationViolation unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ValidationViolation:
        """Test ValidationViolation
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ValidationViolation`
        """
        model = ValidationViolation()
        if include_optional:
            return ValidationViolation(
                path = '/scion/ases/1-ff00:0:1/id',
                reason = 'missing value',
                detail = 'At least one prefix must be specified.'
            )
        else:
            return ValidationViolation(
                path = '/scion/ases/1-ff00:0:1/id',
                reason = 'missing value',
        )
        """

    def testValidationViolation(self):
        """Test ValidationViolation"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
