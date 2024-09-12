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

from openapi_client.models.debug_notify_status_json import DebugNotifyStatusJson

class TestDebugNotifyStatusJson(unittest.TestCase):
    """DebugNotifyStatusJson unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DebugNotifyStatusJson:
        """Test DebugNotifyStatusJson
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DebugNotifyStatusJson`
        """
        model = DebugNotifyStatusJson()
        if include_optional:
            return DebugNotifyStatusJson(
                disabled = True,
                indefinite = True,
                deadline = '2022-02-21T10:31:45Z',
                timeout = '10m'
            )
        else:
            return DebugNotifyStatusJson(
                disabled = True,
        )
        """

    def testDebugNotifyStatusJson(self):
        """Test DebugNotifyStatusJson"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
