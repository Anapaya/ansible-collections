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

from ansible.module_utils.appliance_api_client.models.scion_tunneling_summary import ScionTunnelingSummary

class TestScionTunnelingSummary(unittest.TestCase):
    """ScionTunnelingSummary unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ScionTunnelingSummary:
        """Test ScionTunnelingSummary
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ScionTunnelingSummary`
        """
        model = ScionTunnelingSummary()
        if include_optional:
            return ScionTunnelingSummary(
                sessions = [
                    ansible.module_utils.appliance_api_client.models.scion_tunneling_session.ScionTunnelingSession(
                        session_id = '', 
                        session_id_legacy = 56, 
                        local_isd_as = '1-ff00:0:110', 
                        remote_isd_as = '1-ff00:0:110', 
                        data_addr = '', 
                        probe_addr = '', 
                        pinned = [
                            56
                            ], 
                        domain = '', 
                        traffic_matcher = '', 
                        path_filter = '', 
                        healthy = True, 
                        encryption = 'disabled', 
                        paths = [
                            ansible.module_utils.appliance_api_client.models.scion_tunneling_session_path.ScionTunnelingSessionPath(
                                fingerprint = '', 
                                current = True, 
                                rejected = True, )
                            ], )
                    ],
                routing_chains = [
                    ansible.module_utils.appliance_api_client.models.scion_tunneling_routing_chain.ScionTunnelingRoutingChain(
                        routing_chain_id = '', 
                        routing_chain_id_legacy = 56, 
                        prefixes = [
                            ''
                            ], 
                        domain = '', 
                        traffic_matchers = [
                            ansible.module_utils.appliance_api_client.models.scion_tunneling_traffic_matcher.ScionTunnelingTrafficMatcher(
                                traffic_policy_id = 56, 
                                traffic_matcher = '', 
                                failover_sequence = [
                                    ansible.module_utils.appliance_api_client.models.scion_tunneling_failover_sequence_entry.ScionTunnelingFailoverSequenceEntry(
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
                                selected_path = '', )
                            ], )
                    ],
                paths = {
                    'key' : null
                    }
            )
        else:
            return ScionTunnelingSummary(
                sessions = [
                    ansible.module_utils.appliance_api_client.models.scion_tunneling_session.ScionTunnelingSession(
                        session_id = '', 
                        session_id_legacy = 56, 
                        local_isd_as = '1-ff00:0:110', 
                        remote_isd_as = '1-ff00:0:110', 
                        data_addr = '', 
                        probe_addr = '', 
                        pinned = [
                            56
                            ], 
                        domain = '', 
                        traffic_matcher = '', 
                        path_filter = '', 
                        healthy = True, 
                        encryption = 'disabled', 
                        paths = [
                            ansible.module_utils.appliance_api_client.models.scion_tunneling_session_path.ScionTunnelingSessionPath(
                                fingerprint = '', 
                                current = True, 
                                rejected = True, )
                            ], )
                    ],
                routing_chains = [
                    ansible.module_utils.appliance_api_client.models.scion_tunneling_routing_chain.ScionTunnelingRoutingChain(
                        routing_chain_id = '', 
                        routing_chain_id_legacy = 56, 
                        prefixes = [
                            ''
                            ], 
                        domain = '', 
                        traffic_matchers = [
                            ansible.module_utils.appliance_api_client.models.scion_tunneling_traffic_matcher.ScionTunnelingTrafficMatcher(
                                traffic_policy_id = 56, 
                                traffic_matcher = '', 
                                failover_sequence = [
                                    ansible.module_utils.appliance_api_client.models.scion_tunneling_failover_sequence_entry.ScionTunnelingFailoverSequenceEntry(
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
                                selected_path = '', )
                            ], )
                    ],
                paths = {
                    'key' : null
                    },
        )
        """

    def testScionTunnelingSummary(self):
        """Test ScionTunnelingSummary"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
