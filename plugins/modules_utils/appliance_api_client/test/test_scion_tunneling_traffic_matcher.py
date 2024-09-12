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

from openapi_client.models.scion_tunneling_traffic_matcher import ScionTunnelingTrafficMatcher

class TestScionTunnelingTrafficMatcher(unittest.TestCase):
    """ScionTunnelingTrafficMatcher unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ScionTunnelingTrafficMatcher:
        """Test ScionTunnelingTrafficMatcher
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ScionTunnelingTrafficMatcher`
        """
        model = ScionTunnelingTrafficMatcher()
        if include_optional:
            return ScionTunnelingTrafficMatcher(
                traffic_policy_id = 56,
                traffic_matcher = '',
                failover_sequence = [
                    openapi_client.models.scion_tunneling_failover_sequence_entry.ScionTunnelingFailoverSequenceEntry(
                        path_filter_name = '', 
                        sessions = [
                            ''
                            ], 
                        sessions_legacy = [
                            56
                            ], )
                    ],
                selected_session = '',
                selected_session_legacy = 56,
                selected_path = ''
            )
        else:
            return ScionTunnelingTrafficMatcher(
                traffic_policy_id = 56,
                traffic_matcher = '',
                failover_sequence = [
                    openapi_client.models.scion_tunneling_failover_sequence_entry.ScionTunnelingFailoverSequenceEntry(
                        path_filter_name = '', 
                        sessions = [
                            ''
                            ], 
                        sessions_legacy = [
                            56
                            ], )
                    ],
                selected_session = '',
                selected_session_legacy = 56,
                selected_path = '',
        )
        """

    def testScionTunnelingTrafficMatcher(self):
        """Test ScionTunnelingTrafficMatcher"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
