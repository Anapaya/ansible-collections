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

from ansible.module_utils.appliance_api_client.models.scion_path import ScionPath  # noqa: E501

class TestScionPath(unittest.TestCase):
    """ScionPath unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ScionPath:
        """Test ScionPath
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ScionPath`
        """
        model = ScionPath()  # noqa: E501
        if include_optional:
            return ScionPath(
                fingerprint = '',
                human = '1-ff00:0:110 1>1 1-ff00:0:111',
                hops = [
                    ansible.module_utils.appliance_api_client.models.scion_path_hop.ScionPathHop(
                        ifid = 56, 
                        isd_as = '1-ff00:0:110', )
                    ],
                status = 'alive',
                next_hop = '',
                expiration = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                mtu = 56
            )
        else:
            return ScionPath(
                fingerprint = '',
                human = '1-ff00:0:110 1>1 1-ff00:0:111',
                hops = [
                    ansible.module_utils.appliance_api_client.models.scion_path_hop.ScionPathHop(
                        ifid = 56, 
                        isd_as = '1-ff00:0:110', )
                    ],
                status = 'alive',
                next_hop = '',
                expiration = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                mtu = 56,
        )
        """

    def testScionPath(self):
        """Test ScionPath"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
