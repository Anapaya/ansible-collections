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

from ansible.module_utils.appliance_api_client.models.config_scion_tunneling_domain_traffic_policy import ConfigScionTunnelingDomainTrafficPolicy  # noqa: E501

class TestConfigScionTunnelingDomainTrafficPolicy(unittest.TestCase):
    """ConfigScionTunnelingDomainTrafficPolicy unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ConfigScionTunnelingDomainTrafficPolicy:
        """Test ConfigScionTunnelingDomainTrafficPolicy
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ConfigScionTunnelingDomainTrafficPolicy`
        """
        model = ConfigScionTunnelingDomainTrafficPolicy()  # noqa: E501
        if include_optional:
            return ConfigScionTunnelingDomainTrafficPolicy(
                description = 'Default traffic policy',
                failover_sequence = [
                    ansible.module_utils.appliance_api_client.models.config_scion_tunneling_domain_traffic_policy_failover_sequence_entry.Config_ScionTunneling_Domain_TrafficPolicy_FailoverSequenceEntry(
                        path_filter = '', 
                        sequence_id = 1, )
                    ],
                sequence_id = 1,
                traffic_matcher = ''
            )
        else:
            return ConfigScionTunnelingDomainTrafficPolicy(
                sequence_id = 1,
                traffic_matcher = '',
        )
        """

    def testConfigScionTunnelingDomainTrafficPolicy(self):
        """Test ConfigScionTunnelingDomainTrafficPolicy"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
