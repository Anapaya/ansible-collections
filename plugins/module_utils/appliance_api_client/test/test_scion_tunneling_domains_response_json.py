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

from ansible.module_utils.appliance_api_client.models.scion_tunneling_domains_response_json import ScionTunnelingDomainsResponseJson

class TestScionTunnelingDomainsResponseJson(unittest.TestCase):
    """ScionTunnelingDomainsResponseJson unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ScionTunnelingDomainsResponseJson:
        """Test ScionTunnelingDomainsResponseJson
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ScionTunnelingDomainsResponseJson`
        """
        model = ScionTunnelingDomainsResponseJson()
        if include_optional:
            return ScionTunnelingDomainsResponseJson(
                domains = [
                    ansible.module_utils.appliance_api_client.models.scion_tunneling_domain_config.ScionTunnelingDomainConfig(
                        domain_name = '', 
                        default = True, 
                        encryption = 'disabled', 
                        local_isd_ases = [
                            '1-ff00:0:110'
                            ], 
                        remote_isd_ases = [
                            ansible.module_utils.appliance_api_client.models.scion_tunneling_isd_as_filter.ScionTunnelingIsdAsFilter(
                                action = 'ACCEPT', 
                                isd_as = '1-ff00:0:110', )
                            ], 
                        prefixes = ansible.module_utils.appliance_api_client.models.scion_tunneling_domain_config_prefixes.ScionTunnelingDomainConfig_prefixes(
                            announce_filter = [
                                ansible.module_utils.appliance_api_client.models.scion_tunneling_prefixes_filter.ScionTunnelingPrefixesFilter(
                                    action = 'ACCEPT', 
                                    prefixes = [
                                        ''
                                        ], )
                                ], 
                            accept_filter = [
                                ansible.module_utils.appliance_api_client.models.scion_tunneling_prefixes_filter.ScionTunnelingPrefixesFilter(
                                    action = 'ACCEPT', 
                                    prefixes = [
                                        ''
                                        ], )
                                ], ), 
                        traffic_policies = [
                            ansible.module_utils.appliance_api_client.models.scion_tunneling_traffic_policy.ScionTunnelingTrafficPolicy(
                                traffic_matcher = '', 
                                failover_sequence = [
                                    ''
                                    ], )
                            ], )
                    ]
            )
        else:
            return ScionTunnelingDomainsResponseJson(
                domains = [
                    ansible.module_utils.appliance_api_client.models.scion_tunneling_domain_config.ScionTunnelingDomainConfig(
                        domain_name = '', 
                        default = True, 
                        encryption = 'disabled', 
                        local_isd_ases = [
                            '1-ff00:0:110'
                            ], 
                        remote_isd_ases = [
                            ansible.module_utils.appliance_api_client.models.scion_tunneling_isd_as_filter.ScionTunnelingIsdAsFilter(
                                action = 'ACCEPT', 
                                isd_as = '1-ff00:0:110', )
                            ], 
                        prefixes = ansible.module_utils.appliance_api_client.models.scion_tunneling_domain_config_prefixes.ScionTunnelingDomainConfig_prefixes(
                            announce_filter = [
                                ansible.module_utils.appliance_api_client.models.scion_tunneling_prefixes_filter.ScionTunnelingPrefixesFilter(
                                    action = 'ACCEPT', 
                                    prefixes = [
                                        ''
                                        ], )
                                ], 
                            accept_filter = [
                                ansible.module_utils.appliance_api_client.models.scion_tunneling_prefixes_filter.ScionTunnelingPrefixesFilter(
                                    action = 'ACCEPT', 
                                    prefixes = [
                                        ''
                                        ], )
                                ], ), 
                        traffic_policies = [
                            ansible.module_utils.appliance_api_client.models.scion_tunneling_traffic_policy.ScionTunnelingTrafficPolicy(
                                traffic_matcher = '', 
                                failover_sequence = [
                                    ''
                                    ], )
                            ], )
                    ],
        )
        """

    def testScionTunnelingDomainsResponseJson(self):
        """Test ScionTunnelingDomainsResponseJson"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
