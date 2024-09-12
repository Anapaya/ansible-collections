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

from openapi_client.models.firewall_table_json import FirewallTableJson

class TestFirewallTableJson(unittest.TestCase):
    """FirewallTableJson unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FirewallTableJson:
        """Test FirewallTableJson
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FirewallTableJson`
        """
        model = FirewallTableJson()
        if include_optional:
            return FirewallTableJson(
                table = openapi_client.models.firewall_table.FirewallTable(
                    name = '', 
                    family = 'ip', 
                    chains = [
                        openapi_client.models.firewall_chain.FirewallChain(
                            name = '', 
                            hook = 'prerouting', 
                            priority = 56, 
                            policy = 'accept', 
                            type = 'filter', 
                            rules = [
                                openapi_client.models.firewall_rule.FirewallRule(
                                    rule = '', 
                                    comment = '', )
                                ], )
                        ], 
                    counters = [
                        openapi_client.models.firewall_counter.FirewallCounter(
                            name = '', 
                            packets = 56, 
                            bytes = 56, )
                        ], )
            )
        else:
            return FirewallTableJson(
                table = openapi_client.models.firewall_table.FirewallTable(
                    name = '', 
                    family = 'ip', 
                    chains = [
                        openapi_client.models.firewall_chain.FirewallChain(
                            name = '', 
                            hook = 'prerouting', 
                            priority = 56, 
                            policy = 'accept', 
                            type = 'filter', 
                            rules = [
                                openapi_client.models.firewall_rule.FirewallRule(
                                    rule = '', 
                                    comment = '', )
                                ], )
                        ], 
                    counters = [
                        openapi_client.models.firewall_counter.FirewallCounter(
                            name = '', 
                            packets = 56, 
                            bytes = 56, )
                        ], ),
        )
        """

    def testFirewallTableJson(self):
        """Test FirewallTableJson"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
