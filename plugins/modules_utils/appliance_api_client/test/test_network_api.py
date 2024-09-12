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

from openapi_client.api.network_api import NetworkApi


class TestNetworkApi(unittest.TestCase):
    """NetworkApi unit test stubs"""

    def setUp(self) -> None:
        self.api = NetworkApi()

    def tearDown(self) -> None:
        pass

    def test_network_physical_interfaces_get(self) -> None:
        """Test case for network_physical_interfaces_get

        List the available physical interfaces
        """
        pass

    def test_network_wireguards_get(self) -> None:
        """Test case for network_wireguards_get

        Get list of Wireguard interfaces.
        """
        pass

    def test_network_wireguards_interface_get(self) -> None:
        """Test case for network_wireguards_interface_get

        Get a Wireguard interface.
        """
        pass


if __name__ == '__main__':
    unittest.main()
