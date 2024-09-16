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

from ansible.module_utils.appliance_api_client.models.config_scion import ConfigSCION

class TestConfigSCION(unittest.TestCase):
    """ConfigSCION unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ConfigSCION:
        """Test ConfigSCION
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ConfigSCION`
        """
        model = ConfigSCION()
        if include_optional:
            return ConfigSCION(
                ases = [
                    ansible.module_utils.appliance_api_client.models.config_scion_as.Config_SCION_AS(
                        ca_service = ansible.module_utils.appliance_api_client.models.config_scion_as_ca_service.Config_SCION_AS_CAService(
                            anapaya_vault = ansible.module_utils.appliance_api_client.models.config_scion_as_ca_service_anapaya_vault.Config_SCION_AS_CAService_AnapayaVault(
                                addresses = [
                                    ''
                                    ], 
                                credentials = ansible.module_utils.appliance_api_client.models.config_scion_as_ca_service_anapaya_vault_credentials.Config_SCION_AS_CAService_AnapayaVault_Credentials(
                                    role_id = '', 
                                    secret_id = '', ), 
                                validation = ansible.module_utils.appliance_api_client.models.config_scion_as_ca_service_anapaya_vault_validation.Config_SCION_AS_CAService_AnapayaVault_Validation(
                                    subject = 'MATCHING_ISD_AS', ), ), 
                            external = ansible.module_utils.appliance_api_client.models.config_scion_as_ca_service_external.Config_SCION_AS_CAService_External(
                                address = '192.0.2.3:5000', 
                                client_id = '', 
                                shared_secret = 'shared secret', ), 
                            service_type = 'EXTERNAL', ), 
                        control = ansible.module_utils.appliance_api_client.models.config_scion_as_control.Config_SCION_AS_Control(
                            address = '192.168.1.1:30100', 
                            enabled = True, ), 
                        core = True, 
                        cppki = ansible.module_utils.appliance_api_client.models.config_scion_as_cppki.Config_SCION_AS_CPPKI(
                            disable_auto_renewal = True, 
                            issuers = [
                                ansible.module_utils.appliance_api_client.models.config_scion_as_cppki_issuer.Config_SCION_AS_CPPKI_Issuer(
                                    isd_as = '1-ff00:0:120', 
                                    priority = 56, )
                                ], ), 
                        default = True, 
                        details = ansible.module_utils.appliance_api_client.models.config_scion_as_details.Config_SCION_AS_Details(
                            description = '', 
                            name = '', ), 
                        forwarding_key = '', 
                        isd_as = '1-ff00:0:110', 
                        neighbors = [
                            ansible.module_utils.appliance_api_client.models.config_scion_as_neighbor.Config_SCION_AS_Neighbor(
                                description = '', 
                                interfaces = [
                                    ansible.module_utils.appliance_api_client.models.config_scion_as_neighbor_interface.Config_SCION_AS_Neighbor_Interface(
                                        address = '169.254.0.1:30100', 
                                        administrative_state = 'UP', 
                                        bfd = ansible.module_utils.appliance_api_client.models.config_scion_as_neighbor_interface_bfd.Config_SCION_AS_Neighbor_Interface_BFD(
                                            desired_minimum_tx_interval = 56, 
                                            detection_multiplier = 1, 
                                            enabled = True, 
                                            required_minimum_receive = 56, ), 
                                        description = '', 
                                        enable_scion_rss = True, 
                                        interface_id = 1, 
                                        remote = ansible.module_utils.appliance_api_client.models.config_scion_as_neighbor_interface_remote.Config_SCION_AS_Neighbor_Interface_Remote(
                                            address = '169.254.0.1:30100', 
                                            interface_id = 1, ), 
                                        scion_mtu = 1472, )
                                    ], 
                                neighbor_isd_as = '2-ff00:0:210', 
                                relationship = 'CORE', )
                            ], 
                        router = ansible.module_utils.appliance_api_client.models.config_scion_as_router.Config_SCION_AS_Router(
                            enabled = True, 
                            internal_interface = '192.168.1.1:30100', ), 
                        scion_mtu = 1472, 
                        shard_id = 56, )
                    ],
                synchronization = ansible.module_utils.appliance_api_client.models.config_scion_synchronization.Config_SCION_Synchronization(
                    beacon_synchronization_interval = '4s', 
                    path_segment_synchronization_interval = '4s', )
            )
        else:
            return ConfigSCION(
        )
        """

    def testConfigSCION(self):
        """Test ConfigSCION"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
