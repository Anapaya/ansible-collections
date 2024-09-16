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

from ansible.module_utils.appliance_api_client.models.firewall_chain import FirewallChain

class TestFirewallChain(unittest.TestCase):
    """FirewallChain unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FirewallChain:
        """Test FirewallChain
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FirewallChain`
        """
        model = FirewallChain()
        if include_optional:
            return FirewallChain(
                name = '',
                hook = 'prerouting',
                priority = 56,
                policy = 'accept',
                type = 'filter',
                rules = [
                    ansible.module_utils.appliance_api_client.models.firewall_rule.FirewallRule(
                        rule = '', 
                        comment = '', )
                    ]
            )
        else:
            return FirewallChain(
                name = '',
                rules = [
                    ansible.module_utils.appliance_api_client.models.firewall_rule.FirewallRule(
                        rule = '', 
                        comment = '', )
                    ],
        )
        """

    def testFirewallChain(self):
        """Test FirewallChain"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
