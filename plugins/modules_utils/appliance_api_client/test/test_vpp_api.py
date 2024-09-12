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

from openapi_client.api.vpp_api import VppApi


class TestVppApi(unittest.TestCase):
    """VppApi unit test stubs"""

    def setUp(self) -> None:
        self.api = VppApi()

    def tearDown(self) -> None:
        pass

    def test_get_debug_vpp_address(self) -> None:
        """Test case for get_debug_vpp_address

        Status page listing addresses on VPP interfaces.
        """
        pass

    def test_get_debug_vpp_bfd(self) -> None:
        """Test case for get_debug_vpp_bfd

        Status page reporting the bfd session states.
        """
        pass

    def test_get_debug_vpp_bond(self) -> None:
        """Test case for get_debug_vpp_bond

        Status page reporting bonds created by VPP.
        """
        pass

    def test_get_debug_vpp_buffers(self) -> None:
        """Test case for get_debug_vpp_buffers

        Status page reporting VPP buffers.
        """
        pass

    def test_get_debug_vpp_clear_errors(self) -> None:
        """Test case for get_debug_vpp_clear_errors

        Action path to clear VPP errors.
        """
        pass

    def test_get_debug_vpp_clear_interfaces(self) -> None:
        """Test case for get_debug_vpp_clear_interfaces

        Action path to clear the metrics on VPP interfaces.
        """
        pass

    def test_get_debug_vpp_clear_runtime(self) -> None:
        """Test case for get_debug_vpp_clear_runtime

        Action path to clear the VPP runtime.
        """
        pass

    def test_get_debug_vpp_coredump(self) -> None:
        """Test case for get_debug_vpp_coredump

        Download the coredump.
        """
        pass

    def test_get_debug_vpp_coredumps(self) -> None:
        """Test case for get_debug_vpp_coredumps

        Get the list of avaiable VPP coredumps.
        """
        pass

    def test_get_debug_vpp_dataplane_control(self) -> None:
        """Test case for get_debug_vpp_dataplane_control

        Dump of the VPP state set up by dataplane-control service.
        """
        pass

    def test_get_debug_vpp_error(self) -> None:
        """Test case for get_debug_vpp_error

        Status page reporting VPP errors.
        """
        pass

    def test_get_debug_vpp_events(self) -> None:
        """Test case for get_debug_vpp_events

        Status page reporting VPP events.
        """
        pass

    def test_get_debug_vpp_fib_ip4(self) -> None:
        """Test case for get_debug_vpp_fib_ip4

        Status page reporting VPP IPv4 FIB.
        """
        pass

    def test_get_debug_vpp_fib_ip6(self) -> None:
        """Test case for get_debug_vpp_fib_ip6

        Status page reporting VPP IPv6 FIB.
        """
        pass

    def test_get_debug_vpp_fib_ll(self) -> None:
        """Test case for get_debug_vpp_fib_ll

        Status page reporting VPP IPv6 link-local FIB.
        """
        pass

    def test_get_debug_vpp_gateway(self) -> None:
        """Test case for get_debug_vpp_gateway

        Dump of the VPP state set up by the gateway service.
        """
        pass

    def test_get_debug_vpp_hardware(self) -> None:
        """Test case for get_debug_vpp_hardware

        Status page listing hardware interfaces managed by VPP.
        """
        pass

    def test_get_debug_vpp_interface(self) -> None:
        """Test case for get_debug_vpp_interface

        Status page listing internal VPP interfaces.
        """
        pass

    def test_get_debug_vpp_lacp(self) -> None:
        """Test case for get_debug_vpp_lacp

        Status page reporting VPP LACP info.
        """
        pass

    def test_get_debug_vpp_lcp(self) -> None:
        """Test case for get_debug_vpp_lcp

        Status page listing interfaces mirrored from VPP to Linux.
        """
        pass

    def test_get_debug_vpp_logging(self) -> None:
        """Test case for get_debug_vpp_logging

        Status page reporting VPP logs.
        """
        pass

    def test_get_debug_vpp_memory(self) -> None:
        """Test case for get_debug_vpp_memory

        Status page reporting VPP memory.
        """
        pass

    def test_get_debug_vpp_neighbors_ip4(self) -> None:
        """Test case for get_debug_vpp_neighbors_ip4

        Status page reporting VPP IPv4 neighbors.
        """
        pass

    def test_get_debug_vpp_neighbors_ip6(self) -> None:
        """Test case for get_debug_vpp_neighbors_ip6

        Status page reporting VPP IPv6 neighbors.
        """
        pass

    def test_get_debug_vpp_plugins(self) -> None:
        """Test case for get_debug_vpp_plugins

        Status page listing of loaded VPP plugins.
        """
        pass

    def test_get_debug_vpp_runtime(self) -> None:
        """Test case for get_debug_vpp_runtime

        Status page reporting VPP runtime.
        """
        pass

    def test_get_debug_vpp_scion_interface(self) -> None:
        """Test case for get_debug_vpp_scion_interface

        Status page reporting the SCION interfaces.
        """
        pass

    def test_get_debug_vpp_scion_ipfix_params(self) -> None:
        """Test case for get_debug_vpp_scion_ipfix_params

        Status page reporting the SCION router IPFIX parameters.
        """
        pass

    def test_get_debug_vpp_scion_ipfix_statistics(self) -> None:
        """Test case for get_debug_vpp_scion_ipfix_statistics

        Status page reporting the SCION router IPFIX statistics.
        """
        pass

    def test_get_debug_vpp_scion_ipfix_table(self) -> None:
        """Test case for get_debug_vpp_scion_ipfix_table

        Status page reporting the SCION router IPFIX table.
        """
        pass

    def test_get_debug_vpp_scion_isd_as(self) -> None:
        """Test case for get_debug_vpp_scion_isd_as

        Status page reporting the SCION router ASes.
        """
        pass

    def test_get_debug_vpp_scion_reservation(self) -> None:
        """Test case for get_debug_vpp_scion_reservation

        Status page reporting the SCION router bandwidth reservations.
        """
        pass

    def test_get_debug_vpp_scion_svc(self) -> None:
        """Test case for get_debug_vpp_scion_svc

        Status page reporting the SCION services.
        """
        pass

    def test_get_debug_vpp_scion_tunneling_decap_to_output(self) -> None:
        """Test case for get_debug_vpp_scion_tunneling_decap_to_output

        SCION gateway: trace all ingress IP packets.
        """
        pass

    def test_get_debug_vpp_scion_tunneling_dpdk_to_decap(self) -> None:
        """Test case for get_debug_vpp_scion_tunneling_dpdk_to_decap

        SCION gateway: trace all ingress frames entering via dpdk.
        """
        pass

    def test_get_debug_vpp_scion_tunneling_dpdk_to_encap4(self) -> None:
        """Test case for get_debug_vpp_scion_tunneling_dpdk_to_encap4

        SCION gateway: trace all egress IPv4 packets entering via dpdk.
        """
        pass

    def test_get_debug_vpp_scion_tunneling_dpdk_to_encap6(self) -> None:
        """Test case for get_debug_vpp_scion_tunneling_dpdk_to_encap6

        SCION gateway: trace all egress IPv6 packets entering via dpdk.
        """
        pass

    def test_get_debug_vpp_scion_tunneling_encap4_to_output(self) -> None:
        """Test case for get_debug_vpp_scion_tunneling_encap4_to_output

        SCION gateway: trace all egress frames on top of IPv4 underlay.
        """
        pass

    def test_get_debug_vpp_scion_tunneling_encap6_to_output(self) -> None:
        """Test case for get_debug_vpp_scion_tunneling_encap6_to_output

        SCION gateway: trace all egress frames on top of IPv6 underlay.
        """
        pass

    def test_get_debug_vpp_scion_tunneling_info(self) -> None:
        """Test case for get_debug_vpp_scion_tunneling_info

        SCION gateway: global settings.
        """
        pass

    def test_get_debug_vpp_scion_tunneling_iremote_ia(self) -> None:
        """Test case for get_debug_vpp_scion_tunneling_iremote_ia

        SCION gateway: remote ASes.
        """
        pass

    def test_get_debug_vpp_scion_tunneling_memif_to_decap(self) -> None:
        """Test case for get_debug_vpp_scion_tunneling_memif_to_decap

        SCION gateway: trace all ingress frames entering via memif.
        """
        pass

    def test_get_debug_vpp_scion_tunneling_memif_to_encap4(self) -> None:
        """Test case for get_debug_vpp_scion_tunneling_memif_to_encap4

        SCION gateway: trace all egress IPv4 packets entering via memif.
        """
        pass

    def test_get_debug_vpp_scion_tunneling_memif_to_encap6(self) -> None:
        """Test case for get_debug_vpp_scion_tunneling_memif_to_encap6

        SCION gateway: trace all egress IPv6 packets entering via memif.
        """
        pass

    def test_get_debug_vpp_scion_tunneling_path(self) -> None:
        """Test case for get_debug_vpp_scion_tunneling_path

        SCION gateway: known paths.
        """
        pass

    def test_get_debug_vpp_scion_tunneling_routing(self) -> None:
        """Test case for get_debug_vpp_scion_tunneling_routing

        SCION gateway: routing hierarchy.
        """
        pass

    def test_get_debug_vpp_scion_tunneling_routing_chain(self) -> None:
        """Test case for get_debug_vpp_scion_tunneling_routing_chain

        SCION gateway: routing chains.
        """
        pass

    def test_get_debug_vpp_scion_tunneling_session(self) -> None:
        """Test case for get_debug_vpp_scion_tunneling_session

        SCION gateway: sessions.
        """
        pass

    def test_get_debug_vpp_scion_tunneling_traffic_class(self) -> None:
        """Test case for get_debug_vpp_scion_tunneling_traffic_class

        SCION gateway: traffic classes.
        """
        pass

    def test_get_debug_vpp_scion_tunneling_tun(self) -> None:
        """Test case for get_debug_vpp_scion_tunneling_tun

        SCION gateway: TUN device.
        """
        pass

    def test_get_debug_vpp_trace(self) -> None:
        """Test case for get_debug_vpp_trace

        Action path to execute free form packet trace.
        """
        pass

    def test_get_debug_vpp_trace_dpdk(self) -> None:
        """Test case for get_debug_vpp_trace_dpdk

        Action path to execute a trace for packets entering via DPDK.
        """
        pass

    def test_get_debug_vpp_trace_memif(self) -> None:
        """Test case for get_debug_vpp_trace_memif

        Action path to execute a trace for packets entering via memif.
        """
        pass

    def test_get_debug_vpp_trace_start(self) -> None:
        """Test case for get_debug_vpp_trace_start

        Action path that starts a trace without timeout. The trace can be stopped with the `/vpp/trace/stop` endpoint.
        """
        pass

    def test_get_debug_vpp_trace_stop(self) -> None:
        """Test case for get_debug_vpp_trace_stop

        Action path that stops tracing.
        """
        pass

    def test_get_debug_vpp_trace_udp4_socket(self) -> None:
        """Test case for get_debug_vpp_trace_udp4_socket

        Action path to execute a trace for IPv4 packets entering via VPP UDP socket.
        """
        pass

    def test_get_debug_vpp_trace_udp6_socket(self) -> None:
        """Test case for get_debug_vpp_trace_udp6_socket

        Action path to execute a trace for IPv6 packets entering via VPP UDP socket.
        """
        pass

    def test_get_debug_vpp_trace_virtio(self) -> None:
        """Test case for get_debug_vpp_trace_virtio

        Action path to execute a trace for packets entering via TUN/TAP.
        """
        pass

    def test_get_debug_vpp_tun(self) -> None:
        """Test case for get_debug_vpp_tun

        Status page reporting TUN/TAP devices created by VPP.
        """
        pass

    def test_get_debug_vpp_vrrp(self) -> None:
        """Test case for get_debug_vpp_vrrp

        Status page reporting VPP VRRP.
        """
        pass


if __name__ == '__main__':
    unittest.main()
