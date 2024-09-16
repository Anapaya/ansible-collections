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

from ansible.module_utils.appliance_api_client.models.config_firewall import ConfigFirewall

class TestConfigFirewall(unittest.TestCase):
    """ConfigFirewall unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ConfigFirewall:
        """Test ConfigFirewall
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ConfigFirewall`
        """
        model = ConfigFirewall()
        if include_optional:
            return ConfigFirewall(
                mode = 'AUTO',
                tables = [
                    ansible.module_utils.appliance_api_client.models.config_firewall_table.Config_Firewall_Table(
                        chains = [
                            ansible.module_utils.appliance_api_client.models.config_firewall_table_chain.Config_Firewall_Table_Chain(
                                chaintype = 'FILTER', 
                                hook = 'PREROUTING', 
                                name = '', 
                                policy = 'ACCEPT', 
                                priority = 56, 
                                rules = [
                                    ansible.module_utils.appliance_api_client.models.config_firewall_table_chain_rule.Config_Firewall_Table_Chain_Rule(
                                        comment = '', 
                                        rule = '', 
                                        sequence_id = 1, )
                                    ], )
                            ], 
                        counters = [
                            ansible.module_utils.appliance_api_client.models.config_firewall_table_counter.Config_Firewall_Table_Counter(
                                name = '', )
                            ], 
                        family = 'IP', 
                        name = '', )
                    ]
            )
        else:
            return ConfigFirewall(
        )
        """

    def testConfigFirewall(self):
        """Test ConfigFirewall"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
