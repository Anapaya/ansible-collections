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

from openapi_client.models.config import Config

class TestConfig(unittest.TestCase):
    """Config unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Config:
        """Test Config
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Config`
        """
        model = Config()
        if include_optional:
            return Config(
                advanced = openapi_client.models.config_advanced.Config_Advanced(
                    service_customizations = [
                        openapi_client.models.config_advanced_service_customizations.Config_Advanced_ServiceCustomizations(
                            disabled = True, 
                            service_type = 'CONTROL', 
                            template = '', )
                        ], ),
                bgp = openapi_client.models.config_bgp.Config_Bgp(
                    global = openapi_client.models.config_bgp_global.Config_Bgp_Global(
                        as = 56, 
                        networks = [
                            ''
                            ], 
                        router_id = '', 
                        src_address = '', ), 
                    neighbors = [
                        openapi_client.models.config_bgp_neighbor.Config_Bgp_Neighbor(
                            auth_password = '', 
                            bfd = openapi_client.models.config_bgp_neighbor_bfd.Config_Bgp_Neighbor_Bfd(
                                desired_minimum_tx_interval = 10, 
                                detection_multiplier = 2, 
                                enabled = True, 
                                local_address = '', 
                                minimum_ttl = 1, 
                                multihop = True, 
                                required_minimum_receive = 10, ), 
                            description = '', 
                            ebgp_multihop = 56, 
                            enabled = True, 
                            local_as = 56, 
                            neighbor_address = '', 
                            peer_as = 56, 
                            timers = openapi_client.models.config_bgp_neighbor_timers.Config_Bgp_Neighbor_Timers(
                                connect_retry = 56, 
                                hold_time = 56, 
                                keepalive_interval = 56, 
                                minimum_advertisement_interval = 56, ), 
                            transport = openapi_client.models.config_bgp_neighbor_transport.Config_Bgp_Neighbor_Transport(
                                local_address = '', ), 
                            ttl_security = 56, )
                        ], ),
                cluster = openapi_client.models.config_cluster.Config_Cluster(
                    features = openapi_client.models.config_cluster_features.Config_Cluster_Features(
                        scion_rss = True, ), 
                    peers = [
                        openapi_client.models.config_cluster_peer.Config_Cluster_Peer(
                            description = '', 
                            name = '', 
                            scion = openapi_client.models.config_cluster_peer_scion.Config_Cluster_Peer_Scion(
                                ases = [
                                    openapi_client.models.config_cluster_peer_scion_as.Config_Cluster_Peer_Scion_AS(
                                        control = openapi_client.models.config_cluster_peer_scion_as_control.Config_Cluster_Peer_Scion_AS_Control(
                                            address = '192.168.1.1:30100', ), 
                                        isd_as = '1-ff00:0:110', 
                                        neighbors = [
                                            openapi_client.models.config_cluster_peer_scion_as_neighbor.Config_Cluster_Peer_Scion_AS_Neighbor(
                                                interfaces = [
                                                    openapi_client.models.config_cluster_peer_scion_as_neighbor_interface.Config_Cluster_Peer_Scion_AS_Neighbor_Interface(
                                                        interface_id = 1, 
                                                        next_hop = '169.254.0.1:30100', 
                                                        scion_mtu = 1472, )
                                                    ], 
                                                neighbor_isd_as = '2-ff00:0:210', 
                                                relationship = 'CORE', )
                                            ], 
                                        shard_id = 56, )
                                    ], ), 
                            scion_tunneling = openapi_client.models.config_cluster_peer_scion_tunneling.Config_Cluster_Peer_ScionTunneling(
                                endpoint = openapi_client.models.config_cluster_peer_scion_tunneling_endpoint.Config_Cluster_Peer_ScionTunneling_Endpoint(
                                    allowed_interfaces = [
                                        openapi_client.models.config_cluster_peer_scion_tunneling_endpoint_allowed_interfaces.Config_Cluster_Peer_ScionTunneling_Endpoint_AllowedInterfaces(
                                            isd_as = '', )
                                        ], 
                                    control_port = 40201, 
                                    data_port = 40200, 
                                    disable_auto_allowed_interfaces = True, 
                                    ip = '192.168.1.100', 
                                    probe_port = 40202, ), ), 
                            synchronization = openapi_client.models.config_cluster_peer_synchronization.Config_Cluster_Peer_Synchronization(
                                address = '192.168.1.1:30100', ), )
                        ], 
                    synchronization = openapi_client.models.config_cluster_synchronization.Config_Cluster_Synchronization(
                        address = '192.0.2.3:40000', 
                        node_synchronization_interval = '1m', ), ),
                experiments = openapi_client.models.config_experiments.Config_Experiments(
                    features = [
                        openapi_client.models.config_experiments_feature.Config_Experiments_Feature(
                            name = '', 
                            value = '', )
                        ], ),
                firewall = openapi_client.models.config_firewall.Config_Firewall(
                    mode = 'AUTO', 
                    tables = [
                        openapi_client.models.config_firewall_table.Config_Firewall_Table(
                            chains = [
                                openapi_client.models.config_firewall_table_chain.Config_Firewall_Table_Chain(
                                    chaintype = 'FILTER', 
                                    hook = 'PREROUTING', 
                                    name = '', 
                                    policy = 'ACCEPT', 
                                    priority = 56, 
                                    rules = [
                                        openapi_client.models.config_firewall_table_chain_rule.Config_Firewall_Table_Chain_Rule(
                                            comment = '', 
                                            rule = '', 
                                            sequence_id = 1, )
                                        ], )
                                ], 
                            counters = [
                                openapi_client.models.config_firewall_table_counter.Config_Firewall_Table_Counter(
                                    name = '', )
                                ], 
                            family = 'IP', 
                            name = '', )
                        ], ),
                interfaces = openapi_client.models.config_interfaces.Config_Interfaces(
                    bonds = [
                        openapi_client.models.config_interfaces_bond.Config_Interfaces_Bond(
                            accept_ra = True, 
                            addresses = [
                                ''
                                ], 
                            gateway = openapi_client.models.config_interfaces_bond_gateway.Config_Interfaces_Bond_Gateway(
                                ipv4_gateway = '', 
                                ipv6_gateway = '', ), 
                            interfaces = [
                                ''
                                ], 
                            mac = '', 
                            mtu = 1472, 
                            name = '', 
                            neighbors = [
                                openapi_client.models.config_interfaces_bond_neighbor.Config_Interfaces_Bond_Neighbor(
                                    address = '', 
                                    comment = '', 
                                    mac = '', 
                                    sequence_id = 3, )
                                ], 
                            routes = [
                                openapi_client.models.config_interfaces_bond_route.Config_Interfaces_Bond_Route(
                                    comment = '', 
                                    from = '', 
                                    metric = 56, 
                                    sequence_id = 3, 
                                    to = '', 
                                    via = '', )
                                ], 
                            rx_queue_size = 2048, 
                            tx_queue_size = 2048, 
                            vrrp = [
                                openapi_client.models.config_interfaces_bond_vrrp.Config_Interfaces_Bond_Vrrp(
                                    addresses = [
                                        ''
                                        ], 
                                    no_preempt = True, 
                                    peers = [
                                        ''
                                        ], 
                                    priority = 17, 
                                    vrid = 3, )
                                ], )
                        ], 
                    ethernets = [
                        openapi_client.models.config_interfaces_ethernet.Config_Interfaces_Ethernet(
                            accept_ra = True, 
                            driver = 'LINUX', 
                            mac = '', 
                            mtu = 1472, 
                            name = '', 
                            rx_queue_size = 2048, 
                            tx_queue_size = 2048, 
                            vpp = openapi_client.models.config_interfaces_ethernet_vpp.Config_Interfaces_Ethernet_Vpp(
                                vlan_strip_offload = True, ), )
                        ], 
                    loopbacks = [
                        openapi_client.models.config_interfaces_loopback.Config_Interfaces_Loopback(
                            name = '', )
                        ], 
                    virtual_functions = [
                        openapi_client.models.config_interfaces_virtual_function.Config_Interfaces_VirtualFunction(
                            accept_ra = True, 
                            link = '', 
                            mac = '', 
                            mtu = 1472, 
                            name = '', 
                            rx_queue_size = 2048, 
                            tx_queue_size = 2048, )
                        ], 
                    vlans = [
                        openapi_client.models.config_interfaces_vlan.Config_Interfaces_Vlan(
                            accept_ra = True, 
                            id = 56, 
                            link = '', 
                            mac = '', 
                            mtu = 1472, 
                            name = '', 
                            rx_queue_size = 2048, 
                            tx_queue_size = 2048, )
                        ], 
                    wireguards = [
                        openapi_client.models.config_interfaces_wireguard.Config_Interfaces_Wireguard(
                            mtu = 56, 
                            name = '', 
                            pointopoint = '', 
                            port = 56, )
                        ], ),
                management = openapi_client.models.config_management.Config_Management(
                    api = openapi_client.models.config_management_api.Config_Management_Api(
                        basic_auth = openapi_client.models.config_management_api_basic_auth.Config_Management_Api_BasicAuth(
                            enabled = True, 
                            users = [
                                openapi_client.models.config_management_api_basic_auth_user.Config_Management_Api_BasicAuth_User(
                                    password_hashed = '$2y$10$QNodxwKFABMWu4XlFPmZDOSfqxrsqNvrSn487lCi7tJ/4nTsT/f02', 
                                    username = 'admin', )
                                ], ), 
                        listeners = [
                            openapi_client.models.config_management_api_listener.Config_Management_Api_Listener(
                                address = '127.0.0.1:443', 
                                description = '', )
                            ], 
                        oauth = openapi_client.models.config_management_api_oauth.Config_Management_Api_Oauth(
                            enabled = True, 
                            identity_providers = [
                                openapi_client.models.config_management_api_oauth_identity_provider.Config_Management_Api_Oauth_IdentityProvider(
                                    base_auth_url = 'https://anapaya.eu.auth0.com/', 
                                    client_id = '', 
                                    client_secret = '', 
                                    id = '', 
                                    metadata_url = 'https://anapaya.eu.auth0.com/.well-known/openid-configuration', 
                                    tenant_id = '', 
                                    type = 'GENERIC', )
                                ], 
                            roles = [
                                openapi_client.models.config_management_api_oauth_role.Config_Management_Api_Oauth_Role(
                                    aliases = [
                                        ''
                                        ], 
                                    role = '', )
                                ], 
                            token_verification_keys = [
                                openapi_client.models.config_management_api_oauth_token_verification_key.Config_Management_Api_Oauth_TokenVerificationKey(
                                    id = 'anapaya.auth0', 
                                    jwks_url = 'https://anapaya.eu.auth0.com/.well-known/jwks.json', )
                                ], ), 
                        unprotected = True, ), 
                    hostname = 'anapaya-appliance', 
                    remote_repository = openapi_client.models.config_management_remote_repository.Config_Management_RemoteRepository(
                        cloudsmith = openapi_client.models.config_management_remote_repository_cloudsmith.Config_Management_RemoteRepository_Cloudsmith(
                            access_token = 'APIKEY#ENTITLEMENTTOKEN', 
                            url = 'https://cloudsmith.io/anapaya/repos/external', ), 
                        repository_type = 'CLOUDSMITH', ), 
                    ssh = openapi_client.models.config_management_ssh.Config_Management_Ssh(
                        enable_password_login = True, ), 
                    telemetry = openapi_client.models.config_management_telemetry.Config_Management_Telemetry(
                        address = ':42001', 
                        flow_metrics = openapi_client.models.config_management_telemetry_flow_metrics.Config_Management_Telemetry_FlowMetrics(
                            cleanup_task_interval = '60s', 
                            collector_url = '', 
                            enabled = True, 
                            export_task_interval = '60s', 
                            flow_expiration_interval = '180s', 
                            proxy_url = '', ), 
                        labels = [
                            openapi_client.models.config_management_telemetry_labels.Config_Management_Telemetry_Labels(
                                label = '', 
                                value = '', )
                            ], 
                        logging = openapi_client.models.config_management_telemetry_logging.Config_Management_Telemetry_Logging(
                            logging_type = 'LOKI', 
                            loki = openapi_client.models.config_management_telemetry_logging_loki.Config_Management_Telemetry_Logging_Loki(
                                tls_config = openapi_client.models.config_management_telemetry_logging_loki_tls_config.Config_Management_Telemetry_Logging_Loki_TlsConfig(
                                    insecure_skip_verify = True, ), 
                                url = 'https://loki.anapaya.net/loki/api/v1/push', ), ), ), ),
                nat = openapi_client.models.config_nat.Config_Nat(
                    snat = openapi_client.models.config_nat_snat.Config_Nat_Snat(
                        address_pool = [
                            ''
                            ], 
                        exclude = [
                            ''
                            ], 
                        interfaces = [
                            ''
                            ], ), ),
                scion = openapi_client.models.config_scion.Config_SCION(
                    ases = [
                        openapi_client.models.config_scion_as.Config_SCION_AS(
                            ca_service = openapi_client.models.config_scion_as_ca_service.Config_SCION_AS_CAService(
                                anapaya_vault = openapi_client.models.config_scion_as_ca_service_anapaya_vault.Config_SCION_AS_CAService_AnapayaVault(
                                    addresses = [
                                        ''
                                        ], 
                                    credentials = openapi_client.models.config_scion_as_ca_service_anapaya_vault_credentials.Config_SCION_AS_CAService_AnapayaVault_Credentials(
                                        role_id = '', 
                                        secret_id = '', ), 
                                    validation = openapi_client.models.config_scion_as_ca_service_anapaya_vault_validation.Config_SCION_AS_CAService_AnapayaVault_Validation(
                                        subject = 'MATCHING_ISD_AS', ), ), 
                                external = openapi_client.models.config_scion_as_ca_service_external.Config_SCION_AS_CAService_External(
                                    address = '192.0.2.3:5000', 
                                    client_id = '', 
                                    shared_secret = 'shared secret', ), 
                                service_type = 'EXTERNAL', ), 
                            control = openapi_client.models.config_scion_as_control.Config_SCION_AS_Control(
                                address = '192.168.1.1:30100', 
                                enabled = True, ), 
                            core = True, 
                            cppki = openapi_client.models.config_scion_as_cppki.Config_SCION_AS_CPPKI(
                                disable_auto_renewal = True, 
                                issuers = [
                                    openapi_client.models.config_scion_as_cppki_issuer.Config_SCION_AS_CPPKI_Issuer(
                                        isd_as = '1-ff00:0:120', 
                                        priority = 56, )
                                    ], ), 
                            default = True, 
                            details = openapi_client.models.config_scion_as_details.Config_SCION_AS_Details(
                                description = '', 
                                name = '', ), 
                            forwarding_key = '', 
                            isd_as = '1-ff00:0:110', 
                            neighbors = [
                                openapi_client.models.config_scion_as_neighbor.Config_SCION_AS_Neighbor(
                                    description = '', 
                                    interfaces = [
                                        openapi_client.models.config_scion_as_neighbor_interface.Config_SCION_AS_Neighbor_Interface(
                                            address = '169.254.0.1:30100', 
                                            administrative_state = 'UP', 
                                            bfd = openapi_client.models.config_scion_as_neighbor_interface_bfd.Config_SCION_AS_Neighbor_Interface_BFD(
                                                desired_minimum_tx_interval = 56, 
                                                detection_multiplier = 1, 
                                                enabled = True, 
                                                required_minimum_receive = 56, ), 
                                            description = '', 
                                            enable_scion_rss = True, 
                                            interface_id = 1, 
                                            remote = openapi_client.models.config_scion_as_neighbor_interface_remote.Config_SCION_AS_Neighbor_Interface_Remote(
                                                address = '169.254.0.1:30100', 
                                                interface_id = 1, ), 
                                            scion_mtu = 1472, )
                                        ], 
                                    neighbor_isd_as = '2-ff00:0:210', 
                                    relationship = 'CORE', )
                                ], 
                            router = openapi_client.models.config_scion_as_router.Config_SCION_AS_Router(
                                enabled = True, 
                                internal_interface = '192.168.1.1:30100', ), 
                            scion_mtu = 1472, 
                            shard_id = 56, )
                        ], 
                    synchronization = openapi_client.models.config_scion_synchronization.Config_SCION_Synchronization(
                        beacon_synchronization_interval = '4s', 
                        path_segment_synchronization_interval = '4s', ), ),
                scion_tunneling = openapi_client.models.config_scion_tunneling.Config_ScionTunneling(
                    domains = [
                        openapi_client.models.config_scion_tunneling_domain.Config_ScionTunneling_Domain(
                            default = True, 
                            description = 'The domain. It matches all packets and allows any
path to be used.', 
                            local_isd_ases = [
                                ''
                                ], 
                            name = 'Default Domain', 
                            prefixes = openapi_client.models.config_scion_tunneling_domain_prefixes.Config_ScionTunneling_Domain_Prefixes(
                                accept_filter = [
                                    openapi_client.models.config_scion_tunneling_domain_prefixes_accept_filter_entry.Config_ScionTunneling_Domain_Prefixes_AcceptFilterEntry(
                                        action = 'ACCEPT', 
                                        description = '', 
                                        sequence_id = 1, )
                                    ], 
                                announce_filter = [
                                    openapi_client.models.config_scion_tunneling_domain_prefixes_announce_filter_entry.Config_ScionTunneling_Domain_Prefixes_AnnounceFilterEntry(
                                        action = 'ACCEPT', 
                                        description = '', 
                                        sequence_id = 1, )
                                    ], ), 
                            remote_isd_ases = [
                                openapi_client.models.config_scion_tunneling_domain_remote_matcher.Config_ScionTunneling_Domain_RemoteMatcher(
                                    action = 'ACCEPT', 
                                    description = '', 
                                    isd_as = '0-ff00:0:310', 
                                    sequence_id = 1, )
                                ], 
                            traffic_policies = [
                                openapi_client.models.config_scion_tunneling_domain_traffic_policy.Config_ScionTunneling_Domain_TrafficPolicy(
                                    description = 'Default traffic policy', 
                                    failover_sequence = [
                                        openapi_client.models.config_scion_tunneling_domain_traffic_policy_failover_sequence_entry.Config_ScionTunneling_Domain_TrafficPolicy_FailoverSequenceEntry(
                                            path_filter = '', 
                                            sequence_id = 1, )
                                        ], 
                                    sequence_id = 1, 
                                    traffic_matcher = '', )
                                ], )
                        ], 
                    endpoint = openapi_client.models.config_scion_tunneling_endpoint.Config_ScionTunneling_Endpoint(
                        allowed_interfaces = [
                            openapi_client.models.config_scion_tunneling_endpoint_allowed_interfaces.Config_ScionTunneling_Endpoint_AllowedInterfaces(
                                interfaces = [2,3], 
                                isd_as = '', )
                            ], 
                        control_port = 40201, 
                        data_port = 40200, 
                        description = '', 
                        disable_auto_allowed_interfaces = True, 
                        disable_urpf = True, 
                        enable_scion_rss = True, 
                        enabled = True, 
                        ip = '192.168.1.100', 
                        probe_port = 40202, ), 
                    path_filters = [
                        openapi_client.models.config_scion_tunneling_path_filter.Config_ScionTunneling_PathFilter(
                            acl = ["+ 64-0"], 
                            description = 'Match only paths in the Swiss Isolation Domain (ID 64).', 
                            hop_pattern = '0* 64+ 0+', 
                            name = 'CH ISD only', )
                        ], 
                    remotes = [
                        openapi_client.models.config_scion_tunneling_remote.Config_ScionTunneling_Remote(
                            description = '', 
                            isd_as = '1-ff00:0:310', )
                        ], 
                    static_announcements = [
                        openapi_client.models.config_scion_tunneling_static_announcement.Config_ScionTunneling_StaticAnnouncement(
                            description = '', 
                            next_hop_tracking = openapi_client.models.config_scion_tunneling_static_announcement_next_hop_tracking.Config_ScionTunneling_StaticAnnouncement_NextHopTracking(
                                disabled = True, 
                                target = '192.168.0.1', ), 
                            prefixes = ["192.168.1.0/24","172.30.100.0/28"], 
                            sequence_id = 1, )
                        ], 
                    traffic_matchers = [
                        openapi_client.models.config_scion_tunneling_traffic_matcher.Config_ScionTunneling_TrafficMatcher(
                            condition = 'BOOL=true', 
                            description = ''all packets' matches all packets.', 
                            name = 'all packets', )
                        ], ),
                system = openapi_client.models.config_system.Config_System(
                    dns = openapi_client.models.config_system_dns.Config_System_Dns(
                        servers = [
                            openapi_client.models.config_system_dns_servers.Config_System_Dns_Servers(
                                address = '', )
                            ], ), 
                    kernel = openapi_client.models.config_system_kernel.Config_System_Kernel(
                        hugepage_size = '2M', 
                        hugepages = 56, 
                        iommu_enabled = True, ), 
                    ntp = openapi_client.models.config_system_ntp.Config_System_Ntp(
                        root_distance_max = '5s', ), 
                    resources = openapi_client.models.config_system_resources.Config_System_Resources(
                        service_limits = [
                            openapi_client.models.config_system_resources_service_limit.Config_System_Resources_ServiceLimit(
                                cpu = 1.5, 
                                memory = '2.5G', 
                                name = 'CONTROL', )
                            ], ), 
                    vpp = openapi_client.models.config_system_vpp.Config_System_Vpp(
                        buffers = openapi_client.models.config_system_vpp_buffers.Config_System_Vpp_Buffers(
                            data_size = 56, 
                            num_buffers = 56, ), 
                        connection = openapi_client.models.config_system_vpp_connection.Config_System_Vpp_Connection(
                            health_check = openapi_client.models.config_system_vpp_connection_health_check.Config_System_Vpp_Connection_HealthCheck(
                                probe_interval = '1s', 
                                reply_timeout = '250ms', 
                                threshold = 3, ), 
                            reconnect_attempts = 5, 
                            reconnect_interval = '1s', ), 
                        cpu = openapi_client.models.config_system_vpp_cpu.Config_System_Vpp_Cpu(
                            corelist_workers = '2-3,5', 
                            main_core = 56, 
                            workers = 56, ), 
                        poll_sleep = '0s', 
                        tun = openapi_client.models.config_system_vpp_tun.Config_System_Vpp_Tun(
                            mtu = 1500, 
                            prefixes = ["192.168.1.0/24"], ), ), )
            )
        else:
            return Config(
        )
        """

    def testConfig(self):
        """Test Config"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
